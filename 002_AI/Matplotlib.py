# -*- coding: utf-8 -*-
"""
📊 ULTIMATE MATPLOTLIB CHEAT SHEET
Author: Bạn 😎 | Dựa trên Matplotlib 3.8+
Chạy toàn bộ script để xem ví dụ minh họa!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# ───────────────────────────────────────
# 0️⃣ CÀI ĐẶT STYLE (TÙY CHỌN)
# ───────────────────────────────────────
plt.style.use('seaborn-v0_8')  # hoặc 'ggplot', 'default', 'dark_background'
plt.rcParams.update({'font.size': 10})

# ───────────────────────────────────────
# 1️⃣ VẼ ĐỒ THỊ CƠ BẢN
# ───────────────────────────────────────
print("1️⃣ ĐỒ THỊ CƠ BẢN")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='sin(x)', color='tab:blue', linewidth=2)
plt.title("Đồ thị sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("plot_basic.png")  # lưu ảnh
# plt.show()  # bỏ comment nếu chạy ngoài Jupyter

# ───────────────────────────────────────
# 2️⃣ NHIỀU ĐƯỜNG TRÊN 1 HÌNH
# ───────────────────────────────────────
print("\n2️⃣ NHIỀU ĐƯỜNG")
plt.figure(figsize=(6, 4))
plt.plot(x, np.sin(x), 'b-', label='sin')
plt.plot(x, np.cos(x), 'r--', label='cos')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Sin và Cos")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 3️⃣ BIỂU ĐỒ CỘT & THANH NGANG
# ───────────────────────────────────────
print("\n3️⃣ BIỂU ĐỒ CỘT")
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]

fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(categories, values, color='skyblue', edgecolor='black')
ax.bar_label(bars)  # tự động ghi số
ax.set_title("Biểu đồ cột")
plt.tight_layout()
# plt.show()

# Thanh ngang
plt.figure(figsize=(6, 3))
plt.barh(categories, values, color='lightcoral')
plt.title("Biểu đồ thanh ngang")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 4️⃣ BIỂU ĐỒ PHÂN TÁN (Scatter)
# ───────────────────────────────────────
print("\n4️⃣ SCATTER PLOT")
np.random.seed(42)
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100)
colors = np.random.rand(100)
sizes = 1000 * np.random.rand(100)

plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(label='Màu')
plt.title("Scatter Plot với màu & kích thước")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 5️⃣ HISTOGRAM & KDE
# ───────────────────────────────────────
print("\n5️⃣ HISTOGRAM")
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='green', alpha=0.7, edgecolor='black', density=True)
# Thêm KDE (ước lượng mật độ)
from scipy.stats import gaussian_kde
kde = gaussian_kde(data)
x_kde = np.linspace(-4, 4, 100)
plt.plot(x_kde, kde(x_kde), 'r-', lw=2, label='KDE')
plt.legend()
plt.title("Histogram + KDE")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 6️⃣ SUBPLOTS (NHIỀU HÌNH TRÊN 1 CỬA SỔ)
# ───────────────────────────────────────
print("\n6️⃣ SUBPLOTS")
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title("Sin")

axs[0, 1].scatter(x_scatter[:50], y_scatter[:50])
axs[0, 1].set_title("Scatter")

axs[1, 0].bar(categories, values)
axs[1, 0].set_title("Bar")

axs[1, 1].hist(data, bins=20)
axs[1, 1].set_title("Histogram")

plt.suptitle("4 biểu đồ trong 1 hình")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 7️⃣ VẼ TỪ PANDAS (TÍCH HỢP)
# ───────────────────────────────────────
print("\n7️⃣ VẼ TỪ PANDAS")
df = pd.DataFrame({
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum()
})
df.plot(figsize=(6, 4), title="Line plot từ Pandas")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 8️⃣ BIỂU ĐỒ 3D
# ───────────────────────────────────────
print("\n8️⃣ 3D PLOT")
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')

x3 = np.linspace(-5, 5, 50)
y3 = np.linspace(-5, 5, 50)
X3, Y3 = np.meshgrid(x3, y3)
Z3 = np.sin(np.sqrt(X3**2 + Y3**2))

surf = ax.plot_surface(X3, Y3, Z3, cmap=cm.coolwarm, alpha=0.8)
ax.set_title("3D Surface")
fig.colorbar(surf)
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 9️⃣ TÙY CHỈNH NÂNG CAO: TEXT, ANNOTATE, ARROW
# ───────────────────────────────────────
print("\n9️⃣ TÙY CHỈNH NÂNG CAO")
plt.figure(figsize=(6, 4))
x_peak = np.pi / 2
y_peak = np.sin(x_peak)
plt.plot(x, np.sin(x))
plt.annotate('Cực đại',
             xy=(x_peak, y_peak),
             xytext=(x_peak + 2, y_peak + 0.5),
             arrowprops=dict(arrowstyle='->', color='red'))
plt.text(8, -0.8, "Ghi chú", fontsize=12, color='purple')
plt.title("Annotate & Text")
plt.tight_layout()
# plt.show()

# ───────────────────────────────────────
# 🔟 ANIMATION (CƠ BẢN)
# ───────────────────────────────────────
print("\n🔟 ANIMATION (xem trong Jupyter hoặc lưu .gif)")
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x_anim = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x_anim, np.sin(x_anim))
ax.set_ylim(-2, 2)

def animate(i):
    line.set_ydata(np.sin(x_anim + i / 10))
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
# ani.save("sine_wave.gif", writer='pillow')  # cần cài pillow
# plt.show()

# ───────────────────────────────────────
# 1️⃣1️⃣ LƯU ẢNH VỚI CHẤT LƯỢNG CAO
# ───────────────────────────────────────
print("\n1️⃣1️⃣ LƯU ẢNH")
# plt.savefig("figure.png", dpi=300, bbox_inches='tight')

# ───────────────────────────────────────
# ✅ KẾT THÚC
# ───────────────────────────────────────
print("\n🎉 XONG! Đây là Ultimate Matplotlib Cheat Sheet.")
print("💡 Gợi ý: Dùng trong Jupyter Notebook để xem trực quan!")