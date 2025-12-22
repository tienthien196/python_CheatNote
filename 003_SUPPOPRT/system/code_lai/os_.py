# -*- coding: utf-8 -*-
"""
Module os trong Python cung cấp các hàm để tương tác với hệ điều hành.
Dưới đây là danh sách các hàm, hằng số, và lớp chính trong module os, cùng mô tả cách dùng và ví dụ.
"""

import os

# --- HẰNG SỐ CỦA MODULE OS ---

print("=== HẰNG SỐ ===")

# Đường phân cách thư mục (phụ thuộc hệ điều hành)
print("os.sep:", os.sep)  # Ví dụ: '/' trên Unix, '\\' trên Windows

# Đường phân cách biến môi trường
print("os.pathsep:", os.pathsep)  # ':' trên Unix, ';' trên Windows

# Ký tự đại diện cho người dùng hiện tại (trên một số hệ thống)
print("os.defpath:", os.defpath)  # Ví dụ: "/bin:/usr/bin"

# Hằng số cho phép kiểm tra quyền truy cập
print("os.F_OK:", os.F_OK)  # Kiểm tra tồn tại
print("os.R_OK:", os.R_OK)  # Kiểm tra quyền đọc
print("os.W_OK:", os.W_OK)  # Kiểm tra quyền ghi
print("os.X_OK:", os.X_OK)  # Kiểm tra quyền thực thi

print()

# --- HÀM LIÊN QUAN ĐẾN ĐƯỜNG DẪN ---

print("=== ĐƯỜNG DẪN ===")

# Lấy thư mục làm việc hiện tại
print("os.getcwd():", os.getcwd())

# Thay đổi thư mục làm việc    
# os.chdir('/path/to/new/dir')

# Kiểm tra đường dẫn tồn tại
print("os.path.exists('os_example.py'):", os.path.exists('os_example.py'))

# Kiểm tra đường dẫn là thư mục hay file
print("os.path.isdir('.'):", os.path.isdir('.'))  # Thư mục hiện tại
print("os.path.isfile('os_example.py'):", os.path.isfile('os_example.py'))


# Tách tên thư mục và tên file
path = "/home/user/file.txt"
dirname, basename = os.path.split(path)
print("os.path.split(path):", dirname, basename)

# Nối đường dẫn theo hệ điều hành
new_path = os.path.join("folder", "subfolder", "file.txt")
print("os.path.join(...):", new_path)

# Lấy tên file từ đường dẫn
print("os.path.basename(path):", os.path.basename(path))

# Lấy thư mục cha
print("os.path.dirname(path):", os.path.dirname(path))

print()

# --- HÀM LIÊN QUAN ĐẾN FILE VÀ THƯ MỤC ---

print("=== FILE & THƯ MỤC ===")

# Tạo thư mục mới (nếu chưa tồn tại)
# os.mkdir("new_folder")

# Tạo thư mục và các thư mục cha (nếu chưa tồn tại)
# os.makedirs("parent/child/grandchild", exist_ok=True)

# Liệt kê nội dung thư mục
print("os.listdir('.'): ", os.listdir('.'))

# Xóa file
# os.remove("file_to_delete.txt")

# Xóa thư mục rỗng
# os.rmdir("empty_folder")

# Xóa thư mục và nội dung (cẩn thận!)
# import shutil; shutil.rmtree("folder_to_delete")

# Đổi tên hoặc di chuyển file/thư mục
# os.rename("old_name.txt", "new_name.txt")

# Lấy thông tin file/thư mục
stat_info = os.stat('.')
print("os.stat('.'): ", stat_info)

print()

# --- HÀM LIÊN QUAN ĐẾN MÔI TRƯỜNG ===

print("=== MÔI TRƯỜNG ===")

# Lấy biến môi trường
home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
print("os.environ.get('HOME'):", home)

