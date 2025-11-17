# -*- coding: utf-8 -*-
"""
Module pathlib trong Python cung cấp các lớp để làm việc với đường dẫn file/thư mục theo cách hướng đối tượng.
Dưới đây là danh sách các class và phương thức chính trong module pathlib, cùng mô tả cách dùng và ví dụ.
"""

from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath

# --- CLASS PurePath (LỚP TRỪU TƯỢNG) ---
# Mô tả: Lớp trừu tượng cho các đường dẫn không phụ thuộc hệ điều hành.
# Không được dùng trực tiếp, nhưng là lớp cha cho PurePosixPath và PureWindowsPath.

print("=== PurePath (LỚP TRỪU TƯỢNG) ===")
# PurePath không nên được dùng trực tiếp
# pure_path = PurePath("/home/user/file.txt")

print("PurePath là lớp trừu tượng, không dùng trực tiếp.")
print()

# --- CLASS PurePosixPath ---
# Mô tả: Dùng cho các hệ Unix/Linux/MacOS.

print("=== PurePosixPath ===")
posix_path = PurePosixPath("/home/user/file.txt")
print("PurePosixPath('/home/user/file.txt'):", posix_path)
print("Drive:", posix_path.drive)
print("Root:", posix_path.root)
print("Anchor:", posix_path.anchor)
print("Parent:", posix_path.parent)
print("Name:", posix_path.name)
print("Stem:", posix_path.stem)
print("Suffix:", posix_path.suffix)

print()

# --- CLASS PureWindowsPath ---
# Mô tả: Dùng cho hệ Windows.

print("=== PureWindowsPath ===")
win_path = PureWindowsPath(r"C:\Users\user\file.txt")
print("PureWindowsPath(r'C:\\Users\\user\\file.txt'):", win_path)
print("Drive:", win_path.drive)  # 'C:'
print("Root:", win_path.root)    # '\'
print("Anchor:", win_path.anchor)  # 'C:\\'
print("Parent:", win_path.parent)
print("Name:", win_path.name)
print("Stem:", win_path.stem)
print("Suffix:", win_path.suffix)

print()

# --- CLASS Path (CHÍNH) ---
# Mô tả: Lớp chính được dùng để làm việc với đường dẫn hệ điều hành hiện tại.

print("=== Path (LỚP CHÍNH) ===")

# Tạo một đối tượng Path
p = Path("/home/user/documents")
print("Path('/home/user/documents'):", p)

# Nối đường dẫn
file_path = p / "my_file.txt"
print("p / 'my_file.txt':", file_path)

# Lấy thư mục làm việc hiện tại
current = Path.cwd()
print("Path.cwd():", current)

# Lấy thư mục home của người dùng
home = Path.home()
print("Path.home():", home)

# Lấy tên file/thư mục
print("file_path.name:", file_path.name)  # 'my_file.txt'

# Lấy phần mở rộng
print("file_path.suffix:", file_path.suffix)  # '.txt'

# Lấy tên không có phần mở rộng
print("file_path.stem:", file_path.stem)  # 'my_file'

# Lấy thư mục cha
print("file_path.parent:", file_path.parent)  # /home/user/documents

# Kiểm tra đường dẫn tồn tại
print("file_path.exists():", file_path.exists())

# Kiểm tra là file hay thư mục
print("file_path.is_file():", file_path.is_file())
print("p.is_dir():", p.is_dir())

# Đổi tên phần mở rộng
new_path = file_path.with_suffix('.log')
print("file_path.with_suffix('.log'):", new_path)

# Đổi tên file
newer_path = file_path.with_name('new_file.txt')
print("file_path.with_name('new_file.txt'):", newer_path)

print()

# --- PHƯƠNG THỨC LÀM VIỆC VỚI FILE/THƯ MỤC ===

print("=== PHƯƠNG THỨC LÀM VIỆC VỚI FILE/THƯ MỤC ===")

# Tạo thư mục (nếu chưa tồn tại)
new_dir = Path("new_folder")
# new_dir.mkdir(exist_ok=True)

# Viết file
test_file = Path("test.txt")
# test_file.write_text("Hello from pathlib!", encoding="utf-8")

# Đọc nội dung file
# content = test_file.read_text(encoding="utf-8")
# print("Nội dung file:", content)

# Xóa file
# test_file.unlink()

# Liệt kê nội dung thư mục
print("Liệt kê thư mục hiện tại:")
for item in Path('.').iterdir():
    print(f"  {item} ({'thư mục' if item.is_dir() else 'file'})")

print()

# --- PHƯƠNG THỨC LIÊN QUAN ĐẾN ĐƯỜNG DẪN ===

print("=== PHƯƠNG THỨC LIÊN QUAN ĐẾN ĐƯỜNG DẪN ===")

p = Path("/home/user/../user/documents/./my_file.txt")

# Giải nén đường dẫn (loại bỏ . và ..)
print("p.resolve():", p.resolve())

# So sánh hai đường dẫn
p1 = Path("/home/user/file.txt")
p2 = Path("/home/user/file.txt")
print("p1 == p2:", p1 == p2)

# Kiểm tra xem một đường dẫn có nằm trong thư mục cha không
child = Path("/home/user/documents/report.txt")
parent = Path("/home")
print("child.is_relative_to(parent):", child.is_relative_to(parent))

# Lấy đường dẫn tương đối
relative = child.relative_to(parent)
print("child.relative_to(parent):", relative)

print()

# --- CÁC PHƯƠNG THỨC KHÁC ===

print("=== CÁC PHƯƠNG THỨC KHÁC ===")

p = Path("example.txt")

# Lấy thời gian truy cập/lần sửa cuối
# print("p.stat().st_mtime:", p.stat().st_mtime)

# Kiểm tra quyền truy cập
# print("p.stat().st_mode:", p.stat().st_mode)

# Lấy kích thước file
# print("p.stat().st_size:", p.stat().st_size)

# Kiểm tra là đường dẫn tuyệt đối hay tương đối
print("p.is_absolute():", p.is_absolute())
abs_path = Path("/home/user/example.txt")
print("abs_path.is_absolute():", abs_path.is_absolute())

# Chuyển sang đường dẫn tuyệt đối
print("p.absolute():", p.absolute())

print()

# --- GLOB VÀ TÌM KIẾM ===

print("=== GLOB VÀ TÌM KIẾM ===")

# Tìm file theo mẫu
print("Các file .py trong thư mục hiện tại:")
for py_file in Path('.').glob('*.py'):
    print(f"  {py_file}")

# Tìm đệ quy (tất cả thư mục con)
print("Tất cả file .py trong thư mục con:")
for py_file in Path('.').rglob('*.py'):
    print(f"  {py_file}")

print()

# --- HẾT ---