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
_CONTENT_ID = "4f47ed51-3715-4203-9fb5-9152b4065f08"
_PAGE_INDEX = 0

# ✅ Sửa: Loại bỏ khoảng trắng ở cuối URL
BASE_URL = "https://learn.eltngl.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.6,en;q=0.5",
    "Content-Type": "application/json",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/",
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
# 1. Lấy metadata 
# ================================
def fetch_content_metadata_and_registration():
    url = f"{BASE_URL}/api/v2/groups/{_GROUP_ID}/students/{_STUDENT_ID}/specific_content"
    params = {
        "group_id": _GROUP_ID,
        "assignment_id": _ASSIGNMENT_ID,
        "student_id": _STUDENT_ID
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
            # Tìm bài học
            content_item = None
            for item in data.get("contents", []):
                if item["id"] == _CONTENT_ID:
                    content_item = item
                    break
            if content_item is None:
                content_item = {"name": "Unknown Exercise", "id": _CONTENT_ID}

            return content_item
    except Exception as e:
        print(f"❌ Lỗi khi lấy metadata: {e}")
    # fallback
    return {"name": "Unknown Exercise", "id": _CONTENT_ID}, str(uuid.uuid4())

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
        vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>', xml_clean, re.I | re.S)
        for v in vals:
            primary_ans = v.strip().split('|')[0]
            answers.append(primary_ans)
    if not answers:
        raise ValueError("Không tìm thấy đáp án trong cat*.xml!")
    return answers

# ================================
# 3. GET suspend_data
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
        else:
            print(f"⚠️  Không có suspend_data (status: {resp.status_code}) → sẽ return none dict.")
            return {}
    except Exception as e:
        print(f"❌ Lỗi khi GET suspend_data: {e}")
        return {}

# ================================
# 4. Cập nhật suspend_data
# ================================
def update_suspend_data(original_data: dict, answers: list):
    interaction_id = None
    for k in original_data:
        if k.startswith("interaction_"):
            interaction_id = k
            break

    if interaction_id is None:
        interaction_id = "interaction_0"

    items = []
    for ans in answers:
        items.append({
            "items": [{"id": "e0", "version": 1, "value": ans}],
            "activityState": [{"filled": True, "correct": True, "id": "e0"}]
        })

    original_data[interaction_id] = {
        "items": items,
        "status": "corrected",
        "checkAttempts": 1,
        "manualCheckAttempts": 0,
        "solutionHint": False,
        "notes": [],
        "visited": True,
        "duration": 2499836.30000007,
        "checkAnswerOnSubmitPending": True
    }
    original_data["attempts"] = 1
    original_data["attemptID"] = str(uuid.uuid4())
    original_data["duration"] = 3203525.10000026
    original_data["idleTime"] = 0
    original_data["submitPending"] = True

    return original_data, interaction_id

# ================================
# 5. PUT state
# ================================
def put_state(state_id: str, payload: dict, activity_id: str, agent: dict, registration: str):
    url = f"{BASE_URL}/lrs/xAPI/activities/state"
    params = {
        "stateId": state_id,
        "activityId": activity_id,
        "agent": json.dumps(agent, separators=(',', ':')),
        "registration": registration
    }
    resp = requests.put(url, params=params, json=payload, headers=HEADERS)
    print(f"✅ PUT {state_id}: {resp.status_code}")
    return resp.status_code in (200, 204)

# ================================
# 6. Gửi xAPI statements
# ================================

def send_start_statement(uid, activity_main_id, object_name, registration, attempt_id):
    object_id = f"{activity_main_id}/{_PAGE_INDEX}"
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

    stmt = {
        "id": uid,
        "timestamp": timestamp,
        "actor": AGENT,
        "verb": {"id": "http://activitystrea.ms/schema/1.0/start", "display": {"und": "started"}},
        "context": {
            "registration": registration,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": activity_main_id, "objectType": "Activity"}]}
        },
        "object": {
            "id": object_id,
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"{object_name}, Interaction page {_PAGE_INDEX + 1}"},
                "extensions": {"http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())}
            }
        }
    }

    resp = requests.post(f"{BASE_URL}/lrs/xAPI/statements", json=[stmt], headers=HEADERS)
    print(f"✅ POST Started: {resp.status_code}")
    return resp.status_code == 200

