from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Đường dẫn đến ChromeDriver
chrome_driver_path = r"E:\app_data\chromedriver-win64\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Bỏ dấu # nếu muốn chạy ẩn

driver = webdriver.Chrome(service=service, options=options)

try:
    # Mở GitHub
    driver.get("https://github.com")

    # Tìm ô tìm kiếm
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("deep learning notebook or handbook")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Chờ kết quả tìm kiếm tải xong

    # Lấy danh sách các liên kết repo
    repo_links = driver.find_elements(By.CSS_SELECTOR, "ul.repo-list h3 a")

    if len(repo_links) == 0:
        print("Không tìm thấy repository nào.")
    else:
        print(f"Tìm thấy {len(repo_links)} repository. Bắt đầu duyệt...")

    # Duyệt từng repo
    for i in range(min(3, len(repo_links))):
        repo_url = repo_links[i].get_attribute("href")
        print(f"\nMở repo thứ {i+1}: {repo_url}")

        # Mở tab mới
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(repo_url)

        time.sleep(5)  # Dừng lại 5 giây để xem repo

        driver.close()  # Đóng tab hiện tại
        driver.switch_to.window(driver.window_handles[0])  # Quay lại tab tìm kiếm

finally:
    driver.quit()