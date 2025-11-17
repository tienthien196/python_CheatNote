# -*- coding: utf-8 -*-
"""
Module random trong Python cung cấp các hàm để sinh số ngẫu nhiên.
Dưới đây là danh sách các hàm được export từ module random, cùng mô tả cách dùng, tham số và ví dụ.
"""

import random

# Một instance duy nhất của lớp Random() được tạo để dùng chung cho toàn module
# Điều này giúp các hàm như randint(), choice(),... hoạt động như các hàm module mà không cần khởi tạo object.
# _inst = Random()

# --- CÁC HÀM ĐƯỢC EXPORT TỪ MODULE random ---

# Hàm: seed(a=None, version=2)
# Mô tả: Thiết lập hạt giống cho trình sinh số ngẫu nhiên.
#        Nếu a không được cung cấp, hạt giống sẽ dựa trên thời gian hệ thống hoặc nguồn ngẫu nhiên khác.
# Tham số:
#   a: Hạt giống (int hoặc str). Nếu không có, sẽ dùng giá trị ngẫu nhiên.
#   version: Phiên bản của thuật toán seed (2 là mặc định).
# seed = _inst.seed
print("=== seed() ===")
random.seed(42)  # Hạt giống cố định
print(random.random())  # Luôn ra 0.6394267984578837 nếu seed = 42
print()

# Hàm: random()
# Mô tả: Trả về một số float ngẫu nhiên trong đoạn [0.0, 1.0).
# Tham số: Không có.
# random = _inst.random
print("=== random() ===")
print(random.random())  # Ví dụ: 0.6394267984578837 (nếu seed=42)
print()

# Hàm: uniform(a, b)
# Mô tả: Trả về một số float ngẫu nhiên trong đoạn [a, b] hoặc [b, a] nếu b < a.
# Tham số:
#   a: Giá trị đầu của đoạn.
#   b: Giá trị cuối của đoạn.
# uniform = _inst.uniform
print("=== uniform(a, b) ===")
print(random.uniform(1.0, 10.0))  # Ví dụ: 5.74948000840809
print()

# Hàm: triangular(low, high, mode)
# Mô tả: Trả về một số float ngẫu nhiên theo phân bố tam giác giữa low và high, với điểm mode.
# Tham số:
#   low: Giá trị nhỏ nhất (mặc định 0).
#   high: Giá trị lớn nhất (mặc định 1).
#   mode: Giá trị có xác suất cao nhất (mặc định trung điểm của low và high).
# triangular = _inst.triangular
print("=== triangular(low, high, mode) ===")
print(random.triangular(1, 10, 5))  # Ví dụ: 4.78123
print()

# Hàm: randint(a, b)
# Mô tả: Trả về một số nguyên ngẫu nhiên trong đoạn [a, b] (bao gồm cả a và b).
# Tham số:
#   a: Giá trị nhỏ nhất.
#   b: Giá trị lớn nhất.
# randint = _inst.randint
print("=== randint(a, b) ===")
print(random.randint(1, 10))  # Ví dụ: 7
print()

# Hàm: choice(seq)
# Mô tả: Trả về một phần tử ngẫu nhiên từ chuỗi có thể lặp (sequence) không rỗng.
# Tham số:
#   seq: Một chuỗi (list, tuple, string, v.v.) không rỗng.
# choice = _inst.choice
print("=== choice(seq) ===")
print(random.choice(['a', 'b', 'c']))  # Ví dụ: 'b'
print(random.choice("hello"))           # Ví dụ: 'e'
print()

# Hàm: randrange(start, stop=None, step=1)
# Mô tả: Trả về một số nguyên ngẫu nhiên từ dải [start, stop) với bước nhảy step.
# Tham số:
#   start: Giá trị bắt đầu.
#   stop: Giá trị kết thúc (không bao gồm).
#   step: Bước nhảy (mặc định 1).
# randrange = _inst.randrange
print("=== randrange(start, stop, step) ===")
print(random.randrange(0, 10, 2))  # Chọn số chẵn từ 0 đến 8
print()

# Hàm: sample(population, k, *, counts=None)
# Mô tả: Trả về một list gồm k phần tử khác nhau được chọn ngẫu nhiên từ population.
# Tham số:
#   population: Một chuỗi hoặc tập hợp không lặp lại.
#   k: Số lượng phần tử cần chọn.
#   counts: Danh sách số lượng cho mỗi phần tử (Python 3.9+).
# sample = _inst.sample
print("=== sample(population, k) ===")
print(random.sample([1, 2, 3, 4, 5], 3))  # Ví dụ: [2, 5, 1]
print()

# Hàm: shuffle(x, random=None)
# Mô tả: Xáo trộn ngẫu nhiên các phần tử trong list x tại chỗ (không trả về gì).
# Tham số:
#   x: List cần xáo trộn.
#   random: Hàm sinh số ngẫu nhiên (tùy chọn).
# shuffle = _inst.shuffle
print("=== shuffle(x) ===")
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # Ví dụ: [3, 1, 5, 2, 4]
print()

# Hàm: choices(population, weights=None, *, cum_weights=None, k=1)
# Mô tả: Trả về một list gồm k phần tử được chọn ngẫu nhiên từ population, có thể lặp lại.
#        Có thể dùng weights hoặc cum_weights để phân bố xác suất.
# Tham số:
#   population: Danh sách các phần tử.
#   weights: Trọng số cho từng phần tử (tùy chọn).
#   cum_weights: Trọng số tích lũy (tùy chọn).
#   k: Số lượng phần tử cần chọn (mặc định 1).
# choices = _inst.choices
print("=== choices(population, weights, k) ===")
print(random.choices(['a', 'b', 'c'], weights=[10, 1, 1], k=5))  # Ví dụ: ['a', 'a', 'a', 'b', 'a']
print()

