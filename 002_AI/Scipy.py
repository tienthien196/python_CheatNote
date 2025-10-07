# -*- coding: utf-8 -*-
"""
🔬 ULTIMATE SCIPY CHEAT SHEET
Author: Bạn 😎 | Dựa trên SciPy 1.12+
Chạy toàn bộ script để xem ví dụ minh họa!
"""

import numpy as np
import scipy as sp
from scipy import (
    optimize, integrate, linalg, stats, signal,
    interpolate, fft, ndimage, sparse, special
)
import matplotlib.pyplot as plt  # optional, để vẽ (bỏ qua nếu không cần)

# ───────────────────────────────────────
# 1️⃣ TỐI ƯU HÓA (scipy.optimize)
# ───────────────────────────────────────
print("1️⃣ TỐI ƯU HÓA")
def f(x):
    return x**2 + 4 * np.sin(x)

res = optimize.minimize(f, x0=0)
print("Min tại x =", res.x[0], "với f(x) =", res.fun)

# Root finding
root = optimize.root(lambda x: x**3 - 2*x + 1, x0=0)
print("Nghiệm của x³ - 2x + 1 = 0:", root.x[0])

# Linear programming
c = [-1, -1]  # maximize x + y → minimize -x -y
A_ub = [[1, 2], [3, 1]]
b_ub = [4, 6]
bounds = [(0, None), (0, None)]
lp_res = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
print("LP solution (x, y):", lp_res.x)

# ───────────────────────────────────────
# 2️⃣ TÍCH PHÂN SỐ (scipy.integrate)
# ───────────────────────────────────────
print("\n2️⃣ TÍCH PHÂN")
# Tích phân đơn
result, err = integrate.quad(lambda x: np.exp(-x**2), 0, np.inf)
print("∫₀^∞ e^(-x²) dx =", result, "±", err)

# Tích phân kép
def integrand(y, x):
    return x * y
dbl, _ = integrate.dblquad(integrand, 0, 1, lambda x: 0, lambda x: 1)
print("∫₀¹∫₀¹ xy dy dx =", dbl)

# Giải ODE
def ode(t, y):
    return -2 * y

sol = integrate.solve_ivp(ode, [0, 5], [1], t_eval=np.linspace(0, 5, 10))
print("ODE solution tại t=5:", sol.y[0][-1])

# ───────────────────────────────────────
# 3️⃣ ĐẠI SỐ TUYẾN TÍNH (scipy.linalg)
# ───────────────────────────────────────
print("\n3️⃣ ĐẠI SỐ TUYẾN TÍNH")
A = np.array([[3, 2], [1, 4]], dtype=float)
b = np.array([1, 2])

x = linalg.solve(A, b)
print("Giải Ax = b:", x)

# Phân tích ma trận
lu, piv = linalg.lu_factor(A)
print("LU factorization hoàn tất")

eigvals, eigvecs = linalg.eig(A)
print("Trị riêng:", eigvals)

# Ma trận thưa (sparse) → dùng scipy.sparse.linalg
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
A_sparse = csc_matrix([[3, 2], [1, 4]])
x_sparse = spsolve(A_sparse, b)
print("Giải hệ thưa:", x_sparse)

# ───────────────────────────────────────
# 4️⃣ THỐNG KÊ (scipy.stats)
# ───────────────────────────────────────
print("\n4️⃣ THỐNG KÊ")
# Phân phối chuẩn
norm_dist = stats.norm(loc=0, scale=1)
print("PDF tại x=0:", norm_dist.pdf(0))
print("CDF tại x=0:", norm_dist.cdf(0))
print("Mẫu ngẫu nhiên:", norm_dist.rvs(size=3, random_state=42))

# Kiểm định giả thuyết
sample = np.random.normal(0, 1, 100)
t_stat, p_val = stats.ttest_1samp(sample, 0)
print("T-test p-value:", p_val)

# Tương quan
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)
r, p = stats.pearsonr(x, y)
print("Hệ số tương quan Pearson:", r)

# ───────────────────────────────────────
# 5️⃣ NỘI SUY (scipy.interpolate)
# ───────────────────────────────────────
print("\n5️⃣ NỘI SUY")
x = np.linspace(0, 10, 10)
y = np.sin(x)
f_interp = interpolate.interp1d(x, y, kind='cubic')
print("Nội suy tại x=2.5:", f_interp(2.5))

