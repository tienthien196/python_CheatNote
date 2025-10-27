import requests
import json

DATA = (
    "https://learn.eltngl.com/lrs/xAPI/activities/state"
    "?stateId=suspend_data"
    "&activityId=http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fcontents%2F55541a19-6e96-405b-9f4d-1ea1653fe6ba"
    "&agent=%7B%22objectType%22%3A%22Agent%22%2C%22account%22%3A%7B%22name%22%3A%22691faf92-92de-45f0-b84d-ae8dad27ed53%22%2C%22homePage%22%3A%22http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fusers%2F691faf92-92de-45f0-b84d-ae8dad27ed53%22%7D%7D"
    "&registration=9d767a0b-6d2c-4555-b7bc-cd21fec5d930"
    )
COOKIE = "_unity_session=a629be948ae4f6351e864ffed27c93a0"

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",

    # "authorization": "undefined",          # đúng như bản gốc
    "cookie": "_unity_session=a629be948ae4f6351e864ffed27c93a0",

    "if-none-match": 'W/"fed47a293b3c81625185b7a3ba133ab7904c22e5"',
    "priority": "u=1, i"
}

def get_meta(url, h):
    if not h or not h.get("cookie", ""):
        return
    # headers.cookie = COOKIE
    try: 
        return  requests.get(url, headers = headers)
    except ConnectionError as e:
        print("ERROR CONENCT :", e)
        return e 
    ...

def text2im():
    text = """
{
        "key1":"bgg",
        "key2": "csg"
    }
    """
    print(dict(text)) ### bug

if __name__ == "__main__":...
    # database = get_meta(DATA, headers)
    # print(database.status_code)
    # if  not database.status_code or database.status_code !=200: 
    #     print("can not support API")
    # print(database.text)
    # ...