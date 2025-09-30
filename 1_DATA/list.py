# -*- coding: utf-8 -*-
"""
List Creation & Operations Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về tạo và sử dụng list trong Python
"""

import sys
from copy import deepcopy

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
l_empty = []
l_numbers = [1, 2, 3, 4, 5]
l_mixed = [1, "hello", 3.14, True]
l_nested = [[1, 2], [3, 4], [5, 6]]
l_str = ["Xin", "chào", "Python"]
l_repeated = [0] * 3

# ==============================================================================
# 1. KHỞI TẠO LIST
# ==============================================================================
print_section("1. Khởi tạo list")
print_example("l_empty = []", "List rỗng", l_empty)
print_example("l_numbers = [1, 2, 3]", "List số", l_numbers)
print_example("l_mixed = [1, 'hello', 3.14]", "List hỗn hợp", l_mixed)
print_example("list(range(3))", "Từ range", list(range(3)))
print_example("list('abc')", "Từ chuỗi", list("abc"))
print_example("[0] * 3", "List lặp lại", l_repeated)
print_example("[x for x in range(3)]", "List comprehension", [x for x in range(3)])

# ==============================================================================
# 2. TRUY CẬP PHẦN TỬ
# ==============================================================================
print_section("2. Truy cập phần tử list")
print_example("l_numbers[0]", "Truy cập phần tử đầu", l_numbers[0])
print_example("l_numbers[-1]", "Truy cập phần tử cuối", l_numbers[-1])
print_example("l_numbers[1:4]", "Cắt lát (slice)", l_numbers[1:4])
print_example("l_nested[1][0]", "Truy cập list lồng nhau", l_nested[1][0])
try:
    l_numbers[10]
except IndexError as e:
    print_example("l_numbers[10]", "Truy cập ngoài phạm vi (lỗi)", f"Lỗi: {e}")

# ==============================================================================
# 3. THÊM PHẦN TỬ
# ==============================================================================
print_section("3. Thêm phần tử")
l_temp = l_numbers.copy()
l_temp.append(6)
print_example("l_temp.append(6)", "Thêm vào cuối", l_temp)
l_temp.insert(1, 1.5)
print_example("l_temp.insert(1, 1.5)", "Thêm tại vị trí", l_temp)
l_temp.extend([7, 8])
print_example("l_temp.extend([7, 8])", "Mở rộng list", l_temp)
l_temp += [9]
print_example("l_temp += [9]", "Nối list bằng +=", l_temp)

# ==============================================================================
# 4. XÓA PHẦN TỬ
# ==============================================================================
print_section("4. Xóa phần tử")
l_temp = l_numbers.copy()
l_temp.remove(3)
print_example("l_temp.remove(3)", "Xóa phần tử đầu tiên", l_temp)
popped = l_temp.pop(1)
print_example("l_temp.pop(1)", "Xóa và lấy phần tử tại vị trí", f"popped={popped}, l_temp={l_temp}")
l_temp.pop()
print_example("l_temp.pop()", "Xóa phần tử cuối", l_temp)
l_temp.clear()
print_example("l_temp.clear()", "Xóa toàn bộ list", l_temp)

# ==============================================================================
# 5. SỬA PHẦN TỬ
# ==============================================================================
print_section("5. Sửa phần tử")
l_temp = l_numbers.copy()
l_temp[0] = 10
print_example("l_temp[0] = 10", "Sửa phần tử tại vị trí", l_temp)
l_temp[1:3] = [20, 30]
print_example("l_temp[1:3] = [20, 30]", "Sửa slice", l_temp)

# ==============================================================================
# 6. KIỂM TRA TÍNH CHẤT
# ==============================================================================
print_section("6. Kiểm tra tính chất list")
print_example("2 in l_numbers", "Kiểm tra phần tử có trong list", 2 in l_numbers)
print_example("len(l_numbers)", "Độ dài list", len(l_numbers))
print_example("min(l_numbers)", "Giá trị nhỏ nhất", min(l_numbers))
print_example("max(l_numbers)", "Giá trị lớn nhất", max(l_numbers))
print_example("sum(l_numbers)", "Tổng các phần tử số", sum(l_numbers))
print_example("l_numbers.count(2)", "Đếm số lần xuất hiện", l_numbers.count(2))
print_example("l_numbers.index(3)", "Tìm vị trí phần tử", l_numbers.index(3))

# ==============================================================================
# 7. SẮP XẾP VÀ ĐẢO NGƯỢC
# ==============================================================================
print_section("7. Sắp xếp và đảo ngược")
l_temp = [3, 1, 4, 2, 5]
l_temp.sort()
print_example("l_temp.sort()", "Sắp xếp tăng dần", l_temp)
l_temp.sort(reverse=True)
print_example("l_temp.sort(reverse=True)", "Sắp xếp giảm dần", l_temp)
l_temp = [3, 1, 4, 2, 5]
l_temp.reverse()
print_example("l_temp.reverse()", "Đảo ngược list", l_temp)
print_example("sorted(l_numbers)", "Sắp xếp không sửa list", sorted(l_numbers))

# ==============================================================================
# 8. LIST COMPREHENSION
# ==============================================================================
print_section("8. List comprehension")
print_example("[x*2 for x in l_numbers]", "Nhân đôi phần tử", [x*2 for x in l_numbers])
print_example("[x for x in l_numbers if x > 2]", "Lọc phần tử > 2", [x for x in l_numbers if x > 2])
print_example("[[x, x**2] for x in range(3)]", "Tạo list lồng nhau", [[x, x**2] for x in range(3)])

# ==============================================================================
# 9. XỬ LÝ LIST LỒNG NHAU
# ==============================================================================
print_section("9. Xử lý list lồng nhau")
print_example("l_nested[1][0]", "Truy cập phần tử lồng nhau", l_nested[1][0])
l_nested_copy = deepcopy(l_nested)
l_nested_copy[1][0] = 30
print_example("l_nested_copy[1][0] = 30", "Sửa phần tử lồng nhau", l_nested_copy)
print_example("[item for sublist in l_nested for item in sublist]", "Làm phẳng list", [item for sublist in l_nested for item in sublist])

# ==============================================================================
# 10. KẾT HỢP VÀ SAO CHÉP
# ==============================================================================
print_section("10. Kết hợp và sao chép list")
print_example("l_numbers + l_str", "Nối hai list", l_numbers + l_str)
print_example("l_numbers * 2", "Lặp lại list", l_numbers * 2)
print_example("l_numbers.copy()", "Sao chép nông", l_numbers.copy())
print_example("deepcopy(l_nested)", "Sao chép sâu", deepcopy(l_nested))

# ==============================================================================
# 11. CHUYỂN ĐỔI LIST
# ==============================================================================
print_section("11. Chuyển đổi list")
print_example("tuple(l_numbers)", "Chuyển sang tuple", tuple(l_numbers))
print_example("set(l_numbers)", "Chuyển sang set", set(l_numbers))
print_example("','.join(l_str)", "Chuyển list chuỗi sang chuỗi", ",".join(l_str))
print_example("dict(zip(l_str, l_numbers))", "Chuyển sang dict", dict(zip(l_str, l_numbers)))

# ==============================================================================
# 12. THÔNG TIN LIST
# ==============================================================================
print_section("12. Thông tin list")
all_methods = [m for m in dir(list) if not m.startswith("__")]
print(f"Tổng cộng: {len(all_methods)} phương thức")
print("\n".join(f" • {method:<20} → {getattr(list, method).__doc__.split('.')[0]}" for method in sorted(all_methods)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'LIST CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/stdtypes.html#list':^70}")
print("="*70)