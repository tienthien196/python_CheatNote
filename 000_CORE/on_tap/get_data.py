import requests
from datetime import datetime

key = "d32ef972-fdba-4551-aebb-dc3f18f260e5"
cookie = "_unity_session=a629be948ae4f6351e864ffed27c93a0"
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

try:
    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")

    if response.status_code == 304:
        print(response.text)
        print("✅ Nội dung chưa thay đổi (304 Not Modified). Dùng dữ liệu cũ.")
    elif response.status_code == 200:
        print("✅ Nhận được dữ liệu mới:")
        # In nội dung (có thể là JS hoặc JSON)
        print(response.text)
    else:
        print(f"❌ Lỗi không mong muốn: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"❌ Lỗi kết nối: {e}")