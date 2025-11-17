# web_scraper.py

import requests
from bs4 import BeautifulSoup
import sys

def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi truy cập trang web: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Loại bỏ script, style, nav, footer (tùy chọn, để làm sạch)
    for script_or_style in soup(["script", "style", "nav", "footer", "header", "aside"]):
        script_or_style.decompose()

    # Lấy tiêu đề
    title = soup.title.string.strip() if soup.title else "Không có tiêu đề"
    print(f"Tiêu đề trang: {title}\n")

    # Lấy toàn bộ văn bản từ <body> (hoặc toàn trang nếu không có body)
    body = soup.body if soup.body else soup
    text = body.get_text(separator='\n', strip=True)

    if text:
        print("Toàn bộ nội dung văn bản trên trang:\n")
        print(text)
    else:
        print("Không tìm thấy nội dung văn bản.")

if __name__ == "__main__":
    default_url = "https://tienthien196.github.io/ecosys.resources"
    url = sys.argv[1] if len(sys.argv) > 1 else default_url.strip()
    print(f"Đang cào dữ liệu từ: {url}\n")
    scrape_website(url)