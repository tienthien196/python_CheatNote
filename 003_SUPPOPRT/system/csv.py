# -*- coding: utf-8 -*-
"""
CSV Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module csv trong Python
"""

import csv
import io
import os

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(code, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{code:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu để minh họa
sample_data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

# ==============================================================================
# 1. CẤU TRÚC CSV CƠ BẢN
# ==============================================================================
print_section("1. Cấu trúc CSV cơ bản")
print("CSV (Comma-Separated Values) là định dạng văn bản chứa dữ liệu bảng.")
print("Mỗi dòng là một bản ghi, các cột được phân tách bởi dấu phân cách (thường là dấu phẩy).")

# ==============================================================================
# 2. GHI CSV VỚI CSV.WRITER
# ==============================================================================
print_section("2. Ghi dữ liệu vào CSV")
print("--- Ghi với csv.writer ---")

# Ghi vào một file tạm thời
csv_file_path = "temp_sample.csv"
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

print_example("csv.writer(file)", "Tạo writer object", "Thành công")
print_example("writer.writerows(data)", "Ghi nhiều hàng", "Thành công")
print_example("writer.writerow(row)", "Ghi một hàng", "Thành công")

# Ghi vào StringIO để minh họa
string_buffer = io.StringIO()
writer = csv.writer(string_buffer, delimiter=',')
writer.writerows(sample_data)
csv_content = string_buffer.getvalue()
print_example("csv.writer(StringIO)", "Ghi vào bộ nhớ", repr(csv_content.split('\n')[0]))

# Ghi với định dạng khác
string_buffer_alt = io.StringIO()
writer_alt = csv.writer(string_buffer_alt, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
writer_alt.writerows(sample_data)
csv_content_alt = string_buffer_alt.getvalue()
print_example("csv.writer(..., delimiter=';')", "Ghi với dấu phân cách khác", repr(csv_content_alt.split('\n')[0]))

# ==============================================================================
# 3. ĐỌC CSV VỚI CSV.READER
# ==============================================================================
print_section("3. Đọc dữ liệu từ CSV")
print("--- Đọc với csv.reader ---")

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

print_example("csv.reader(file)", "Tạo reader object", "Thành công")
print_example("list(reader)", "Đọc tất cả hàng", rows)

# Đọc từ StringIO
string_buffer.seek(0) # Đặt lại con trỏ
reader = csv.reader(io.StringIO(csv_content))
header = next(reader)
first_row = next(reader)
print_example("next(reader)", "Đọc hàng tiêu đề", header)
print_example("next(reader)", "Đọc hàng đầu tiên", first_row)

# ==============================================================================
# 4. GHI & ĐỌC VỚI CSV.DICTWRITER & CSV.DICTREADER
# ==============================================================================
print_section("4. Ghi/Đọc với DictReader & DictWriter")
print("--- Ghi với csv.DictWriter ---")

sample_dict_data = [
    {"Name": "Alice", "Age": "30", "City": "New York"},
    {"Name": "Bob", "Age": "25", "City": "Los Angeles"},
    {"Name": "Charlie", "Age": "35", "City": "Chicago"}
]

dict_csv_file_path = "temp_dict_sample.csv"
with open(dict_csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(sample_dict_data)

print_example("csv.DictWriter(file, fieldnames)", "Tạo DictWriter", "Thành công")
print_example("writer.writeheader()", "Ghi hàng tiêu đề", "Thành công")
print_example("writer.writerow(dict_row)", "Ghi một hàng từ dict", "Thành công")
print_example("writer.writerows(dict_list)", "Ghi nhiều hàng từ list dict", "Thành công")

print("--- Đọc với csv.DictReader ---")

with open(dict_csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    dict_rows = list(reader)

print_example("csv.DictReader(file)", "Tạo DictReader", "Thành công")
print_example("list(reader)", "Đọc tất cả hàng thành list dict", dict_rows)
print_example("next(reader)", "Đọc hàng đầu tiên thành dict", next(iter(dict_rows)))

# ==============================================================================
# 5. CÁC THAM SỐ ĐỊNH DẠNG CSV
# ==============================================================================
print_section("5. Các tham số định dạng CSV")
print_example("delimiter=';'", "Dấu phân cách giữa các trường", "Dùng ';', mặc định là ','")
print_example("quotechar='\"'", "Ký tự trích dẫn trường", "Dùng '\"', mặc định là '\"'")
print_example("quoting=csv.QUOTE_ALL", "Luôn trích dẫn tất cả trường", "csv.QUOTE_ALL")
print_example("quoting=csv.QUOTE_MINIMAL", "Chỉ trích dẫn khi cần", "csv.QUOTE_MINIMAL (mặc định)")
print_example("skipinitialspace=True", "Bỏ qua khoảng trắng sau dấu phân cách", "True/False")

# Ví dụ về quoting
string_buffer_quote = io.StringIO()
writer_quote = csv.writer(string_buffer_quote, quoting=csv.QUOTE_ALL)
writer_quote.writerow(["Name", "Description"])
writer_quote.writerow(["Alice", "Engineer, Data Scientist"])
content_quoted = string_buffer_quote.getvalue()
print_example("quoting=csv.QUOTE_ALL", "Trích dẫn trường có dấu phân cách", repr(content_quoted.split('\n')[1]))

# ==============================================================================
# 6. XỬ LÝ LỖI
# ==============================================================================
print_section("6. Xử lý lỗi")
try:
    with open("non_existent.csv", mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
except FileNotFoundError as e:
    print_example('open("non_existent.csv", ...)', "Lỗi file không tồn tại", f"Lỗi: {e}")

# ==============================================================================
# 7. MỘT SỐ HẰNG SỐ HỮU ÍCH
# ==============================================================================
print_section("7. Một số hằng số hữu ích")
print_example("csv.QUOTE_ALL", "Luôn trích dẫn", csv.QUOTE_ALL)
print_example("csv.QUOTE_MINIMAL", "Trích dẫn khi cần", csv.QUOTE_MINIMAL)
print_example("csv.QUOTE_NONE", "Không trích dẫn", csv.QUOTE_NONE)
print_example("csv.QUOTE_NONNUMERIC", "Chỉ trích dẫn trường không phải số", csv.QUOTE_NONNUMERIC)

# ==============================================================================
# 8. THÔNG TIN MODULE CSV
# ==============================================================================
print_section("8. Thông tin module csv")
all_csv = [m for m in dir(csv) if not m.startswith("_")]
print(f"Tổng cộng: {len(all_csv)} đối tượng (hằng số, hàm, lớp)")
# print("\n".join(f" • {item:<20}" for item in sorted(all_csv))) # In danh sách nếu cần

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'CSV MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, __import__('sys').version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/csv.html':^70}")
print("="*70)

# Dọn dẹp file tạm
try:
    os.remove(csv_file_path)
    os.remove(dict_csv_file_path)
except OSError:
    pass