def send_answered_statement(uid, activity_main_id, object_name, interaction_data, answers, registration, attempt_id):
    object_id = f"{activity_main_id}/{_PAGE_INDEX}"
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    max_score = len(answers)

    stmt = {
        "id": uid,
        "timestamp": timestamp,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"und": "answered"}},
        "result": {
            "duration": "PT13M7S",
            "response": json.dumps(interaction_data, separators=(',', ':')),
            "score": {"scaled": 1.0, "raw": max_score, "min": 0, "max": max_score}
        },
        "context": {
            "registration": registration,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": activity_main_id, "objectType": "Activity"}]}
        },
        "object": {
            "id": object_id,
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"{object_name}, Interaction page {_PAGE_INDEX + 1}"},
                "extensions": {"http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())}
            }
        }
    }

    resp = requests.post(f"{BASE_URL}/lrs/xAPI/statements", json=[stmt], headers=HEADERS)
    print(f"✅ POST answered: {resp.status_code}")
    return resp.status_code == 200

def send_scored_attempted_statements(uid, activity_main_id, object_name, answers, registration, attempt_id):
    timestamp = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    max_score = len(answers)

    scored = {
        "id": uid,
        "timestamp": timestamp,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/scored", "display": {"und": "scored"}},
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
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id}
        },
        "object": {
            "id": activity_main_id,
            "objectType": "Activity",
            "definition": {"name": {"und": object_name}}
        }
    }

    attempted = {
        "id": str(uuid.uuid4()),
        "timestamp": timestamp,
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/attempted", "display": {"und": "attempted"}},
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
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id}
        },
        "object": {
            "id": activity_main_id,
            "objectType": "Activity",
            "definition": {"name": {"und": object_name}}
        }
    }

    resp = requests.post(f"{BASE_URL}/lrs/xAPI/statements", json=[scored], headers=HEADERS)
    print(f"✅ POST scored + attempted: {resp.status_code}")
    return resp.status_code == 200

# ================================
# 7. Main — HOÀN CHỈNH
# ================================
def main():
    activity_main_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"
    meta, registration = fetch_content_metadata_and_registration()

    register_lession_id  = str(uuid.uuid4())
    register_registration = "d605976c-8c54-490c-9036-014ce7ac4da5"
    attempt_id = str(uuid.uuid4())
    # send_start_statement(register_lession_id,activity_main_id, meta["name"], register_registration, attempt_id)

    print("🔍 Lấy metadata và registration...")
    registration = register_registration
    # registration = "9f55b2b6-2222-43df-a848-0051b6f18722"
    base_name = meta["name"]
    print(f"📚 Bài: {base_name}")
    print(f"🔑 Registration: {registration}")

    print("🔍 Lấy đáp án từ data.js...")
    answers = fetch_answers_from_data_js()
    print(f"✅ Đáp án: {answers}")

    

    print("🔍 GET suspend_data gốc...")
    original_suspend = get_suspend_data(activity_main_id, AGENT, register_registration)
    print("📥 Dữ liệu suspend hiện tại:", json.dumps(original_suspend, indent=2, ensure_ascii=False))

    print("🔄 Cập nhật đáp án vào suspend_data...")
    updated_suspend, interaction_id = update_suspend_data(original_suspend, answers)
    print("- This is data update", (updated_suspend))
     

    # ============= LẦN 1: PUT trước `answered` =============
    put_state("suspend_data", updated_suspend, activity_main_id, AGENT, register_registration)
    put_state("bookmark", {"page": str(_PAGE_INDEX)}, activity_main_id, AGENT, register_registration)

    # # Gửi `answered`
    # send_answered_statement(register_lession_id,
    #     activity_main_id, base_name,
    #     updated_suspend[interaction_id],
    #     answers, registration, attempt_id
    # )

    # # ============= LẦN 2: PUT trước `scored` + `attempted` =============
    # put_state("suspend_data", updated_suspend, activity_main_id, AGENT, register_registration)
    # put_state("bookmark", {"page": str(_PAGE_INDEX)}, activity_main_id, AGENT, register_registration)

    # # Gửi `scored` + `attempted`
    # send_scored_attempted_statements(register_lession_id,activity_main_id, base_name, answers, register_registration, attempt_id)

    print("\n🎉 Hoàn thành: 2 lần PUT + 2 request xAPI (3 statements)!")


if __name__ == "__main__":
    main()