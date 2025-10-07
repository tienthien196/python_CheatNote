# -*- coding: utf-8 -*-
"""
🔥 ULTIMATE NUMPY CHEAT SHEET
Author: Bạn 😎 | Dựa trên NumPy 2.x
Chạy toàn bộ script để xem ví dụ minh họa!
"""

import numpy as np

# ───────────────────────────────────────
# 1️⃣ KHỞI TẠO MẢNG
# ───────────────────────────────────────
print("1️⃣ KHỞI TẠO MẢNG")
a = np.array([1, 2, 3])                     # từ list
b = np.zeros((2, 3))                        # toàn 0
c = np.ones((2, 2))                         # toàn 1
d = np.full((2, 3), 7)                      # điền giá trị
e = np.eye(3)                               # ma trận đơn vị
f = np.arange(0, 10, 2)                     # [0 2 4 6 8]
g = np.linspace(0, 1, 5)                    # khoảng đều: [0. 0.25 0.5 0.75 1.]
h = np.random.default_rng(42).random((2,2)) # random (reproducible)
i = np.empty((2, 2))                        # chưa khởi tạo
j = np.array([[1, 2], [3, 4]], dtype=np.float32)

print("arange:", f)
print("linspace:", g)
print("random:\n", h)

# ───────────────────────────────────────
# 2️⃣ THUỘC TÍNH & KIỂU DỮ LIỆU
# ───────────────────────────────────────
print("\n2️⃣ THUỘC TÍNH & DTYPE")
print("Shape:", a.shape)
print("Size:", a.size)
print("Ndims:", a.ndim)
print("Dtype:", a.dtype)
print("Itemsize (bytes):", a.itemsize)

# Kiểu dữ liệu chuẩn
print("int64:", np.int64)
print("float32:", np.float32)
print("complex128:", np.complex128)

# ❌ Tránh: np.int, np.float → đã bị DEPRECATED từ NumPy 1.20+

# ───────────────────────────────────────
# 3️⃣ RESHAPE, TRANSPOSE, FLATTEN
# ───────────────────────────────────────
print("\n3️⃣ RESHAPE & CHUYỂN VỊ")
arr = np.arange(12).reshape(3, 4)
print("Original:\n", arr)
print("Reshape (4,3):\n", arr.reshape(4, 3))
print("Transpose:\n", arr.T)
print("Flatten (ravel):", arr.ravel())      # view (nhanh)
print("Flatten (flatten):", arr.flatten())  # copy

# ───────────────────────────────────────
# 4️⃣ INDEXING & SLICING
# ───────────────────────────────────────
print("\n4️⃣ INDEXING & SLICING")
mat = np.arange(1, 10).reshape(3, 3)
print("Ma trận:\n", mat)
print("mat[1, 2] =", mat[1, 2])             # 6
print("Hàng 1:", mat[1, :])
print("Cột 2:", mat[:, 2])
print("Con ma trận:\n", mat[0:2, 1:3])

# Boolean indexing
print("Giá trị >5:", mat[mat > 5])

# Fancy indexing
print("Chọn hàng [0,2]:\n", mat[[0, 2]])

# ───────────────────────────────────────
# 5️⃣ TOÁN HỌC CƠ BẢN & VECTOR HÓA
# ───────────────────────────────────────
print("\n5️⃣ TOÁN HỌC & VECTOR HÓA")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x + y =", x + y)
print("x * y =", x * y)                     # nhân từng phần tử
print("x @ y =", x @ y)                     # tích vô hướng
print("np.sum(x) =", np.sum(x))
print("np.mean(x) =", np.mean(x))
print("np.std(x) =", np.std(x))

# Trên trục
print("Tổng theo cột:", np.sum(mat, axis=0))
print("Max theo hàng:", np.max(mat, axis=1))

# ───────────────────────────────────────
# 6️⃣ HÀM TOÁN HỌC NÂNG CAO
# ───────────────────────────────────────
print("\n6️⃣ HÀM TOÁN HỌC")
print("sqrt(x) =", np.sqrt(x))
print("exp(x) =", np.exp(x))
print("log(x) =", np.log(x))
print("sin(x) =", np.sin(x))
print("abs([-1,2]) =", np.abs([-1, 2]))

# ───────────────────────────────────────
# 7️⃣ ĐẠI SỐ TUYẾN TÍNH (linalg)
# ───────────────────────────────────────
print("\n7️⃣ ĐẠI SỐ TUYẾN TÍNH")
A = np.array([[1, 2], [3, 4]], dtype=float)
b = np.array([5, 6])
print("Định thức:", np.linalg.det(A))
print("Nghịch đảo:\n", np.linalg.inv(A))
print("Giải hệ Ax=b:", np.linalg.solve(A, b))
print("Trị riêng:", np.linalg.eigvals(A))
print("Phân tích SVD:", [s.shape for s in np.linalg.svd(A)])

