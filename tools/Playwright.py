# -*- coding: utf-8 -*-
"""
Playwright Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module playwright (sync_api) trong Python
"""

import sys
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None  # Để chạy trong môi trường không có playwright

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Kiểm tra nếu playwright được cài đặt
if not sync_playwright:
    print("Module playwright không được cài đặt. Cài đặt bằng: pip install playwright && playwright install")
    sys.exit(1)

# Dữ liệu mẫu
url = "https://www.example.com"
search_url = "https://www.google.com"
sample_query = "Python Playwright"
sample_selector = "input[name='q']"

# Khởi tạo Playwright (chỉ để kiểm tra, không chạy trong console)
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()

# ==============================================================================
# 1. KHỞI TẠO TRÌNH DUYỆT
# ==============================================================================
print_section("1. Khởi tạo trình duyệt")
print_example('sync_playwright().chromium.launch()', "Khởi tạo Chromium", "Trình duyệt Chromium được mở")
print_example('p.chromium.launch(headless=True)', "Chạy ở chế độ headless", "Không hiển thị giao diện")
print_example('p.firefox.launch()', "Khởi tạo Firefox", "Trình duyệt Firefox được mở")
print_example('browser.new_page()', "Tạo trang mới", "Trang web mới")

# ==============================================================================
# 2. ĐIỀU HƯỚNG WEB
# ==============================================================================
print_section("2. Điều hướng web")
# page.goto(url)
print_example('page.goto("https://www.example.com")', "Mở URL", url)
# page.reload()
print_example('page.reload()', "Làm mới trang", "Trang được tải lại")
# page.go_back()
print_example('page.go_back()', "Quay lại trang trước", "Điều hướng ngược")
# page.go_forward()
print_example('page.go_forward()', "Tiến tới trang tiếp theo", "Điều hướng tiến")

# ==============================================================================
# 3. TÌM KIẾM PHẦN TỬ
# ==============================================================================
print_section("3. Tìm kiếm phần tử")
print_example('page.query_selector("h1")', "Tìm bằng CSS selector", "Trả về phần tử h1")
print_example('page.query_selector_all("a")', "Tìm tất cả thẻ a", "Danh sách các thẻ a")
print_example('page.locator("input[name=\'q\']")', "Tìm bằng locator", "Trả về input name='q'")
print_example('page.locator("text=Example")', "Tìm bằng văn bản", "Phần tử chứa văn bản")
print_example('page.locator("//h1")', "Tìm bằng XPath", "Trả về thẻ h1")

# ==============================================================================
# 4. TƯƠNG TÁC VỚI PHẦN TỬ
# ==============================================================================
print_section("4. Tương tác với phần tử")
# page.goto(search_url)
# page.fill(sample_selector, sample_query)
print_example('page.fill("input[name=\'q\']", ...)', "Nhập văn bản", sample_query)
# page.press(sample_selector, "Enter")
print_example('page.press("input[name=\'q\']", "Enter")', "Nhấn phím Enter", "Gửi biểu mẫu")
# page.click("button")
print_example('page.click("button")', "Nhấn vào phần tử", "Thực hiện click")
# page.locator(sample_selector).clear()
print_example('page.locator(...).clear()', "Xóa nội dung ô nhập", "Xóa văn bản")

# ==============================================================================
# 5. LẤY THÔNG TIN PHẦN TỬ
# ==============================================================================
print_section("5. Lấy thông tin phần tử")
# element = page.query_selector("h1")
print_example('page.query_selector("h1").text_content()', "Lấy văn bản", "Nội dung văn bản h1")
print_example('page.query_selector("a").get_attribute("href")', "Lấy thuộc tính href", "Giá trị thuộc tính")
print_example('page.locator("h1").is_visible()', "Kiểm tra hiển thị", "True nếu h1 hiển thị")
print_example('page.locator("button").is_enabled()', "Kiểm tra kích hoạt", "True nếu button hoạt động")

# ==============================================================================
# 6. ĐỢI PHẦN TỬ (WAITING)
# ==============================================================================
print_section("6. Đợi phần tử")
# page.wait_for_selector("h1")
print_example('page.wait_for_selector("h1")', "Đợi phần tử xuất hiện", "Phần tử h1 xuất hiện")
# page.wait_for_timeout(1000)
print_example('page.wait_for_timeout(1000)', "Đợi 1 giây", "Tạm dừng 1000ms")
# page.locator("button").wait_for(state="visible")
print_example('page.locator("button").wait_for("visible")', "Đợi phần tử hiển thị", "Button hiển thị")
# page.wait_for_load_state("load")
print_example('page.wait_for_load_state("load")', "Đợi trang tải xong", "Trang tải hoàn tất")

# ==============================================================================
# 7. XỬ LÝ ALERT
# ==============================================================================
print_section("7. Xử lý alert")
# page.on("dialog", lambda dialog: dialog.accept())
print_example('page.on("dialog", lambda dialog: ...)', "Chấp nhận alert", "Đóng alert với OK")
# page.on("dialog", lambda dialog: dialog.dismiss())
print_example('page.on("dialog", lambda dialog: ...)', "Hủy alert", "Đóng alert với Cancel")
# page.evaluate("alert('Test alert')")
print_example('page.evaluate("alert(...)")', "Kích hoạt alert", "Tạo thông báo thử")

# ==============================================================================
# 8. QUẢN LÝ CỬA SỔ VÀ TAB
# ==============================================================================
print_section("8. Quản lý cửa sổ và tab")
# page.context.new_page()
print_example('page.context.new_page()', "Tạo tab mới", "Tab mới được tạo")
# page.context.pages[1].bring_to_front()
print_example('page.context.pages[1].bring_to_front()', "Chuyển tab", "Chuyển sang tab khác")
print_example('page.url', "Lấy URL hiện tại", "URL của trang hiện tại")
print_example('page.title()', "Lấy tiêu đề trang", "Tiêu đề của trang")

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    # page.query_selector("nonexistent")
    print_example('page.query_selector("nonexistent")', "Lỗi phần tử không tồn tại", "TimeoutError")
except Exception as e:
    print_example('page.query_selector("nonexistent")', "Lỗi phần tử không tồn tại", f"Lỗi: {str(e)[:50]}...")
try:
    # page.wait_for_selector("nonexistent", timeout=100)
    print_example('page.wait_for_selector("nonexistent")', "Lỗi hết thời gian đợi", "TimeoutError")
except Exception as e:
    print_example('page.wait_for_selector("nonexistent")', "Lỗi hết thời gian đợi", f"Lỗi: {str(e)[:50]}...")

# ==============================================================================
# 10. THÔNG TIN MODULE PLAYWRIGHT
# ==============================================================================
print_section("10. Thông tin module playwright.sync_api")
from playwright.sync_api import sync_playwright
all_classes = [m for m in dir(sync_playwright()) if not m.startswith("_") and isinstance(getattr(sync_playwright(), m), type)]
print(f"Tổng cộng: {len(all_classes)} lớp")
print("\n".join(f" • {cls:<20} → {getattr(sync_playwright(), cls).__doc__.split('.')[0]}" for cls in sorted(all_classes)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'PLAYWRIGHT MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://playwright.dev/python/docs/intro':^70}")
print("="*70)

# Đóng trình duyệt (chỉ để kiểm tra, không chạy trong console)
# browser.close()