import math
import random
import csv
from typing import List, Tuple

# ==============================
# 1. Tạo dataset mẫu (giá nhà dựa trên diện tích & số phòng)
# ==============================
def generate_sample_data(n: int = 100) -> List[List[float]]:
    """
    Tạo dữ liệu giả: [area (m2), bedrooms, price (triệu VND)]
    price = 20 * area + 50 * bedrooms + noise
    """
    data = []
    random.seed(42)
    for _ in range(n):
        area = random.uniform(30, 150)
        bedrooms = random.randint(1, 5)
        noise = random.uniform(-30, 30)
        price = 20 * area + 50 * bedrooms + noise
        data.append([area, bedrooms, price])
    return data

# ==============================
# 2. Linear Regression từ đầu
# ==============================
class LinearRegressionFromScratch:
    def __init__(self, learning_rate: float = 0.001, epochs: int = 1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0

    def fit(self, X: List[List[float]], y: List[float]):
        n_samples = len(X)
        n_features = len(X[0])
        # Khởi tạo weights = 0
        self.weights = [0.0 for _ in range(n_features)]
        self.bias = 0.0

        # Gradient Descent
        for _ in range(self.epochs):
            # Dự đoán
            y_pred = self.predict(X)
            # Tính đạo hàm
            dw = [0.0 for _ in range(n_features)]
            db = 0.0
            for i in range(n_samples):
                error = y_pred[i] - y[i]
                db += error
                for j in range(n_features):
                    dw[j] += error * X[i][j]
            # Cập nhật
            for j in range(n_features):
                self.weights[j] -= (self.lr * dw[j]) / n_samples
            self.bias -= (self.lr * db) / n_samples

    def predict(self, X: List[List[float]]) -> List[float]:
        y_pred = []
        for x in X:
            pred = self.bias
            for j in range(len(x)):
                pred += self.weights[j] * x[j]
            y_pred.append(pred)
        return y_pred

# ==============================
# 3. Đánh giá mô hình
# ==============================
def rmse(y_true: List[float], y_pred: List[float]) -> float:
    return math.sqrt(sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true))

def r2_score(y_true: List[float], y_pred: List[float]) -> float:
    mean_y = sum(y_true) / len(y_true)
    ss_res = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))
    ss_tot = sum((yt - mean_y) ** 2 for yt in y_true)
    return 1 - (ss_res / ss_tot)

# ==============================
# 4. Chia dữ liệu train/test
# ==============================
def train_test_split(X: List[List[float]], y: List[float], test_size: float = 0.2, seed: int = 42):
    random.seed(seed)
    indices = list(range(len(X)))
    random.shuffle(indices)
    n_test = int(len(X) * test_size)
    test_idx = set(indices[:n_test])
    X_train, X_test, y_train, y_test = [], [], [], []
    for i in range(len(X)):
        if i in test_idx:
            X_test.append(X[i])
            y_test.append(y[i])
        else:
            X_train.append(X[i])
            y_train.append(y[i])
    return X_train, X_test, y_train, y_test
# Thêm hàm chuẩn hóa Min-Max
def min_max_normalize(X: List[List[float]]) -> Tuple[List[List[float]], List[float], List[float]]:
    n_features = len(X[0])
    mins = []
    maxs = []
    for j in range(n_features):
        col = [row[j] for row in X]
        min_val = min(col)
        max_val = max(col)
        mins.append(min_val)
        maxs.append(max_val)
    
    X_norm = []
    for row in X:
        norm_row = []
        for j in range(n_features):
            val = row[j]
            if maxs[j] == mins[j]:  # tránh chia cho 0
                norm_val = 0.0
            else:
                norm_val = (val - mins[j]) / (maxs[j] - mins[j])
            norm_row.append(norm_val)
        X_norm.append(norm_row)
    return X_norm, mins, maxs

# Hàm chuẩn hóa ngược (nếu cần dự đoán trên scale gốc)
def denormalize_y(y_norm: List[float], y_min: float, y_max: float) -> List[float]:
    return [y * (y_max - y_min) + y_min for y in y_norm]


# ==============================
# 5. MAIN
# ==============================
def main():
    print("🚀 Dự đoán giá nhà - Linear Regression từ đầu (không dùng thư viện thứ 3)")
    
    # Tạo dữ liệu
    data = generate_sample_data(n=200)
    X = [[row[0], row[1]] for row in data]  # area, bedrooms
    y = [row[2] for row in data]            # price

    # Chuẩn hóa X
    X_norm, x_mins, x_maxs = min_max_normalize(X)
    
    # Chuẩn hóa y luôn (giúp hội tụ nhanh hơn)
    y_min, y_max = min(y), max(y)
    y_norm = [(val - y_min) / (y_max - y_min) for val in y]

    # Chia train/test TRÊN DỮ LIỆU ĐÃ CHUẨN HÓA
    X_train, X_test, y_train, y_test = train_test_split(X_norm, y_norm, test_size=0.2)

    # Huấn luyện với dữ liệu chuẩn hóa
    model = LinearRegressionFromScratch(learning_rate=0.01, epochs=2000)  # learning_rate có thể tăng nhẹ
    model.fit(X_train, y_train)

    # Dự đoán trên dữ liệu chuẩn hóa
    y_pred_train_norm = model.predict(X_train)
    y_pred_test_norm = model.predict(X_test)

    # Chuẩn hóa ngược về giá trị thật
    y_train_real = denormalize_y(y_train, y_min, y_max)
    y_test_real = denormalize_y(y_test, y_min, y_max)
    y_pred_train_real = denormalize_y(y_pred_train_norm, y_min, y_max)
    y_pred_test_real = denormalize_y(y_pred_test_norm, y_min, y_max)

    # Đánh giá trên giá trị thật
    train_rmse = rmse(y_train_real, y_pred_train_real)
    test_rmse = rmse(y_test_real, y_pred_test_real)
    test_r2 = r2_score(y_test_real, y_pred_test_real)

    print(f"\n📈 Kết quả Linear Regression:")
    print(f"   Train RMSE: {train_rmse:.2f}")
    print(f"   Test RMSE : {test_rmse:.2f}")
    print(f"   Test R²   : {test_r2:.4f}")

    # 💡 Dự đoán ví dụ (cần chuẩn hóa input trước!)
    example = [80, 3]
    # Chuẩn hóa input
    example_norm = [
        (example[0] - x_mins[0]) / (x_maxs[0] - x_mins[0]),
        (example[1] - x_mins[1]) / (x_maxs[1] - x_mins[1])
    ]
    pred_norm = model.predict([example_norm])[0]
    pred_real = pred_norm * (y_max - y_min) + y_min
    print(f"\n💡 Ví dụ: Nhà {example[0]}m2, {example[1]} phòng → Dự đoán giá: {pred_real:.1f} triệu VND")

if __name__ == "__main__":
    main()