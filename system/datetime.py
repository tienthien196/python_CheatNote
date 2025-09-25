# -*- coding: utf-8 -*-
"""
Datetime Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module datetime trong Python
"""

import sys
from datetime import datetime, date, time, timedelta, timezone
import time

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
now = datetime.now()
sample_date = date(2025, 9, 25)
sample_time = time(17, 56)
sample_datetime = datetime(2025, 9, 25, 17, 56)
sample_timedelta = timedelta(days=5, hours=3)

# ==============================================================================
# 1. KHỞI TẠO NGÀY GIỜ
# ==============================================================================
print_section("1. Khởi tạo ngày giờ")
print_example("datetime.now()", "Ngày giờ hiện tại", datetime.now())
print_example("date(2025, 9, 25)", "Tạo date", sample_date)
print_example("time(17, 56)", "Tạo time", sample_time)
print_example("datetime(2025, 9, 25, 17, 56)", "Tạo datetime", sample_datetime)
print_example("datetime.fromisoformat('2025-09-25')", "Từ chuỗi ISO", datetime.fromisoformat("2025-09-25"))
print_example("datetime.fromtimestamp(time.time())", "Từ timestamp", datetime.fromtimestamp(time.time()))

# ==============================================================================
# 2. TRUY CẬP THÀNH PHẦN
# ==============================================================================
print_section("2. Truy cập thành phần")
print_example("sample_datetime.year", "Lấy năm", sample_datetime.year)
print_example("sample_datetime.month", "Lấy tháng", sample_datetime.month)
print_example("sample_datetime.day", "Lấy ngày", sample_datetime.day)
print_example("sample_datetime.hour", "Lấy giờ", sample_datetime.hour)
print_example("sample_datetime.minute", "Lấy phút", sample_datetime.minute)
print_example("sample_datetime.weekday()", "Lấy thứ (0=Thứ Hai)", sample_datetime.weekday())
print_example("sample_datetime.isoweekday()", "Lấy thứ (1=Thứ Hai)", sample_datetime.isoweekday())

# ==============================================================================
# 3. ĐỊNH DẠNG NGÀY GIỜ
# ==============================================================================
print_section("3. Định dạng ngày giờ")
print_example('sample_datetime.strftime("%Y-%m-%d")', "Định dạng YYYY-MM-DD", sample_datetime.strftime("%Y-%m-%d"))
print_example('sample_datetime.strftime("%H:%M:%S")', "Định dạng HH:MM:SS", sample_datetime.strftime("%H:%M:%S"))
print_example('sample_datetime.strftime("%d/%m/%Y")', "Định dạng DD/MM/YYYY", sample_datetime.strftime("%d/%m/%Y"))
print_example('datetime.strptime("25/09/2025", "%d/%m/%Y")', "Từ chuỗi sang datetime", datetime.strptime("25/09/2025", "%d/%m/%Y"))
print_example('sample_date.isoformat()', "Định dạng ISO", sample_date.isoformat())

# ==============================================================================
# 4. PHÉP TOÁN VỚI NGÀY GIỜ
# ==============================================================================
print_section("4. Phép toán với ngày giờ")
print_example("sample_datetime + timedelta(days=5)", "Cộng 5 ngày", sample_datetime + timedelta(days=5))
print_example("sample_datetime - timedelta(hours=3)", "Trừ 3 giờ", sample_datetime - timedelta(hours=3))
print_example("(datetime.now() - sample_datetime)", "Khoảng cách thời gian", str(datetime.now() - sample_datetime))
print_example("sample_date > date(2025, 9, 24)", "So sánh ngày", sample_date > date(2025, 9, 24))
print_example("sample_datetime.replace(year=2026)", "Thay đổi năm", sample_datetime.replace(year=2026))

# ==============================================================================
# 5. LÀM VIỆC VỚI TIMEDELTA
# ==============================================================================
print_section("5. Làm việc với timedelta")
print_example("timedelta(days=5, hours=3)", "Tạo timedelta", sample_timedelta)
print_example("sample_timedelta.total_seconds()", "Chuyển sang giây", sample_timedelta.total_seconds())
print_example("sample_timedelta.days", "Lấy số ngày", sample_timedelta.days)
print_example("sample_timedelta.seconds", "Lấy số giây (không tính ngày)", sample_timedelta.seconds)
print_example("timedelta(weeks=1)", "Tạo từ tuần", timedelta(weeks=1))

# ==============================================================================
# 6. MÚI GIỜ
# ==============================================================================
print_section("6. Múi giờ")
utc_dt = datetime.now(timezone.utc)
print_example("datetime.now(timezone.utc)", "Ngày giờ UTC", utc_dt)
print_example("sample_datetime.astimezone(timezone.utc)", "Chuyển sang UTC", sample_datetime.replace(tzinfo=timezone.utc))
print_example("sample_datetime.tzinfo", "Thông tin múi giờ", sample_datetime.tzinfo)
offset = timezone(timedelta(hours=7))
print_example("timezone(timedelta(hours=7))", "Tạo múi giờ +07:00", sample_datetime.replace(tzinfo=offset))

# ==============================================================================
# 7. CHUYỂN ĐỔI VÀ ĐỊNH DẠNG
# ==============================================================================
print_section("7. Chuyển đổi và định dạng")
print_example("sample_datetime.timestamp()", "Chuyển sang timestamp", sample_datetime.timestamp())
print_example("datetime.fromtimestamp(1753608960)", "Từ timestamp sang datetime", datetime.fromtimestamp(1753608960))
print_example("sample_date.toordinal()", "Số ngày từ 0001-01-01", sample_date.toordinal())
print_example("date.fromordinal(739055)", "Từ ordinal sang date", date.fromordinal(739055))
print_example('sample_datetime.strftime("%B %d, %Y")', "Định dạng đầy đủ", sample_datetime.strftime("%B %d, %Y"))

# ==============================================================================
# 8. XỬ LÝ LỖI
# ==============================================================================
print_section("8. Xử lý lỗi")
try:
    datetime(2025, 13, 1)
except ValueError as e:
    print_example("datetime(2025, 13, 1)", "Lỗi tháng không hợp lệ", f"Lỗi: {e}")
try:
    datetime.strptime("2025-09-25", "%Y-%m")
except ValueError as e:
    print_example('datetime.strptime("2025-09-25", "%Y-%m")', "Lỗi định dạng", f"Lỗi: {e}")

# ==============================================================================
# 9. CÁC PHƯƠNG THỨC NÂNG CAO
# ==============================================================================
print_section("9. Các phương thức nâng cao")
print_example("sample_datetime.isocalendar()", "Lịch ISO (năm, tuần, thứ)", sample_datetime.isocalendar())
print_example("sample_datetime.ctime()", "Định dạng kiểu ctime", sample_datetime.ctime())
print_example("date.today()", "Ngày hiện tại", date.today())
print_example("datetime.combine(sample_date, sample_time)", "Kết hợp date và time", datetime.combine(sample_date, sample_time))

# ==============================================================================
# 10. THÔNG TIN MODULE DATETIME
# ==============================================================================
print_section("10. Thông tin module datetime")
all_functions = [m for m in dir(datetime) if not m.startswith("_") and callable(getattr(datetime, m))]
print(f"Tổng cộng: {len(all_functions)} hàm")
print("\n".join(f" • {func:<20} → {getattr(datetime, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'DATETIME MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/datetime.html':^70}")
print("="*70)