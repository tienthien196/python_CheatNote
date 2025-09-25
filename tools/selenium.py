# -*- coding: utf-8 -*-
"""
Selenium Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module selenium trong Python
"""

import sys
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
except ImportError:
    webdriver = None  # Để chạy trong môi trường không có selenium

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Kiểm tra nếu selenium được cài đặt
if not webdriver:
    print("Module selenium không được cài đặt. Cài đặt bằng: pip install selenium")
    sys.exit(1)

# Dữ liệu mẫu
url = "https://www.example.com"
search_url = "https://www.google.com"
sample_query = "Python Selenium"
sample_html = "<input name='q'>"

# Khởi tạo trình duyệt với tùy chọn (chỉ để kiểm tra, không chạy trong console)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy không giao diện (headless mode)
# driver = webdriver.Chrome(options=chrome_options)

# ==============================================================================
# 1. KHỞI TẠO TRÌNH DUYỆT
# ==============================================================================
print_section("1. Khởi tạo trình duyệt")
print_example('webdriver.Chrome()', "Khởi tạo Chrome driver", "Trình duyệt Chrome được mở")
print_example('chrome_options.add_argument("--headless")', "Chạy ở chế độ headless", "Không hiển thị giao diện")
print_example('webdriver.Firefox()', "Khởi tạo Firefox driver", "Yêu cầu geckodriver")
print_example('driver.maximize_window()', "Phóng to cửa sổ", "Cửa sổ toàn màn hình")

# ==============================================================================
# 2. ĐIỀU HƯỚNG WEB
# ==============================================================================
print_section("2. Điều hướng web")
# driver.get(url)
print_example('driver.get("https://www.example.com")', "Mở URL", url)
# driver.refresh()
print_example('driver.refresh()', "Làm mới trang", "Trang được tải lại")
# driver.back()
print_example('driver.back()', "Quay lại trang trước", "Điều hướng ngược")
# driver.forward()
print_example('driver.forward()', "Tiến tới trang tiếp theo", "Điều hướng tiến")

# ==============================================================================
# 3. TÌM KIẾM PHẦN TỬ
# ==============================================================================
print_section("3. Tìm kiếm phần tử")
print_example('driver.find_element(By.ID, "id")', "Tìm bằng ID", "Trả về phần tử với ID")
print_example('driver.find_element(By.NAME, "q")', "Tìm bằng name", "Trả về input name='q'")
print_example('driver.find_elements(By.TAG_NAME, "a")', "Tìm tất cả thẻ a", "Danh sách các thẻ a")
print_example('driver.find_element(By.CSS_SELECTOR, ".class")', "Tìm bằng CSS selector", "Phần tử với class")
print_example('driver.find_element(By.XPATH, "//h1")', "Tìm bằng XPath", "Trả về thẻ h1")

# ==============================================================================
# 4. TƯƠNG TÁC VỚI PHẦN TỬ
# ==============================================================================
print_section("4. Tương tác với phần tử")
# driver.get(search_url)
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys(sample_query)
print_example('element.send_keys("Python Selenium")', "Nhập văn bản", sample_query)
# search_box.send_keys(Keys.RETURN)
print_example('element.send_keys(Keys.RETURN)', "Nhấn phím Enter", "Gửi biểu mẫu")
# button = driver.find_element(By.TAG_NAME, "button")
# button.click()
print_example('element.click()', "Nhấn vào phần tử", "Thực hiện click")
print_example('element.clear()', "Xóa nội dung ô nhập", "Xóa văn bản")

# ==============================================================================
# 5. LẤY THÔNG TIN PHẦN TỬ
# ==============================================================================
print_section("5. Lấy thông tin phần tử")
# element = driver.find_element(By.TAG_NAME, "h1")
print_example('element.text', "Lấy văn bản", "Nội dung văn bản của phần tử")
print_example('element.get_attribute("href")', "Lấy thuộc tính href", "Giá trị thuộc tính")
print_example('element.is_displayed()', "Kiểm tra hiển thị", "True nếu phần tử hiển thị")
print_example('element.is_enabled()', "Kiểm tra kích hoạt", "True nếu phần tử hoạt động")

# ==============================================================================
# 6. ĐỢI PHẦN TỬ (WAITING)
# ==============================================================================
print_section("6. Đợi phần tử")
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, "id")))
print_example('WebDriverWait(...).until(EC.presence...)', "Đợi phần tử xuất hiện", "Phần tử có ID")
# wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
print_example('EC.element_to_be_clickable(...)', "Đợi phần tử có thể click", "Phần tử có thể click")
print_example('EC.visibility_of_element_located(...)', "Đợi phần tử hiển thị", "Phần tử hiển thị")

# ==============================================================================
# 7. XỬ LÝ ALERT
# ==============================================================================
print_section("7. Xử lý alert")
# driver.execute_script("alert('Test alert');")
# alert = driver.switch_to.alert
print_example('driver.switch_to.alert', "Chuyển đến alert", "Đối tượng alert")
# alert.accept()
print_example('alert.accept()', "Chấp nhận alert", "Đóng alert với OK")
# alert.dismiss()
print_example('alert.dismiss()', "Hủy alert", "Đóng alert với Cancel")
# alert.text
print_example('alert.text', "Lấy văn bản alert", "Nội dung thông báo")

# ==============================================================================
# 8. QUẢN LÝ CỬA SỔ
# ==============================================================================
print_section("8. Quản lý cửa sổ")
# driver.execute_script("window.open('');")
print_example('driver.execute_script("window.open(...)")', "Mở tab mới", "Tab mới được tạo")
# driver.switch_to.window(driver.window_handles[1])
print_example('driver.switch_to.window(...)', "Chuyển tab", "Chuyển sang tab khác")
print_example('driver.current_url', "Lấy URL hiện tại", "URL của trang hiện tại")
print_example('driver.title', "Lấy tiêu đề trang", "Tiêu đề của trang")

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    # driver.find_element(By.ID, "nonexistent")
    print_example('driver.find_element(By.ID, "nonexistent")', "Lỗi phần tử không tồn tại", "NoSuchElementException")
except Exception as e:
    print_example('driver.find_element(By.ID, "nonexistent")', "Lỗi phần tử không tồn tại", f"Lỗi: {str(e)[:50]}...")
try:
    # WebDriverWait(driver, 0.1).until(EC.presence_of_element_located((By.ID, "nonexistent")))
    print_example('WebDriverWait(...).until(...)', "Lỗi hết thời gian đợi", "TimeoutException")
except Exception as e:
    print_example('WebDriverWait(...).until(...)', "Lỗi hết thời gian đợi", f"Lỗi: {str(e)[:50]}...")

# ==============================================================================
# 10. THÔNG TIN MODULE SELENIUM
# ==============================================================================
print_section("10. Thông tin module selenium.webdriver")
from selenium import webdriver
all_classes = [m for m in dir(webdriver) if not m.startswith("_") and isinstance(getattr(webdriver, m), type)]
print(f"Tổng cộng: {len(all_classes)} lớp")
print("\n".join(f" • {cls:<20} → {getattr(webdriver, cls).__doc__.split('.')[0]}" for cls in sorted(all_classes)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'SELENIUM MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://www.selenium.dev/documentation/':^70}")
print("="*70)

# Đóng trình duyệt (chỉ để kiểm tra, không chạy trong console)
# driver.quit()