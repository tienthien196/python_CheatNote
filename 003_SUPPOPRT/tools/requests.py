# -*- coding: utf-8 -*-
"""
Requests Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module requests trong Python
"""

import sys
try:
    import requests
except ImportError:
    requests = None  # Để chạy trong môi trường không có requests

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
url = "https://httpbin.org/get"
post_url = "https://httpbin.org/post"
sample_params = {"key": "value"}
sample_data = {"name": "Python", "version": 3.10}
sample_headers = {"User-Agent": "Python-Requests"}
sample_json = {"id": 1, "title": "Test"}

# Kiểm tra nếu requests được cài đặt
if not requests:
    print("Module requests không được cài đặt. Cài đặt bằng: pip install requests")
    sys.exit(1)

# ==============================================================================
# 1. GỬI YÊU CẦU GET
# ==============================================================================
print_section("1. Gửi yêu cầu GET")
response = requests.get(url)
print_example('requests.get("https://httpbin.org/get")', "Gửi GET cơ bản", response.status_code)
response = requests.get(url, params=sample_params)
print_example('requests.get(..., params={"key": "value"})', "GET với tham số", response.url)
response = requests.get(url, headers=sample_headers)
print_example('requests.get(..., headers={...})', "GET với tiêu đề", response.request.headers["User-Agent"])

# ==============================================================================
# 2. GỬI YÊU CẦU POST
# ==============================================================================
print_section("2. Gửi yêu cầu POST")
response = requests.post(post_url, data=sample_data)
print_example('requests.post(..., data={...})', "POST với dữ liệu form", response.status_code)
response = requests.post(post_url, json=sample_json)
print_example('requests.post(..., json={...})', "POST với dữ liệu JSON", response.json().get("json"))
response = requests.post(post_url, data=sample_data, headers=sample_headers)
print_example('requests.post(..., headers={...})', "POST với tiêu đề", response.request.headers["User-Agent"])

# ==============================================================================
# 3. CÁC PHƯƠNG THỨC HTTP KHÁC
# ==============================================================================
print_section("3. Các phương thức HTTP khác")
response = requests.put(post_url, data=sample_data)
print_example('requests.put(...)', "Gửi yêu cầu PUT", response.status_code)
response = requests.delete("https://httpbin.org/delete")
print_example('requests.delete(...)', "Gửi yêu cầu DELETE", response.status_code)
response = requests.patch(post_url, data=sample_data)
print_example('requests.patch(...)', "Gửi yêu cầu PATCH", response.status_code)

# ==============================================================================
# 4. XỬ LÝ PHẢN HỒI
# ==============================================================================
print_section("4. Xử lý phản hồi")
response = requests.get(url)
print_example('response.status_code', "Mã trạng thái", response.status_code)
print_example('response.text', "Nội dung dạng chuỗi", response.text[:50] + "...")
print_example('response.json()', "Nội dung dạng JSON", response.json().get("url"))
print_example('response.headers', "Tiêu đề phản hồi", dict(response.headers).get("Content-Type"))
print_example('response.ok', "Kiểm tra phản hồi OK", response.ok)

# ==============================================================================
# 5. QUẢN LÝ TIÊU ĐỀ VÀ THAM SỐ
# ==============================================================================
print_section("5. Quản lý tiêu đề và tham số")
response = requests.get(url, params={"q": "test", "id": 1})
print_example('requests.get(..., params={...})', "Tham số truy vấn", response.url)
response = requests.get(url, headers={"Accept": "application/json"})
print_example('requests.get(..., headers={...})', "Tiêu đề tùy chỉnh", response.request.headers["Accept"])
response = requests.get(url, cookies={"session": "abc123"})
print_example('requests.get(..., cookies={...})', "Gửi cookie", response.request.headers.get("Cookie"))

# ==============================================================================
# 6. XỬ LÝ LỖI
# ==============================================================================
print_section("6. Xử lý lỗi")
try:
    response = requests.get("https://nonexistent.example.com")
except requests.exceptions.RequestException as e:
    print_example('requests.get("nonexistent")', "Lỗi kết nối", f"Lỗi: {e}")
try:
    response = requests.get(url, timeout=0.001)
except requests.exceptions.Timeout as e:
    print_example('requests.get(..., timeout=0.001)', "Lỗi hết thời gian", f"Lỗi: {e}")
response = requests.get("https://httpbin.org/status/404")
print_example('response.raise_for_status()', "Kiểm tra lỗi HTTP", "Lỗi 404" if not response.ok else "OK")

# ==============================================================================
# 7. GỬI FILE
# ==============================================================================
print_section("7. Gửi file")
files = {"file": ("test.txt", b"Sample content")}
response = requests.post("https://httpbin.org/post", files=files)
print_example('requests.post(..., files={...})', "Gửi file", response.status_code)
multipart_data = {"field": "value"}
response = requests.post(post_url, data=multipart_data, files=files)
print_example('requests.post(..., data, files)', "Gửi multipart", response.status_code)

# ==============================================================================
# 8. QUẢN LÝ PHIÊN (SESSION)
# ==============================================================================
print_section("8. Quản lý phiên")
session = requests.Session()
session.headers.update({"User-Agent": "Custom-Agent"})
response = session.get(url)
print_example('session.get(...)', "GET với phiên", response.request.headers["User-Agent"])
session.auth = ("user", "pass")
response = session.get("https://httpbin.org/basic-auth/user/pass")
print_example('session.auth = ("user", "pass")', "Xác thực cơ bản", response.status_code)

# ==============================================================================
# 9. XỬ LÝ STREAMING
# ==============================================================================
print_section("9. Xử lý streaming")
response = requests.get("https://httpbin.org/stream/3", stream=True)
stream_data = [line.decode("utf-8") for line in response.iter_lines() if line]
print_example('response.iter_lines()', "Đọc dữ liệu theo dòng", len(stream_data))
response = requests.get("https://httpbin.org/stream-bytes/1024", stream=True)
content = sum(len(chunk) for chunk in response.iter_content(chunk_size=128))
print_example('response.iter_content(chunk_size=128)', "Đọc dữ liệu theo khối", content)

# ==============================================================================
# 10. THÔNG TIN MODULE REQUESTS
# ==============================================================================
print_section("10. Thông tin module requests")
all_functions = [m for m in dir(requests) if not m.startswith("_") and callable(getattr(requests, m))]
print(f"Tổng cộng: {len(all_functions)} hàm")
print("\n".join(f" • {func:<20} → {getattr(requests, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'REQUESTS MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://requests.readthedocs.io/en/latest/':^70}")
print("="*70)