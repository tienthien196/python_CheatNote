import requests
import re
import json
import uuid
from datetime import datetime, timezone

# ================================
# Cấu hình
# ================================
_SESSION_COOKIE = "_unity_session=cf16606540b697d98e6416511fc9d0a0"
_GROUP_ID = "841496c0-b4f4-47f3-8283-88b0a9d39ebe"
_STUDENT_ID = "7eaa9602-e032-4de6-b645-e42c19fdd16f"

_ASSIGNMENT_ID = "dded0533-b8c8-4045-9d2c-3fb630b6b27c"
_CONTENT_ID = "9ea84b6c-c80c-4a47-8098-28a1ca55b91e"
_PAGE_INDEX = 0

BASE_URL = "https://learn.eltngl.com"  # ✅ Đã loại bỏ khoảng trắng thừa

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
# Hỗ trợ: Thời gian UTC theo chuẩn ISO 8601
# ================================
def _now_utc_iso():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


# ================================
# 1. Lấy metadata bài học và registration
# ================================
def fetch_lesson_metadata():
    url = f"{BASE_URL}/api/v2/groups/{_GROUP_ID}/students/{_STUDENT_ID}/specific_content"
    params = {
        "group_id": _GROUP_ID,
        "assignment_id": _ASSIGNMENT_ID,
        "student_id": _STUDENT_ID
    }
    headers = {k: v for k, v in HEADERS.items() if k != 'Content-Type'}

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        if resp.status_code != 200:
            raise Exception(f"HTTP {resp.status_code}")

        data = resp.json()
        contents = data.get("contents", [])
        content = next((item for item in contents if item["id"] == _CONTENT_ID), None)

        if content is None:
            content = {"name": "Unknown Exercise", "id": _CONTENT_ID}

        registrations = data.get("registrations", {})
        registration = registrations.get(_CONTENT_ID) or str(uuid.uuid4())
        if _CONTENT_ID not in registrations:
            print(f"⚠️ Không tìm thấy registration → dùng mới: {registration}")

        return content, registration

    except Exception as e:
        print(f"❌ Lỗi khi lấy metadata: {e}")
        return {"name": "Unknown Exercise", "id": _CONTENT_ID}, str(uuid.uuid4())


# ================================
# 2. Trích xuất đáp án từ data.js
# ================================
def extract_answers():
    url = f"{BASE_URL}/cdn_proxy/{_CONTENT_ID}/data.js"
    headers = {k: v for k, v in HEADERS.items() if k != 'Content-Type'}
    resp = requests.get(url, headers=headers, timeout=10)
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
        correct_vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>', xml_clean, re.I | re.S)
        for v in correct_vals:
            primary = v.strip().split('|')[0]
            answers.append(primary)

    if not answers:
        raise ValueError("Không tìm thấy đáp án hợp lệ trong cat*.xml")
    return answers


# ================================
# 3. Lấy và cập nhật suspend_data
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
            print(f"⚠️ Không có suspend_data (status: {resp.status_code}) → sẽ khởi tạo mới.")
            return {}
    except Exception as e:
        print(f"❌ Lỗi khi GET suspend_data: {e}")
        return {}


def build_suspend_payload(original_data, answers):
    interaction_key = next((k for k in original_data if k.startswith("interaction_")), "interaction_0")

    # Tạo items với ID tăng dần: e0, e1, e2, ...
    items = []
    for idx, ans in enumerate(answers):
        item_id = f"e{idx}"
        items.append({
            "items": [{"id": item_id, "version": 1, "value": ans, "selected": ans}],
            "activityState": [{"filled": True, "correct": True, "id": item_id}]
        })

    payload = original_data.copy()
    payload[interaction_key] = {
        "items": items,
        "status": "input",
        "checkAttempts": 0,
        "manualCheckAttempts": 0,
        "solutionHint": False,
        "notes": [],
        "visited": True,
        "duration": 2499836.30000007,
        # "checkAnswerOnSubmitPending": True
    }
    payload.update({
        "attempts": 1,
        "attemptID": original_data.get("attemptID"),
        "duration": original_data.get("duration", 3203525.10000026),
        "idleTime": 0,
        # "submitPending": True
    })
    return payload, interaction_key

# ================================
# 4. Gửi dữ liệu trạng thái (PUT suspend_data / bookmark)
# ================================
def send_suspend_state(payload, activity_id, registration):
    return _send_state("suspend_data", payload, activity_id, registration)


def send_bookmark_state(page_index, activity_id, registration):
    return _send_state("bookmark", {"page": str(page_index)}, activity_id, registration)


