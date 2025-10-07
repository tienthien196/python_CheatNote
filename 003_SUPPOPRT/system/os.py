# -*- coding: utf-8 -*-
"""
OS Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module os trong Python
"""

import os
import sys
import stat
from datetime import datetime

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
sample_dir = "sample_dir"
sample_file = "sample.txt"
sample_path = os.path.join(sample_dir, sample_file)
current_dir = os.getcwd()

# Tạo dữ liệu mẫu để minh họa
try:
    os.makedirs(sample_dir, exist_ok=True)
    with open(sample_file, "w") as f:
        f.write("Hello, Python!")
except OSError:
    pass

# ==============================================================================
# 1. QUẢN LÝ ĐƯỜNG DẪN
# ==============================================================================
print_section("1. Quản lý đường dẫn")
print_example("os.getcwd()", "Lấy thư mục làm việc hiện tại", os.getcwd())
print_example('os.path.join("dir", "file.txt")', "Nối đường dẫn", os.path.join("dir", "file.txt"))
print_example('os.path.abspath("sample.txt")', "Đường dẫn tuyệt đối", os.path.abspath(sample_file))
print_example('os.path.basename(sample_path)', "Lấy tên file", os.path.basename(sample_path))
print_example('os.path.dirname(sample_path)', "Lấy thư mục cha", os.path.dirname(sample_path))
print_example('os.path.splitext("sample.txt")', "Tách tên và phần mở rộng", os.path.splitext(sample_file))
print_example('os.path.exists(sample_file)', "Kiểm tra file tồn tại", os.path.exists(sample_file))
print_example('os.path.isfile(sample_file)', "Kiểm tra là file", os.path.isfile(sample_file))
print_example('os.path.isdir(sample_dir)', "Kiểm tra là thư mục", os.path.isdir(sample_dir))

# ==============================================================================
# 2. QUẢN LÝ FILE
# ==============================================================================
print_section("2. Quản lý file")
print_example('os.path.getsize(sample_file)', "Kích thước file (bytes)", os.path.getsize(sample_file))
print_example('os.path.getmtime(sample_file)', "Thời gian sửa đổi cuối", datetime.fromtimestamp(os.path.getmtime(sample_file)))
print_example('os.access(sample_file, os.R_OK)', "Kiểm tra quyền đọc", os.access(sample_file, os.R_OK))
print_example('os.access(sample_file, os.W_OK)', "Kiểm tra quyền ghi", os.access(sample_file, os.W_OK))
try:
    os.chmod(sample_file, stat.S_IRUSR | stat.S_IWUSR)
    print_example('os.chmod(sample_file, ...)', "Thay đổi quyền file", "Thành công")
except OSError as e:
    print_example('os.chmod(sample_file, ...)', "Thay đổi quyền file", f"Lỗi: {e}")
try:
    os.rename(sample_file, "renamed.txt")
    print_example('os.rename(sample_file, ...)', "Đổi tên file", "Thành công")
    os.rename("renamed.txt", sample_file)  # Khôi phục tên
except OSError as e:
    print_example('os.rename(sample_file, ...)', "Đổi tên file", f"Lỗi: {e}")

# ==============================================================================
# 3. QUẢN LÝ THƯ MỤC
# ==============================================================================
print_section("3. Quản lý thư mục")
print_example('os.makedirs("new_dir", exist_ok=True)', "Tạo thư mục", "Thành công" if os.path.exists("new_dir") else "Thất bại")
print_example('os.listdir(sample_dir)', "Liệt kê nội dung thư mục", os.listdir(sample_dir))
try:
    os.rmdir("new_dir")
    print_example('os.rmdir("new_dir")', "Xóa thư mục rỗng", "Thành công")
except OSError as e:
    print_example('os.rmdir("new_dir")', "Xóa thư mục rỗng", f"Lỗi: {e}")

# ==============================================================================
# 4. DUYỆT THƯ MỤC
# ==============================================================================
print_section("4. Duyệt thư mục")
print_example('os.walk(sample_dir)', "Duyệt thư mục (đệ quy)", [(root, dirs, files) for root, dirs, files in os.walk(sample_dir)][0])
print_example('os.scandir(sample_dir)', "Liệt kê chi tiết", [entry.name for entry in os.scandir(sample_dir)])

# ==============================================================================
# 5. XỬ LÝ FILE VÀ XÓA
# ==============================================================================
print_section("5. Xử lý file và xóa")
try:
    with open("temp.txt", "w") as f:
        f.write("Temporary file")
    print_example('open("temp.txt", "w")', "Tạo file tạm", "Thành công")
    os.remove("temp.txt")
    print_example('os.remove("temp.txt")', "Xóa file", "Thành công")
except OSError as e:
    print_example('os.remove("temp.txt")', "Xóa file", f"Lỗi: {e}")

# ==============================================================================
# 6. THÔNG TIN HỆ THỐNG
# ==============================================================================
print_section("6. Thông tin hệ thống")
print_example("os.name", "Tên hệ điều hành", os.name)
print_example("os.environ.get('PATH')", "Biến môi trường PATH", os.environ.get("PATH", "")[:50] + "...")
print_example("os.cpu_count()", "Số CPU", os.cpu_count())
print_example("os.getlogin()", "Tên người dùng", os.getlogin())
print_example("os.getpid()", "ID tiến trình hiện tại", os.getpid())

# ==============================================================================
# 7. THỰC THI LỆNH HỆ THỐNG
# ==============================================================================
print_section("7. Thực thi lệnh hệ thống")
try:
    result = os.system("echo Hello from os.system")
    print_example('os.system("echo Hello...")', "Chạy lệnh hệ thống", result)
except OSError as e:
    print_example('os.system("echo Hello...")', "Chạy lệnh hệ thống", f"Lỗi: {e}")

# ==============================================================================
# 8. BIẾN MÔI TRƯỜNG
# ==============================================================================
print_section("8. Biến môi trường")
print_example('os.environ["HOME"]', "Lấy biến HOME", os.environ.get("HOME", "Không có"))
try:
    os.environ["TEST_VAR"] = "test"
    print_example('os.environ["TEST_VAR"] = "test"', "Thiết lập biến môi trường", os.environ["TEST_VAR"])
except OSError as e:
    print_example('os.environ["TEST_VAR"] = "test"', "Thiết lập biến môi trường", f"Lỗi: {e}")

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    os.stat("non_existent_file.txt")
except FileNotFoundError as e:
    print_example('os.stat("non_existent_file.txt")', "Lỗi file không tồn tại", f"Lỗi: {e}")
try:
    os.makedirs(sample_dir)
except FileExistsError as e:
    print_example('os.makedirs(sample_dir)', "Lỗi thư mục đã tồn tại", f"Lỗi: {e}")

# ==============================================================================
# 10. THÔNG TIN MODULE OS
# ==============================================================================
print_section("10. Thông tin module os")
all_functions = [m for m in dir(os) if not m.startswith("_") and callable(getattr(os, m))]
print(f"Tổng cộng: {len(all_functions)} hàm")
print("\n".join(f" • {func:<20} → {getattr(os, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'OS MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/os.html':^70}")
print("="*70)

# Dọn dẹp dữ liệu mẫu
try:
    os.remove(sample_file)
    os.rmdir(sample_dir)
except OSError:
    pass