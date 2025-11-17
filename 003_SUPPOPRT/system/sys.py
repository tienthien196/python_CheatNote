# -*- coding: utf-8 -*-
"""
Sys Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module sys trong Python
"""

# sys.argv
# sys.exit
# sys.path
# sys.version
# sys.platform
# sys.stdin
# sys.stdout
# sys.stderr

import sys
import os

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(variable_or_func, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{str(variable_or_func):<35} | {desc:<28} | Giá trị: {result}")

# ==============================================================================
# 1. THÔNG TIN PHIÊN BẢN PYTHON
# ==============================================================================
print_section("1. Thông tin phiên bản Python")
print_example("sys.version", "Chuỗi phiên bản đầy đủ", sys.version)
print_example("sys.version_info", "Tuple phiên bản (major, minor, micro)", sys.version_info)
print_example("sys.version_info.major", "Phiên bản chính", sys.version_info.major)
print_example("sys.version_info.minor", "Phiên bản phụ", sys.version_info.minor)
print_example("sys.version_info.micro", "Phiên bản vá", sys.version_info.micro)
print_example("sys.hexversion", "Phiên bản dưới dạng hex", sys.hexversion)

# ==============================================================================
# 2. THÔNG TIN HỆ THỐNG
# ==============================================================================
print_section("2. Thông tin hệ thống")
print_example("sys.platform", "Tên nền tảng (os)", sys.platform)
print_example("sys.implementation", "Chi tiết implementation", sys.implementation.name)
print_example("sys.byteorder", "Thứ tự byte (little/big)", sys.byteorder)
print_example("sys.maxsize", "Giá trị số nguyên lớn nhất", sys.maxsize)
print_example("sys.maxunicode", "Giá trị Unicode lớn nhất", sys.maxunicode)

# ==============================================================================
# 3. ĐƯỜNG DẪN & MODULE
# ==============================================================================
print_section("3. Đường dẫn & Module")
print_example("sys.path", "Danh sách thư mục tìm module", sys.path[:3]) # In ngắn gọn
print_example("sys.modules", "Dict các module đã tải", list(sys.modules.keys())[:5]) # In 5 module đầu
print_example("sys.builtin_module_names", "Tên các module built-in", sys.builtin_module_names[:5]) # In 5 module đầu

# ==============================================================================
# 4. THAM SỐ DÒNG LỆNH
# ==============================================================================
print_section("4. Tham số dòng lệnh")
print_example("sys.argv", "Danh sách tham số dòng lệnh", sys.argv)

# ==============================================================================
# 5. LUỒNG NHẬP/XUẤT
# ==============================================================================
print_section("5. Luồng nhập/xuất chuẩn")
print_example("sys.stdin", "Luồng nhập chuẩn", sys.stdin) # sys.stdin.read()
print_example("sys.stdout", "Luồng xuất chuẩn", sys.stdout)
print_example("sys.stderr", "Luồng lỗi chuẩn", sys.stderr)
print_example("sys.getdefaultencoding()", "Mã hóa mặc định", sys.getdefaultencoding())
print_example("sys.getfilesystemencoding()", "Mã hóa hệ thống tệp", sys.getfilesystemencoding())

# ==============================================================================
# 6. BỘ NHỚ & BIỂU DIỄN ĐỐI TƯỢNG
# ==============================================================================
print_section("6. Bộ nhớ & Biểu diễn đối tượng")
print_example("sys.getsizeof([])", "Kích thước của một list rỗng (bytes)", sys.getsizeof([]))
print_example("sys.getsizeof({})", "Kích thước của một dict rỗng (bytes)", sys.getsizeof({}))
print_example("sys.getsizeof('')", "Kích thước của một chuỗi rỗng (bytes)", sys.getsizeof(''))
print_example("sys.getsizeof(0)", "Kích thước của số nguyên 0 (bytes)", sys.getsizeof(0))
print_example("sys.int_info", "Thông tin về số nguyên", sys.int_info)
print_example("sys.float_info", "Thông tin về số thực", sys.float_info)

# ==============================================================================
# 7. TRÌNH THÔNG DỊCH & HIỆU SUẤT
# ==============================================================================
print_section("7. Trình thông dịch & Hiệu suất")
print_example("sys.getrecursionlimit()", "Giới hạn đệ quy hiện tại", sys.getrecursionlimit())
print_example("sys.setrecursionlimit(2000)", "Thiết lập giới hạn đệ quy", "Thành công" if sys.setrecursionlimit(2000) is None else "Thất bại")
print_example("sys.getrefcount([])", "Đếm số tham chiếu đến object", sys.getrefcount([])) # Luôn tăng 1 do truyền vào hàm
print_example("sys.getprofile()", "Hàm profiler hiện tại", sys.getprofile())
print_example("sys.gettrace()", "Hàm trace hiện tại", sys.gettrace())

# ==============================================================================
# 8. XỬ LÝ LỖI & THOÁT
# ==============================================================================
print_section("8. Xử lý lỗi & Thoát")
print_example("sys.exc_info()", "Thông tin ngoại lệ hiện tại", sys.exc_info())
try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print_example("sys.exc_info() sau lỗi", "Loại, giá trị, traceback", (exc_type.__name__, str(exc_value), exc_traceback is not None))
print_example("sys.exit(0)", "Thoát chương trình", "Chạy sys.exit(0) sẽ kết thúc script")
print_example("sys.excepthook", "Hàm xử lý ngoại lệ mặc định", sys.excepthook)

# ==============================================================================
# 9. CÀI ĐẶT PYTHON
# ==============================================================================
print_section("9. Cài đặt Python")
print_example("sys.executable", "Đường dẫn đến trình thông dịch Python", sys.executable)
print_example("sys.prefix", "Tiền tố cài đặt Python", sys.prefix)
print_example("sys.exec_prefix", "Tiền tố thực thi Python", sys.exec_prefix)
print_example("sys.base_prefix", "Tiền tố cơ sở (cho venv)", sys.base_prefix)
print_example("sys.base_exec_prefix", "Tiền tố thực thi cơ sở", sys.base_exec_prefix)

# ==============================================================================
# 10. THÔNG TIN MODULE SYS
# ==============================================================================
print_section("10. Thông tin module sys")
all_sys = [m for m in dir(sys) if not m.startswith("_") and not callable(getattr(sys, m))]
all_sys_func = [m for m in dir(sys) if not m.startswith("_") and callable(getattr(sys, m))]
print(f"Biến: {len(all_sys)} | Hàm: {len(all_sys_func)}")
# print("\n".join(f" • {var:<20}" for var in sorted(all_sys))) # In danh sách nếu cần

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'SYS MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/sys.html':^70}")
print("="*70)