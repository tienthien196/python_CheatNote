import json, requests, datetime as dt, uuid

# ===== THÔNG SỐ CẦN THAY =====
COOKIE = '_unity_session=59f25bd45736f95ebbcaad5fcb6ea948'   # cookie nguyên bản
AGENT    = {"objectType":"Agent","account":{"name":"7eaa9602-e032-4de6-b645-e42c19fdd16f","homePage":"http://web-cen-unity-prod.avallain.net/identifiers/users/7eaa9602-e032-4de6-b645-e42c19fdd16f"}}
REG      = "16eea48a-9c6e-4371-a0d6-d4c5c5114938"
ACT_ID   = "http://web-cen-unity-prod.avallain.net/identifiers/contents/d32ef972-fdba-4551-aebb-dc3f18f260e5"
# =============================

HEADERS = {
    'Origin': 'https://learn.eltngl.com',
    'Referer': f'https://learn.eltngl.com/cdn_proxy/d32ef972-fdba-4551-aebb-dc3f18f260e5/index',
    'Content-Type': 'application/json',
    'X-Experience-API-Version': '1.0.1',
    'Cookie': COOKIE
}

BASE_STATE = f'https://learn.eltngl.com/lrs/xAPI/activities/state'
BASE_STMT  = f'https://learn.eltngl.com/lrs/xAPI/statements'

# 1. Đáp án đúng từ XML
ANSWERS = [
    {"id":f"e{i}","version":1,"value":v} 
    for i,v in enumerate(["starts","watches","flies","passes","lives","studies","finishes","relaxes"])
]
ACT_STATE = [{"filled":True,"correct":True,"id":f"e{i}"} for i in range(8)]

# 2. Build suspend_data
suspend = {
    "interaction_839104480":{
        "items":[{"items":ANSWERS,"activityState":ACT_STATE}],
        "status":"corrected","checkAttempts":1,"manualCheckAttempts":0,
        "solutionHint":False,"notes":[],"visited":True,
        "duration":1279255.7,"checkAnswerOnSubmitPending":True
    },
    "duration":3522329,"idleTime":0,
    "attemptID":"58d4b32d-ecce-4323-8692-1f80dccd9234","submitPending":True
}

# 3. Build statement
stmt = [{
    "id": str(uuid.uuid4()),
    "timestamp": dt.datetime.utcnow().isoformat()+'Z',
    "actor": AGENT,
    "verb": {"id":"http://adlnet.gov/expapi/verbs/answered","display":{"und":"answered"}},
    "result":{
        "duration":"PT37M21S",
        "response":json.dumps({
            "items":[{"items":ANSWERS,"activityState":ACT_STATE}],
            "status":"corrected","checkAttempts":1,"manualCheckAttempts":0,
            "solutionHint":False,"notes":[],"visited":True,"duration":1279255.7
        }),
        "score":{"scaled":1,"raw":8,"min":0,"max":8}
    },
    "context":{
        "registration":REG,
        "extensions":{"http://id.tincanapi.com/extension/attempt-id":"58d4b32d-ecce-4323-8692-1f80dccd9234"},
        "contextActivities":{"parent":[{"id":ACT_ID,"objectType":"Activity"}]}
    },
    "object":{
        "id":ACT_ID+"/0",
        "objectType":"Activity",
        "definition":{
            "name":{"und":"1a | Grammar 1 | Exercise 2, Interaction page 1"},
            "extensions":{"http://xapi.avallain.net/extensions/uniqueId":"cf366c63-c386-44d5-a9ca-25c83ae2fed1"}
        }
    }
}]

def run():
    # 1. PUT suspend_data
    r1 = requests.put(
        BASE_STATE,
        params={"stateId":"suspend_data","activityId":ACT_ID,"agent":json.dumps(AGENT),"registration":REG},
        headers=HEADERS, json=suspend
    )
    print('PUT suspend_data', r1.status_code)

    # 2. PUT bookmark
    r2 = requests.put(
        BASE_STATE,
        params={"stateId":"bookmark","activityId":ACT_ID,"agent":json.dumps(AGENT),"registration":REG},
        headers=HEADERS, json={"page":"0"}
    )
    print('PUT bookmark', r2.status_code)

    # 3. POST statements
    r3 = requests.post(BASE_STMT, headers=HEADERS, json=stmt)
    print('POST statements', r3.status_code, r3.text)

if __name__ == '__main__':
    run()