import requests

url = (
    "https://learn.eltngl.com/lrs/xAPI/activities/state"
    "?stateId=suspend_data"
    "&activityId=http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fcontents%2F55541a19-6e96-405b-9f4d-1ea1653fe6ba"
    "&agent=%7B%22objectType%22%3A%22Agent%22%2C%22account%22%3A%7B%22name%22%3A%22691faf92-92de-45f0-b84d-ae8dad27ed53%22%2C%22homePage%22%3A%22http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fusers%2F691faf92-92de-45f0-b84d-ae8dad27ed53%22%7D%7D"
    "&registration=9d767a0b-6d2c-4555-b7bc-cd21fec5d930"
)

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "authorization": "undefined",          # đúng như bản gốc
    "cookie": "_unity_session=a629be948ae4f6351e864ffed27c93a0",
    "if-none-match": 'W/"fed47a293b3c81625185b7a3ba133ab7904c22e5"',
    "priority": "u=1, i",
    "referer": (
        "https://learn.eltngl.com/cdn_proxy/55541a19-6e96-405b-9f4d-1ea1653fe6ba/index"
        "?a5_lo_profile=MTQ%3D&a5_options_overwrite=true&a5_restore=true&a5_start_task=0"
        "&a5_store=false&a5_stt_audio_lang=en-US"
        "&activityID=http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fcontents%2F55541a19-6e96-405b-9f4d-1ea1653fe6ba"
        "&agents=%7B%22user%22%3A%7B%22account%22%3A%7B%22homePage%22%3A%22http%3A%2F%2Fweb-cen-unity-prod.avallain.net%2Fidentifiers%2Fusers%2F691faf92-92de-45f0-b84d-ae8dad27ed53%22%2C%22name%22%3A%22691faf92-92de-45f0-b84d-ae8dad27ed53%22%7D%7D%7D"
        "&auth=&index_file=index.html&overview=false"
        "&reg=9d767a0b-6d2c-4555-b7bc-cd21fec5d930&registration=9d767a0b-6d2c-4555-b7bc-cd21fec5d930"
        "&statements=started%2Cterminated%2Cscored%2Cattempted%2Canswered&stores=%5B%7B%22endpoint%22%3A%22https%3A%2F%2Flearn.eltngl.com%2Flrs%2FxAPI%22%7D%5D"
    ),
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "x-experience-api-version": "1.0.1",
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print("Body:", response.text)