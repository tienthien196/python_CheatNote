import requests
import re
import json
import uuid
from datetime import datetime, timezone

# ================================
# Cấu hình toàn cục
# ================================
_SESSION_COOKIE = "_unity_session=32237839b27c83dc7b546681e72c5c14"
_GROUP_ID = "841496c0-b4f4-47f3-8283-88b0a9d39ebe"
_STUDENT_ID = "7eaa9602-e032-4de6-b645-e42c19fdd16f"

_ASSIGNMENT_ID = "dded0533-b8c8-4045-9d2c-3fb630b6b27c"
_CONTENT_ID = "e5778758-8883-43f6-9371-dd6eaa1ce09a"
_PAGE_INDEX = 0

BASE_URL = "https://learn.eltngl.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.6,en;q=0.5",
    "Content-Type": "application/json",
    "Origin": "https://learn.eltngl.com",
    "Referer": "https://learn.eltngl.com/",
    "Cookie": _SESSION_COOKIE,
    "Authorization": "undefined"
}

AGENT = {
    "objectType": "Agent",
    "account": {
        "name": _STUDENT_ID,
        "homePage": f"http://web-cen-unity-prod.avallain.net/identifiers/users/{_STUDENT_ID}"
    }
}

# ================================
# 1. Lấy metadata bài học
# ================================
def fetch_content_metadata():
    url = f"{BASE_URL}/api/v2/groups/{_GROUP_ID}/students/{_STUDENT_ID}/specific_content"
    params = {
        "group_id": _GROUP_ID,
        "assignment_id": _ASSIGNMENT_ID,
        "student_id": _STUDENT_ID
    }
    resp = requests.get(url, headers={k: v for k, v in HEADERS.items() if k != 'Content-Type'}, params=params)
    resp.raise_for_status()
    data = resp.json()
    for item in data["contents"]:
        if item["id"] == _CONTENT_ID:
            return item
    raise ValueError(f"Content ID {_CONTENT_ID} not found in assignment")

# ================================
# 2. Lấy đáp án từ data.js
# ================================
def fetch_answers_from_data_js():
    url = f"{BASE_URL}/cdn_proxy/{_CONTENT_ID}/data.js"
    resp = requests.get(url, headers={k: v for k, v in HEADERS.items() if k != 'Content-Type'})
    resp.raise_for_status()
    match = re.search(r'ajaxData\s*=\s*({.*?})\s*;', resp.text, re.S)
    if not match:
        raise ValueError("ajaxData not found in data.js")
    ajax_data = json.loads(match.group(1))
    answers = []
    for filename, xml_escaped in ajax_data.items():
        if not (filename.startswith("cat") and filename.endswith(".xml")):
            continue
        xml_clean = xml_escaped.encode().decode('unicode-escape')
        vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>\s*</correctResponse>', xml_clean, re.I | re.S)
        answers.extend([v.strip() for v in vals])
    return answers

# ================================
# 3. Lấy interaction_id từ suspend_data GET
# ================================
def fetch_interaction_id():
    ACTIVITY_MAIN_ID = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"
    params = {
        "stateId": "suspend_data",
        "activityId": ACTIVITY_MAIN_ID,
        "agent": json.dumps(AGENT, separators=(',', ':')),
        "registration": str(uuid.uuid4())  # registration tạm
    }
    resp = requests.get(f"{BASE_URL}/lrs/xAPI/activities/state", params=params, headers=HEADERS)
    if resp.status_code == 200:
        data = resp.json()
        keys = [k for k in data.keys() if k.startswith("interaction_")]
        if keys:
            return keys[0]
    # Fallback: dùng giá trị mặc định nếu không có
    return f"interaction_{abs(hash(_CONTENT_ID)) % 10**9}"

# ================================
# 4. Xây dựng suspend_data payload
# ================================
def build_suspend_payload(answers, interaction_id, status="corrected", check_attempts=1, attempts=1):
    items = []
    for ans in answers:
        items.append({
            "items": [{"id": "e0", "version": 1, "value": ans}],
            "activityState": [{"filled": True, "correct": True, "id": "e0"}]
        })
    return {
        interaction_id: {
            "items": items,
            "status": status,
            "checkAttempts": check_attempts,
            "manualCheckAttempts": 0,
            "solutionHint": False,
            "notes": [],
            "visited": True,
            "duration": 1102775.1
        },
        "duration": 1891828,
        "idleTime": 0,
        "attemptID": str(uuid.uuid4()),
        "attempts": attempts
    }

# ================================
# 5. PUT suspend_data & bookmark
# ================================
def put_state(state_id, payload):
    ACTIVITY_MAIN_ID = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"
    params = {
        "stateId": state_id,
        "activityId": ACTIVITY_MAIN_ID,
        "agent": json.dumps(AGENT, separators=(',', ':')),
        "registration": str(uuid.uuid4())
    }
    url = f"{BASE_URL}/lrs/xAPI/activities/state"
    resp = requests.put(url, params=params, json=payload, headers=HEADERS)
    print(f"✅ PUT {state_id}: {resp.status_code}")
    return resp

