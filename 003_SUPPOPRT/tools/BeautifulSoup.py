# -*- coding: utf-8 -*-
"""
BeautifulSoup Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module BeautifulSoup (bs4) trong Python
"""

import sys
try:
    from bs4 import BeautifulSoup
    import requests
except ImportError:
    BeautifulSoup, requests = None, None  # Để chạy trong môi trường không có bs4 hoặc requests

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
sample_html = """
<html>
<head><title>Sample Page</title></head>
<body>
<h1>Welcome to BeautifulSoup</h1>
<div class="content">
    <p id="intro">Hello, Python!</p>
    <a href="https://example.com">Link 1</a>
    <a href="https://test.org">Link 2</a>
</div>
<ul>
    <li>Item 1</li>
    <li class="active">Item 2</li>
</ul>
</body>
</html>
"""
url = "https://httpbin.org/html"

# Kiểm tra nếu BeautifulSoup và requests được cài đặt
if not BeautifulSoup or not requests:
    print("Module bs4 hoặc requests không được cài đặt. Cài đặt bằng: pip install beautifulsoup4 requests")
    sys.exit(1)

# Khởi tạo BeautifulSoup với HTML mẫu
soup = BeautifulSoup(sample_html, "html.parser")

# ==============================================================================
# 1. KHỞI TẠO BEAUTIFULSOUP
# ==============================================================================
print_section("1. Khởi tạo BeautifulSoup")
print_example('BeautifulSoup(html, "html.parser")', "Khởi tạo với HTML", soup.title.text if soup.title else None)
response = requests.get(url)
soup_web = BeautifulSoup(response.text, "html.parser")
print_example('BeautifulSoup(response.text, ...)', "Khởi tạo từ web", soup_web.title.text if soup_web.title else None)
print_example('BeautifulSoup(html, "lxml")', "Sử dụng parser lxml", "Yêu cầu pip install lxml")
print_example('soup.prettify()', "Định dạng HTML đẹp", soup.prettify()[:50] + "...")

# ==============================================================================
# 2. TÌM KIẾM THEO TAG
# ==============================================================================
print_section("2. Tìm kiếm theo tag")
print_example('soup.find("h1")', "Tìm tag h1 đầu tiên", soup.find("h1").text if soup.find("h1") else None)
print_example('soup.find_all("a")', "Tìm tất cả tag a", [a.text for a in soup.find_all("a")])
print_example('soup.find("p", id="intro")', "Tìm tag p với id", soup.find("p", id="intro").text if soup.find("p", id="intro") else None)
print_example('soup.find_all("li", class_="active")', "Tìm tag li với class", [li.text for li in soup.find_all("li", class_="active")])

# ==============================================================================
# 3. TÌM KIẾM VỚI THUỘC TÍNH
# ==============================================================================
print_section("3. Tìm kiếm với thuộc tính")
print_example('soup.find(attrs={"href": "https://example.com"})', "Tìm tag với href cụ thể", soup.find(attrs={"href": "https://example.com"}).text)
print_example('soup.select("div.content")', "Tìm bằng CSS selector", [div.text.strip() for div in soup.select("div.content")])
print_example('soup.select_one("#intro")', "Tìm một tag bằng ID", soup.select_one("#intro").text if soup.select_one("#intro") else None)
print_example('soup.find_all(attrs={"class": "active"})', "Tìm tag với class", [tag.text for tag in soup.find_all(attrs={"class": "active"})])

# ==============================================================================
# 4. ĐIỀU HƯỚNG CÂY HTML
# ==============================================================================
print_section("4. Điều hướng cây HTML")
print_example('soup.h1.parent.name', "Tìm thẻ cha của h1", soup.h1.parent.name if soup.h1 else None)
print_example('soup.p.next_sibling.name', "Tìm thẻ tiếp theo", soup.p.next_sibling.name if soup.p and soup.p.next_sibling else None)
print_example('soup.ul.find_all("li")', "Tìm tất cả con của ul", [li.text for li in soup.ul.find_all("li")])
print_example('soup.div.contents', "Lấy nội dung con của div", [child.text.strip() for child in soup.div.contents if child.name])

