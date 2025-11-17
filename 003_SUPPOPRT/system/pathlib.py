# -*- coding: utf-8 -*-
"""
Pathlib Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module pathlib trong Python
"""

from pathlib import Path, PurePath
import tempfile
import os
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
sample_dir = Path("sample_dir")
sample_file = Path("sample.txt")
sample_path = sample_dir / sample_file

# Tạo dữ liệu mẫu để minh họa
try:
    sample_dir.mkdir(exist_ok=True)
    sample_file.write_text("Hello, Python with Pathlib!")
except OSError:
    pass

# ==============================================================================
# 1. TẠO PATH
# ==============================================================================
print_section("1. Tạo đối tượng Path")
print_example("Path('.')", "Thư mục hiện tại", Path('.'))
print_example("Path.home()", "Thư mục home", Path.home())
print_example('Path("dir", "file.txt")', "Nối đường dẫn", Path("dir", "file.txt"))
print_example('Path("dir") / "file.txt"', "Dùng toán tử / để nối", Path("dir") / "file.txt")
print_example('Path("sample.txt")', "Tạo từ chuỗi", Path("sample.txt"))

# ==============================================================================
# 2. THUỘC TÍNH PATH
# ==============================================================================
print_section("2. Thuộc tính của Path")
print_example('sample_path.parts', "Các phần của đường dẫn", sample_path.parts)
print_example('sample_path.parent', "Thư mục cha", sample_path.parent)
print_example('sample_path.parents[0]', "Cấp cha đầu tiên", sample_path.parents[0])
print_example('sample_path.name', "Tên file/thư mục", sample_path.name)
print_example('sample_path.stem', "Tên không có phần mở rộng", sample_path.stem)
print_example('sample_path.suffix', "Phần mở rộng", sample_path.suffix)
print_example('sample_path.suffixes', "Tất cả phần mở rộng", sample_path.suffixes)
print_example('sample_path.anchor', "Phần neo (root)", sample_path.anchor)
print_example('sample_path.root', "Phần gốc", sample_path.root if hasattr(sample_path, 'root') else "N/A")
print_example('sample_path.drive', "Ổ đĩa (Windows)", sample_path.drive if hasattr(sample_path, 'drive') else "N/A")
print_example('sample_path.is_absolute()', "Là đường dẫn tuyệt đối?", sample_path.is_absolute())

# ==============================================================================
# 3. CHUYỂN ĐỔI PATH
# ==============================================================================
print_section("3. Chuyển đổi và chuẩn hóa")
print_example('sample_path.resolve()', "Đường dẫn tuyệt đối thực", sample_path.resolve())
print_example('sample_path.absolute()', "Đường dẫn tuyệt đối", sample_path.absolute())
print_example('Path("..").resolve()', "Chuẩn hóa đường dẫn", Path("..").resolve())

# ==============================================================================
# 4. KIỂM TRA TỒN TẠI & LOẠI
# ==============================================================================
print_section("4. Kiểm tra tồn tại & loại")
print_example('sample_file.exists()', "File tồn tại?", sample_file.exists())
print_example('sample_dir.is_dir()', "Là thư mục?", sample_dir.is_dir())
print_example('sample_file.is_file()', "Là file?", sample_file.is_file())
print_example('sample_file.is_symlink()', "Là symbolic link?", sample_file.is_symlink())
print_example('sample_file.is_absolute()', "Là đường dẫn tuyệt đối?", sample_file.is_absolute())

# ==============================================================================
# 5. LÀM VIỆC VỚI FILE
# ==============================================================================
print_section("5. Làm việc với file")
print_example('sample_file.read_text()', "Đọc nội dung file", repr(sample_file.read_text()))
print_example('sample_file.read_bytes()', "Đọc nội dung dưới byte", len(sample_file.read_bytes()))
print_example('sample_file.write_text("New content")', "Ghi nội dung mới", "Thành công" if sample_file.write_text("New content") is not None else "Thất bại")
print_example('sample_file.stat().st_size', "Kích thước file (bytes)", sample_file.stat().st_size)
print_example('datetime.fromtimestamp(...)', "Thời gian sửa đổi", datetime.fromtimestamp(sample_file.stat().st_mtime))

# ==============================================================================
# 6. LÀM VIỆC VỚI THƯ MỤC
# ==============================================================================
print_section("6. Làm việc với thư mục")
print_example('sample_dir.mkdir(exist_ok=True)', "Tạo thư mục", "Thành công")
new_dir = Path("new_dir")
new_dir.mkdir(exist_ok=True)
print_example('new_dir.mkdir(exist_ok=True)', "Tạo thư mục mới", "Thành công")
try:
    new_dir.rmdir()
    print_example('new_dir.rmdir()', "Xóa thư mục rỗng", "Thành công")
except OSError:
    print_example('new_dir.rmdir()', "Xóa thư mục rỗng", "Thư mục không trống")

# ==============================================================================
# 7. DUYỆT NỘI DUNG THƯ MỤC
# ==============================================================================
print_section("7. Duyệt nội dung thư mục")
print_example('list(sample_dir.iterdir())', "Liệt kê nội dung thư mục", list(sample_dir.iterdir()))
print_example('list(sample_dir.glob("*.txt"))', "Tìm file theo mẫu", list(sample_dir.glob("*.txt")))
print_example('list(sample_dir.rglob("*.txt"))', "Tìm đệ quy theo mẫu", list(sample_dir.rglob("*.txt")))

# ==============================================================================
# 8. SO SÁNH & GỘP PATH
# ==============================================================================
print_section("8. So sánh & gộp path")
p1 = Path("a", "b")
p2 = Path("a", "c")
print_example('p1 == p2', "So sánh bằng nhau", p1 == p2)
print_example('p1 < p2', "So sánh thứ tự", p1 < p2)
print_example('p1 / "d"', "Gộp path với /", p1 / "d")

# ==============================================================================
# 9. PUREPATH (Không tương tác hệ thống)
# ==============================================================================
print_section("9. PurePath (Không tương tác hệ thống)")
pure_posix = PurePath("/a/b/c")
pure_windows = PurePath(r"C:\a\b\c")
print_example('PurePath("/a/b/c")', "PurePosixPath", pure_posix)
print_example('PurePath(r"C:\\a\\b\\c")', "PureWindowsPath", pure_windows)
print_example('pure_posix.parts', "Phân tách đường dẫn", pure_posix.parts)

# ==============================================================================
# 10. XỬ LÝ LỖI
# ==============================================================================
print_section("10. Xử lý lỗi")
try:
    Path("non_existent.txt").read_text()
except FileNotFoundError as e:
    print_example('Path("non_existent.txt").read_text()', "Lỗi file không tồn tại", f"Lỗi: {e}")

# ==============================================================================
# 11. THÔNG TIN MODULE PATHLIB
# ==============================================================================
print_section("11. Thông tin module pathlib")
all_pathlib = [m for m in dir(Path) if not m.startswith("_") or m in ['__truediv__', '__new__']]
all_pathlib = [m for m in all_pathlib if callable(getattr(Path, m, None))]
print(f"Tổng cộng: {len(all_pathlib)} phương thức (trên lớp Path)")
# print("\n".join(f" • {func:<20}" for func in sorted(all_pathlib)[:10])) # Giới hạn in

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'PATHLIB MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, __import__('sys').version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/pathlib.html':^70}")
print("="*70)

# Dọn dẹp dữ liệu mẫu
try:
    sample_file.unlink()  # Xóa file
    sample_dir.rmdir()    # Xóa thư mục
except OSError:
    pass