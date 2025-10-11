import requests
import json
import urllib.parse
from typing import Dict, Any, Optional, List

class NGLxAPIClient:
    """
    Client chính xác cho hệ thống Avallain Unity + xAPI của National Geographic Learning.
    """

    def __init__(
        self,
        user_id: str,
        content_uuid: str,
        registration_id: str,
        session_cookie: str,
        base_url: str = "https://learn.eltngl.com"
    ):
        self.user_id = user_id
        self.content_uuid = content_uuid
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

        self.activity_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{self.content_uuid}"

    def _get_headers(self) -> Dict[str, str]:
        return {
            "Cookie": self.session_cookie,
            "Content-Type": "application/json",
            "X-Experience-API-Version": "1.0.1",
            "Referer": f"{self.base_url}/"
        }

    def _build_state_url(self, state_id: str) -> str:
        params = {
            "stateId": state_id,
            "activityId": self.activity_id,
            "agent": json.dumps(self.agent, separators=(',', ':')),
            "registration": self.registration_id
        }
        encoded_params = {
            k: urllib.parse.quote(str(v), safe='') for k, v in params.items()
        }
        query = "&".join(f"{k}={v}" for k, v in encoded_params.items())
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

    def put_state(self, state_id: str, data: Any) -> bool:  # ✅ ĐÃ SỬA: thêm `data: Any`
        url = self._build_state_url(state_id)
        resp = requests.put(
            url,
            data=json.dumps(data, separators=(',', ':')),
            headers=self._get_headers()
        )
        resp.raise_for_status()
        return resp.status_code in (204, 200)

    def post_statements(self, statements: List[Dict]) -> bool:
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

    # --- Helpers ---
    def get_bookmark(self):
        return self.get_state("bookmark")

    def save_bookmark(self, data):
        return self.put_state("bookmark", data)

    def get_suspend_data(self):
        return self.get_state("suspend_data")

    def save_suspend_data(self, data):
        return self.put_state("suspend_data", data)

    def send_attempted(self):
        return self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/attempted", "display": {"en-US": "attempted"}}
        }])

    def send_answered(self, responses: Dict[str, str], duration: Optional[float] = None):
        stmt = {
            "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"en-US": "answered"}},
            "result": {"response": json.dumps(responses, separators=(',', ':'))}
        }
        if duration is not None:
            stmt["result"]["duration"] = f"PT{duration:.3f}S"
        return self.post_statements([stmt])

    def send_completed(self, score_scaled: float, success: bool = True):
        return self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/completed", "display": {"en-US": "completed"}},
            "result": {
                "completion": True,
                "success": success,
                "score": {
                    "scaled": score_scaled,
                    "raw": score_scaled * 12,
                    "min": 0,
                    "max": 12
                }
            }
        }])

    def send_terminated(self):
        return self.post_statements([{
            "verb": {"id": "http://adlnet.gov/expapi/verbs/terminated", "display": {"en-US": "terminated"}}
        }])