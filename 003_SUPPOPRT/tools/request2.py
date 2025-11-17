# -*- coding: utf-8 -*-
"""
Requests Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng thư viện requests trong Python
"""

import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(code, desc, result=None):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{code:<40} | {desc:<25} | Kết quả: {result or '...'}")

# ==============================================================================
# 1. CÀI ĐẶT & NHẬP THƯ VIỆN
# ==============================================================================
print_section("1. Cài đặt & Nhập thư viện")
print("Cài đặt: pip install requests")
print_example("import requests", "Nhập thư viện", "Thành công")

# ==============================================================================
# 2. CÁC PHƯƠNG THỨC HTTP CƠ BẢN
# ==============================================================================
print_section("2. Các phương thức HTTP cơ bản")
print_example("requests.get(url)", "GET", "Lấy dữ liệu")
print_example("requests.post(url, data=payload)", "POST", "Gửi dữ liệu")
print_example("requests.put(url, data=payload)", "PUT", "Cập nhật dữ liệu")
print_example("requests.patch(url, data=payload)", "PATCH", "Cập nhật một phần")
print_example("requests.delete(url)", "DELETE", "Xóa dữ liệu")

# ==============================================================================
# 3. GỬI YÊU CẦU ĐƠN GIẢN
# ==============================================================================
print_section("3. Gửi yêu cầu đơn giản")
print_example("r = requests.get('https://httpbin.org/get')", "Gửi GET request", "Response object")
print_example("r.status_code", "Mã trạng thái HTTP", "200")
print_example("r.headers", "Header phản hồi", "{'Content-Type': '...'}")
print_example("r.text", "Nội dung phản hồi (chuỗi)", "HTML hoặc JSON dạng chuỗi")
print_example("r.json()", "Nội dung phản hồi (JSON -> dict)", "{'args': {}, 'headers': ...}")
print_example("r.content", "Nội dung phản hồi (bytes)", b'...')

# ==============================================================================
# 4. THAM SỐ TRONG YÊU CẦU
# ==============================================================================
print_section("4. Tham số trong yêu cầu")
print_example("params = {'key': 'value'}", "Tham số URL", "Thành công")
print_example("requests.get(url, params=params)", "Gửi tham số GET", "https://example.com?key=value")

print("--- Dữ liệu gửi đi ---")
print_example("data = {'username': 'admin', 'password': '123'}", "Dữ liệu POST (form)", "dict")
print_example("requests.post(url, data=data)", "Gửi dữ liệu form", "Thành công")
print_example("json_data = {'name': 'Alice'}", "Dữ liệu JSON", "dict")
print_example("requests.post(url, json=json_data)", "Gửi JSON (tự động set header)", "Thành công")

# ==============================================================================
# 5. HEADER & AUTHENTICATION
# ==============================================================================
print_section("5. Header & Xác thực")
print_example("headers = {'User-Agent': 'My App 1.0'}", "Header tùy chỉnh", "Thành công")
print_example("requests.get(url, headers=headers)", "Gửi header", "Thành công")
print_example("requests.get(url, auth=('user', 'pass'))", "Xác thực cơ bản", "Thành công")
print_example("requests.get(url, auth=HTTPDigestAuth('user', 'pass'))", "Xác thực Digest", "Thành công")

# ==============================================================================
# 6. TIMEOUT & SESSION
# ==============================================================================
print_section("6. Timeout & Session")
print_example("requests.get(url, timeout=5)", "Thiết lập timeout (giây)", "Thành công")
print_example("session = requests.Session()", "Tạo session", "Thành công")
print_example("session.get(url)", "Gửi yêu cầu bằng session", "Thành công")
print_example("session.cookies", "Cookie được giữ trong session", "RequestsCookieJar")

# ==============================================================================
# 7. XỬ LÝ FILE & NỘI DUNG NHỊ PHÂN
# ==============================================================================
print_section("7. Xử lý file & nội dung nhị phân")
print_example("files = {'file': open('report.xls', 'rb')}", "Upload file", "Thành công")
print_example("requests.post(url, files=files)", "Gửi file", "Thành công")
print_example("r = requests.get(url)", "Tải file", "Response object")
print_example("with open('file.jpg', 'wb') as f: f.write(r.content)", "Lưu nội dung nhị phân", "Thành công")

# ==============================================================================
# 8. XỬ LÝ NGOẠI LỆ
# ==============================================================================
print_section("8. Xử lý ngoại lệ thường gặp")
print_example("from requests.exceptions import RequestException", "Lỗi chung", "Thành công")
print_example("from requests.exceptions import ConnectionError", "Lỗi kết nối", "Thành công")
print_example("from requests.exceptions import Timeout", "Lỗi timeout", "Thành công")
print_example("from requests.exceptions import HTTPError", "Lỗi HTTP (4xx, 5xx)", "Thành công")
print_example("r.raise_for_status()", "Nâng lỗi nếu status >= 400", "Thành công nếu < 400")

# ==============================================================================
# 9. MÃ TRẠNG THÁI HTTP
# ==============================================================================
print_section("9. Mã trạng thái HTTP phổ biến")
print_example("200", "Thành công", "OK")
print_example("201", "Tạo thành công", "Created")
print_example("400", "Yêu cầu sai", "Bad Request")
print_example("401", "Chưa xác thực", "Unauthorized")
print_example("403", "Bị cấm truy cập", "Forbidden")
print_example("404", "Không tìm thấy", "Not Found")
print_example("500", "Lỗi máy chủ", "Internal Server Error")

# ==============================================================================
# 10. MỘT SỐ ĐIỀU CẦN LƯU Ý
# ==============================================================================
print_section("10. Một số điều cần lưu ý")
print("- Luôn kiểm tra `r.status_code` hoặc dùng `r.raise_for_status()`")
print("- Dùng `session` để tái sử dụng kết nối và giữ cookie")
print("- Luôn đóng file khi upload: dùng `with open(...) as f:`")
print("- Cẩn trọng với `verify=False` khi dùng HTTPS (bỏ qua xác minh SSL)")
print("- `requests` không hỗ trợ JavaScript. Dùng Selenium nếu cần render JS.")

# ==============================================================================
# 11. THÔNG TIN THƯ VIỆN REQUESTS
# ==============================================================================
print_section("11. Thông tin thư viện requests")
print("Cài đặt: pip install requests")
print("Tài liệu: https://requests.readthedocs.io/")
print("Tác giả: Kenneth Reitz")

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'REQUESTS MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://requests.readthedocs.io/':^70}")
print("="*70)