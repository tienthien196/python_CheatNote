# -*- coding: utf-8 -*-
"""
🐼 ULTIMATE PANDAS CHEAT SHEET
Author: Bạn 😎 | Dựa trên Pandas 2.x
Chạy toàn bộ script để xem ví dụ minh họa!
"""

import pandas as pd
import numpy as np

# ───────────────────────────────────────
# 1️⃣ TẠO DataFrame & Series
# ───────────────────────────────────────
print("1️⃣ TẠO DỮ LIỆU")
# Từ dict
df = pd.DataFrame({
    'Tên': ['An', 'Bình', 'Chi', 'Dũng'],
    'Tuổi': [25, 30, 22, 28],
    'Lương': [500, 700, 450, 600],
    'Thành phố': ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Hà Nội']
})
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print("DataFrame:\n", df)
print("\nSeries:", s)

# Từ mảng NumPy
arr = np.random.randn(4, 3)
df2 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print("\nTừ NumPy:\n", df2)

# Dữ liệu thời gian
dates = pd.date_range('2025-01-01', periods=5)
ts = pd.Series(np.random.randn(5), index=dates)
print("\nTime Series:\n", ts)

# ───────────────────────────────────────
# 2️⃣ THUỘC TÍNH CƠ BẢN
# ───────────────────────────────────────
print("\n2️⃣ THUỘC TÍNH")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index)
print("Dtypes:\n", df.dtypes)
print("Info:")
df.info()

# ───────────────────────────────────────
# 3️⃣ XEM DỮ LIỆU (Viewing)
# ───────────────────────────────────────
print("\n3️⃣ XEM DỮ LIỆU")
print("head():\n", df.head(2))
print("tail():\n", df.tail(2))
print("sample():\n", df.sample(2))
print("describe():\n", df.describe())  # chỉ số thống kê
print("value_counts (Thành phố):\n", df['Thành phố'].value_counts())

# ───────────────────────────────────────
# 4️⃣ TRUY CẬP DỮ LIỆU
# ───────────────────────────────────────
print("\n4️⃣ TRUY CẬP")
print("Cột 'Tuổi':", df['Tuổi'].values)
print("Nhiều cột:", df[['Tên', 'Lương']])
print("Hàng theo vị trí (iloc):", df.iloc[0])  # hàng đầu tiên
print("Hàng theo label (loc):", df.loc[0, 'Tên'])
print("Điều kiện:", df[df['Tuổi'] > 25])

# ───────────────────────────────────────
# 5️⃣ LÀM SẠCH DỮ LIỆU
# ───────────────────────────────────────
print("\n5️⃣ LÀM SẠCH")
# Thêm dữ liệu thiếu
df_na = df.copy()
df_na.loc[1, 'Lương'] = np.nan
print("Có NaN:\n", df_na)

print("isna():\n", df_na.isna())
print("dropna():\n", df_na.dropna())
print("fillna():\n", df_na.fillna(df_na['Lương'].mean()))

# Loại bỏ trùng lặp
df_dup = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("Sau khi drop_duplicates:\n", df_dup.drop_duplicates())

# ───────────────────────────────────────
# 6️⃣ THAY ĐỔI CẤU TRÚC
# ───────────────────────────────────────
print("\n6️⃣ THAY ĐỔI CẤU TRÚC")
# Thêm cột
df['Thu nhập cao'] = df['Lương'] > 550
print("Thêm cột:\n", df[['Lương', 'Thu nhập cao']])

# Xoá cột
df_temp = df.drop(columns=['Thu nhập cao'])
print("Sau khi drop cột:", df_temp.columns.tolist())

# Đổi tên cột
df_renamed = df.rename(columns={'Tuổi': 'Age', 'Lương': 'Salary'})
print("Đổi tên:", df_renamed.columns.tolist())

# Sắp xếp
print("Sắp xếp theo Lương:\n", df.sort_values('Lương', ascending=False))

