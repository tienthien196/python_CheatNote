# -*- coding: utf-8 -*-
"""
Dictionary Creation & Operations Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về tạo và sử dụng dictionary trong Python
"""

import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<45} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
d_empty = {}
d_simple = {"name": "Python", "version": 3.10}
d_nested = {"user": {"name": "Alice", "age": 25}, "active": True}
d_numbers = {"a": 1, "b": 2, "c": 3}
d_mixed = {"id": 1, "tags": ["code", "learn"], "valid": True}
d_pairs = [("x", 10), ("y", 20)]
d_fromkeys = dict.fromkeys(["key1", "key2"], 0)

# ==============================================================================
# 1. KHỞI TẠO DICTIONARY
# ==============================================================================
print_section("1. Khởi tạo dictionary")
print_example("d_empty = {}", "Dictionary rỗng", d_empty)
print_example('d_simple = {"name": "Python"}', "Dictionary cơ bản", d_simple)
print_example('dict([("x", 10), ("y", 20)])', "Từ danh sách cặp", dict(d_pairs))
print_example('dict.fromkeys(["key1", "key2"], 0)', "Từ khóa với giá trị mặc định", d_fromkeys)
print_example('{k: v for k, v in zip(["a", "b"], [1, 2])}', "Dict comprehension", {k: v for k, v in zip(["a", "b"], [1, 2])})
print_example('dict(name="Python", version=3.10)', "Từ tham số từ khóa", dict(name="Python", version=3.10))

# ==============================================================================
# 2. TRUY CẬP PHẦN TỬ
# ==============================================================================
print_section("2. Truy cập phần tử dictionary")
print_example('d_simple["name"]', "Truy cập bằng key", d_simple["name"])
print_example('d_simple.get("name")', "Truy cập an toàn (get)", d_simple.get("name"))
print_example('d_simple.get("missing", "N/A")', "Get với giá trị mặc định", d_simple.get("missing", "N/A"))
print_example('d_nested["user"]["name"]', "Truy cập dict lồng nhau", d_nested["user"]["name"])
try:
    d_simple["missing"]
except KeyError as e:
    print_example('d_simple["missing"]', "Truy cập key không tồn tại (lỗi)", f"Lỗi: {e}")

# ==============================================================================
# 3. THÊM VÀ SỬA PHẦN TỬ
# ==============================================================================
print_section("3. Thêm và sửa phần tử")
d_temp = d_simple.copy()
d_temp["year"] = 2025
print_example('d_temp["year"] = 2025', "Thêm key-value mới", d_temp)
d_temp["name"] = "Python 3.11"
print_example('d_temp["name"] = "Python 3.11"', "Sửa giá trị của key", d_temp)
d_temp.update({"version": 3.11, "license": "PSF"})
print_example('d_temp.update(...)', "Cập nhật nhiều cặp key-value", d_temp)

# ==============================================================================
# 4. XÓA PHẦN TỬ
# ==============================================================================
print_section("4. Xóa phần tử")
d_temp = d_numbers.copy()
del d_temp["a"]
print_example('del d_temp["a"]', "Xóa key cụ thể", d_temp)
popped = d_temp.pop("b")
print_example('d_temp.pop("b")', "Xóa và lấy giá trị", f"popped={popped}, d_temp={d_temp}")
d_temp.popitem()
print_example('d_temp.popitem()', "Xóa cặp cuối cùng", d_temp)
d_temp.clear()
print_example('d_temp.clear()', "Xóa toàn bộ dictionary", d_temp)

# ==============================================================================
# 5. KIỂM TRA TÍNH CHẤT
# ==============================================================================
print_section("5. Kiểm tra tính chất dictionary")
print_example('"name" in d_simple', "Kiểm tra key tồn tại", "name" in d_simple)
print_example('len(d_numbers)', "Độ dài dictionary", len(d_numbers))
print_example('d_empty == {}', "So sánh dictionary rỗng", d_empty == {})
print_example('d_numbers.keys()', "Lấy tất cả key", list(d_numbers.keys()))
print_example('d_numbers.values()', "Lấy tất cả value", list(d_numbers.values()))
print_example('d_numbers.items()', "Lấy tất cả cặp key-value", list(d_numbers.items()))

# ==============================================================================
# 6. KẾT HỢP DICTIONARY
# ==============================================================================
print_section("6. Kết hợp dictionary")
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d_merged = d1 | d2
print_example('d1 | d2', "Hợp nhất (Python 3.9+)", d_merged)
d_updated = d1.copy()
d_updated.update(d2)
print_example('d_updated.update(d2)', "Hợp nhất bằng update", d_updated)
print_example('{**d1, **d2}', "Hợp nhất bằng unpacking", {**d1, **d2})

# ==============================================================================
# 7. DUYỆT DICTIONARY
# ==============================================================================
print_section("7. Duyệt dictionary")
print_example('for k in d_numbers', "Duyệt qua key", [k for k in d_numbers])
print_example('for v in d_numbers.values()', "Duyệt qua value", [v for v in d_numbers.values()])
print_example('for k, v in d_numbers.items()', "Duyệt qua cặp key-value", [(k, v) for k, v in d_numbers.items()])

# ==============================================================================
# 8. DICT COMPREHENSION
# ==============================================================================
print_section("8. Dict comprehension")
print_example('{k: v*2 for k, v in d_numbers.items()}', "Nhân đôi value", {k: v*2 for k, v in d_numbers.items()})
print_example('{k: v for k, v in d_numbers.items() if v > 1}', "Lọc value > 1", {k: v for k, v in d_numbers.items() if v > 1})
print_example('{str(i): i**2 for i in range(3)}', "Tạo dict từ range", {str(i): i**2 for i in range(3)})

# ==============================================================================
# 9. XỬ LÝ DICTIONARY LỒNG NHAU
# ==============================================================================
print_section("9. Xử lý dictionary lồng nhau")
print_example('d_nested["user"]["name"]', "Truy cập key lồng nhau", d_nested["user"]["name"])
d_nested_copy = d_nested.copy()
d_nested_copy["user"]["age"] = 30
print_example('d_nested_copy["user"]["age"] = 30', "Sửa key lồng nhau", d_nested_copy)
from copy import deepcopy
d_deep_copy = deepcopy(d_nested)
print_example('deepcopy(d_nested)', "Sao chép sâu", d_deep_copy)

# ==============================================================================
# 10. THÔNG TIN DICTIONARY
# ==============================================================================
print_section("10. Thông tin dictionary")
all_methods = [m for m in dir(dict) if not m.startswith("__")]
print(f"Tổng cộng: {len(all_methods)} phương thức")
print("\n".join(f" • {method:<20} → {getattr(dict, method).__doc__.split('.')[0]}" for method in sorted(all_methods)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'DICTIONARY CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/stdtypes.html#dict':^70}")
print("="*70)