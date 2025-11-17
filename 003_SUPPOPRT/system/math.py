# -*- coding: utf-8 -*-
"""
Math Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module math trong Python
"""

import math
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
# 1. HẰNG SỐ TOÁN HỌC
# ==============================================================================
print_section("1. Hằng số toán học")
print_example("math.pi", "Số Pi (π)", math.pi)
print_example("math.e", "Số Euler (e)", math.e)
print_example("math.tau", "Số Tau (τ = 2π)", math.tau)
print_example("math.inf", "Vô cực dương", math.inf)
print_example("math.nan", "Not a Number", math.nan)

# ==============================================================================
# 2. HÀM SỐ HỌC CƠ BẢN
# ==============================================================================
print_section("2. Hàm số học cơ bản")
print_example("math.sqrt(16)", "Căn bậc hai", math.sqrt(16))
print_example("math.pow(2, 3)", "Lũy thừa (2³)", math.pow(2, 3))
print_example("math.exp(1)", "e^x", math.exp(1))
print_example("math.log(10)", "log(x) cơ số e", math.log(10))
print_example("math.log(100, 10)", "log(x, base)", math.log(100, 10))
print_example("math.log10(1000)", "log cơ số 10", math.log10(1000))
print_example("math.log2(256)", "log cơ số 2", math.log2(256))

# ==============================================================================
# 3. HÀM LÀM TRÒN & LÀM TRƠN
# ==============================================================================
print_section("3. Làm tròn & kiểm tra số nguyên")
print_example("math.ceil(4.2)", "Làm tròn lên", math.ceil(4.2))
print_example("math.floor(4.8)", "Làm tròn xuống", math.floor(4.8))
print_example("math.trunc(4.9)", "Cắt phần thập phân", math.trunc(4.9))
print_example("round(4.5)", "Làm tròn chuẩn (built-in)", round(4.5))  # không dùng math.round
print_example("math.isclose(0.1+0.2, 0.3)", "So sánh số thực gần bằng", math.isclose(0.1 + 0.2, 0.3))

# ==============================================================================
# 4. HÀM LƯỢNG GIÁC
# ==============================================================================
print_section("4. Lượng giác (góc tính bằng radian)")
print_example("math.sin(math.pi/2)", "sin(π/2)", math.sin(math.pi / 2))
print_example("math.cos(0)", "cos(0)", math.cos(0))
print_example("math.tan(math.pi/4)", "tan(π/4)", math.tan(math.pi / 4))
print_example("math.asin(1)", "arcsin(1)", math.asin(1))
print_example("math.acos(0)", "arccos(0)", math.acos(0))
print_example("math.atan(1)", "arctan(1)", math.atan(1))
print_example("math.atan2(1, 1)", "arctan2(y, x)", math.atan2(1, 1))
print_example("math.hypot(3, 4)", "√(x² + y²)", math.hypot(3, 4))

# Chuyển đổi đơn vị
print_example("math.degrees(math.pi)", "Radian → Độ", math.degrees(math.pi))
print_example("math.radians(180)", "Độ → Radian", math.radians(180))

# ==============================================================================
# 5. HÀM GIAI THỪA & TỔ HỢP
# ==============================================================================
print_section("5. Giai thừa & tổ hợp")
print_example("math.factorial(5)", "5!", math.factorial(5))
print_example("math.comb(5, 2)", "Tổ hợp C(5,2)", math.comb(5, 2))
print_example("math.perm(5, 2)", "Chỉnh hợp P(5,2)", math.perm(5, 2))

# ==============================================================================
# 6. HÀM LÀM VIỆC VỚI SỐ NGUYÊN & CHẴN LẺ
# ==============================================================================
print_section("6. Số nguyên & kiểm tra đặc tính")
print_example("math.gcd(48, 18)", "ƯCLN", math.gcd(48, 18))
print_example("math.lcm(12, 15)", "BCNN (Python ≥3.9)", math.lcm(12, 15))
print_example("math.isfinite(3.14)", "Số hữu hạn?", math.isfinite(3.14))
print_example("math.isinf(math.inf)", "Là vô cực?", math.isinf(math.inf))
print_example("math.isnan(math.nan)", "Là NaN?", math.isnan(math.nan))
print_example("math.fmod(10, 3)", "Phần dư dấu theo tử (fmod)", math.fmod(10, 3))
print_example("math.modf(3.14)", "Tách phần nguyên & thập phân", math.modf(3.14))

# ==============================================================================
# 7. HÀM LÀM VIỆC VỚI DẤU & GIÁ TRỊ TUYỆT ĐỐI
# ==============================================================================
print_section("7. Dấu & giá trị tuyệt đối")
print_example("math.fabs(-5.5)", "Giá trị tuyệt đối (float)", math.fabs(-5.5))
print_example("math.copysign(3.5, -2)", "Sao chép dấu", math.copysign(3.5, -2))
print_example("math.remainder(10, 3)", "Phần dư IEEE 754", math.remainder(10, 3))

# ==============================================================================
# 8. HÀM LÀM VIỆC VỚI SỐ THỰC & ĐỘ CHÍNH XÁC
# ==============================================================================
print_section("8. Độ chính xác & biểu diễn")
print_example("math.nextafter(1.0, 2.0)", "Số thực tiếp theo", math.nextafter(1.0, 2.0))
print_example("math.ulp(1.0)", "Đơn vị ở vị trí cuối cùng", math.ulp(1.0))

# ==============================================================================
# 9. HÀM ĐẶC BIỆT (Hàm Gamma, Erf...)
# ==============================================================================
print_section("9. Hàm đặc biệt")
print_example("math.gamma(5)", "Hàm Gamma (Γ(n) = (n-1)!)", math.gamma(5))
print_example("math.lgamma(5)", "log(|Γ(x)|)", math.lgamma(5))
print_example("math.erf(1)", "Hàm sai số (error function)", math.erf(1))
print_example("math.erfc(1)", "Hàm sai số bổ sung", math.erfc(1))

# ==============================================================================
# 10. THÔNG TIN MODULE MATH
# ==============================================================================
print_section("10. Thông tin module math")
all_math = [m for m in dir(math) if not m.startswith("_")]
print(f"Tổng cộng: {len(all_math)} hàm & hằng số")
# print("\n".join(f" • {item:<20}" for item in sorted(all_math)))  # In đầy đủ nếu cần

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'MATH MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/math.html':^70}")
print("="*70)