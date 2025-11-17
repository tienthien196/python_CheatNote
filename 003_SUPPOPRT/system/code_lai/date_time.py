# -*- coding: utf-8 -*-
"""
Module datetime trong Python cung cấp các lớp để làm việc với ngày, giờ, khoảng thời gian.
Dưới đây là danh sách các class và phương thức chính, cùng mô tả cách dùng và ví dụ.
"""

import datetime

# --- LỚP datetime.datetime ---
# Mô tả: Đại diện cho ngày và giờ (năm, tháng, ngày, giờ, phút, giây, microsecond).
# Cú pháp: datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])

print("=== datetime.datetime ===")

# Tạo một đối tượng datetime
dt = datetime.datetime(2025, 11, 17, 14, 30, 45, 123456)
print("Đối tượng datetime:", dt)  # 2025-11-17 14:30:45.123456

# Truy cập các thuộc tính
print("Năm:", dt.year)            # 2025
print("Tháng:", dt.month)         # 11
print("Ngày:", dt.day)            # 17
print("Giờ:", dt.hour)            # 14
print("Phút:", dt.minute)         # 30
print("Giây:", dt.second)         # 45
print("Micro giây:", dt.microsecond)  # 123456

# Lấy thời gian hiện tại
now = datetime.datetime.now()
print("Thời gian hiện tại:", now)

# Lấy thời gian UTC hiện tại
utc_now = datetime.datetime.utcnow()
print("Thời gian UTC hiện tại:", utc_now)

# Chuyển đổi datetime thành timestamp (số giây từ epoch)
timestamp = dt.timestamp()
print("Timestamp:", timestamp)

# Chuyển đổi từ timestamp thành datetime
dt_from_ts = datetime.datetime.fromtimestamp(timestamp)
print("Datetime từ timestamp:", dt_from_ts)

# Định dạng datetime thành chuỗi
formatted = dt.strftime("%A, %d %B %Y %H:%M:%S")
print("Định dạng:", formatted)  # Monday, 17 November 2025 14:30:45

# Chuyển đổi từ chuỗi thành datetime
dt_parsed = datetime.datetime.strptime("2025-11-17 14:30:00", "%Y-%m-%d %H:%M:%S")
print("Chuỗi -> datetime:", dt_parsed)

# Cộng/trừ thời gian với timedelta
future = dt + datetime.timedelta(days=10, hours=2)
print("10 ngày 2 giờ sau:", future)

past = dt - datetime.timedelta(days=5)
print("5 ngày trước:", past)

print()

# --- LỚP datetime.date ---
# Mô tả: Đại diện cho ngày (năm, tháng, ngày) không có giờ.

print("=== datetime.date ===")

# Tạo một đối tượng date
d = datetime.date(2025, 11, 17)
print("Đối tượng date:", d)  # 2025-11-17

# Lấy ngày hiện tại
today = datetime.date.today()
print("Ngày hôm nay:", today)

# Truy cập thuộc tính
print("Năm:", d.year)       # 2025
print("Tháng:", d.month)    # 11
print("Ngày:", d.day)       # 17

# Cộng/trừ ngày
next_week = d + datetime.timedelta(days=7)
print("7 ngày sau:", next_week)

# So sánh ngày
print("So sánh:", d < next_week)  # True

print()

# --- LỚP datetime.time ---
# Mô tả: Đại diện cho thời gian (giờ, phút, giây, microsecond) không có ngày.

print("=== datetime.time ===")

# Tạo một đối tượng time
t = datetime.time(14, 30, 45, 123456)
print("Đối tượng time:", t)  # 14:30:45.123456

# Truy cập thuộc tính
print("Giờ:", t.hour)           # 14
print("Phút:", t.minute)        # 30
print("Giây:", t.second)        # 45
print("Micro giây:", t.microsecond)  # 123456

print()

# --- LỚP datetime.timedelta ---
# Mô tả: Đại diện cho một khoảng thời gian (hiệu của hai datetime hoặc date).

print("=== datetime.timedelta ===")

# Tạo một khoảng thời gian
delta = datetime.timedelta(days=7, hours=3, minutes=30)
print("Khoảng thời gian:", delta)  # 7 days, 3:30:00

# Cộng với datetime
future_time = now + delta
print("Thời gian sau delta:", future_time)

# Trừ hai datetime để ra timedelta
diff = future_time - now
print("Hiệu giữa hai thời gian:", diff)

print()

# --- LỚP datetime.timezone ---
# Mô tả: Đại diện cho một múi giờ có UTC offset cố định.

print("=== datetime.timezone ===")

# UTC
utc = datetime.timezone.utc
print("Múi giờ UTC:", utc)

# Tạo múi giờ cụ thể (UTC+7)
tz_plus_7 = datetime.timezone(datetime.timedelta(hours=7))
dt_with_tz = datetime.datetime(2025, 11, 17, 14, 30, tzinfo=tz_plus_7)
print("Datetime với múi giờ +7:", dt_with_tz)

print()

# --- LỚP datetime.tzinfo ---
# Mô tả: Lớp trừu tượng dùng để làm việc với múi giờ phức tạp (ví dụ: daylight saving time).
# Người dùng thường không dùng trực tiếp, mà kế thừa để tạo lớp riêng.
# Không có ví dụ trực tiếp ở đây.

print("=== datetime.tzinfo ===")
print("Lớp trừu tượng. Không dùng trực tiếp.")

print()

# --- HẰNG SỐ ===

print("=== HẰNG SỐ ===")
print("Năm nhỏ nhất được hỗ trợ:", datetime.MINYEAR)  # 1
print("Năm lớn nhất được hỗ trợ:", datetime.MAXYEAR)  # 9999
print("Đối tượng UTC:", datetime.timezone.utc)

print()

# --- HẾT ---