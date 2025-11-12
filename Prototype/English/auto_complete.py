import requests
import json
import re
import uuid
from datetime import datetime


KEY = "d73eea0c-396f-4494-a692-af003f567319"

# === CONFIG ===
COOKIE = "_unity_session=32237839b27c83dc7b546681e72c5c14"
AGENT = {
    "objectType": "Agent",
    "account": {
        "name": "7eaa9602-e032-4de6-b645-e42c19fdd16f",
        "homePage": "http://web-cen-unity-prod.avallain.net/identifiers/users/7eaa9602-e032-4de6-b645-e42c19fdd16f"
    }
}
ACTIVITY_ID = "http://web-cen-unity-prod.avallain.net/identifiers/contents/"+KEY
REGISTRATION = "f26ddcfe-22fc-4d2d-bd02-4db1888a59b8"
DATA_JS_URL = "https://learn.eltngl.com/cdn_proxy/"+KEY+"/data.js"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Cookie": COOKIE,
    "Content-Type": "application/json"
}

# === UTILS ===
def get_suspend_data():
    url = f"https://learn.eltngl.com/lrs/xAPI/activities/state"
    params = {
        "stateId": "suspend_data",
        "activityId": ACTIVITY_ID,
        "agent": json.dumps(AGENT),
        "registration": REGISTRATION
    }
    res = requests.get(url, headers=HEADERS, params=params)
    res.raise_for_status()
    return res.json()

def get_answers():
    res = requests.get(DATA_JS_URL, headers=HEADERS)
    res.raise_for_status()
    js = res.text
    raw_json = re.search(r'ajaxData\s*=\s*({.*?})\s*;', js, re.S).group(1)
    ajax_data = json.loads(raw_json)
    answers = []
    for key, xml_escaped in ajax_data.items():
        if not key.startswith("cat") or not key.endswith(".xml"):
            continue
        xml = xml_escaped.encode().decode('unicode-escape')
        vals = re.findall(r'<correctResponse>\s*<value>([^<]+)</value>\s*</correctResponse>', xml, re.I)
        for v in vals:
            answers.append(v.strip())
    return answers

def build_payload(key, answers, attempt_id):
    items = []
    for ans in answers:
        items.append({
            "items": [{"id": "e0", "version": 1, "value": ans}],
            "activityState": [{"filled": True, "correct": True, "id": "e0"}]
        })
    return {
        key: {
            "items": items,
            "status": "corrected",
            "checkAttempts": 1,
            "manualCheckAttempts": 0,
            "solutionHint": False,
            "notes": [],
            "visited": True,
            "duration": 1102775.1
        },
        "duration": 1891828,
        "idleTime": 0,
        "attemptID": attempt_id,
        "attempts": 1
    }

def put_suspend_data(payload):
    url = f"https://learn.eltngl.com/lrs/xAPI/activities/state"
    params = {
        "stateId": "suspend_data",
        "activityId": ACTIVITY_ID,
        "agent": json.dumps(AGENT),
        "registration": REGISTRATION
    }
    res = requests.put(url, headers=HEADERS, params=params, json=payload)
    res.raise_for_status()

def put_bookmark():
    url = f"https://learn.eltngl.com/lrs/xAPI/activities/state"
    params = {
        "stateId": "bookmark",
        "activityId": ACTIVITY_ID,
        "agent": json.dumps(AGENT),
        "registration": REGISTRATION
    }
    requests.put(url, headers=HEADERS, params=params, json={"page": "0"})

def post_statements(attempt_id, answers):
    answered = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/answered", "display": {"und": "answered"}},
        "result": {
            "duration": "PT13M7S",
            "response": json.dumps({
                "items": [
                    {"items": [{"id": "e0", "version": 1, "value": ans}], "activityState": [{"filled": True, "correct": True, "id": "e0"}]}
                    for ans in answers
                ],
                "status": "corrected",
                "checkAttempts": 1,
                "duration": 1102775.1
            }),
            "score": {"scaled": 1, "raw": len(answers), "min": 0, "max": len(answers)}
        },
        "context": {
            "registration": REGISTRATION,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": ACTIVITY_ID, "objectType": "Activity"}]}
        },
        "object": {
            "id": f"{ACTIVITY_ID}/0",
            "objectType": "Activity",
            "definition": {"name": {"und": "Auto Exercise"}, "extensions": {"http://xapi.avallain.net/extensions/uniqueId": "auto"}}
        }
    }

    scored = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "actor": AGENT,
        "verb": {"id": "http://adlnet.gov/expapi/verbs/scored", "display": {"und": "scored"}},
        "result": {
            "duration": "PT13M8S",
            "extensions": {
                "http://id.tincanapi.com/extension/duration": "PT31M32S",
                "http://xapi.avallain.net/extensions/idle-time": "PT0S"
            },
            "score": {"scaled": 1, "raw": len(answers), "min": 0, "max": len(answers)}
        },
        "context": {
            "registration": REGISTRATION,
            "extensions": {"http://id.tincanapi.com/extension/attempt-id": attempt_id},
            "contextActivities": {"parent": [{"id": ACTIVITY_ID, "objectType": "Activity"}]}
        },
        "object": {
            "id": ACTIVITY_ID,
            "objectType": "Activity",
            "definition": {"name": {"und": "Auto Exercise"}}
        }
    }

    url = "https://learn.eltngl.com/lrs/xAPI/statements"
    requests.post(url, headers=HEADERS, json=[answered])
    requests.post(url, headers=HEADERS, json=[scored])

# === MAIN ===
def main():
    print("🔍 Lấy suspend_data...")
    suspend = get_suspend_data()
    key = [k for k in suspend.keys() if k.startswith("interaction_")][0]
    attempt_id = suspend["attemptID"]

    print("🔍 Lấy đáp án từ data.js...")
    answers = get_answers()
    print("✅ Đáp án:", answers)

    print("🧠 Build payload...")
    payload = build_payload(key, answers, attempt_id)

    print("📤 PUT suspend_data lần 1...")
    put_suspend_data(payload)

    print("📤 PUT suspend_data lần 2...")
    put_suspend_data(payload)

    print("📤 PUT bookmark...")
    put_bookmark()

    print("📤 POST xAPI statements...")
    post_statements(attempt_id, answers)

    print("🎉 Xong! Bài đã auto-complete 100%.")

if __name__ == "__main__":
    main()