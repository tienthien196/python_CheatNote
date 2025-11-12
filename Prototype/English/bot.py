#!/usr/bin/env python3
import json, re, uuid, datetime as dt, requests

# ================== CONFIG ==================
KEY    = "5c81bd5a-afe3-434e-8451-91cc838cdea4"   # thay đổi ở đây
COOKIE = "_unity_session=32237839b27c83dc7b546681e72c5c14"   # cookie hợp lệ
# ===========================================

BASE_JS   = f"https://learn.eltngl.com/cdn_proxy/{KEY}/data.js"
BASE_STATE= "https://learn.eltngl.com/lrs/xAPI/activities/state"
BASE_STMT = "https://learn.eltngl.com/lrs/xAPI/statements"
BASE_EVT  = "https://learn.eltngl.com/api/v2/events"

AGENT = {
    "objectType": "Agent",
    "account": {
        "name": "7eaa9602-e032-4de6-b645-e42c19fdd16f",
        "homePage": "http://web-cen-unity-prod.avallain.net/identifiers/users/7eaa9602-e032-4de6-b645-e42c19fdd16f"
    }
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Content-Type": "application/json",
    "X-Experience-API-Version": "1.0.1",
    "Origin": "https://learn.eltngl.com",
    "Referer": f"https://learn.eltngl.com/cdn_proxy/{KEY}/index",
    "Cookie": COOKIE
}

# ---------- helpers ----------
def get_xml_answers(xml_str: str):
    """Trích tất cả <value> trong <correctResponse> → list đáp án đúng"""
    vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>\s*</correctResponse>', xml_str, re.I)
    return [v.strip() for v in vals]

def build_suspend_data(answers: list):
    n = len(answers)
    items = [{"id": f"e{i}", "version": 1, "value": answers[i]} for i in range(n)]
    act_state = [{"filled": True, "correct": True, "id": f"e{i}"} for i in range(n)]
    return {
        "interaction_839104480": {
            "items": [{"items": items, "activityState": act_state}],
            "status": "corrected",
            "checkAttempts": 1,
            "manualCheckAttempts": 0,
            "solutionHint": False,
            "notes": [],
            "visited": True,
            "duration": 1279255.700000024,
            "checkAnswerOnSubmitPending": True
        },
        "duration": 3522329,
        "idleTime": 0,
        "attemptID": str(uuid.uuid4()),
        "submitPending": True
    }

def build_statement(answers: list, activity_id: str, page_id: str, reg: str, attempt_id: str):
    n = len(answers)
    return [{
        "id": str(uuid.uuid4()),
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"und": "answered"}},
        "result": {
            "duration": "PT37M21S",
            "response": json.dumps({
                "items": [{"items": [{"id": f"e{i}", "version": 1, "value": answers[i]} for i in range(n)],
                           "activityState": [{"filled": True, "correct": True, "id": f"e{i}"} for i in range(n)]}],
                "status": "corrected",
                "checkAttempts": 1,
                "manualCheckAttempts": 0,
                "solutionHint": False,
                "notes": [],
                "visited": True,
                "duration": 1279255.700000024
            }),
            "score": {"scaled": 1, "raw": n, "min": 0, "max": n}
        },
        "context": {
            "registration": reg,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": activity_id, "objectType": "Activity"}]}
        },
        "object": {
            "id": f"{activity_id}/0",
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"Grammar Exercise ({n} items)"},
                "extensions": {"http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())}
            }
        }
    }]