# Nội suy 2D
x = np.linspace(0, 5, 6)
y = np.linspace(0, 5, 6)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
f2d = interpolate.RectBivariateSpline(x, y, Z)
print("Nội suy 2D tại (2.5, 3.5):", f2d(2.5, 3.5)[0, 0])

# ───────────────────────────────────────
# 6️⃣ XỬ LÝ TÍN HIỆU (scipy.signal)
# ───────────────────────────────────────
print("\n6️⃣ XỬ LÝ TÍN HIỆU")
# Thiết kế bộ lọc
b, a = signal.butter(4, 0.2, 'low')
print("Bộ lọc Butterworth (hệ số):", b[:3], "...")

# Chập (convolution)
impulse = np.zeros(10)
impulse[0] = 1
response = signal.lfilter(b, a, impulse)
print("Đáp ứng xung (3 mẫu đầu):", response[:3])

# FFT (dùng scipy.fft thay vì numpy.fft để đồng bộ)
from scipy.fft import fft, fftfreq
t = np.linspace(0, 1, 1000)
sig = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
yf = fft(sig)
xf = fftfreq(len(sig), t[1] - t[0])
print("Tần số phát hiện (2 đỉnh lớn nhất):", xf[np.argsort(np.abs(yf))[-3:-1]])

# ───────────────────────────────────────
# 7️⃣ XỬ LÝ ẢNH (scipy.ndimage)
# ───────────────────────────────────────
print("\n7️⃣ XỬ LÝ ẢNH")
img = np.zeros((20, 20))
img[5:15, 5:15] = 1  # hình vuông trắng
img_noisy = img + 0.2 * np.random.randn(*img.shape)

# Làm mờ
blurred = ndimage.gaussian_filter(img_noisy, sigma=1)
print("Làm mờ hoàn tất")

# Phát hiện biên
sobel = ndimage.sobel(img)
print("Phát hiện biên (Sobel) – max:", sobel.max())

# Nhãn thành phần liên thông
from scipy.ndimage import label
labeled, num_features = label(img.astype(int))
print("Số vùng liên thông:", num_features)

# ───────────────────────────────────────
# 8️⃣ MA TRẬN THƯA (scipy.sparse)
# ───────────────────────────────────────
print("\n8️⃣ MA TRẬN THƯA")
row = [0, 1, 2, 0]
col = [0, 1, 2, 2]
data = [1, 2, 3, 4]
sparse_mat = sparse.coo_matrix((data, (row, col)), shape=(3, 3))
print("Ma trận thưa (dense):\n", sparse_mat.toarray())

# Chuyển định dạng
csr = sparse_mat.tocsr()
print("Định dạng CSR – hàng 0:", csr[0].toarray())

# ───────────────────────────────────────
# 9️⃣ HÀM ĐẶC BIỆT (scipy.special)
# ───────────────────────────────────────
print("\n9️⃣ HÀM ĐẶC BIỆT")
print("Gamma(5) =", special.gamma(5))          # = 4! = 24
print("Beta(2, 3) =", special.beta(2, 3))
print("Erf(1) =", special.erf(1))              # hàm sai số
print("Bessel J0(1) =", special.j0(1))

# ───────────────────────────────────────
# 🔟 BIẾN ĐỔI FOURIER (scipy.fft)
# ───────────────────────────────────────
print("\n🔟 FFT (scipy.fft)")
# Đã demo ở phần signal, nhưng đây là module riêng
from scipy.fft import rfft, rfftfreq
y = np.sin(2*np.pi*5*np.linspace(0, 1, 1000))
yf = rfft(y)
xf = rfftfreq(len(y), 1/1000)
peak_freq = xf[np.argmax(np.abs(yf))]
print("Tần số phát hiện (real FFT):", peak_freq)

# ───────────────────────────────────────
# ✅ KẾT THÚC
# ───────────────────────────────────────
print("\n🎉 XONG! Đây là Ultimate SciPy Cheat Sheet.")
print("💡 Gợi ý: Dùng trong Jupyter Notebook để kết hợp với matplotlib!")