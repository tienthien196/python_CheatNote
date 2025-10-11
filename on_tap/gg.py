import requests
import json
import urllib.parse
import re
from typing import Dict, Any, Optional, List
from xml.etree import ElementTree as ET

class NGLxAPIClient:
    """
    Client tự động cho hệ thống Avallain Unity + xAPI của National Geographic Learning.
    Hỗ trợ:
      - Tải data.js
      - Trích xuất XML và đáp án
      - Tự động gửi statement (attempted → answered → completed)
      - Lưu state (bookmark, suspend_data)
    """

    def __init__(
        self,
        user_id: str,
        registration_id: str,
        session_cookie: str,
        base_url: str = "https://learn.eltngl.com"
    ):
        self.user_id = user_id
        self.registration_id = registration_id
        self.session_cookie = session_cookie
        self.base_url = base_url.rstrip('/')
        self.lrs_url = f"{self.base_url}/lrs/xAPI"

        self.agent = {
            "objectType": "Agent",
            "account": {
                "name": self.user_id,
                "homePage": f"http://web-cen-unity-prod.avallain.net/identifiers/users/{self.user_id}"
            }
        }

        # Sẽ được điền sau khi tải data.js
        self.content_uuid: Optional[str] = None
        self.activity_id: Optional[str] = None
        self.maximum_score: int = 0
        self.answers: Dict[str, List[str]] = {}

    def _get_headers(self, include_json: bool = True) -> Dict[str, str]:
        headers = {
            "Cookie": self.session_cookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
            "Referer": f"{self.base_url}/"
        }
        if include_json:
            headers["Content-Type"] = "application/json"
            headers["X-Experience-API-Version"] = "1.0.1"
        return headers

    def load_from_key(self, key: str) -> None:
        """
        Tải data.js từ key (UUID), trích xuất metadata và đáp án.
        """
        url = f"{self.base_url}/cdn_proxy/{key}/data.js"
        resp = requests.get(url, headers=self._get_headers(include_json=False))
        resp.raise_for_status()

        # Trích xuất JSON từ `ajaxData = {...};`
        match = re.search(r"ajaxData\s*=\s*(\{.*\});", resp.text, re.DOTALL)
        if not match:
            raise ValueError("Không tìm thấy ajaxData trong data.js")

        ajax_data = json.loads(match.group(1))

        # --- Parse LearningObjectInfo.xml ---
        lo_xml = ajax_data["LearningObjectInfo.xml"]
        lo_root = ET.fromstring(lo_xml)
        self.content_uuid = lo_root.find("uuid").text
        self.activity_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{self.content_uuid}"
        self.maximum_score = int(lo_root.find("maximumscore").text)

        # --- Parse catXXXXXXX.xml ---
        cat_key = next(k for k in ajax_data.keys() if k.startswith("cat") and k.endswith(".xml"))
        cat_xml = ajax_data[cat_key]
        cat_root = ET.fromstring(cat_xml)

        # Trích xuất đáp án: RESPONSE0, RESPONSE1, ...
        self.answers = {}
        for resp_decl in cat_root.findall(".//{http://www.imsglobal.org/xsd/imsqti_v2p2}responseDeclaration"):
            resp_id = resp_decl.get("identifier")
            values = [v.text for v in resp_decl.findall(".//{http://www.imsglobal.org/xsd/imsqti_v2p2}value")]
            self.answers[resp_id] = values

        print(f"✅ Đã tải bài học: {self.content_uuid}")
        print(f"✅ Đáp án ({len(self.answers)} câu):")
        for i, (k, v) in enumerate(self.answers.items()):
            print(f"   {i}. {v[0]}")

    def _build_state_url(self, state_id: str) -> str:
        if not self.activity_id:
            raise RuntimeError("Chưa gọi load_from_key()!")
        params = {
            "stateId": state_id,
            "activityId": self.activity_id,
            "agent": json.dumps(self.agent, separators=(',', ':')),
            "registration": self.registration_id
        }
        encoded = {k: urllib.parse.quote(str(v), safe='') for k, v in params.items()}
        query = "&".join(f"{k}={v}" for k, v in encoded.items())
        return f"{self.lrs_url}/activities/state?{query}"

    def get_state(self, state_id: str) -> Optional[Any]:
        url = self._build_state_url(state_id)
        resp = requests.get(url, headers=self._get_headers())
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 404:
            return None
        else:
            resp.raise_for_status()

    def put_state(self, state_id: str,  data: Any) -> bool:
        url = self._build_state_url(state_id)
        resp = requests.put(
            url,
            data=json.dumps(data, separators=(',', ':')),
            headers=self._get_headers()
        )
        resp.raise_for_status()
        return True

    def post_statements(self, statements: List[Dict]) -> bool:
        if not self.activity_id:
            raise RuntimeError("Chưa gọi load_from_key()!")
        for stmt in statements:
            stmt.setdefault("actor", self.agent)
            stmt.setdefault("object", {"id": self.activity_id, "objectType": "Activity"})
            stmt.setdefault("context", {})
            stmt["context"].setdefault("registration", self.registration_id)
        resp = requests.post(
            f"{self.lrs_url}/statements",
            data=json.dumps(statements, separators=(',', ':')),
            headers=self._get_headers()
        )
        resp.raise_for_status()
        return True

    # --- Tự động làm bài ---
    def auto_submit(self, duration: float = 10.0) -> None:
        """Tự động gửi toàn bộ sự kiện: attempted → answered → completed → terminated"""
        if not self.answers:
            raise RuntimeError("Chưa có đáp án. Gọi load_from_key() trước.")

        # 1. attempted
        self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/attempted", "display": {"en-US": "attempted"}}
        }])

        # 2. answered
        responses = {resp_id: answers[0] for resp_id, answers in self.answers.items()}
        self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"en-US": "answered"}},
            "result": {
                "response": json.dumps(responses, separators=(',', ':')),
                "duration": f"PT{duration:.3f}S"
            }
        }])

        # 3. completed (điểm tối đa)
        score_scaled = 1.0
        self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/completed", "display": {"en-US": "completed"}},
            "result": {
                "completion": True,
                "success": True,
                "score": {
                    "scaled": score_scaled,
                    "raw": float(self.maximum_score),
                    "min": 0,
                    "max": float(self.maximum_score)
                }
            }
        }])

        # 4. terminated
        self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/terminated", "display": {"en-US": "terminated"}}
        }])

        print(f"✅ Đã tự động nộp bài với điểm tối đa ({self.maximum_score}/{self.maximum_score})")

    # --- Helpers ---
    def save_bookmark(self, data):
        return self.put_state("bookmark", data)

    def save_suspend_data(self, data):
        return self.put_state("suspend_data", data)
    
# Thông tin từ bạn
user_id = "691faf92-92de-45f0-b84d-ae8dad27ed53"
registration_id = "6ff24efb-834d-416c-9da3-fceee914d88d"
session_cookie = "_unity_session=a629be948ae4f6351e864ffed27c93a0"
key = "dded0533-b8c8-4045-9d2c-3fb630b6b27c"  # UUID bài học

# Tạo client và tự động làm bài
client = NGLxAPIClient(user_id, registration_id, session_cookie)
client.load_from_key(key)      # Tải data.js, trích xuất đáp án
client.auto_submit(duration=12.5)  # Tự động nộp bài