def build_statements(answers: list, activity_id: str, reg: str, attempt_id: str = 1):
    n = len(answers)
    now = dt.datetime.utcnow().isoformat() + "Z"
    base_obj = {
        "id": activity_id,
        "objectType": "Activity",
        "definition": {"name": {"und": f"Grammar Exercise ({n} items)"}}
    }
    # 1. answered (chi tiết)
    answered = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"und": "answered"}},
        "result": {
            "duration": "PT37M21S",
            "response": json.dumps({
                "items": [{"items": [{"id": f"e{i}", "version": 1, "value": answers[i]} for i in range(n)],
                           "activityState": [{"filled": True, "correct": True, "id": f"e{i}"} for i in range(n)]}],
                "status": "corrected", "checkAttempts": 1, "manualCheckAttempts": 0,
                "solutionHint": False, "notes": [], "visited": True, "duration": 1279255.700000024
            }),
            "score": {"scaled": 1, "raw": n, "min": 0, "max": n}
        },
        "context": {
            "registration": reg,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [base_obj]}
        },
        "object": {**base_obj, "id": f"{activity_id}/0"}
    }
    # 2. scored (điểm tổng)
    scored = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/scored", "display": {"und": "scored"}},
        "result": {
            "duration": "PT37M21S",
            "extensions": {
                "http://id.tincanapi.com/extension/duration": "PT58M43S",
                "http://xapi.avallain.net/extensions/idle-time": "PT0S"
            },
            "score": {"scaled": 1, "raw": n, "min": 0, "max": n}
        },
        "context": {
            "registration": reg,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [base_obj]}
        },
        "object": base_obj
    }
    # 3. attempted (tiến độ)
    attempted = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/attempted", "display": {"und": "attempted"}},
        "result": {
            "duration": "PT37M21S",
            "extensions": {
                "http://id.tincanapi.com/extension/duration": "PT58M43S",
                "http://xapi.avallain.net/extensions/idle-time": "PT0S"
            },
            "score": {"raw": 1, "min": 0, "max": 3}
        },
        "context": {
            "registration": reg,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [base_obj]}
        },
        "object": base_obj
    }
    return [answered, scored, attempted]
# ---------- thay thế toàn bộ phần "Lấy đáp án" ----------
def get_answers_from_data(data: dict):
    """
    Trả về list đáp án đúng theo thứ tự e0, e1...
    bằng cách duyệt TẤT CẢ cat*.xml trong ajaxData
    """
    answers = []
    # Duyệt tất cả các mục trong ajaxData
    for key, xml_escaped in data.items():
        if not key.startswith("cat") or not key.endswith(".xml"):
            continue
        # Giải mã chuỗi Unicode escape (ví dụ: \u003c → <)
        xml_clean = xml_escaped.encode().decode('unicode-escape')
        # Trích xuất tất cả <value> trong <correctResponse>
        vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>\s*</correctResponse>', xml_clean, re.I)
        for v in vals:
            answers.append(v.strip())
    if not answers:
        raise ValueError("Không tìm thấy cat*.xml nào chứa đáp án!")
    return answers

# ---------- trong main() ----------
    # 2. Lấy đáp án từ TẤT CẢ cat*.xml
    answers = get_answers_from_data(data)

# ---------- flow ----------
def main():
    # 1. Tải data.js
    js = requests.get(BASE_JS, headers={"Cookie": COOKIE, "User-Agent": HEADERS["User-Agent"]}).text
    raw_json = re.search(r'ajaxData\s*=\s*({.*?})\s*;', js, flags=re.S).group(1)
    data = json.loads(raw_json)


    # 2. Lấy đáp án từ cat*.xml
    answers = get_answers_from_data(data)
    if not answers:
        print("Không tìm thấy đáp án trong cat2104000.xml")
        return
    print(f"Đáp án đúng ({len(answers)}): {answers}")

    # 3. Build dữ liệu
    activity_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{KEY}"
    reg = str(uuid.uuid4())
    attempt = str(uuid.uuid4())
    suspend = build_suspend_data(answers)
    stmt = build_statements(answers, activity_id, reg, attempt)

    # 4. Gửi 4 request thay player
    s = requests.Session()
    s.headers.update(HEADERS)

    # 4a. PUT suspend_data
    r1 = s.put(BASE_STATE, params={"stateId": "suspend_data", "activityId": activity_id,
                                   "agent": json.dumps(AGENT), "registration": reg}, json=suspend)
    print("PUT suspend_data", r1.status_code)

    # 4b. PUT bookmark
    r2 = s.put(BASE_STATE, params={"stateId": "bookmark", "activityId": activity_id,
                                   "agent": json.dumps(AGENT), "registration": reg}, json={"page": "0"})
    print("PUT bookmark", r2.status_code)

    # 4c. POST statements
    r3 = s.post(BASE_STMT, json=stmt)
    print("POST statements", r3.status_code, r3.text)

    # 4d. POST event analytics
    evt = {"data": {"type": "events", "attributes": {"name": "Activity_preview_complete.unity"}}}
    r4 = s.post(BASE_EVT, json=evt)
    print("POST events", r4.status_code)

    print(">>> Bot hoàn thành – điểm đã ghi:", f"{len(answers)}/{len(answers)}")

if __name__ == "__main__":
    main()