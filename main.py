from datetime import datetime, date, time, timedelta

print("=== PYTHON DATETIME MODULE DEMO ===\n")
# XXX
# 1. Lấy thời gian hiện tại
print("1. Thời gian hiện tại:")
now = datetime.now()
print(f"   Ngày giờ đầy đủ: {now}")
print(f"   Chỉ ngày: {now.date()}")
print(f"   Chỉ giờ: {now.time()}")
print()

# 2. Tạo một đối tượng datetime cụ thể
print("2. Tạo một ngày cụ thể (25/12/2025 14:30:00):")
custom_date = datetime(2025, 12, 25, 14, 30, 0)
print(f"   Ngày đã tạo: {custom_date}")
print()

# 3. Lấy chỉ ngày hoặc giờ
print("3. Tách riêng ngày và giờ:")
today = date.today()
print(f"   Hôm nay: {today}")
current_time = time(10, 45, 30)
print(f"   Một giờ cụ thể: {current_time}")
print()

# 4. Định dạng ngày thành chuỗi (strftime)
print("4. Định dạng ngày thành chuỗi:")
formatted_date = now.strftime("%A, %d %B %Y")
formatted_time = now.strftime("%H:%M:%S")
print(f"   Ngày định dạng: {formatted_date}")
print(f"   Giờ định dạng: {formatted_time}")
print()

# 5. Chuyển đổi chuỗi thành datetime (strptime)
print("5. Chuyển đổi chuỗi thành datetime:")
date_string = "2025-11-20 16:45:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"   Chuỗi: '{date_string}' -> {parsed_datetime}")
print()

# 6. Tính toán ngày (cộng/trừ timedelta)
print("6. Tính toán ngày:")
future_date = now + timedelta(days=10)
past_date = now - timedelta(weeks=2)
print(f"   10 ngày sau: {future_date.date()}")
print(f"   2 tuần trước: {past_date.date()}")
print()

# 7. So sánh hai ngày
print("7. So sánh ngày:")
if future_date > now:
    print(f"   {future_date.date()} là sau ngày {now.date()}")
print()

# 8. Một số thuộc tính hữu ích
print("8. Một số thuộc tính của datetime:")
print(f"   Năm: {now.year}")
print(f"   Tháng: {now.month}")
print(f"   Ngày: {now.day}")
print(f"   Thứ (0=Thứ Hai, 6=Chủ Nhật): {now.weekday()}")
print(f"   Số ngày từ epoch (1/1/1970): {now.toordinal()}")
print()

# 9. Ví dụ: Tính số ngày giữa hai mốc
print("9. Tính số ngày giữa hai mốc:")
start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)
diff = end_date - start_date
print(f"   Từ {start_date} đến {end_date} có {diff.days} ngày.")
print()

# 10. Ví dụ nâng cao: Tạo danh sách các ngày trong tuần
print("10. Danh sách các ngày trong tuần tới:")
week_ahead = [now.date() + timedelta(days=i) for i in range(1, 8)]
for day in week_ahead:
    print(f"   - {day.strftime('%A, %d %b %Y')}")