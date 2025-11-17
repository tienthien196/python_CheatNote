# -*- coding: utf-8 -*-
"""
BeautifulSoup 4 (bs4) Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng thư viện bs4 trong Python
"""

import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(code, desc, result=None):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{code:<45} | {desc:<22} | Kết quả: {result or '...'}")

# ==============================================================================
# 1. CÀI ĐẶT & NHẬP THƯ VIỆN
# ==============================================================================
print_section("1. Cài đặt & Nhập thư viện")
print("Cài đặt: pip install beautifulsoup4")
print("Thường dùng với: pip install lxml (parser nhanh) hoặc html.parser (mặc định)")
print_example("from bs4 import BeautifulSoup", "Nhập BeautifulSoup", "Thành công")
print_example("import requests", "Nhập requests (thường dùng chung)", "Thành công")

# ==============================================================================
# 2. TẠO OBJECT SOUP
# ==============================================================================
print_section("2. Tạo object BeautifulSoup")
print_example("soup = BeautifulSoup(html_doc, 'html.parser')", "Tạo từ chuỗi HTML", "Soup object")
print_example("soup = BeautifulSoup(html_doc, 'lxml')", "Dùng parser lxml (nhanh hơn)", "Soup object")
print_example("soup = BeautifulSoup(response.text, 'html.parser')", "Kết hợp với requests", "Soup object")

# ==============================================================================
# 3. TÌM KIẾM ĐƠN GIẢN
# ==============================================================================
print_section("3. Tìm kiếm đơn giản")
print_example("soup.title", "Lấy thẻ <title>", "<title>Page Title</title>")
print_example("soup.title.name", "Lấy tên thẻ", "title")
print_example("soup.title.string", "Lấy nội dung bên trong", "Page Title")
print_example("soup.p", "Lấy thẻ <p> đầu tiên", "<p>First paragraph</p>")
print_example("soup.find('p')", "Tìm thẻ <p> đầu tiên", "<p>First paragraph</p>")
print_example("soup.find_all('p')", "Tìm tất cả thẻ <p>", "[<p>1</p>, <p>2</p>, ...]")

# ==============================================================================
# 4. TÌM THEO THUỘC TÍNH
# ==============================================================================
print_section("4. Tìm kiếm theo thuộc tính")
print_example("soup.find('div', class_='content')", "Tìm theo class", "<div class='content'>...")
print_example("soup.find('div', id='main')", "Tìm theo id", "<div id='main'>...")
print_example("soup.find('a', href='https://example.com')", "Tìm theo href", "<a href='...'>")
print_example("soup.find_all('a', limit=5)", "Giới hạn số lượng tìm thấy", "[<a>, <a>, ...]")

# ==============================================================================
# 5. TÌM THEO CSS SELECTOR
# ==============================================================================
print_section("5. Tìm kiếm bằng CSS Selector")
print_example("soup.select('div.classname')", "CSS: .class", "[<div>, ...]")
print_example("soup.select('#idname')", "CSS: #id", "[<tag id='idname'>, ...]")
print_example("soup.select('p a')", "CSS: con gián tiếp", "[<a> inside <p>]")
print_example("soup.select('p > a')", "CSS: con trực tiếp", "[<a> direct child of <p>]")
print_example("soup.select('p ~ .sibling')", "CSS: anh/chị/em", "[.sibling after <p>]")
print_example("soup.select('a[href*=\"example\"]')", "CSS: chứa chuỗi trong attr", "[<a>, ...]")

# ==============================================================================
# 6. LẤY THUỘC TÍNH & NỘI DUNG
# ==============================================================================
print_section("6. Lấy nội dung và thuộc tính")
print_example("tag = soup.find('a')", "Lấy tag", "<a href='...'>")
print_example("tag.get('href')", "Lấy giá trị thuộc tính", "https://example.com")
print_example("tag.get('class')", "Lấy class (dưới dạng list)", "['class1', 'class2']")
print_example("tag.text", "Lấy nội dung văn bản (kể cả con)", "Text content")
print_example("tag.get_text()", "Lấy nội dung văn bản", "Text content")
print_example("tag.get_text(strip=True)", "Lấy văn bản, xóa đầu/cuối dòng", "Text content")

# ==============================================================================
# 7. DUYỆT CÂY HTML (NAVIGATION)
# ==============================================================================
print_section("7. Duyệt cây HTML")
print_example("tag.parent", "Thẻ cha", "<div>...")
print_example("tag.children", "Các thẻ con trực tiếp", "Iterator")
print_example("list(tag.children)", "Chuyển iterator thành list", "[<p>, <span>, ...]")
print_example("tag.descendants", "Tất cả thẻ con (đệ quy)", "Iterator")
print_example("tag.find_next_sibling()", "Thẻ anh/em phía sau", "<p>Next sibling</p>")
print_example("tag.find_previous_sibling()", "Thẻ anh/em phía trước", "<p>Prev sibling</p>")
print_example("tag.find_next()", "Thẻ tiếp theo bất kỳ", "<p>Any next tag</p>")

# ==============================================================================
# 8. LỌC NÂNG CAO (FILTERS)
# ==============================================================================
print_section("8. Lọc nâng cao với hàm")
print_example("def has_class(tag): return tag.has_attr('class')", "Hàm lọc", "Thành công")
print_example("soup.find(has_class)", "Tìm với hàm", "<tag class='...'>")
print_example("soup.find_all(string='exact text')", "Tìm chuỗi chính xác", "['exact text']")
print_example("soup.find_all(string=re.compile('pattern'))", "Tìm chuỗi theo regex", "['text1', 'text2']")

# ==============================================================================
# 9. XỬ LÝ NGOẠI LỆ
# ==============================================================================
print_section("9. Xử lý ngoại lệ")
print_example("if tag: print(tag.text)", "Kiểm tra tag có tồn tại", "Tránh lỗi .text")
print_example("tag.get('attr') or 'default'", "Lấy thuộc tính hoặc mặc định", "Giá trị hoặc 'default'")

# ==============================================================================
# 10. MỘT SỐ ĐIỀU CẦN LƯU Ý
# ==============================================================================
print_section("10. Một số điều cần lưu ý")
print("- Dùng `lxml` nếu muốn tốc độ cao hơn `html.parser`.")
print("- Kết quả từ `.find()` có thể là None -> kiểm tra trước khi dùng.")
print("- Kết quả từ `.find_all()` luôn là list (có thể rỗng).")
print("- `BeautifulSoup` không thể xử lý JavaScript. Dùng Selenium nếu cần render JS.")
print("- Rất hiệu quả khi kết hợp với `requests` để crawl dữ liệu.")

# ==============================================================================
# 11. THÔNG TIN THƯ VIỆN BS4
# ==============================================================================
print_section("11. Thông tin thư viện bs4")
print("Cài đặt: pip install beautifulsoup4")
print("Tài liệu: https://beautiful-soup-4.readthedocs.io/")
print("Tác giả: Leonard Richardson")

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'BS4 (BEAUTIFULSOUP4) MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://beautiful-soup-4.readthedocs.io/':^70}")
print("="*70)