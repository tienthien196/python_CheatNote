import requests
import re
import json
import uuid
from datetime import datetime, timezone

# ================================
# Cấu hình người dùng
# ================================
_SESSION_COOKIE = "_unity_session=32237839b27c83dc7b546681e72c5c14"
_GROUP_ID = "841496c0-b4f4-47f3-8283-88b0a9d39ebe"
_STUDENT_ID = "7eaa9602-e032-4de6-b645-e42c19fdd16f"

_ASSIGNMENT_ID = "dded0533-b8c8-4045-9d2c-3fb630b6b27c"
_CONTENT_ID = "1f5408e9-cfd8-4cc6-a025-ca030fafa380"
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
        "name": _STUDENT_ID,  # fallback
        "homePage": f"http://web-cen-unity-prod.avallain.net/identifiers/users/{_STUDENT_ID}"
    }
}

# Tự động cập nhật AGENT từ API
def fetch_student_info():
    global AGENT
    url = f"{BASE_URL}/api/v2/groups/{_GROUP_ID}/students/{_CONTENT_ID.replace('-', '')[:36]}/specific_content"
    # Không cần gọi thật nếu bạn đã biết student_id
    # Tạm thời giữ nguyên như trên

# ================================
# 1. Lấy metadata bài học
# ================================
def fetch_content_metadata():
    url = f"{BASE_URL}/api/v2/groups/{_GROUP_ID}/students/{_CONTENT_ID.replace('-', '')[:36]}/specific_content"
    params = {
        "group_id": _GROUP_ID,
        "assignment_id": _ASSIGNMENT_ID,
        "student_id": _CONTENT_ID.replace('-', '')[:36]
    }
    try:
        resp = requests.get(
            url,
            headers={k: v for k, v in HEADERS.items() if k != 'Content-Type'},
            params=params,
            timeout=10
        )
        if resp.status_code == 200:
            data = resp.json()
            for item in data["contents"]:
                if item["id"] == _CONTENT_ID:
                    return item
    except:
        pass
    return {"name": "Unknown Exercise", "id": _CONTENT_ID}

# ================================
# 2. Lấy đáp án từ data.js
# ================================
def fetch_answers_from_data_js():
    url = f"{BASE_URL}/cdn_proxy/{_CONTENT_ID}/data.js"
    resp = requests.get(url, headers={k: v for k, v in HEADERS.items() if k != 'Content-Type'}, timeout=10)
    resp.raise_for_status()
    match = re.search(r'ajaxData\s*=\s*({.*?})\s*;', resp.text, re.S)
    if not match:
        raise ValueError("Không tìm thấy ajaxData trong data.js")
    ajax_data = json.loads(match.group(1))
    answers = []
    for filename, xml_escaped in ajax_data.items():
        if not (filename.startswith("cat") and filename.endswith(".xml")):
            continue
        xml_clean = xml_escaped.encode().decode('unicode-escape')
        vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>\s*</correctResponse>', xml_clean, re.I | re.S)
        for v in vals:
           answers.append(v.strip()) 
    if not answers:
        raise ValueError("Không tìm thấy cat*.xml nào chứa đáp án!")
    return answers

