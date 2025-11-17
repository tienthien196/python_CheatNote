# -*- coding: utf-8 -*-
"""
Random Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module random trong Python
"""

import random
import sys

def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(code, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{code:<35} | {desc:<28} | Kết quả: {result}")

# ==============================================================================
# 1. CẤU TRÚC CƠ BẢN & HÀM NGẪU NHIÊN ĐƠN GIẢN
# ==============================================================================
print_section("1. Hàm ngẫu nhiên cơ bản")
print("--- Sinh số ngẫu nhiên ---")

print_example("random.random()", "Số float [0.0, 1.0)", random.random())
print_example("random.uniform(1.5, 10.5)", "Số float trong khoảng [a, b]", random.uniform(1.5, 10.5))
print_example("random.randint(1, 10)", "Số nguyên trong khoảng [a, b]", random.randint(1, 10))
print_example("random.randrange(0, 10, 2)", "Số nguyên trong range(start, stop, step)", random.randrange(0, 10, 2))

# ==============================================================================
# 2. CHỌN NGẪU NHIÊN
# ==============================================================================
print_section("2. Chọn ngẫu nhiên từ chuỗi/danh sách")
sample_list = [1, 2, 3, 4, 5, "apple", "banana", "cherry"]
sample_string = "hello"

print_example("random.choice([1,2,3])", "Chọn 1 phần tử ngẫu nhiên", random.choice(sample_list))
print_example("random.choices([1,2,3], k=2)", "Chọn k phần tử (có thể trùng)", random.choices(sample_list, k=2))
print_example("random.sample([1,2,3], 2)", "Chọn k phần tử (không trùng)", random.sample(sample_list, 2))

# ==============================================================================
# 3. TRỘN DỮ LIỆU
# ==============================================================================
print_section("3. Trộn dữ liệu")
list_to_shuffle = [1, 2, 3, 4, 5]
print(f"Trước khi shuffle: {list_to_shuffle}")
random.shuffle(list_to_shuffle)
print(f"Sau khi shuffle: {list_to_shuffle}")
print_example("random.shuffle(list)", "Trộn ngẫu nhiên list (in-place)", "Thành công")

# ==============================================================================
# 4. HẠT GIỐNG NGẪU NHIÊN (SEED)
# ==============================================================================
print_section("4. Hạt giống ngẫu nhiên (Seed)")
print("--- Cài đặt seed để lặp lại kết quả ---")
random.seed(42)
first_run = random.random()
print_example("random.seed(42); random.random()", "Lần 1 với seed 42", first_run)

random.seed(42)
second_run = random.random()
print_example("random.seed(42); random.random()", "Lần 2 với seed 42", second_run)
print(f"Kết quả giống nhau: {first_run == second_run}")

# ==============================================================================
# 5. PHÂN PHỐI NGẪU NHIÊN NÂNG CAO
# ==============================================================================
print_section("5. Phân phối ngẫu nhiên nâng cao")
print_example("random.gauss(0, 1)", "Phân phối Gauss (Normal)", random.gauss(0, 1))
print_example("random.expovariate(1.5)", "Phân phối Exponential", random.expovariate(1.5))
print_example("random.betavariate(2, 5)", "Phân phối Beta", random.betavariate(2, 5))
print_example("random.gammavariate(2, 3)", "Phân phối Gamma", random.gammavariate(2, 3))
print_example("random.triangular(1, 10, 5)", "Phân phối Tam giác (low, high, mode)", random.triangular(1, 10, 5))

# ==============================================================================
# 6. BIẾN THỂ CỦA RANDOM
# ==============================================================================
print_section("6. Biến thể của Random (instance riêng)")
rng = random.Random(123) # Tạo instance riêng với seed
print_example("rng = random.Random(123)", "Tạo instance Random riêng", "Thành công")
print_example("rng.random()", "Ngẫu nhiên từ instance riêng", rng.random())

# ==============================================================================
# 7. CÁC HẰNG SỐ HỮU ÍCH
# ==============================================================================
print_section("7. Một số hằng số & thuộc tính")
# print_example("random.bpf", "Số bit cho số nguyên được sử dụng", random.bpf)
# print_example("random.REALVARS", "Danh sách các phân phối số thực", random.REALVARS)
# print_example("random.VERSION", "Phiên bản module random", random.VERSION)

# ==============================================================================
# 8. XỬ LÝ LỖI
# ==============================================================================
print_section("8. Xử lý lỗi")
try:
    random.sample([1, 2, 3], 5) # Lấy nhiều hơn số phần tử
except ValueError as e:
    print_example("random.sample([1,2,3], 5)", "Lỗi lấy mẫu nhiều hơn số phần tử", f"Lỗi: {e}")

try:
    random.randrange(10, 5) # start > stop
except ValueError as e:
    print_example("random.randrange(10, 5)", "Lỗi range start > stop", f"Lỗi: {e}")

# ==============================================================================
# 9. ỨNG DỤNG THỰC TẾ (Ví dụ)
# ==============================================================================
print_section("9. Ứng dụng thực tế (Ví dụ)")
# Tạo mật khẩu ngẫu nhiên
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password = "".join(random.choices(chars, k=12))
print_example("Tạo mật khẩu 12 ký tự", "random.choices(chars, k=12)", password)

# Chọn ngẫu nhiên người thắng cuộc
contestants = ["Alice", "Bob", "Charlie", "David"]
winner = random.choice(contestants)
print_example("Chọn người thắng cuộc", "random.choice(contestants)", winner)

# Trộn dữ liệu huấn luyện
training_data = [f"data_{i}" for i in range(10)]
random.shuffle(training_data)
print_example("Trộn dữ liệu huấn luyện", "random.shuffle(data)", training_data[:3])

# ==============================================================================
# 10. THÔNG TIN MODULE RANDOM
# ==============================================================================
print_section("10. Thông tin module random")
all_random = [m for m in dir(random) if not m.startswith("_")]
print(f"Tổng cộng: {len(all_random)} đối tượng (hàm, lớp, hằng số)")
# print("\n".join(f" • {item:<20}" for item in sorted(all_random))) # In danh sách nếu cần

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'RANDOM MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/random.html':^70}")
print("="*70)