# Thiết lập biến môi trường
os.environ['MY_VAR'] = 'my_value'
print("os.environ['MY_VAR']:", os.environ.get('MY_VAR'))

# Lấy giá trị biến môi trường (nếu không có thì trả về giá trị mặc định)
path_value = os.getenv('PATH', 'default_path')
print("os.getenv('PATH'):", path_value[:50] + "...")  # In ngắn gọn

print()

# --- HÀM LIÊN QUAN ĐẾN QUYỀN TRUY CẬP ===

print("=== QUYỀN TRUY CẬP ===")

# Kiểm tra quyền truy cập file/thư mục
print("os.access('.', os.R_OK):", os.access('.', os.R_OK))  # Có quyền đọc không?
print("os.access('.', os.W_OK):", os.access('.', os.W_OK))  # Có quyền ghi không?

print()

# --- HÀM LIÊN QUAN ĐẾN THỰC THI ===

print("=== THỰC THI ===")

# Chạy lệnh hệ điều hành (không an toàn, chỉ dùng khi kiểm soát đầu vào)
# os.system("echo 'Hello from OS'")

# Lấy ID người dùng hiện tại
print("os.getuid():", os.getuid())  # Trên Unix/Linux/MacOS

# Lấy ID nhóm người dùng hiện tại
print("os.getgid():", os.getgid())  # Trên Unix/Linux/MacOS

# Lấy tên người dùng hiện tại
import getpass
print("getpass.getuser():", getpass.getuser())

print()

# --- HÀM LIÊN QUAN ĐẾN THỜI GIAN ===

print("=== THỜI GIAN ===")

# Lấy thời gian hiện tại theo Unix timestamp
print("os.times():", os.times())  # Trả về thời gian CPU và hệ thống

# os.utime(path, times) – Cập nhật thời gian truy cập và sửa đổi

print()

# --- LỚP os.stat_result ===

print("=== os.stat_result ===")

# Kết quả trả về từ os.stat()
stat_info = os.stat('.')
print("st_mode (quyền):", stat_info.st_mode)
print("st_size (kích thước):", stat_info.st_size)
print("st_mtime (thời gian sửa):", stat_info.st_mtime)

print()

# --- HÀM LIÊN QUAN ĐẾN TÊN FILE ===

print("=== TÊN FILE ===")

# Phân tích tên file
name, ext = os.path.splitext("example.py")
print("os.path.splitext('example.py'):", name, ext)

print()

# --- HÀM LIÊN QUAN ĐẾN TEMP ===

print("=== TEMP ===")

# Lấy thư mục tạm thời
print("os.gettempdir():", os.gettempdir())

print()

# --- HÀM LIÊN QUAN ĐẾN PID ===

print("=== PID ===")

# Lấy PID của tiến trình hiện tại
print("os.getpid():", os.getpid())

# Lấy PID của tiến trình cha
print("os.getppid():", os.getppid())

print()

# --- HÀM LIÊN QUAN ĐẾN CWD ===

print("=== CWD ===")

# Lưu thư mục hiện tại
original_dir = os.getcwd()
print("Thư mục ban đầu:", original_dir)

# Thay đổi thư mục
os.chdir('..')
print("Thư mục sau khi cd ..:", os.getcwd())

# Trở lại thư mục ban đầu
os.chdir(original_dir)
print("Trở lại thư mục ban đầu:", os.getcwd())

print()

# --- HÀM LIÊN QUAN ĐẾN ĐỌC GHI FILE (os.open, os.read, os.write) ===

print("=== ĐỌC GHI FILE CẤP THẤP ===")

# Mở file ở cấp hệ điều hành (thường không dùng, dùng open() là đủ)
# fd = os.open("test.txt", os.O_CREAT | os.O_WRONLY)
# os.write(fd, b"Hello from os.write")
# os.close(fd)

print("os.open, os.read, os.write: Dùng để thao tác file ở cấp thấp, thường không cần thiết.")

print()

# --- HẾT ---