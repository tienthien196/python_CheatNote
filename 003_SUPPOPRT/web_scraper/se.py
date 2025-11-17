# web_scraper_selenium.py

import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def scrape_with_selenium(url, timeout=10):
    # Cấu hình Chrome ở chế độ headless (không hiện cửa sổ trình duyệt)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")

    driver = None
    try:
        print(f"Đang khởi động trình duyệt và truy cập: {url}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # Đợi cho đến khi <body> xuất hiện (hoặc timeout)
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Thêm thời gian chờ ngắn để đảm bảo JS đã chạy xong (tuỳ trang)
        time.sleep(2)

        # Lấy HTML sau khi render
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Làm sạch: loại bỏ script, style, v.v.
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        # Lấy tiêu đề
        title = soup.title.string.strip() if soup.title else "Không có tiêu đề"
        print(f"\nTiêu đề trang: {title}\n")

        # Lấy toàn bộ văn bản có thể nhìn thấy
        text = soup.get_text(separator='\n', strip=True)
        if text:
            print("Nội dung toàn trang (sau khi render JavaScript):\n")
            print(text)
        else:
            print("Không tìm thấy nội dung.")

    except Exception as e:
        print(f"Lỗi khi cào dữ liệu bằng Selenium: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    default_url = "https://notebooklm.google.com/notebook/aa9f9c90-73d9-4b2e-b09a-194fb4d07520?artifactId=feb41baf-b3b0-4050-9655-2d4410895e42"
    url = sys.argv[1] if len(sys.argv) > 1 else default_url
    scrape_with_selenium(url.strip())