# -*- coding: utf-8 -*-
"""
Phân loại hoa Iris bằng Machine Learning (không cần công thức tường minh!)
"""

# 1. Nhập các thư viện cần thiết
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Tải dữ liệu hoa Iris
iris = datasets.load_iris()
X = iris.data      # Các đặc trưng: sepal length, sepal width, petal length, petal width
y = iris.target    # Nhãn: 0 = setosa, 1 = versicolor, 2 = virginica

# 3. Chia dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Tạo và huấn luyện mô hình (Random Forest - không cần công thức!)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Dự đoán trên tập kiểm tra
y_pred = model.predict(X_test)

# 6. Đánh giá kết quả
accuracy = accuracy_score(y_test, y_pred)
print("🎯 Độ chính xác của mô hình:", f"{accuracy:.2%}")
print("\n📋 Báo cáo phân loại chi tiết:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# 7. Ví dụ dự đoán một bông hoa mới
new_flower = [[5.1, 3.5, 1.4, 0.2]]  # sepal length, sepal width, petal length, petal width
predicted_class = model.predict(new_flower)
predicted_name = iris.target_names[predicted_class[0]]
print(f"\n🔍 Dự đoán cho bông hoa mới {new_flower[0]}: **{predicted_name}**")