def _send_state(state_id, payload, activity_id, registration):
    url = f"{BASE_URL}/lrs/xAPI/activities/state"
    params = {
        "stateId": state_id,
        "activityId": activity_id,
        "agent": json.dumps(AGENT, separators=(',', ':')),
        "registration": registration
    }
    resp = requests.put(url, params=params, json=payload, headers=HEADERS)
    print(f"✅ PUT [{state_id}]: {resp.status_code}")
    return resp.status_code in (200, 204)


# ================================
# 5. Gửi xAPI statements
# ================================
def send_xapi_statements(statements):
    url = f"{BASE_URL}/lrs/xAPI/statements"
    resp = requests.post(url, json=statements, headers=HEADERS)
    print(f"✅ POST xAPI statements: {resp.status_code}")
    return resp.status_code == 200


def build_start_statement(activity_id, lesson_name, registration, attempt_id, page_index):
    return {
        "id": str(uuid.uuid4()),
        "timestamp": _now_utc_iso(),
        "actor": AGENT,
        "verb": {"id": "http://activitystrea.ms/schema/1.0/start", "display": {"und": "started"}},
        "context": {
            "registration": registration,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": activity_id, "objectType": "Activity"}]}
        },
        "object": {
            "id": f"{activity_id}/{page_index}",
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"{lesson_name}, Interaction page {page_index + 1}"},
                "extensions": {"http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())}
            }
        }
    }


def build_answered_statement(activity_id, lesson_name, interaction_data, answers, registration, attempt_id, page_index):
    return {
        "id": str(uuid.uuid4()),
        "timestamp": _now_utc_iso(),
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"und": "answered"}},
        "result": {
            "duration": "PT13M7S",
            "response": json.dumps(interaction_data, separators=(',', ':')),
            "score": {"scaled": 1.0, "raw": len(answers), "min": 0, "max": len(answers)}
        },
        "context": {
            "registration": registration,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": activity_id, "objectType": "Activity"}]}
        },
        "object": {
            "id": f"{activity_id}/{page_index}",
            "objectType": "Activity",
            "definition": {
                "name": {"und": f"{lesson_name}, Interaction page {page_index + 1}"},
                "extensions": {"http://xapi.avallain.net/extensions/uniqueId": str(uuid.uuid4())}
            }
        }
    }


def build_scored_and_attempted_statements(activity_id, lesson_name, answers, registration, attempt_id):
    max_score = len(answers)
    now = _now_utc_iso()
    common_context = {
        "registration": registration,
        "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id}
    }

    scored = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
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
        "context": common_context,
        "object": {
            "id": activity_id,
            "objectType": "Activity",
            "definition": {"name": {"und": lesson_name}}
        }
    }

    attempted = {
        "id": str(uuid.uuid4()),
        "timestamp": now,
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
        "context": common_context,
        "object": {
            "id": activity_id,
            "objectType": "Activity",
            "definition": {"name": {"und": lesson_name}}
        }
    }
    return [scored, attempted]


# ================================
# 6. Main
# ================================
def main():
    activity_id = f"http://web-cen-unity-prod.avallain.net/identifiers/contents/{_CONTENT_ID}"

    print("🔍 Lấy metadata bài học...")
    lesson_meta, _ = fetch_lesson_metadata()
    lesson_name = lesson_meta["name"]
    print(f"📚 Bài học: {lesson_name}")

    print("🔍 Lấy đáp án từ data.js...")
    answers = extract_answers()
    print(f"✅ Đáp án: {answers}")

    # Cấu hình giả lập registration cố định cho demo
    registration = "3d933b22-fe09-400b-b167-968ce7ad808f"
    # attempt_id = str(uuid.uuid4())
    print(f"🔑 Registration: {registration}")

    print("📥 Lấy suspend_data hiện tại...")
    original_suspend = get_suspend_data(activity_id, AGENT, registration)
    # print(json.dumps(original_suspend, indent=2, ensure_ascii=False))

    print("🔄 Cập nhật đáp án vào suspend_data...")
    updated_suspend, interaction_key = build_suspend_payload(original_suspend, answers)
    print("_ This is data update:", updated_suspend)

    # —————————————— GỬI TRẠNG THÁI ——————————————
    send_suspend_state(updated_suspend, activity_id, registration)
    send_bookmark_state(_PAGE_INDEX, activity_id, registration)

    # —————————————— GỬI xAPI (tùy chọn bật/tắt) ——————————————
    # statements = [
    #     build_start_statement(activity_id, lesson_name, registration, attempt_id, _PAGE_INDEX),
    #     build_answered_statement(activity_id, lesson_name, updated_suspend[interaction_key], answers, registration, attempt_id, _PAGE_INDEX),
    #     *build_scored_and_attempted_statements(activity_id, lesson_name, answers, registration, attempt_id)
    # ]
    # send_xapi_statements(statements)

    print("\n🎉 Hoàn tất: cập nhật trạng thái thành công!")


if __name__ == "__main__":
    main()