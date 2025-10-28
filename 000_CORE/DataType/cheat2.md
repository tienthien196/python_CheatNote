```
==================================================
          HIỂU VỀ SOCKET TRONG PYTHON
==================================================

Socket là điểm cuối (endpoint) trong kết nối mạng, cho phép giao tiếp hai chiều giữa các tiến trình — 
có thể trên cùng máy hoặc qua mạng. Python cung cấp module `socket` trong thư viện chuẩn để làm việc 
với TCP và UDP ở mức thấp.

Hai giao thức chính:
- TCP (SOCK_STREAM): Hướng kết nối, đáng tin cậy, có thứ tự.
- UDP (SOCK_DGRAM): Không kết nối, nhanh, không đảm bảo thứ tự/giao hàng.

⚠️ Lưu ý: TCP và UDP là hai giao thức riêng biệt — không thể giao tiếp lẫn nhau dù cùng cổng.

==================================================
          CHEAT SHEET: MODULE `socket`
==================================================

1. Tạo socket
   - socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)
     • family: 
         AF_INET   → IPv4 (mặc định)
         AF_INET6  → IPv6
     • type:
         SOCK_STREAM → TCP
         SOCK_DGRAM  → UDP

   Ví dụ:
     s = socket.socket()  # TCP/IPv4
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

2. Cấu hình socket (tuỳ chọn)
   - s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Cho phép reuse cổng
   - s.settimeout(seconds)  # Đặt timeout cho recv/accept

3. Gắn & Lắng nghe (Server)
   - s.bind((host, port))
        host = '' hoặc '0.0.0.0' → mọi interface
        host = '127.0.0.1' → chỉ local
   - TCP: s.listen(backlog)  # Bắt đầu lắng nghe
   - UDP: KHÔNG cần listen()

4. Nhận dữ liệu
   - TCP Server:
        client_sock, addr = s.accept()     # Chấp nhận kết nối
        data = client_sock.recv(bufsize)   # Nhận dữ liệu
   - UDP Server:
        data, addr = s.recvfrom(bufsize)   # Nhận dữ liệu + địa chỉ client
   - Client (TCP/UDP):
        data = s.recv(bufsize)

5. Gửi dữ liệu
   - TCP: 
        s.send(bytes)      → Gửi một phần
        s.sendall(bytes)   → Gửi toàn bộ (khuyên dùng)
   - UDP:
        s.sendto(bytes, (host, port))  → Gửi kèm địa chỉ đích

   ⚠️ Dữ liệu PHẢI là bytes → dùng b"..." hoặc .encode()

6. Client kết nối
   - TCP Client: s.connect((host, port))
   - UDP Client: KHÔNG cần connect() → dùng sendto() trực tiếp

7. Đóng kết nối
   - s.close() → Giải phóng socket và cổng

8. Hằng số & tiện ích quan trọng
   - socket.AF_INET       → IPv4
   - socket.AF_INET6      → IPv6
   - socket.SOCK_STREAM   → TCP
   - socket.SOCK_DGRAM    → UDP
   - socket.gethostname() → Lấy tên máy
   - socket.gethostbyname(name) → DNS lookup (tên → IP)

==================================================
          VÍ DỤ MINH HỌA
==================================================

🔸 TCP SERVER
import socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8888))
s.listen(1)
conn, addr = s.accept()
print("Connected by", addr)
data = conn.recv(1024)
conn.send(b"Echo: " + data)
conn.close()
s.close()

🔸 TCP CLIENT
import socket
s = socket.socket()
s.connect(('localhost', 8888))
s.send(b"Hello TCP")
print(s.recv(1024))
s.close()

🔸 UDP SERVER
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 8888))
while True:
    data, addr = s.recvfrom(1024)
    print(f"From {addr}: {data}")
    s.sendto(b"Echo UDP", addr)

🔸 UDP CLIENT
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b"Hello UDP", ('localhost', 8888))
data, _ = s.recvfrom(1024)
print(data)
s.close()

==================================================
          LƯU Ý QUAN TRỌNG
==================================================
- Luôn đóng socket bằng .close() để tránh rò rỉ tài nguyên.
- Dữ liệu gửi/nhận phải là bytes → dùng .encode() khi gửi chuỗi, .decode() khi nhận.
- TCP: có kết nối → cần accept() và connect().
- UDP: không kết nối → dùng sendto() / recvfrom().
- Cổng TCP và UDP là độc lập — cùng số cổng nhưng khác giao thức → không xung đột.
- Trong production, nên dùng try/finally hoặc context manager để đảm bảo close() luôn được gọi.

==================================================
          KẾT LUẬN
==================================================
Module `socket` là nền tảng của mọi giao tiếp mạng trong Python. 
Hiểu rõ cách dùng socket giúp bạn:
  • Viết server/client tùy chỉnh
  • Hiểu cách HTTP, FTP, SMTP... hoạt động
  • Debug vấn đề mạng ở mức thấp

→ Đây là kiến thức cốt lõi trong Core Python networking.

==================================================
          HIỂU VỀ THƯ VIỆN `requests` TRONG PYTHON
==================================================

`requests` là thư viện HTTP **phổ biến nhất** trong Python — đơn giản, trực quan, mạnh mẽ.
Nó **KHÔNG** nằm trong thư viện chuẩn → phải cài đặt bằng `pip`.

Mục đích: Gửi yêu cầu HTTP/HTTPS (GET, POST, PUT, DELETE...) và xử lý phản hồi một cách dễ dàng.

✅ Ưu điểm so với urllib:
  • Cú pháp ngắn gọn, dễ đọc
  • Tự động xử lý JSON, mã hóa, cookies, sessions...
  • Hỗ trợ SSL, timeout, redirect, authentication...

==================================================
          CÀI ĐẶT
==================================================
# Cài đặt (chỉ cần làm 1 lần)
pip install requests

# Kiểm tra phiên bản
python -c "import requests; print(requests.__version__)"

==================================================
          CÚ PHÁP CƠ BẢN
==================================================

1. Nhập thư viện
   import requests

2. Gửi yêu cầu cơ bản
   response = requests.get('https://httpbin.org/get')
   response = requests.post('https://httpbin.org/post', data={'key': 'value'})

3. Truy cập dữ liệu phản hồi
   - response.status_code  → mã trạng thái (200, 404, 500...)
   - response.text         → nội dung phản hồi dạng chuỗi
   - response.content      → nội dung dạng bytes
   - response.json()       → phân tích JSON → dict/list (nếu có)
   - response.headers      → dict chứa headers từ server
   - response.url          → URL cuối cùng (sau redirect)

4. Kiểm tra thành công
   response.raise_for_status()  → ném exception nếu mã lỗi (4xx/5xx)

==================================================
          CÁC PHƯƠNG THỨC HTTP
==================================================

- requests.get(url, params=..., **kwargs)
- requests.post(url, data=..., json=..., **kwargs)
- requests.put(url, data=..., **kwargs)
- requests.patch(url, data=..., **kwargs)
- requests.delete(url, **kwargs)
- requests.head(url, **kwargs)
- requests.options(url, **kwargs)

==================================================
          THAM SỐ THƯỜNG DÙNG
==================================================

• `params` (dict): Tham số truy vấn (query string)
    requests.get('https://api.example.com/search', params={'q': 'python'})
    → URL: https://api.example.com/search?q=python

• `data` (dict hoặc str): Dữ liệu form (application/x-www-form-urlencoded)
    requests.post(url, data={'name': 'Alice'})

• `json` (dict/list): Gửi JSON tự động (Content-Type: application/json)
    requests.post(url, json={'name': 'Alice'})

• `headers` (dict): Gửi custom headers
    requests.get(url, headers={'User-Agent': 'MyApp/1.0'})

• `timeout` (float hoặc tuple): Giới hạn thời gian chờ (bắt buộc trong production!)
    requests.get(url, timeout=5)  # 5 giây

• `auth` (tuple hoặc callable): Xác thực cơ bản
    requests.get(url, auth=('user', 'pass'))

• `cookies` (dict): Gửi cookies
    requests.get(url, cookies={'session_id': 'abc123'})

==================================================
          SESSIONS (Duy trì trạng thái)
==================================================

Dùng khi cần gửi nhiều yêu cầu với cùng cookies/headers/auth:

s = requests.Session()
s.headers.update({'User-Agent': 'MyApp/1.0'})
s.get('https://httpbin.org/cookies/set/sessionid/123')
r = s.get('https://httpbin.org/cookies')  # Tự động gửi cookie

→ Session tự động lưu cookies, headers, và tái sử dụng kết nối (HTTP keep-alive).

==================================================
          XỬ LÝ FILE & UPLOAD
==================================================

• Tải file từ URL:
    r = requests.get(url)
    with open('image.jpg', 'wb') as f:
        f.write(r.content)

• Upload file:
    with open('report.pdf', 'rb') as f:
        requests.post(url, files={'file': f})

• Upload với tên & kiểu MIME:
    files = {'file': ('report.pdf', open('report.pdf', 'rb'), 'application/pdf')}
    requests.post(url, files=files)

==================================================
          VÍ DỤ MINH HỌA
==================================================

🔸 GET đơn giản
import requests
r = requests.get('https://api.github.com/users/octocat')
print(r.json()['name'])

🔸 POST JSON
r = requests.post('https://httpbin.org/post', json={'message': 'Hello'})
print(r.json()['json'])

🔸 Dùng Session để login
s = requests.Session()
s.post('https://example.com/login', data={'user': 'alice', 'pass': 'secret'})
profile = s.get('https://example.com/profile')

🔸 Tải ảnh
r = requests.get('https://example.com/photo.jpg')
with open('photo.jpg', 'wb') as f:
    f.write(r.content)

🔸 Xử lý lỗi
try:
    r = requests.get('https://httpbin.org/status/404', timeout=3)
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
except requests.exceptions.Timeout:
    print("Timeout!")
except requests.exceptions.RequestException as e:
    print("Network error:", e)

==================================================
          LƯU Ý QUAN TRỌNG
==================================================
- Luôn dùng `timeout` để tránh treo chương trình.
- Dùng `response.raise_for_status()` để phát hiện lỗi HTTP.
- Đóng file đúng cách khi upload/download (dùng `with`).
- Trong môi trường production, cân nhắc:
    • Xác thực (API keys, OAuth)
    • Rate limiting
    • Retry logic (dùng `urllib3.Retry` hoặc thư viện như `tenacity`)
- `requests` không hỗ trợ async → dùng `httpx` hoặc `aiohttp` nếu cần async.

==================================================
          SO SÁNH VỚI urllib (built-in)
==================================================
| Tính năng          | requests                     | urllib (built-in)            |
|--------------------|------------------------------|------------------------------|
| Cú pháp            | Rất đơn giản                 | Rườm rà, nhiều bước          |
| JSON               | response.json()              | json.loads(response.read())  |
| POST dữ liệu       | data= hoặc json=             | urlencode + Request object   |
| Session/Cookies    | Tích hợp sẵn                 | Phải dùng CookieJar          |
| Cài đặt            | Cần pip install              | Có sẵn                       |

→ Dùng `requests` cho mọi dự án thực tế. Dùng `urllib` chỉ khi không được cài package.

==================================================
          KẾT LUẬN
==================================================
`requests` là thư viện **không thể thiếu** khi làm việc với HTTP trong Python.
Nó biến việc gọi API, scrape web, tích hợp dịch vụ... thành thao tác đơn giản như gọi hàm.

→ Học `requests` ngay sau khi nắm vững core Python và urllib!
```