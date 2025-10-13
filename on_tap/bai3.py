"""
docs.py - Tài liệu tóm tắt Bài 5: Kiểm tra đơn vị (Unit Testing)
Khóa học: Nhập môn lập trình với Python (CS50)

Tác giả: David J. Malan (Harvard University)
Nguồn: CS50 - https://cs50.harvard.edu/python/

Mục tiêu: Giới thiệu cách viết và tổ chức unit test trong Python
          sử dụng `assert` và thư viện `pytest`.
"""

# ===================================================================
# 1. Vấn đề khi kiểm thử thủ công
# ===================================================================
"""
- Trước đây, người học thường dùng `print()` để kiểm tra đầu ra.
- Cách này không mở rộng được, dễ bỏ sót "trường hợp biên" (edge cases).
- Trong thực tế, lập trình viên nên tự viết mã kiểm thử cho mã của mình.
"""

# ===================================================================
# 2. Sử dụng `assert` để kiểm thử đơn giản
# ===================================================================
"""
Cú pháp:
    assert biểu_thức, "Thông báo lỗi (tùy chọn)"

Ví dụ:
    assert square(2) == 4

Nếu biểu thức sai → ném `AssertionError`.
"""

def square(n):
    """Trả về bình phương của n."""
    return n * n

# Ví dụ kiểm thử bằng assert (không khuyến khích dùng trong production test):
# assert square(2) == 4
# assert square(-3) == 9

# ===================================================================
# 3. Giới thiệu `pytest` – framework kiểm thử mạnh mẽ
# ===================================================================
"""
- Cài đặt: `pip install pytest`
- Viết các hàm bắt đầu bằng `test_`
- Chạy test: `pytest tên_file.py` hoặc `pytest thư_mục/`

Ưu điểm:
- Tự động phát hiện và chạy tất cả hàm test.
- Hiển thị rõ lỗi khi test thất bại.
- Tiếp tục chạy các test khác ngay cả khi một test thất bại.
"""

# ===================================================================
# 4. Ví dụ: test_calculator.py
# ===================================================================
"""
# calculator.py
def square(n):
    return n * n

# test_calculator.py
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    import pytest
    with pytest.raises(TypeError):
        square("cat")
"""

# ===================================================================
# 5. Lưu ý quan trọng: Hàm phải `return`, không `print`
# ===================================================================
"""
Ví dụ sai:
    def hello(to="world"):
        print("hello,", to)   # ← Không thể kiểm thử bằng assert!

Ví dụ đúng:
    def hello(to="world"):
        return f"hello, {to}"  # ← Có thể kiểm thử!

Test:
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"
"""

# ===================================================================
# 6. Tổ chức test vào thư mục
# ===================================================================
"""
Cấu trúc đề xuất:
    project/
    ├── hello.py
    └── test/
        ├── __init__.py   # (có thể để trống)
        └── test_hello.py

Lệnh chạy toàn bộ thư mục test:
    pytest test/
"""

# ===================================================================
# 7. Tóm tắt
# ===================================================================
"""
- Unit testing giúp đảm bảo mã hoạt động đúng trong mọi trường hợp.
- Dùng `assert` cho test đơn giản.
- Dùng `pytest` cho test chuyên nghiệp, có tổ chức.
- Luôn tách biệt logic (return) và giao diện (print/input).
- Tổ chức test theo hàm và thư mục để dễ bảo trì.
"""

# ===================================================================
# Gợi ý học tập
# ===================================================================
"""
- Viết test trước khi viết hàm (Test-Driven Development).
- Kiểm thử cả trường hợp hợp lệ, không hợp lệ và biên.
- Đảm bảo mỗi hàm test chỉ kiểm tra **một khía cạnh**.
"""
