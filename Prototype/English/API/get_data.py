import requests
from datetime import datetime
import re
import json
import os


keys = ["4e6d6d4c-853f-4e86-8e01-46555d91271d", "2dc90c25-8733-4174-aded-7524cde0a1ea", "d68b089e-db75-452c-a3e6-185e8171e1ef"]
key = "0afa6520-34c2-4829-9953-22b098670ee9"
cookie = "_unity_session=32237839b27c83dc7b546681e72c5c14"
# Cấu hình URL và headers
url = "https://learn.eltngl.com/cdn_proxy/"+ key + "/data.js"

# Headers mô phỏng trình duyệt Chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Cache-Control": "max-age=0",
    # Cookie (thay thế bằng session hợp lệ của bạn nếu cần)
    "Cookie": cookie
}

# Các header điều kiện để kiểm tra cập nhật (ETag & Last-Modified)
# Bạn có thể lưu lại từ lần request trước để dùng cho lần sau
etag = '"3fc44ff16b15b75604b65f49a04aba67"'
last_modified = "Thu, 18 Sep 2025 10:18:25 GMT"

# headers["If-None-Match"] = f'W/{etag}'
# headers["If-Modified-Since"] = last_modified
js_content = '''
'''
try:
    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")

    if response.status_code == 304:

        print("✅ Nội dung chưa thay đổi (304 Not Modified). Dùng dữ liệu cũ.")
    elif response.status_code == 200:
        print("✅ Nhận được dữ liệu mới:")
        js_content = response.text
        # In nội dung (có thể là JS hoặc JSON)

    else:
        print(f"❌ Lỗi không mong muốn: {response.status_code}")


except requests.exceptions.RequestException as e:
    print(f"❌ Lỗi kết nối: {e}")


# 2. Tách phần JSON
raw_json = re.search(r'ajaxData\s*=\s*({.*?})\s*;', js_content, flags=re.S).group(1)
data = json.loads(raw_json)


# 3. Tạo thư mục chứa kết quả
os.makedirs(r'./output', exist_ok=True)

# 4. Ghi từng file
for filename, xml_escaped in data.items():
    xml_clean = xml_escaped.encode().decode('unicode-escape')
    with open(os.path.join('output' , filename), 'w', encoding='utf-8') as f:
        f.write(xml_clean)

print('Đã ghi xong các file vào thư mục "output"')