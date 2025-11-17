# -*- coding: utf-8 -*-
"""
JSON Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module json trong Python
"""

import json
import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method_call, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method_call:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu Python
sample_data = {
    "name": "Võ Tiến Thiện",
    "age": 22,
    "student": True,
    "courses": ["Math", "Physics", "Python"],
    "address": {
        "city": "Ho Chi Minh City",
        "zip_code": "700000"
    },
    "graduated": None
}

# JSON string mẫu
sample_json_str = json.dumps(sample_data)

# ==============================================================================
# 1. CHUYỂN ĐỔI PYTHON -> JSON (SERIALIZE)
# ==============================================================================
print_section("1. Chuyển đổi Python sang JSON (Serialize)")
print_example('json.dumps(data)', "Chuyển dict sang chuỗi JSON", json.dumps(sample_data))
print_example('json.dumps(data, indent=2)', "JSON có thụt lề (indent)", json.dumps(sample_data, indent=2))
print_example('json.dumps(data, sort_keys=True)', "JSON với khóa được sắp xếp", json.dumps(sample_data, sort_keys=True))
print_example('json.dumps(data, separators=(",", ":"))', "JSON với dấu phân cách tùy chỉnh", json.dumps(sample_data, separators=(',', ':')))
print_example('json.dumps(data, ensure_ascii=False)', "JSON với ký tự Unicode", json.dumps({"tiếng việt": "đẹp"}, ensure_ascii=False))

# ==============================================================================
# 2. CHUYỂN ĐỔI JSON -> PYTHON (DESERIALIZE)
# ==============================================================================
print_section("2. Chuyển đổi JSON sang Python (Deserialize)")
print_example('json.loads(json_str)', "Chuyển chuỗi JSON sang Python", json.loads(sample_json_str))
nested_json = '{"person": {"name": "Alice", "age": 30}}'
print_example('json.loads(nested_json)', "JSON lồng nhau", json.loads(nested_json))

# ==============================================================================
# 3. LÀM VIỆC VỚI TỆP JSON
# ==============================================================================
print_section("3. Làm việc với tệp JSON")
# Ví dụ sử dụng tệp tạm thời trong thực tế:
# with open('data.json', 'w') as f:
#     json.dump(sample_data, f, indent=2)
# with open('data.json', 'r') as f:
#     loaded_data = json.load(f)
# print_example('json.dump(data, f)', "Ghi dữ liệu vào tệp", "Thành công")
# print_example('json.load(f)', "Đọc dữ liệu từ tệp", loaded_data)

# Thay vì thao tác với tệp thật, ta mô phỏng hành vi
try:
    from io import StringIO
    # Mô phỏng ghi
    string_buffer_write = StringIO()
    json.dump(sample_data, string_buffer_write)
    print_example('json.dump(data, file)', "Ghi dữ liệu vào file object", "Thành công")
    # Mô phỏng đọc
    string_buffer_read = StringIO(string_buffer_write.getvalue())
    loaded_from_file = json.load(string_buffer_read)
    print_example('json.load(file)', "Đọc dữ liệu từ file object", loaded_from_file == sample_data)
except ImportError:
    pass

# ==============================================================================
# 4. CẤU TRÚC DỮ LIỆU HỖ TRỢ
# ==============================================================================
print_section("4. Cấu trúc dữ liệu hỗ trợ")
py_to_json_map = {
    "dict": "object",
    "list, tuple": "array",
    "str": "string",
    "int, float": "number",
    "True": "true",
    "False": "false",
    "None": "null"
}
for py_type, json_type in py_to_json_map.items():
    print_example(f"{py_type:<20}", f"→ {json_type}", "-")

# ==============================================================================
# 5. XỬ LÝ LỖI
# ==============================================================================
print_section("5. Xử lý lỗi")
invalid_json_str = '{"name": "Alice", "age":}' # JSON sai cú pháp
try:
    json.loads(invalid_json_str)
except json.JSONDecodeError as e:
    print_example('json.loads(invalid_str)', "Lỗi giải mã JSON", f"Lỗi: {e}")

# Cố gắng serialize một object không hỗ trợ
try:
    import datetime
    invalid_py_obj = {"now": datetime.datetime.now()}
    json.dumps(invalid_py_obj)
except TypeError as e:
    print_example('json.dumps(obj_with_datetime)', "Lỗi serialize object", f"Lỗi: {e}")

# ==============================================================================
# 6. TÙY CHỈNH SERIALIZER/DESERIALIZER
# ==============================================================================
print_section("6. Tùy chỉnh (Nâng cao)")
# Ví dụ: custom default function cho json.dumps
def custom_serializer(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

custom_data = {"tags": {"python", "json", "cheatsheet"}}
print_example('json.dumps(custom_data, default=custom_serializer)', "Dùng hàm serialize tùy chỉnh", json.dumps(custom_data, default=custom_serializer))

# Ví dụ: custom object_hook cho json.loads
json_with_obj = '{"name": "Alice", "scores": [10, 20, 30]}'
def object_hook(dct):
    # Có thể chuyển đổi dict thành object tùy chỉnh
    # Ở đây chỉ in ra để minh họa
    return dct

parsed_with_hook = json.loads(json_with_obj, object_hook=object_hook)
print_example('json.loads(json_str, object_hook=hook)', "Dùng hàm deserialize tùy chỉnh", parsed_with_hook)

# ==============================================================================
# 7. SO SÁNH DỮ LIỆU
# ==============================================================================
print_section("7. So sánh dữ liệu trước/sau serialize")
original = sample_data
serialized = json.dumps(original)
deserialized = json.loads(serialized)
print_example('original == deserialized', "So sánh sau serialize/deserialize", original == deserialized)

# ==============================================================================
# 8. THÔNG TIN MODULE JSON
# ==============================================================================
print_section("8. Thông tin module json")
all_json = [m for m in dir(json) if not m.startswith("_") and callable(getattr(json, m))]
print(f"Tổng cộng: {len(all_json)} hàm")
# print("\n".join(f" • {func:<20}" for func in sorted(all_json)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'JSON MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/json.html':^70}")
print("="*70)