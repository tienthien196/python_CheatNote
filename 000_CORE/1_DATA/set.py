# -*- coding: utf-8 -*-
"""
Set Creation & Operations Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về tạo và sử dụng set trong Python
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
s_empty = set()
s_numbers = {1, 2, 3, 4, 5}
s_mixed = {1, "hello", 3.14}
s_str = {"Xin", "chào", "Python"}
s_numbers2 = {4, 5, 6, 7}
s_frozen = frozenset([1, 2, 3])

# ==============================================================================
# 1. KHỞI TẠO SET
# ==============================================================================
print_section("1. Khởi tạo set")
print_example("s_empty = set()", "Set rỗng", s_empty)
print_example("s_numbers = {1, 2, 3}", "Set số", s_numbers)
print_example("s_mixed = {1, 'hello', 3.14}", "Set hỗn hợp", s_mixed)
print_example("set([1, 2, 2, 3])", "Từ list (loại bỏ trùng lặp)", set([1, 2, 2, 3]))
print_example("set('abc')", "Từ chuỗi", set("abc"))
print_example("{x for x in range(3)}", "Set comprehension", {x for x in range(3)})
print_example("frozenset([1, 2, 3])", "Tạo frozenset (bất biến)", s_frozen)

# ==============================================================================
# 2. TRUY CẬP VÀ KIỂM TRA
# ==============================================================================
print_section("2. Truy cập và kiểm tra set")
print_example("2 in s_numbers", "Kiểm tra phần tử có trong set", 2 in s_numbers)
print_example("len(s_numbers)", "Độ dài set", len(s_numbers))
print_example("min(s_numbers)", "Giá trị nhỏ nhất", min(s_numbers))
print_example("max(s_numbers)", "Giá trị lớn nhất", max(s_numbers))
print_example("sum(s_numbers)", "Tổng các phần tử số", sum(s_numbers))
try:
    s_numbers[0]
except TypeError as e:
    print_example("s_numbers[0]", "Truy cập chỉ số (lỗi)", f"Lỗi: {e}")

# ==============================================================================
# 3. THÊM PHẦN TỬ
# ==============================================================================
print_section("3. Thêm phần tử")
s_temp = s_numbers.copy()
s_temp.add(6)
print_example("s_temp.add(6)", "Thêm một phần tử", s_temp)
s_temp.update([7, 8])
print_example("s_temp.update([7, 8])", "Thêm nhiều phần tử", s_temp)
try:
    s_frozen.add(4)
except AttributeError as e:
    print_example("s_frozen.add(4)", "Thêm vào frozenset (lỗi)", f"Lỗi: {e}")

# ==============================================================================
# 4. XÓA PHẦN TỬ
# ==============================================================================
print_section("4. Xóa phần tử")
s_temp = s_numbers.copy()
s_temp.remove(3)
print_example("s_temp.remove(3)", "Xóa phần tử (lỗi nếu không có)", s_temp)
s_temp.discard(10)
print_example("s_temp.discard(10)", "Xóa phần tử (không lỗi)", s_temp)
popped = s_temp.pop()
print_example("s_temp.pop()", "Xóa và lấy phần tử ngẫu nhiên", f"popped={popped}, s_temp={s_temp}")
s_temp.clear()
print_example("s_temp.clear()", "Xóa toàn bộ set", s_temp)

# ==============================================================================
# 5. CÁC PHÉP TOÁN TẬP HỢP
# ==============================================================================
print_section("5. Các phép toán tập hợp")
print_example("s_numbers | s_numbers2", "Hợp (union)", s_numbers | s_numbers2)
print_example("s_numbers & s_numbers2", "Giao (intersection)", s_numbers & s_numbers2)
print_example("s_numbers - s_numbers2", "Hiệu (difference)", s_numbers - s_numbers2)
print_example("s_numbers ^ s_numbers2", "Hiệu đối xứng (symmetric diff)", s_numbers ^ s_numbers2)
print_example("s_numbers.issubset({1, 2, 3, 4, 5, 6})", "Là tập con?", s_numbers.issubset({1, 2, 3, 4, 5, 6}))
print_example("s_numbers.issuperset({1, 2})", "Là tập cha?", s_numbers.issuperset({1, 2}))
print_example("{1, 2}.isdisjoint({3, 4})", "Không giao nhau?", {1, 2}.isdisjoint({3, 4}))

# ==============================================================================
# 6. CẬP NHẬT TẬP HỢP
# ==============================================================================
print_section("6. Cập nhật tập hợp")
s_temp = s_numbers.copy()
s_temp.update([6, 7])
print_example("s_temp.update([6, 7])", "Cập nhật hợp", s_temp)
s_temp = s_numbers.copy()
s_temp.intersection_update(s_numbers2)
print_example("s_temp.intersection_update(...)", "Cập nhật giao", s_temp)
s_temp = s_numbers.copy()
s_temp.difference_update({1, 2})
print_example("s_temp.difference_update({1, 2})", "Cập nhật hiệu", s_temp)
s_temp = s_numbers.copy()
s_temp.symmetric_difference_update({3, 6, 7})
print_example("s_temp.symmetric_difference_update(...)", "Cập nhật hiệu đối xứng", s_temp)

# ==============================================================================
# 7. DUYỆT SET
# ==============================================================================
print_section("7. Duyệt set")
print_example("for x in s_numbers", "Duyệt qua phần tử", [x for x in s_numbers])
print_example("sorted(s_numbers)", "Duyệt theo thứ tự", sorted(s_numbers))

# ==============================================================================
# 8. SET COMPREHENSION
# ==============================================================================
print_section("8. Set comprehension")
print_example("{x*2 for x in s_numbers}", "Nhân đôi phần tử", {x*2 for x in s_numbers})
print_example("{x for x in s_numbers if x > 2}", "Lọc phần tử > 2", {x for x in s_numbers if x > 2})
print_example("{x**2 for x in range(3)}", "Tạo set từ range", {x**2 for x in range(3)})

# ==============================================================================
# 9. FROZENSET
# ==============================================================================
print_section("9. Frozenset (tập hợp bất biến)")
print_example("frozenset([1, 2, 3])", "Tạo frozenset", s_frozen)
print_example("s_frozen | {4, 5}", "Hợp với frozenset", s_frozen | {4, 5})
print_example("hash(s_frozen)", "Mã hash frozenset (8 số cuối)", hash(s_frozen) % 10**8)
try:
    s_frozen | {4}
except TypeError as e:
    print_example("s_frozen | {4}", "Hợp sai kiểu (lỗi)", f"Lỗi: {e}")

# ==============================================================================
# 10. CHUYỂN ĐỔI SET
# ==============================================================================
print_section("10. Chuyển đổi set")
print_example("list(s_numbers)", "Chuyển sang list", list(s_numbers))
print_example("tuple(s_numbers)", "Chuyển sang tuple", tuple(s_numbers))
print_example("','.join(s_str)", "Chuyển set chuỗi sang chuỗi", ",".join(s_str))
print_example("{k: v for k, v in zip(s_str, s_numbers)}", "Chuyển sang dict", {k: v for k, v in zip(s_str, s_numbers)})

# ==============================================================================
# 11. THÔNG TIN SET
# ==============================================================================
print_section("11. Thông tin set")
all_methods = [m for m in dir(set) if not m.startswith("__")]
print(f"Tổng cộng: {len(all_methods)} phương thức")
print("\n".join(f" • {method:<20} → {getattr(set, method).__doc__.split('.')[0]}" for method in sorted(all_methods)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'SET CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/stdtypes.html#set':^70}")
print("="*70)