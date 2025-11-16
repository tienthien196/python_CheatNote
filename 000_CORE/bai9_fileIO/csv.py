# -*- coding: utf-8 -*-
"""
CSV Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module csv trong Python
"""

import csv
import sys
import os
from io import StringIO

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
sample_data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Tokyo"]
]
sample_file = "sample.csv"

# Tạo file CSV mẫu để minh họa
try:
    with open(sample_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
except OSError:
    pass

# ==============================================================================
# 1. ĐỌC FILE CSV
# ==============================================================================
print_section("1. Đọc file CSV")
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)
print_example('csv.reader(file)', "Đọc toàn bộ file CSV", data)
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
print_example('next(csv.reader(file))', "Đọc tiêu đề", header)
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # Bỏ qua tiêu đề
    first_row = next(reader)
print_example('next(reader) sau bỏ tiêu đề', "Đọc dòng đầu tiên", first_row)

# ==============================================================================
# 2. GHI FILE CSV
# ==============================================================================
print_section("2. Ghi file CSV")
new_file = "output.csv"
new_data = [["ID", "Product", "Price"], [1, "Laptop", 999.99], [2, "Phone", 499.99]]
with open(new_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(new_data)
print_example('csv.writer(file).writerows(data)', "Ghi nhiều dòng", os.path.exists(new_file))
with open(new_file, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([3, "Tablet", 299.99])
print_example('writer.writerow([...])', "Thêm một dòng", "Thành công")

# ==============================================================================
# 3. ĐỌC VÀ GHI VỚI DICT
# ==============================================================================
print_section("3. Đọc và ghi với Dict")
with open(sample_file, "r", newline="") as f:
    dict_reader = csv.DictReader(f)
    dict_data = list(dict_reader)
print_example('csv.DictReader(file)', "Đọc thành danh sách dict", dict_data)
dict_data = [{"ID": 1, "Product": "Laptop", "Price": 999.99}, {"ID": 2, "Product": "Phone", "Price": 499.99}]
with open("dict_output.csv", "w", newline="") as f:
    dict_writer = csv.DictWriter(f, fieldnames=["ID", "Product", "Price"])
    dict_writer.writeheader()
    dict_writer.writerows(dict_data)
print_example('csv.DictWriter(file, ...)', "Ghi từ danh sách dict", os.path.exists("dict_output.csv"))

# ==============================================================================
# 4. XỬ LÝ DẤU PHÂN CÁCH VÀ KÝ TỰ ĐẶC BIỆT
# ==============================================================================
print_section("4. Xử lý dấu phân cách và ký tự đặc biệt")
with open(sample_file, "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(sample_data)
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    data_semicolon = list(reader)
print_example('csv.reader(file, delimiter=";")', "Đọc với dấu phân cách ;", data_semicolon)
with open("quote.csv", "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Text", "Data, with comma"])
print_example('csv.writer(..., quoting=QUOTE_MINIMAL)', "Xử lý dấu phẩy trong dữ liệu", "Thành công")

# ==============================================================================
# 5. ĐỌC CSV TỪ CHUỖI
# ==============================================================================
print_section("5. Đọc CSV từ chuỗi")
csv_string = "Name,Age,City\nAlice,25,New York\nBob,30,London"
string_reader = csv.reader(StringIO(csv_string))
string_data = list(string_reader)
print_example('csv.reader(StringIO(string))', "Đọc CSV từ chuỗi", string_data)

# ==============================================================================
# 6. GHI CSV RA CHUỖI
# ==============================================================================
print_section("6. Ghi CSV ra chuỗi")
output = StringIO()
writer = csv.writer(output)
writer.writerow(["Name", "Age", "City"])
writer.writerow(["Alice", 25, "New York"])
csv_output = output.getvalue()
print_example('csv.writer(StringIO())', "Ghi CSV ra chuỗi", csv_output.strip())

# ==============================================================================
# 7. XỬ LÝ LỖI
# ==============================================================================
print_section("7. Xử lý lỗi")
try:
    with open("non_existent.csv", "r", newline="") as f:
        reader = csv.reader(f)
        list(reader)
except FileNotFoundError as e:
    print_example('open("non_existent.csv")', "Lỗi file không tồn tại", f"Lỗi: {e}")
try:
    with open(sample_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Valid", 123])
        writer.writerow(["Invalid", "text", "extra"])  # Dòng có số cột sai
except csv.Error as e:
    print_example('writer.writerow([...])', "Lỗi số cột không đồng nhất", f"Lỗi: {e}")

# ==============================================================================
# 8. TÙY CHỈNH ĐỌC/GHI
# ==============================================================================
print_section("8. Tùy chỉnh đọc/ghi")
with open(sample_file, "w", newline="") as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(sample_data)
print_example('csv.writer(..., lineterminator="\\n")', "Tùy chỉnh ký tự xuống dòng", "Thành công")
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f, skipinitialspace=True)
    data_skipspace = list(reader)
print_example('csv.reader(..., skipinitialspace=True)', "Bỏ khoảng trắng đầu dòng", data_skipspace)

# ==============================================================================
# 9. LÀM VIỆC VỚI CSV LỚN
# ==============================================================================
print_section("9. Làm việc với CSV lớn")
with open(sample_file, "r", newline="") as f:
    reader = csv.reader(f)
    count = sum(1 for row in reader)
print_example('sum(1 for row in reader)', "Đếm số dòng", count)
with open(sample_file, "r", newline="") as f:
    reader = csv.DictReader(f)
    filtered = [row for row in reader if int(row["Age"]) > 25]
print_example('filter DictReader', "Lọc dòng theo điều kiện", filtered)

# ==============================================================================
# 10. THÔNG TIN MODULE CSV
# ==============================================================================
print_section("10. Thông tin module csv")
all_functions = [m for m in dir(csv) if not m.startswith("_") and callable(getattr(csv, m))]
print(f"Tổng cộng: {len(all_functions)} hàm")
print("\n".join(f" • {func:<20} → {getattr(csv, func).__doc__.split('.')[0]}" for func in sorted(all_functions)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'CSV MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/csv.html':^70}")
print("="*70)

# Dọn dẹp dữ liệu mẫu
try:
    os.remove(sample_file)
    os.remove(new_file)
    os.remove("dict_output.csv")
    os.remove("quote.csv")
except OSError:
    pass