# -*- coding: utf-8 -*-
"""
Regular Expressions (re) Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module re trong Python
"""

import re
import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
sample_text = "Xin chào, email: user@example.com, phone: +84-123-456-7890, date: 2025-09-25"
url_text = "Visit https://example.com and http://test.org"
number_text = "Numbers: 123, 45.67, -89"
mixed_text = "apple, banana; orange! grape"
email = "user@example.com"
phone = "+84-123-456-7890"

# ==============================================================================
# 1. CÁC MẪU REGEX PHỔ BIẾN
# ==============================================================================
print_section("1. Các mẫu regex phổ biến")
print_example(r"'\\d+'", "Tìm tất cả số", re.findall(r"\d+", number_text))
print_example(r"'\\w+'", "Tìm tất cả từ", re.findall(r"\w+", sample_text))
print_example(r"'[a-zA-Z]+'", "Tìm chữ cái", re.findall(r"[a-zA-Z]+", sample_text))
print_example(r"'\\S+'", "Tìm chuỗi không khoảng trắng", re.findall(r"\S+", sample_text))
print_example(r"'[^a-zA-Z0-9]+'", "Tìm ký tự đặc biệt", re.findall(r"[^a-zA-Z0-9]+", sample_text))
print_example(r"'\\b\\w+\\b'", "Tìm từ toàn vẹn (word boundary)", re.findall(r"\b\w+\b", sample_text))

# ==============================================================================
# 2. TÌM KIẾM VÀ KHỚP
# ==============================================================================
print_section("2. Tìm kiếm và khớp")
print_example(r're.match(r"\w+", sample_text)', "Khớp đầu chuỗi", re.match(r"\w+", sample_text).group() if re.match(r"\w+", sample_text) else None)
print_example(r're.search(r"\w+@\w+\.\w+", sample_text)', "Tìm email", re.search(r"\w+@\w+\.\w+", sample_text).group())
print_example(r're.findall(r"\w+@\w+\.\w+", sample_text)', "Tìm tất cả email", re.findall(r"\w+@\w+\.\w+", sample_text))
print_example(r're.fullmatch(r".*@\w+\.\w+", email)', "Khớp toàn chuỗi", bool(re.fullmatch(r".*@\w+\.\w+", email)))
print_example(r're.search(r"\+\d{2}-\d{3}-\d{3}-\d{4}", sample_text)', "Tìm số điện thoại", re.search(r"\+\d{2}-\d{3}-\d{3}-\d{4}", sample_text).group())

# ==============================================================================
# 3. NHÓM VÀ GHI NHỚ
# ==============================================================================
print_section("3. Nhóm và ghi nhớ")
match = re.search(r"(\w+)@(\w+)\.(\w+)", email)
print_example(r're.search(r"(\w+)@(\w+)\.(\w+)", email)', "Tách email thành nhóm", match.groups() if match else None)
match = re.search(r"(?P<user>\w+)@(?P<domain>\w+)\.(?P<ext>\w+)", email)
print_example(r're.search(r"(?P<user>\w+)...", email)', "Nhóm đặt tên", match.groupdict() if match else None)
print_example(r're.findall(r"(\w+) (\w+)", sample_text)', "Tìm cặp từ", re.findall(r"(\w+) (\w+)", sample_text))

# ==============================================================================
# 4. THAY THẾ CHUỖI
# ==============================================================================
print_section("4. Thay thế chuỗi")
print_example(r're.sub(r"\w+@\w+\.\w+", "***", sample_text)', "Ẩn email", re.sub(r"\w+@\w+\.\w+", "***", sample_text))
print_example(r're.sub(r"\d+", "#", number_text)', "Thay số bằng #", re.sub(r"\d+", "#", number_text))
print_example(r're.sub(r"(\w+)@(\w+)\.(\w+)", r"\1@hidden.\3", email)', "Thay thế nhóm", re.sub(r"(\w+)@(\w+)\.(\w+)", r"\1@hidden.\3", email))

# ==============================================================================
# 5. TÁCH CHUỖI
# ==============================================================================
print_section("5. Tách chuỗi")
print_example(r're.split(r"\W+", mixed_text)', "Tách bằng ký tự đặc biệt", re.split(r"\W+", mixed_text))
print_example(r're.split(r"[,:;]+", mixed_text)', "Tách bằng dấu phẩy, hai chấm", re.split(r"[,:;]+", mixed_text))
print_example(r're.split(r"\s*,\s*", sample_text.strip())', "Tách bằng dấu phẩy và khoảng trắng", re.split(r"\s*,\s*", sample_text.strip()))

# ==============================================================================
# 6. BIÊN DỊCH REGEX (re.compile)
# ==============================================================================
print_section("6. Biên dịch regex")
pattern = re.compile(r"\w+@\w+\.\w+")
print_example(r'pattern.search(sample_text)', "Tìm email với pattern", pattern.search(sample_text).group() if pattern.search(sample_text) else None)
print_example(r'pattern.findall(sample_text)', "Tìm tất cả email", pattern.findall(sample_text))
pattern_phone = re.compile(r"\+\d{2}-\d{3}-\d{3}-\d{4}")
print_example(r'pattern_phone.search(sample_text)', "Tìm số điện thoại", pattern_phone.search(sample_text).group() if pattern_phone.search(sample_text) else None)

# ==============================================================================
# 7. CỜ (FLAGS) TRONG REGEX
# ==============================================================================
print_section("7. Cờ (Flags) trong regex")
print_example(r're.findall(r"xin chào", sample_text, re.IGNORECASE)', "Bỏ qua hoa/thường", re.findall(r"xin chào", sample_text, re.IGNORECASE))
print_example(r're.findall(r"^Xin.*", sample_text, re.MULTILINE)', "Khớp đầu dòng (multiline)", re.findall(r"^Xin.*", sample_text, re.MULTILINE))
print_example(r're.findall(r".+", url_text, re.DOTALL)', "Khớp cả dòng mới (dotall)", re.findall(r".+", url_text, re.DOTALL))

# ==============================================================================
# 8. MẪU REGEX NÂNG CAO
# ==============================================================================
print_section("8. Mẫu regex nâng cao")
print_example(r're.findall(r"https?://[\w\.-]+", url_text)', "Tìm URL", re.findall(r"https?://[\w\.-]+", url_text))
print_example(r're.findall(r"-?\d+\.?\d*", number_text)', "Tìm số (bao gồm âm, thập phân)", re.findall(r"-?\d+\.?\d*", number_text))
print_example(r're.findall(r"\d{4}-\d{2}-\d{2}", sample_text)', "Tìm ngày (YYYY-MM-DD)", re.findall(r"\d{4}-\d{2}-\d{2}", sample_text))

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    re.compile(r"[a-z+")
except re.error as e:
    print_example(r're.compile(r"[a-z+")', "Lỗi cú pháp regex", f"Lỗi: {e}")
try:
    re.search(r"\w+", None)
except TypeError as e:
    print_example(r're.search(r"\w+", None)', "Lỗi kiểu dữ liệu", f"Lỗi: {e}")

# ==============================================================================
# 10. THÔNG TIN MODULE RE
# ==============================================================================
print_section("10. Thông tin module re")
all_functions = [m for m in dir(re) if not m.startswith("_") and callable(getattr(re, m))]
print(f"Tổng cộng: {len(all_functions)} hàm")
print("\n".join(f" • {func:<20} → {getattr(re, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'REGEX CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/re.html':^70}")
print("="*70)