# ==============================================================================
# 5. TRÍCH XUẤT DỮ LIỆU
# ==============================================================================
print_section("5. Trích xuất dữ liệu")
print_example('soup.title.text', "Lấy văn bản của title", soup.title.text if soup.title else None)
print_example('soup.a["href"]', "Lấy thuộc tính href", soup.a["href"] if soup.a else None)
print_example('soup.get_text().strip()', "Lấy toàn bộ văn bản", soup.get_text().strip()[:50] + "...")
print_example('soup.find("a").string', "Lấy chuỗi bên trong tag", soup.find("a").string if soup.find("a") else None)

# ==============================================================================
# 6. SỬA ĐỔI HTML
# ==============================================================================
print_section("6. Sửa đổi HTML")
soup_copy = BeautifulSoup(sample_html, "html.parser")
soup_copy.h1.string = "Updated Title"
print_example('soup.h1.string = "Updated Title"', "Sửa văn bản của h1", soup_copy.h1.text)
new_tag = soup_copy.new_tag("p")
new_tag.string = "New paragraph"
soup_copy.body.append(new_tag)
print_example('soup.body.append(new_tag)', "Thêm tag mới", soup_copy.body.find_all("p")[-1].text)
soup_copy.find("li", class_="active")["class"] = "inactive"
print_example('soup.find("li").["class"] = "inactive"', "Sửa thuộc tính class", soup_copy.find("li", class_="inactive")["class"])

# ==============================================================================
# 7. LÀM VIỆC VỚI WEB
# ==============================================================================
print_section("7. Làm việc với web")
response = requests.get(url)
soup_web = BeautifulSoup(response.text, "html.parser")
print_example('BeautifulSoup(requests.get(url).text)', "Tải HTML từ web", soup_web.title.text if soup_web.title else None)
print_example('soup_web.find_all("p")', "Tìm tất cả tag p từ web", [p.text.strip()[:30] + "..." for p in soup_web.find_all("p")])
print_example('soup_web.select("body h1")', "Tìm h1 trong body", [h1.text for h1 in soup_web.select("body h1")])

# ==============================================================================
# 8. XỬ LÝ LỖI
# ==============================================================================
print_section("8. Xử lý lỗi")
try:
    soup.find("nonexistent").text
except AttributeError as e:
    print_example('soup.find("nonexistent").text', "Lỗi tag không tồn tại", f"Lỗi: {e}")
try:
    soup.find("a")["invalid_attr"]
except KeyError as e:
    print_example('soup.find("a")["invalid_attr"]', "Lỗi thuộc tính không tồn tại", f"Lỗi: {e}")

# ==============================================================================
# 9. TÙY CHỈNH PARSER
# ==============================================================================
print_section("9. Tùy chỉnh parser")
print_example('BeautifulSoup(..., "html.parser")', "Sử dụng html.parser", "Parser mặc định Python")
print_example('BeautifulSoup(..., "lxml")', "Sử dụng lxml", "Yêu cầu pip install lxml")
print_example('BeautifulSoup(..., "html5lib")', "Sử dụng html5lib", "Yêu cầu pip install html5lib")
soup_xml = BeautifulSoup("<root><item>Test</item></root>", "xml")
print_example('BeautifulSoup(..., "xml")', "Parser XML", soup_xml.item.text if soup_xml.item else None)

# ==============================================================================
# 10. THÔNG TIN MODULE BEAUTIFULSOUP
# ==============================================================================
print_section("10. Thông tin module BeautifulSoup")
all_functions = [m for m in dir(BeautifulSoup) if not m.startswith("_") and callable(getattr(BeautifulSoup, m))]
print(f"Tổng cộng: {len(all_functions)} phương thức")
print("\n".join(f" • {func:<20} → {getattr(BeautifulSoup, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'BEAUTIFULSOUP MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://www.crummy.com/software/BeautifulSoup/bs4/doc/':^70}")
print("="*70)