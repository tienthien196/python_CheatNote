# -*- coding: utf-8 -*-
"""
Tuple Creation & Operations Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về tạo và sử dụng tuple trong Python
"""

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
t_empty = ()
t_single = (42,)
t_numbers = (1, 2, 3, 4, 5)
t_mixed = (1, "hello", 3.14, True)
t_nested = ((1, 2), (3, 4), (5, 6))
t_str = ("Xin", "chào", "Python")
t_repeated = (0,) * 3

# ==============================================================================
# 1. KHỞI TẠO TUPLE
# ==============================================================================
print_section("1. Khởi tạo tuple")
print_example("t_empty = ()", "Tuple rỗng", t_empty)
print_example("t_single = (42,)", "Tuple 1 phần tử (cần dấu phẩy)", t_single)
print_example("t_numbers = (1, 2, 3)", "Tuple nhiều số", t_numbers)
print_example("t_mixed = (1, 'hello', 3.14)", "Tuple hỗn hợp", t_mixed)
print_example("tuple([1, 2, 3])", "Từ list sang tuple", tuple([1, 2, 3]))
print_example("tuple('abc')", "Từ chuỗi sang tuple", tuple("abc"))
print_example("(1, 2, *t_numbers)", "Mở rộng tuple với *", (1, 2, *t_numbers))

# ==============================================================================
# 2. TRUY CẬP PHẦN TỬ
# ==============================================================================
print_section("2. Truy cập phần tử tuple")
print_example("t_numbers[0]", "Truy cập phần tử đầu", t_numbers[0])
print_example("t_numbers[-1]", "Truy cập phần tử cuối", t_numbers[-1])
print_example("t_numbers[1:4]", "Cắt lát (slice)", t_numbers[1:4])
print_example("t_nested[1][0]", "Truy cập tuple lồng nhau", t_nested[1][0])
print_example("t_numbers.index(3)", "Tìm vị trí phần tử", t_numbers.index(3))
print_example("t_numbers.count(2)", "Đếm số lần xuất hiện", t_numbers.count(2))

# ==============================================================================
# 3. KIỂM TRA TÍNH CHẤT
# ==============================================================================
print_section("3. Kiểm tra tính chất tuple")
print_example("'hello' in t_mixed", "Kiểm tra phần tử có trong tuple", "hello" in t_mixed)
print_example("len(t_numbers)", "Độ dài tuple", len(t_numbers))
print_example("min(t_numbers)", "Giá trị nhỏ nhất", min(t_numbers))
print_example("max(t_numbers)", "Giá trị lớn nhất", max(t_numbers))
print_example("sum(t_numbers)", "Tổng các phần tử số", sum(t_numbers))
print_example("all(t_mixed)", "Tất cả phần tử là True?", all(t_mixed))
print_example("any(t_mixed)", "Có ít nhất 1 phần tử True?", any(t_mixed))

# ==============================================================================
# 4. KẾT HỢP VÀ LẶP LẠI TUPLE
# ==============================================================================
print_section("4. Kết hợp và lặp lại tuple")
print_example("t_numbers + t_single", "Nối hai tuple", t_numbers + t_single)
print_example("t_single * 3", "Lặp lại tuple", t_single * 3)
print_example("(0,) * 3", "Tạo tuple lặp", t_repeated)
print_example("tuple(sorted(t_numbers))", "Sắp xếp tuple", tuple(sorted(t_numbers, reverse=True)))

# ==============================================================================
# 5. GIẢI NÉN (UNPACKING) TUPLE
# ==============================================================================
print_section("5. Giải nén tuple")
a, b, c = t_str
print_example("a, b, c = t_str", "Giải nén cơ bản", f"a={a}, b={b}, c={c}")
first, *rest = t_numbers
print_example("first, *rest = t_numbers", "Giải nén với *", f"first={first}, rest={rest}")
*start, last = t_numbers
print_example("*start, last = t_numbers", "Giải nén lấy cuối", f"start={start}, last={last}")

# ==============================================================================
# 6. TÍNH BẤT BIẾN (IMMUTABILITY)
# ==============================================================================
print_section("6. Tính bất biến của tuple")
try:
    t_numbers[0] = 10
except TypeError as e:
    print_example("t_numbers[0] = 10", "Thử sửa phần tử (lỗi)", f"Lỗi: {e}")
print_example("id(t_numbers)", "ID bộ nhớ của tuple", id(t_numbers))
print_example("hash(t_numbers)", "Mã hash (8 số cuối)", hash(t_numbers) % 10**8)

# ==============================================================================
# 7. CHUYỂN ĐỔI VÀ SỬ DỤNG
# ==============================================================================
print_section("7. Chuyển đổi và sử dụng tuple")
print_example("list(t_numbers)", "Chuyển tuple sang list", list(t_numbers))
print_example("set(t_numbers)", "Chuyển tuple sang set", set(t_numbers))
print_example("','.join(t_str)", "Chuyển tuple chuỗi sang chuỗi", ",".join(t_str))
print_example("tuple(zip(t_numbers, t_str))", "Kết hợp nhiều tuple", tuple(zip(t_numbers, t_str)))

# ==============================================================================
# 8. THÔNG TIN TUPLE
# ==============================================================================
print_section("8. Thông tin tuple")
all_methods = [m for m in dir(tuple) if not m.startswith("__")]
print(f"Tổng cộng: {len(all_methods)} phương thức")
print("\n".join(f" • {method:<20} → {getattr(tuple, method).__doc__.split('.')[0]}" for method in sorted(all_methods)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'TUPLE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/stdtypes.html#tuple':^70}")
print("="*70)