# ================================
# 6. Gửi xAPI statements
# ================================
def send_xapi_statements(
    base_name: str,
    interaction_data: dict,
    answers: list,
    attempt_id: str,
    registration: str
):
    ACTIVITY_MAIN_ID = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"
    OBJECT_ID = f"{ACTIVITY_MAIN_ID}/{_PAGE_INDEX}"
    OBJECT_NAME = f"{base_name}, Interaction page {_PAGE_INDEX + 1}"

    now = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    max_score = len(answers)

    stmt1 = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/answered",
            "display": {"und": "answered"}
        },
        "result": {
            "duration": f"PT13M7S",
            "response": json.dumps(interaction_data, separators=(',', ':')),
            "score": {"scaled": 1.0, "raw": max_score, "min": 0, "max": max_score}
        },
        "context": {
            "registration": registration,
            "extensions": {
                "http://id.tincanapi.com/extension/attempt-id": attempt_id
            },
            "contextActivities": {
                "parent": [{"id": ACTIVITY_MAIN_ID, "objectType": "Activity"}]
            }
        },
        "object": {
            "id": OBJECT_ID,
            "objectType": "Activity",
            "definition": {
                "name": {"und": OBJECT_NAME},
                "extensions": {
                    "http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())
                }
            }
        }
    }

    stmt2 = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/scored",
            "display": {"und": "scored"}
        },
        "result": {
            "duration": "PT13M8S",
            "extensions": {
                "http://id.tincanapi.com/extension/duration": "PT31M32S",
                "http://xapi.avallain.net/extensions/idle-time": "PT0S"
            },
            "score": {"scaled": 1.0, "raw": max_score, "min": 0, "max": max_score}
        },
        "context": {
            "registration": registration,
            "extensions": {
                "http://id.tincanapi.com/extension/attempt-id": attempt_id
            }
        },
        "object": {
            "id": ACTIVITY_MAIN_ID,
            "objectType": "Activity",
            "definition": {"name": {"und": base_name}}
        }
    }

    stmt3 = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
        "actor": AGENT,
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/attempted",
            "display": {"und": "attempted"}
        },
        "result": {
            "duration": "PT13M8S",
            "extensions": {
                "http://id.tincanapi.com/extension/duration": "PT31M32S",
                "http://xapi.avallain.net/extensions/idle-time": "PT0S"
            },
            "score": {"raw": 1, "min": 0, "max": 3}
        },
        "context": {
            "registration": registration,
            "extensions": {
                "http://id.tincanapi.com/extension/attempt-id": attempt_id
            }
        },
        "object": {
            "id": ACTIVITY_MAIN_ID,
            "objectType": "Activity",
            "definition": {"name": {"und": base_name}}
        }
    }

    # Gửi
    url = f"{BASE_URL}/lrs/xAPI/statements"
    resp1 = requests.post(url, json=[stmt1], headers=HEADERS)
    print(f"✅ POST answered: {resp1.status_code}")

    resp2 = requests.post(url, json=[stmt2, stmt3], headers=HEADERS)
    print(f"✅ POST scored + attempted: {resp2.status_code}")

# ================================
# 7. Main flow
# ================================
def main():
    print("🔍 Lấy metadata bài học...")
    meta = fetch_content_metadata()
    base_name = meta["name"]
    print(f"📚 Bài học: {base_name}")

    print("🔍 Lấy đáp án từ data.js...")
    answers = fetch_answers_from_data_js()
    print(f"✅ Đáp án: {answers}")

    print("🔍 Lấy interaction_id...")
    interaction_id = fetch_interaction_id()
    print(f"🆔 Interaction ID: {interaction_id}")

    registration = str(uuid.uuid4())
    attempt_id = str(uuid.uuid4())

    # ============= LẦN 1: Cập nhật trạng thái HOÀN THÀNH =============
    payload1 = build_suspend_payload(
        answers, interaction_id,
        status="corrected", check_attempts=1, attempts=1
    )
    payload1["attemptID"] = attempt_id
    put_state("suspend_data", payload1)
    put_state("bookmark", {"page": str(_PAGE_INDEX)})

    # ============= GỬI STATEMENTS =============
    interaction_data = payload1[interaction_id]
    send_xapi_statements(base_name, interaction_data, answers, attempt_id, registration)

    # ============= LẦN 2: Cập nhật lại lần cuối (như hành vi thật) =============
    payload2 = build_suspend_payload(
        answers, interaction_id,
        status="corrected", check_attempts=1, attempts=1
    )
    payload2["attemptID"] = attempt_id
    put_state("suspend_data", payload2)
    put_state("bookmark", {"page": str(_PAGE_INDEX)})

    print("\n🎉 Hoàn thành giả lập thành công!")

if __name__ == "__main__":
    main()