# ================================
# 3. GET suspend_data gốc
# ================================
def get_suspend_data(activity_id, agent, registration):
    url = f"{BASE_URL}/lrs/xAPI/activities/state"
    params = {
        "stateId": "suspend_data",
        "activityId": activity_id,
        "agent": json.dumps(agent, separators=(',', ':')),
        "registration": registration
    }
    try:
        resp = requests.get(url, params=params, headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            return resp.json()
    except:
        print("has error get suspend assigment")
    return None

# ================================
# 4. Cập nhật đáp án vào suspend_data gốc
# ================================
def update_suspend_data(original_data: dict, answers: list):
    interaction_id = None
    for k in original_data:
        if k.startswith("interaction_"):
            interaction_id = k
            break

    if interaction_id is None:
        # Tạo mới nếu chưa có (hiếm)
        interaction_id = f"interaction_{abs(hash(_CONTENT_ID)) % 10**9}"
        original_data[interaction_id] = {
            "items": [{"items": [None], "activityState": []} for _ in answers],
            "status": "input",
            "checkAttempts": 0,
            "manualCheckAttempts": 0,
            "solutionHint": False,
            "notes": [],
            "visited": True,
            "duration": 1102775.1
        }

    interaction = original_data[interaction_id]
    items = interaction["items"]

    ans_idx = 0
    for item in items:
        if ans_idx >= len(answers):
            break
        state = item.get("activityState", [{}])[0] if item.get("activityState") else {}
        if state.get("prefilled") or state.get("disabled"):
            continue
        if item.get("items") and item["items"][0] is None:
            item["items"] = [{"id": "e0", "version": 1, "value": answers[ans_idx]}]
            item["activityState"] = [{"filled": True, "correct": True, "id": "e0"}]
            ans_idx += 1

    interaction["status"] = "corrected"
    interaction["checkAttempts"] = 1
    original_data["attempts"] = 1
    original_data["attemptID"] = str(uuid.uuid4())
    original_data["duration"] = 1891828
    original_data["idleTime"] = 0

    return original_data, interaction_id

# ================================
# 5. PUT state (suspend_data / bookmark)
# ================================
def put_state(state_id: str, payload, activity_id: str, agent: dict, registration: str):
    url = f"{BASE_URL}/lrs/xAPI/activities/state"
    params = {
        "stateId": state_id,
        "activityId": activity_id,
        "agent": json.dumps(agent, separators=(',', ':')),
        "registration": registration
    }
    resp = requests.put(url, params=params, json=payload, headers=HEADERS)
    print(f"✅ PUT {state_id}: {resp.status_code}")
    return resp

# ================================
# 6. Gửi xAPI statements
# ================================
def send_xapi_statements(
    activity_main_id: str,
    object_name: str,
    interaction_data: dict,
    answers: list,
    registration: str,
    attempt_id: str
):
    object_id = f"{activity_main_id}/{_PAGE_INDEX}"
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    max_score = len(answers)

    # Statement 1: answered
    stmt1 = {
        "id": str(uuid.uuid4()),
        "timestamp": timestamp,
        "actor": AGENT,
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/answered",
            "display": {"und": "answered"}
        },
        "result": {
            "duration": "PT13M7S",
            "response": json.dumps(interaction_data, separators=(',', ':')),
            "score": {"scaled": 1.0, "raw": max_score, "min": 0, "max": max_score}
        },
        "context": {
            "registration": registration,
            "extensions": {
                "http://id.tincanapi.com/extension/attempt-id": attempt_id
            },
            "contextActivities": {
                "parent": [{"id": activity_main_id, "objectType": "Activity"}]
            }
        },
        "object": {
            "id": object_id,
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"{object_name}, Interaction page {_PAGE_INDEX + 1}"},
                "extensions": {
                    "http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())
                }
            }
        }
    }

    # Statements 2: scored + attempted
    stmt2 = {
        "id": str(uuid.uuid4()),
        "timestamp": timestamp,
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
            "id": activity_main_id,
            "objectType": "Activity",
            "definition": {"name": {"und": object_name}}
        }
    }

    stmt3 = {
        "id": str(uuid.uuid4()),
        "timestamp": timestamp,
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
            "id": activity_main_id,
            "objectType": "Activity",
            "definition": {"name": {"und": object_name}}
        }
    }

    url = f"{BASE_URL}/lrs/xAPI/statements"
    resp1 = requests.post(url, json=[stmt1], headers=HEADERS)
    print(f"✅ POST answered: {resp1.status_code}")

    resp2 = requests.post(url, json=[stmt2, stmt3], headers=HEADERS)
    print(f"✅ POST scored + attempted: {resp2.status_code}")

# ================================
# 7. Main
# ================================
def main():
    print("🔍 Lấy metadata bài học...")
    meta = fetch_content_metadata()
    base_name = meta["name"]
    print(f"📚 Bài: {base_name}")

    print("🔍 Lấy đáp án từ data.js...") 
    answers = fetch_answers_from_data_js()
    print(f"✅ Đáp án: {answers}") # đáp án  list

    activity_main_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"
    registration = "34630a7b-e652-4bec-bd54-fd0d274f0e7a"

    print("🔍 GET suspend_data gốc...")
    original_suspend = get_suspend_data(activity_main_id, AGENT, registration)
    print("this is ỏigin suppend  :",original_suspend) # có cấu trúc susspend dict

    print("🔄 Cập nhật đáp án vào cấu trúc gốc...")
    updated_suspend, interaction_id = update_suspend_data(original_suspend, answers)

    # ============= LẦN 1: PUT TRƯỚC KHI GỬI STATEMENTS =============
    put_state("suspend_data", updated_suspend, activity_main_id, AGENT, registration)
    put_state("bookmark", {"page": str(_PAGE_INDEX)}, activity_main_id, AGENT, registration)

    # ============= GỬI STATEMENTS =============
    interaction_data = updated_suspend[interaction_id]
    send_xapi_statements(activity_main_id, base_name, interaction_data, answers, registration, updated_suspend["attemptID"])

    # ============= LẦN 2: PUT SAU KHI GỬI STATEMENTS =============
    put_state("suspend_data", updated_suspend, activity_main_id, AGENT, registration)
    put_state("bookmark", {"page": str(_PAGE_INDEX)}, activity_main_id, AGENT, registration)

    print("\n🎉 Hoàn thành giả lập thành công!")

if __name__ == "__main__":
    main()