# --- CÁC HÀM PHÂN BỐ THỐNG KÊ ---

# Hàm: normalvariate(mu, sigma)
# Mô tả: Trả về số theo phân bố chuẩn (normal distribution) với trung bình mu và độ lệch chuẩn sigma.
# Tham số:
#   mu: Trung bình.
#   sigma: Độ lệch chuẩn.
# normalvariate = _inst.normalvariate
print("=== normalvariate(mu, sigma) ===")
print(random.normalvariate(0, 1))  # Ví dụ: -0.496714
print()

# Hàm: lognormvariate(mu, sigma)
# Mô tả: Trả về số theo phân bố log chuẩn.
# Tham số:
#   mu: Trung bình của logarit.
#   sigma: Độ lệch chuẩn của logarit.
# lognormvariate = _inst.lognormvariate
print("=== lognormvariate(mu, sigma) ===")
print(random.lognormvariate(0, 1))  # Ví dụ: 0.888
print()

# Hàm: expovariate(lambd)
# Mô tả: Trả về số theo phân bố mũ.
# Tham số:
#   lambd: Tham số lambda (1/mean).
# expovariate = _inst.expovariate
print("=== expovariate(lambd) ===")
print(random.expovariate(1.5))  # Ví dụ: 0.234
print()

# Hàm: vonmisesvariate(mu, kappa)
# Mô tả: Trả về số theo phân bố Von Mises.
# Tham số:
#   mu: Góc trung bình (radian).
#   kappa: Độ tập trung.
# vonmisesvariate = _inst.vonmisesvariate
print("=== vonmisesvariate(mu, kappa) ===")
print(random.vonmisesvariate(0, 4))  # Ví dụ: 0.345
print()

# Hàm: gammavariate(alpha, beta)
# Mô tả: Trả về số theo phân bố Gamma.
# Tham số:
#   alpha: Tham số hình dạng (shape).
#   beta: Tham số tỷ lệ (scale).
# gammavariate = _inst.gammavariate
print("=== gammavariate(alpha, beta) ===")
print(random.gammavariate(2, 3))  # Ví dụ: 6.123
print()

# Hàm: gauss(mu, sigma)
# Mô tả: Trả về số theo phân bố chuẩn, nhanh hơn normalvariate().
# Tham số:
#   mu: Trung bình.
#   sigma: Độ lệch chuẩn.
# gauss = _inst.gauss
print("=== gauss(mu, sigma) ===")
print(random.gauss(0, 1))  # Ví dụ: 0.950
print()

# Hàm: betavariate(alpha, beta)
# Mô tả: Trả về số theo phân bố Beta.
# Tham số:
#   alpha, beta: Các tham số hình dạng.
# betavariate = _inst.betavariate
print("=== betavariate(alpha, beta) ===")
print(random.betavariate(2, 3))  # Ví dụ: 0.456
print()

# Hàm: binomialvariate(n, p)
# Mô tả: Trả về số theo phân bố nhị thức.
# Tham số:
#   n: Số thử nghiệm.
#   p: Xác suất thành công.
# binomialvariate = _inst.binomialvariate
print("=== binomialvariate(n, p) ===")
print(random.binomialvariate(10, 0.5))  # Ví dụ: 6 (số mặt ngửa khi tung đồng xu 10 lần)
print()

# Hàm: paretovariate(alpha)
# Mô tả: Trả về số theo phân bố Pareto.
# Tham số:
#   alpha: Tham số hình dạng.
# paretovariate = _inst.paretovariate
print("=== paretovariate(alpha) ===")
print(random.paretovariate(1.16))  # Ví dụ: 2.345
print()

# Hàm: weibullvariate(alpha, beta)
# Mô tả: Trả về số theo phân bố Weibull.
# Tham số:
#   alpha: Tham số tỷ lệ (scale).
#   beta: Tham số hình dạng (shape).
# weibullvariate = _inst.weibullvariate
print("=== weibullvariate(alpha, beta) ===")
print(random.weibullvariate(1, 1.5))  # Ví dụ: 0.789
print()

# --- CÁC HÀM LIÊN QUAN ĐẾN TRẠNG THÁI VÀ BIT ---

# Hàm: getstate()
# Mô tả: Trả về trạng thái nội bộ của trình sinh số ngẫu nhiên.
#        Có thể dùng với setstate() để khôi phục trạng thái.
# Tham số: Không có.
# getstate = _inst.getstate
print("=== getstate() và setstate() ===")
state = random.getstate()
print(random.random())  # Ví dụ: 0.255
random.setstate(state)
print(random.random())  # Trả về cùng giá trị như trên
print()

# Hàm: getrandbits(k)
# Mô tả: Trả về một số nguyên có k bit ngẫu nhiên.
# Tham số:
#   k: Số bit (phải > 0).
# getrandbits = _inst.getrandbits
print("=== getrandbits(k) ===")
print(random.getrandbits(8))  # Ví dụ: 187 (số trong khoảng 0 đến 255)
print()

# Hàm: randbytes(n)
# Mô tả: Trả về n byte ngẫu nhiên dưới dạng bytes.
# Tham số:
#   n: Số lượng byte.
# randbytes = _inst.randbytes
print("=== randbytes(n) ===")
print(random.randbytes(5))  # Ví dụ: b'\x8f\x9e\x1a\x0c\x9b'
print()

# --- HẾT ---