# ───────────────────────────────────────
# 7️⃣ GOM NHÓM & TỔNG HỢP (GroupBy)
# ───────────────────────────────────────
print("\n7️⃣ GROUPBY")
grouped = df.groupby('Thành phố')
print("Trung bình theo thành phố:\n", grouped['Lương'].mean())
print("Tổng hợp:\n", grouped.agg({'Tuổi': 'mean', 'Lương': ['min', 'max']}))

# ───────────────────────────────────────
# 8️⃣ KẾT HỢP DỮ LIỆU (Merge/Join/Concat)
# ───────────────────────────────────────
print("\n8️⃣ KẾT HỢP DỮ LIỆU")
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

print("Merge (inner):\n", pd.merge(df1, df2, on='key', how='inner'))
print("Concat dọc:\n", pd.concat([df1, df2], ignore_index=True))

# ───────────────────────────────────────
# 9️⃣ XỬ LÝ CHUỖI & THỜI GIAN
# ───────────────────────────────────────
print("\n9️⃣ XỬ LÝ CHUỖI & DATETIME")
df_str = pd.DataFrame({'email': ['user1@gmail.com', 'user2@yahoo.com']})
print("Tách domain:", df_str['email'].str.split('@').str[1])

# Thời gian
df_time = pd.DataFrame({'date': ['2025-01-01', '2025-02-15']})
df_time['date'] = pd.to_datetime(df_time['date'])
df_time['month'] = df_time['date'].dt.month
print("Trích tháng:", df_time[['date', 'month']])

# ───────────────────────────────────────
# 🔟 PIVOT & MELT (reshape)
# ───────────────────────────────────────
print("\n🔟 PIVOT & MELT")
sales = pd.DataFrame({
    'product': ['A', 'A', 'B', 'B'],
    'quarter': ['Q1', 'Q2', 'Q1', 'Q2'],
    'sales': [100, 150, 200, 250]
})
pivot = sales.pivot(index='product', columns='quarter', values='sales')
print("Pivot:\n", pivot)

melted = pd.melt(pivot.reset_index(), id_vars='product', var_name='quarter', value_name='sales')
print("Melted:\n", melted.head())

# ───────────────────────────────────────
# 1️⃣1️⃣ NHẬP/XUẤT DỮ LIỆU
# ───────────────────────────────────────
print("\n1️⃣1️⃣ I/O")
# Lưu & tải
df.to_csv('temp.csv', index=False)
df_loaded = pd.read_csv('temp.csv')
print("Tải từ CSV:\n", df_loaded.head())

# Excel (nếu cài openpyxl/xlsxwriter)
# df.to_excel('temp.xlsx', index=False)

# JSON
df.to_json('temp.json', orient='records', lines=True)
df_json = pd.read_json('temp.json', lines=True)
print("Từ JSON:\n", df_json.head())

# ───────────────────────────────────────
# 1️⃣2️⃣ ÁP DỤNG HÀM (Apply, Map, Vectorization)
# ───────────────────────────────────────
print("\n1️⃣2️⃣ ÁP DỤNG HÀM")
df['Tuổi nhóm'] = df['Tuổi'].apply(lambda x: 'Trẻ' if x < 27 else 'Trưởng thành')
print("Dùng apply:", df[['Tuổi', 'Tuổi nhóm']])

# Vectorized (nhanh hơn)
df['Lương gấp đôi'] = df['Lương'] * 2
print("Vectorized:", df['Lương gấp đôi'].head())

# ───────────────────────────────────────
# 1️⃣3️⃣ XỬ LÝ DỮ LIỆU THỜI GIAN NÂNG CAO
# ───────────────────────────────────────
print("\n1️⃣3️⃣ TIME SERIES")
ts = pd.Series(np.random.randn(100), index=pd.date_range('2025-01-01', periods=100))
print("Resample theo tuần:\n", ts.resample('W').mean().head())

# Rolling window
print("Rolling mean (window=5):\n", ts.rolling(window=5).mean().tail())

# ───────────────────────────────────────
# ✅ KẾT THÚC
# ───────────────────────────────────────
print("\n🎉 XONG! Đây là Ultimate Pandas Cheat Sheet.")
print("💡 Gợi ý: Dùng trong Jupyter Notebook để xem kết quả đẹp hơn!")