# -*- coding: utf-8 -*-
"""
Exception Handling & File I/O Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo về try/except và đọc/ghi file
"""

import sys
from pathlib import Path


def print_section(title):
    """In tiêu đề nhóm nội dung"""
    print("\n" + "=" * 70)
    print(f"{title.upper():^70}")
    print("=" * 70)


def print_example(code, desc, result=None):
    """In ví dụ theo định dạng chuẩn"""
    if result is not None:
        print(f"{code:<40} | {desc:<25} | → {result}")
    else:
        print(f"{code:<40} | {desc}")


# Dữ liệu mẫu
filename = "test.txt"
content = "Xin chào từ Python!\nDòng thứ hai."
invalid_filename = "/invalid/path/test.txt"


# ==============================================================================
# 1. CƠ CHẾ TRY / EXCEPT CƠ BẢN
# ==============================================================================
print_section("1. Cơ chế try / except cơ bản")

try:
    result = 10 / 0
except ZeroDivisionError:
    result = "Lỗi chia cho 0"

print_example("try: 10/0", "Bắt lỗi cụ thể", result)


# ==============================================================================
# 2. CÁC KHỐI LỆNH TRONG TRY-EXCEPT
# ==============================================================================
print_section("2. Các khối lệnh: try, except, else, finally")

try:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Thử mở file để ghi.")
except FileNotFoundError:
    extra = "Không tìm thấy đường dẫn"
else:
    extra = "File được tạo thành công"
finally:
    try:
        Path(filename).unlink()  # Xóa file sau khi test
    except:
        pass  # Không sao nếu file không tồn tại

print_example("try-except-else-finally", "Sử dụng đầy đủ các khối", extra)


# ==============================================================================
# 3. BẮT NHIỀU LOẠI NGOẠI LỆ
# ==============================================================================
print_section("3. Bắt nhiều loại ngoại lệ")

errors = []
for value in [10, 0, "abc"]:
    try:
        result = 10 / value
    except ZeroDivisionError:
        errors.append("Chia cho 0")
    except TypeError:
        errors.append("Sai kiểu dữ liệu")
    except Exception as e:
        errors.append(f"Lỗi khác: {e}")

print_example("except ZeroDivisionError:", "Bắt từng lỗi cụ thể", errors)


# ==============================================================================
# 4. BẮT NGOẠI LỆ TỔNG QUÁT
# ==============================================================================
print_section("4. Bắt ngoại lệ tổng quát")

try:
    x = int("không phải số")
except Exception as e:
    error_msg = str(e)

print_example("except Exception as e:", "Bắt mọi lỗi + lưu thông báo", error_msg)


# ==============================================================================
# 5. RAISE – PHÁT SINH NGOẠI LỆ
# ==============================================================================
print_section("5. raise – Phát sinh ngoại lệ")

def validate_age(age):
    if age < 0:
        raise ValueError("Tuổi không thể âm!")
    return "Hợp lệ"

try:
    validate_age(-5)
except ValueError as e:
    raised_error = str(e)

print_example('raise ValueError("...")', "Tự phát sinh lỗi", )


# ==============================================================================
# 6. ASSERT – KIỂM TRA ĐIỀU KIỆN
# ==============================================================================
print_section("6. assert – Kiểm tra điều kiện")

assert_result = "Không có lỗi"
try:
    assert 2 + 2 == 5, "Toán học sai rồi!"
except AssertionError as e:
    assert_result = str(e)

print_example('assert x == y, "msg"', "Kiểm tra điều kiện", assert_result)


# ==============================================================================
# 7. MỞ VÀ ĐÓNG FILE (CŨ – DÙNG CLOSE)
# ==============================================================================
print_section("7. Mở file kiểu cũ (dùng close)")

f = open(filename, 'w', encoding='utf-8')
f.write("Dữ liệu thử nghiệm")
f.close()

# Đọc lại
f = open(filename, 'r', encoding='utf-8')
data_old = f.read()
f.close()

# Dọn dẹp
Path(filename).unlink()

print_example("open() + close()", "Phương pháp cũ", repr(data_old))


# ==============================================================================
# 8. MỞ FILE BẰNG WITH (KHUYÊN DÙNG)
# ==============================================================================
print_section("8. Mở file bằng with (context manager)")

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

with open(filename, 'r', encoding='utf-8') as f:
    data_with = f.read()

Path(filename).unlink()  # Xóa file

print_example("with open(...) as f:", "Tự động đóng file", data_with)


# ==============================================================================
# 9. CÁC CHẾ ĐỘ MỞ FILE
# ==============================================================================
print_section("9. Các chế độ mở file")

modes = [
    ("r", "Đọc (mặc định)"),
    ("w", "Ghi – ghi đè hoặc tạo mới"),
    ("a", "Ghi – nối vào cuối"),
    ("x", "Tạo mới – báo lỗi nếu đã tồn tại"),
    ("r+", "Đọc và ghi"),
    ("w+", "Ghi và đọc – ghi đè"),
    ("a+", "Nối và đọc"),
]

for mode, desc in modes:
    print(f" • {mode:<2} → {desc}")


# ==============================================================================
# 10. ĐỌC FILE THEO CÁCH KHÁC NHAU
# ==============================================================================
print_section("10. Đọc file theo nhiều cách")