# ───────────────────────────────────────
# 8️⃣ BIẾN ĐỔI FOURIER (fft)
# ───────────────────────────────────────
print("\n8️⃣ FFT")
t = np.linspace(0, 1, 100)
signal = np.sin(2*np.pi*5*t)
fft_vals = np.fft.fft(signal)
print("FFT shape:", fft_vals.shape)
print("Tần số cơ bản:", np.argmax(np.abs(fft_vals)))

# ───────────────────────────────────────
# 9️⃣ SINH SỐ NGẪU NHIÊN (random)
# ───────────────────────────────────────
print("\n9️⃣ RANDOM (modern API)")
rng = np.random.default_rng(seed=42)
print("Uniform:", rng.random(3))
print("Normal:", rng.normal(size=3))
print("Integers:", rng.integers(0, 10, size=5))
print("Choice:", rng.choice([10, 20, 30], size=2))
print("Permutation:", rng.permutation([1, 2, 3, 4]))

# ───────────────────────────────────────
# 🔟 XỬ LÝ DỮ LIỆU & THỐNG KÊ
# ───────────────────────────────────────
print("\n🔟 XỬ LÝ DỮ LIỆU")
data = np.array([1, np.nan, 3, 4, np.inf])
print("isfinite:", np.isfinite(data))
print("nansum (bỏ NaN):", np.nansum(data))
print("median:", np.median([1, 2, 3, 4, 5]))

# Unique
vals, counts = np.unique([1, 2, 2, 3, 3, 3], return_counts=True)
print("Unique:", vals, "| Counts:", counts)

# Where
arr = np.array([1, -1, 2, -2])
print("np.where(arr > 0, arr, 0):", np.where(arr > 0, arr, 0))

# ───────────────────────────────────────
# 1️⃣1️⃣ GHÉP & TÁCH MẢNG
# ───────────────────────────────────────
print("\n1️⃣1️⃣ GHÉP & TÁCH")
a1 = np.array([[1], [2]])
a2 = np.array([[3], [4]])
print("vstack:\n", np.vstack([a1, a2]))
print("hstack:", np.hstack([a1, a2]).flatten())
print("concatenate axis=1:", np.concatenate([a1, a2], axis=1))

# Tách
split_me = np.arange(8).reshape(2, 4)
print("hsplit into 2:\n", np.hsplit(split_me, 2))

# ───────────────────────────────────────
# 1️⃣2️⃣ NHẬP/XUẤT DỮ LIỆU
# ───────────────────────────────────────
print("\n1️⃣2️⃣ I/O")
np.save("temp.npy", arr)
loaded = np.load("temp.npy")
print("Tải từ .npy:", loaded)

# CSV
np.savetxt("temp.csv", mat, delimiter=",", fmt="%d")
csv_loaded = np.loadtxt("temp.csv", delimiter=",", dtype=int)
print("Tải từ CSV:\n", csv_loaded)

# ───────────────────────────────────────
# 1️⃣3️⃣ BROADCASTING (quy tắc mở rộng)
# ───────────────────────────────────────
print("\n1️⃣3️⃣ BROADCASTING")
A = np.array([[1, 2, 3]])      # shape (1,3)
B = np.array([[1], [2]])       # shape (2,1)
C = A + B                      # shape (2,3)
print("Broadcasting kết quả:\n", C)

# ───────────────────────────────────────
# 1️⃣4️⃣ SO SÁNH & LOGIC
# ───────────────────────────────────────
print("\n1️⃣4️⃣ SO SÁNH")
x = np.array([1, 2, 3])
y = np.array([1, 2, 4])
print("x == y:", x == y)
print("np.array_equal:", np.array_equal(x, y))
print("allclose (sai số):", np.allclose(x, y, atol=1))

# ───────────────────────────────────────
# 1️⃣5️⃣ CÁC HÀM TIỆN ÍCH KHÁC
# ───────────────────────────────────────
print("\n1️⃣5️⃣ TIỆN ÍCH")
print("meshgrid:", np.meshgrid([1,2], [3,4]))
print("diag:", np.diag([1,2,3]))
print("clip (giới hạn):", np.clip([1, 5, 10], 2, 8))
print("searchsorted:", np.searchsorted([1,3,5,7], 4))  # vị trí chèn

# ───────────────────────────────────────
# ✅ KẾT THÚC
# ───────────────────────────────────────
print("\n🎉 XONG! Đây là Ultimate NumPy Cheat Sheet.")
print("💡 Gợi ý: Dùng trong Jupyter Notebook để xem kết quả đẹp hơn!")