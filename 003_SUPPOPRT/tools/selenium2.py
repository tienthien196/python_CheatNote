# -*- coding: utf-8 -*-
"""
Selenium Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng Selenium WebDriver trong Python
"""

import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(code, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{code:<45} | {desc:<22} | Kết quả: {result}")

# ==============================================================================
# 1. CÀI ĐẶT & KHỞI TẠO WEBDRIVER
# ==============================================================================
print_section("1. Cài đặt & Khởi tạo WebDriver")
print("Cài đặt: pip install selenium")
print("Cần tải WebDriver phù hợp (ChromeDriver, GeckoDriver...)")
print("Hoặc dùng: pip install webdriver-manager để tự động tải.")

# Ví dụ minh họa (chưa thực thi)
print_example("from selenium import webdriver", "Nhập thư viện", "Thành công")
print_example("from selenium.webdriver.common.by import By", "Nhập By", "Thành công")
print_example("from selenium.webdriver.support.ui import WebDriverWait", "Nhập WebDriverWait", "Thành công")
print_example("from selenium.webdriver.support import expected_conditions as EC", "Nhập EC", "Thành công")

# ==============================================================================
# 2. KHỞI TẠO TRÌNH DUYỆT (Chrome)
# ==============================================================================
print_section("2. Khởi tạo trình duyệt")
print("--- Chrome ---")
print_example("driver = webdriver.Chrome()", "Khởi tạo ChromeDriver", "Phải có chromedriver trong PATH")
print_example("from webdriver_manager.chrome import ChromeDriverManager", "Tự động tải driver", "Cài đặt webdriver-manager")
print_example("options = webdriver.ChromeOptions()", "Tạo tùy chọn Chrome", "Thành công")
print_example('options.add_argument("--headless")', "Chạy ẩn (headless)", "Không hiện giao diện")
print_example('options.add_argument("--no-sandbox")', "Tùy chọn cho server", "Thành công")
print_example('driver = webdriver.Chrome(options=options)', "Khởi tạo với options", "Thành công")

# ==============================================================================
# 3. ĐIỀU HƯỚNG TRANG WEB
# ==============================================================================
print_section("3. Điều hướng trang web")
print_example("driver.get('https://example.com')", "Mở trang web", "Thành công")
print_example("driver.current_url", "Lấy URL hiện tại", "https://example.com")
print_example("driver.title", "Lấy tiêu đề trang", "Example Domain")
print_example("driver.back()", "Quay lại trang trước", "Thành công")
print_example("driver.forward()", "Đi tới trang tiếp", "Thành công")
print_example("driver.refresh()", "Làm mới trang", "Thành công")

# ==============================================================================
# 4. TÌM KIẾM PHẦN TỬ (FIND ELEMENTS)
# ==============================================================================
print_section("4. Tìm kiếm phần tử")
print_example("driver.find_element(By.ID, 'id')", "Tìm theo ID", "WebElement")
print_example("driver.find_element(By.NAME, 'name')", "Tìm theo NAME", "WebElement")
print_example("driver.find_element(By.TAG_NAME, 'div')", "Tìm theo TAG", "WebElement")
print_example("driver.find_element(By.CLASS_NAME, 'class')", "Tìm theo CLASS", "WebElement")
print_example("driver.find_element(By.CSS_SELECTOR, 'input[name=\"q\"]')", "Tìm theo CSS Selector", "WebElement")
print_example("driver.find_element(By.XPATH, '//input[@id=\"search\"]')", "Tìm theo XPATH", "WebElement")
print_example("driver.find_elements(By.CLASS_NAME, 'item')", "Tìm nhiều phần tử", "List[WebElement]")

# ==============================================================================
# 5. TƯƠNG TÁC VỚI PHẦN TỬ
# ==============================================================================
print_section("5. Tương tác với phần tử")
print_example("element.click()", "Nhấp chuột", "Thành công")
print_example("element.send_keys('text')", "Gõ văn bản", "Thành công")
print_example("element.clear()", "Xóa nội dung ô nhập", "Thành công")
print_example("element.text", "Lấy nội dung văn bản", "Text content")
print_example("element.get_attribute('href')", "Lấy thuộc tính", "https://example.com")
print_example("element.is_displayed()", "Kiểm tra hiển thị", "True/False")
print_example("element.is_enabled()", "Kiểm tra kích hoạt", "True/False")
print_example("element.is_selected()", "Kiểm tra chọn (checkbox)", "True/False")

# ==============================================================================
# 6. CHỜ (WAIT)
# ==============================================================================
print_section("6. Chờ phần tử")
print("--- Chờ ngầm định ---")
print_example("driver.implicitly_wait(10)", "Chờ ngầm 10 giây", "Thành công")

print("--- Chờ tường minh (WebDriverWait + EC) ---")
print_example("wait = WebDriverWait(driver, 10)", "Khởi tạo WebDriverWait", "Thành công")
print_example("element = wait.until(EC.presence_of_element_located((By.ID, 'id')))", "Chờ phần tử xuất hiện", "Thành công")
print_example("element = wait.until(EC.element_to_be_clickable((By.ID, 'button')))", "Chờ phần tử click được", "Thành công")
print_example("EC.title_is('Expected Title')", "Chờ tiêu đề trang", "Thành công")
print_example("EC.url_contains('search')", "Chờ URL chứa chuỗi", "Thành công")

# ==============================================================================
# 7. CỬA SỔ & FRAME
# ==============================================================================
print_section("7. Cửa sổ & Frame")
print_example("driver.window_handles", "Danh sách cửa sổ", "['window1', 'window2']")
print_example("driver.switch_to.window(window_name)", "Chuyển sang cửa sổ khác", "Thành công")
print_example("driver.switch_to.frame('frame_id')", "Chuyển vào frame", "Thành công")
print_example("driver.switch_to.default_content()", "Quay về frame gốc", "Thành công")
print_example("driver.close()", "Đóng tab hiện tại", "Thành công")
print_example("driver.quit()", "Đóng toàn bộ trình duyệt", "Thành công")

# ==============================================================================
# 8. KEYS & HÀNH ĐỘNG
# ==============================================================================
print_section("8. Nhấn phím & hành động")
print_example("from selenium.webdriver.common.keys import Keys", "Nhập Keys", "Thành công")
print_example("element.send_keys(Keys.ENTER)", "Nhấn Enter", "Thành công")
print_example("element.send_keys(Keys.CONTROL, 'a')", "Nhấn Ctrl+A", "Thành công")
print_example("from selenium.webdriver.common.action_chains import ActionChains", "Nhập ActionChains", "Thành công")
print_example("actions = ActionChains(driver)", "Khởi tạo chuỗi hành động", "Thành công")
print_example("actions.move_to_element(element).perform()", "Hover chuột", "Thành công")
print_example("actions.drag_and_drop(source, target).perform()", "Kéo thả", "Thành công")

# ==============================================================================
# 9. LẤY THÔNG TIN TRANG WEB
# ==============================================================================
print_section("9. Lấy thông tin trang")
print_example("driver.get_cookies()", "Lấy danh sách cookie", "[{'name': 'session', ...}]")
print_example("driver.add_cookie({'name': 'key', 'value': 'value'})", "Thêm cookie", "Thành công")
print_example("driver.delete_cookie('name')", "Xóa cookie", "Thành công")
print_example("driver.delete_all_cookies()", "Xóa tất cả cookie", "Thành công")

# ==============================================================================
# 10. CHỤP ẢNH MÀN HÌNH
# ==============================================================================
print_section("10. Chụp ảnh màn hình")
print_example("driver.save_screenshot('screenshot.png')", "Chụp toàn trang", "Thành công")
print_example("element.screenshot('element.png')", "Chụp phần tử", "Thành công")

# ==============================================================================
# 11. XỬ LÝ NGOẠI LỆ
# ==============================================================================
print_section("11. Xử lý ngoại lệ thường gặp")
print_example("from selenium.common.exceptions import NoSuchElementException", "Lỗi không tìm thấy phần tử", "Thành công")
print_example("from selenium.common.exceptions import TimeoutException", "Lỗi chờ quá lâu", "Thành công")
print_example("from selenium.common.exceptions import ElementClickInterceptedException", "Lỗi click bị chặn", "Thành công")

# ==============================================================================
# 12. MỘT SỐ ĐIỀU CẦN LƯU Ý
# ==============================================================================
print_section("12. Một số điều cần lưu ý")
print("- Luôn đóng trình duyệt sau khi xong: driver.quit()")
print("- Dùng WebDriverWait thay vì time.sleep() để tối ưu hiệu suất.")
print("- Dùng headless=True để chạy ẩn, tăng tốc độ.")
print("- Selenium không phải là công cụ scrape nhanh nhất. Dùng requests/BeautifulSoup nếu không cần tương tác.")
print("- Có thể bị chặn bởi bot detection (CAPTCHA, Cloudflare...).")

# ==============================================================================
# 13. THÔNG TIN MODULE SELENIUM
# ==============================================================================
print_section("13. Thông tin module selenium")
print("Cài đặt: pip install selenium")
print("Tài liệu: https://selenium-python.readthedocs.io/")
print("Hỗ trợ: Chrome, Firefox, Edge, Safari...")

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'SELENIUM MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://selenium-python.readthedocs.io/':^70}")
print("="*70)