# Ghi file tạm
with open(filename, 'w', encoding='utf-8') as f:
    f.write("Dòng 1\nDòng 2\nDòng 3\n")

with open(filename, 'r', encoding='utf-8') as f:
    read_all = f.read()
with open(filename, 'r', encoding='utf-8') as f:
    read_line = f.readline()
with open(filename, 'r', encoding='utf-8') as f:
    read_lines = f.readlines()

Path(filename).unlink()

print_example(".read()", "Đọc toàn bộ nội dung", repr(read_all))
print_example(".readline()", "Đọc 1 dòng đầu", repr(read_line))
print_example(".readlines()", "Đọc thành danh sách dòng", len(read_lines))


# ==============================================================================
# 11. GHI FILE – GHI ĐÈ VÀ NỐI
# ==============================================================================
print_section("11. Ghi file – ghi đè vs nối")

# Ghi đè (w)
with open(filename, 'w', encoding='utf-8') as f:
    f.write("Ghi đè\n")

# Nối (a)
with open(filename, 'a', encoding='utf-8') as f:
    f.write("Nối thêm dòng\n")

with open(filename, 'r', encoding='utf-8') as f:
    append_content = f.read()

Path(filename).unlink()

print_example("'w' mode", "Ghi đè", "Ghi đè ở dòng đầu")
print_example("'a' mode", "Nối vào cuối", repr(append_content))


# ==============================================================================
# 12. XỬ LÝ LỖI KHI LÀM VIỆC VỚI FILE
# ==============================================================================
print_section("12. Xử lý lỗi khi làm việc với file")

file_status = ""
try:
    with open(invalid_filename, 'r', encoding='utf-8') as f:
        data = f.read()
except FileNotFoundError:
    file_status = "File hoặc thư mục không tồn tại"
except PermissionError:
    file_status = "Không có quyền truy cập"
except Exception as e:
    file_status = f"Lỗi khác: {e}"

print_example("FileNotFoundError", "Bắt lỗi mở file", file_status)


# ==============================================================================
# 13. KIỂM TRA SỰ TỒN TẠI CỦA FILE
# ==============================================================================
print_section("13. Kiểm tra sự tồn tại của file")

existing = Path(filename).exists()
Path(filename).touch()  # Tạo file rỗng
still_exists = Path(filename).exists()
Path(filename).unlink()  # Xóa

print_example("Path(file).exists()", "Kiểm tra file tồn tại?", still_exists)
print_example("Path(file).is_file()", "Có phải là file?", Path(__file__).is_file())


# ==============================================================================
# 14. SỬ DỤNG PATHLIB (MODERN WAY)
# ==============================================================================
print_section("14. Sử dụng pathlib – hiện đại & an toàn")

# Tạo đường dẫn
p = Path("data") / "output.txt"

print_example("Path('data') / 'file.txt'", "Nối đường dẫn", p)
print_example("p.parent", "Thư mục cha", p.parent)
print_example("p.name", "Tên file", p.name)
print_example("p.suffix", "Phần mở rộng", p.suffix)

# Ghi và đọc bằng pathlib
p.write_text("Hello từ pathlib!", encoding='utf-8')
read_back = p.read_text(encoding='utf-8')
p.unlink()  # Xóa

print_example("p.write_text()", "Ghi nhanh", repr(read_back))


# ==============================================================================
# 15. EXCEPTIONS THƯỜNG GẶP
# ==============================================================================
print_section("15. Các Exception thường gặp")

common_exceptions = [
    ("ValueError", "Dữ liệu không hợp lệ (int('abc'))"),
    ("TypeError", "Sai kiểu (1 + 'a')"),
    ("FileNotFoundError", "Không tìm thấy file"),
    ("PermissionError", "Không có quyền"),
    ("IndexError", "Truy cập chỉ số ngoài danh sách"),
    ("KeyError", "Truy cập key không tồn tại trong dict"),
    ("ZeroDivisionError", "Chia cho 0"),
    ("ImportError", "Không tìm thấy module"),
    ("UnicodeDecodeError", "Lỗi mã hóa (đọc file sai encoding)"),
]

for exc, desc in common_exceptions:
    print(f" • {exc:<18} → {desc}")


# ==============================================================================
# 16. TIPS & BEST PRACTICES
# ==============================================================================
print_section("16. Tips & Best Practices")

tips = [
    "✅ Luôn dùng `with open()` thay vì `open()` + `close()`",
    "✅ Dùng `encoding='utf-8'` khi xử lý tiếng Việt",
    "✅ Bắt lỗi cụ thể hơn là `except Exception`",
    "✅ Dùng `pathlib.Path` thay cho chuỗi đường dẫn",
    "✅ Kiểm tra tồn tại file trước khi đọc nếu cần",
    "✅ Tránh hardcode đường dẫn tuyệt đối",
    "✅ Dùng `try-except` khi tương tác với hệ thống ngoài",
]

for tip in tips:
    print(f" {tip}")


# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "=" * 70)
print(f"{'CHEAT SHEET: TRY/EXCEPT & FILE I/O HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/tutorial/errors.html':^70}")
print("=" * 70)