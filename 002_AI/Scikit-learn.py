# -*- coding: utf-8 -*-
"""
🤖 ULTIMATE SCIKIT-LEARN CHEAT SHEET
Author: Bạn 😎 | Dựa trên scikit-learn 1.4+
Chạy toàn bộ script để xem ví dụ minh họa!
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing, model_selection, metrics
from sklearn import linear_model, svm, tree, ensemble, cluster, decomposition
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

# ───────────────────────────────────────
# 1️⃣ TẢI DỮ LIỆU MẪU
# ───────────────────────────────────────
print("1️⃣ TẢI DỮ LIỆU")
# Bộ dữ liệu phân loại (Iris)
X_cls, y_cls = datasets.load_iris(return_X_y=True)
# Bộ dữ liệu hồi quy (Boston bị gỡ → dùng California Housing)
X_reg, y_reg = datasets.fetch_california_housing(return_X_y=True)
# Dữ liệu không giám sát (digits để clustering)
X_unsup = datasets.load_digits().data

print("Phân loại: X shape =", X_cls.shape)
print("Hồi quy: X shape =", X_reg.shape)

# ───────────────────────────────────────
# 2️⃣ CHIA DỮ LIỆU (Train/Test)
# ───────────────────────────────────────
print("\n2️⃣ CHIA DỮ LIỆU")
X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X_cls, y_cls, test_size=0.2, random_state=42, stratify=y_cls
)
print("Train size:", X_train.shape[0], "| Test size:", X_test.shape[0])

# ───────────────────────────────────────
# 3️⃣ TIỀN XỬ LÝ DỮ LIỆU
# ───────────────────────────────────────
print("\n3️⃣ TIỀN XỬ LÝ")
# Chuẩn hóa (StandardScaler)
scaler = preprocessing.StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Mã hóa nhãn (nếu cần)
label_enc = preprocessing.LabelEncoder()
# y_encoded = label_enc.fit_transform(y_categorical)

# One-hot encoding (dành cho dữ liệu phân loại trong DataFrame)
# df = pd.DataFrame(X_cls, columns=['sepal_l', 'sepal_w', 'petal_l', 'petal_w'])
# preprocessor = ColumnTransformer(
#     transformers=[('num', preprocessing.StandardScaler(), numerical_cols)],
#     remainder='passthrough'
# )

# ───────────────────────────────────────
# 4️⃣ HUẤN LUYỆN MÔ HÌNH PHÂN LOẠI
# ───────────────────────────────────────
print("\n4️⃣ PHÂN LOẠI")
models = {
    "LogisticRegression": linear_model.LogisticRegression(max_iter=200),
    "SVM": svm.SVC(),
    "RandomForest": ensemble.RandomForestClassifier(random_state=42)
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    acc = model.score(X_test_scaled, y_test)
    print(f"{name}: Accuracy = {acc:.3f}")

# ───────────────────────────────────────
# 5️⃣ HUẤN LUYỆN MÔ HÌNH HỒI QUY
# ───────────────────────────────────────
print("\n5️⃣ HỒI QUY")
Xr_train, Xr_test, yr_train, yr_test = model_selection.train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)
scaler_r = preprocessing.StandardScaler()
Xr_train_scaled = scaler_r.fit_transform(Xr_train)
Xr_test_scaled = scaler_r.transform(Xr_test)

reg_models = {
    "Linear": linear_model.LinearRegression(),
    "Ridge": linear_model.Ridge(alpha=1.0),
    "RandomForest": ensemble.RandomForestRegressor(random_state=42)
}

for name, model in reg_models.items():
    model.fit(Xr_train_scaled, yr_train)
    r2 = model.score(Xr_test_scaled, yr_test)
    print(f"{name}: R² = {r2:.3f}")

# ───────────────────────────────────────
# 6️⃣ ĐÁNH GIÁ MÔ HÌNH
# ───────────────────────────────────────
print("\n6️⃣ ĐÁNH GIÁ")
best_model = models["RandomForest"]
y_pred = best_model.predict(X_test_scaled)

# Phân loại
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Classification Report:\n", metrics.classification_report(y_test, y_pred))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, y_pred))

# Hồi quy (dùng mô hình hồi quy)
y_pred_reg = reg_models["Ridge"].predict(Xr_test_scaled)
print("MAE:", metrics.mean_absolute_error(yr_test, y_pred_reg))
print("MSE:", metrics.mean_squared_error(yr_test, y_pred_reg))

# ───────────────────────────────────────
# 7️⃣ CROSS-VALIDATION
# ───────────────────────────────────────
print("\n7️⃣ CROSS-VALIDATION")
from sklearn.model_selection import cross_val_score
scores = cross_val_score(models["SVM"], X_train_scaled, y_train, cv=5)
print("CV Accuracy:", scores.mean(), "±", scores.std())

# ───────────────────────────────────────
# 8️⃣ TINH CHỈNH SIÊU THAM SỐ (Hyperparameter Tuning)
# ───────────────────────────────────────
print("\n8️⃣ TINH CHỈNH SIÊU THAM SỐ")
from sklearn.model_selection import GridSearchCV

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}
grid = GridSearchCV(svm.SVC(), param_grid, cv=3, scoring='accuracy')
grid.fit(X_train_scaled, y_train)
print("Best params:", grid.best_params_)
print("Best CV score:", grid.best_score_)

# ───────────────────────────────────────
# 9️⃣ HỌC KHÔNG GIÁM SÁT: CLUSTERING
# ───────────────────────────────────────
print("\n9️⃣ CLUSTERING")
kmeans = cluster.KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_unsup[:100])  # chỉ 100 mẫu để nhanh
print("Số cụm:", len(np.unique(clusters)))

# Đánh giá (nếu có nhãn thật)
# from sklearn.metrics import adjusted_rand_score
# ari = adjusted_rand_score(true_labels, clusters)

# ───────────────────────────────────────
# 🔟 GIẢM CHIỀU DỮ LIỆU (PCA)
# ───────────────────────────────────────
print("\n🔟 PCA")
pca = decomposition.PCA(n_components=2)
X_pca = pca.fit_transform(X_unsup[:100])
print("Giải thích phương sai:", pca.explained_variance_ratio_.sum())

# Vẽ (nếu cần)
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='tab10')
# plt.title("PCA + KMeans")
# plt.show()

# ───────────────────────────────────────
# 1️⃣1️⃣ PIPELINE TỰ ĐỘNG
# ───────────────────────────────────────
print("\n1️⃣1️⃣ PIPELINE")
pipe = Pipeline([
    ('scaler', preprocessing.StandardScaler()),
    ('clf', ensemble.RandomForestClassifier(random_state=42))
])
pipe.fit(X_train, y_train)
print("Pipeline accuracy:", pipe.score(X_test, y_test))

# ───────────────────────────────────────
# 1️⃣2️⃣ LƯU & TẢI MÔ HÌNH
# ───────────────────────────────────────
print("\n1️⃣2️⃣ LƯU/TẢI MÔ HÌNH")
joblib.dump(pipe, "model.pkl")
loaded_model = joblib.load("model.pkl")
print("Mô hình tải lại hoạt động:", loaded_model.score(X_test, y_test))

# ───────────────────────────────────────
# ✅ KẾT THÚC
# ───────────────────────────────────────
print("\n🎉 XONG! Đây là Ultimate Scikit-learn Cheat Sheet.")
print("💡 Gợi ý: Dùng trong Jupyter Notebook để kết hợp với matplotlib!")