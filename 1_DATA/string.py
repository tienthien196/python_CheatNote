# -*- coding: utf-8 -*-
"""
String Methods & Text Processing Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 2.1
Mục đích: Tài liệu tham khảo toàn diện về xử lý chuỗi trong Python
"""

import sys
import os
import re
from difflib import SequenceMatcher
from pathlib import Path


def print_section(title):
    """In tiêu đề nhóm phương thức"""
    print("\n" + "=" * 70)
    print(f"{title.upper():^70}")
    print("=" * 70)


def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")


# Dữ liệu mẫu
s = "  Xin chao, The gioi!  "
s_clean = "Xin chao, The gioi!"
num_str = "123"
float_str = "123.45"
hex_str = "ff"
filename = "file.txt"
path = "res://scenes/level.tscn"
text = "Hello\nWorld"
email = "user@example.com"
name = "Godot"


# ==============================================================================
# 1. KHỞI TẠO CHUỖI
# ==============================================================================
print_section("1. Khởi tạo chuỗi từ các kiểu dữ liệu")
print_example("str(123)",       "Số nguyên → chuỗi", str(123))
print_example("str(3.14)",      "Số thực → chuỗi", str(3.14))
print_example("str([1,2])",     "List → chuỗi", str([1, 2]))
print_example("str({'a':1})",   "Dict → chuỗi", str({"a": 1}))


# ==============================================================================
# 2. KIỂM TRA TÍNH CHẤT CHUỖI (Boolean Checks)
# ==============================================================================
print_section("2. Kiểm tra tính chất chuỗi")
print_example('"".islower()',           "Toàn chữ thường? (rỗng → False)", "".islower())
print_example('"hello".islower()',      "Toàn chữ thường?", "hello".islower())
print_example('"HELLO".isupper()',      "Toàn chữ hoa?", "HELLO".isupper())
print_example('"Hello".istitle()',      "Viết hoa đầu từ?", "Hello".istitle())
print_example('"123".isdigit()',        "Chỉ là số (0-9)?", "123".isdigit())
print_example('"abc".isalpha()',        "Chỉ là chữ cái?", "abc".isalpha())
print_example('"abc123".isalnum()',     "Chỉ chữ+số?", "abc123".isalnum())
print_example('"   ".isspace()',        "Chỉ khoảng trắng?", "   ".isspace())  # Sửa: dùng chuỗi có khoảng trắng
print_example('"½".isnumeric()',        "Là số (Unicode)?", "½".isnumeric())
print_example('"123".isdecimal()',      "Là số thập phân?", "123".isdecimal())
print_example('"café".isascii()',       "Chỉ ký tự ASCII?", "café".isascii())
print_example('filename.endswith(".txt")', "Kết thúc bằng .txt?", filename.endswith(".txt"))
print_example('path.startswith("res://")', "Bắt đầu bằng res://?", path.startswith("res://"))


# ==============================================================================
# 3. TÌM KIẾM VÀ VỊ TRÍ
# ==============================================================================
print_section("3. Tìm kiếm và vị trí")
print_example('s_clean.find("T")',      "Tìm vị trí đầu (không thấy → -1)", s_clean.find("T"))
print_example('s_clean.rfind("o")',     "Tìm từ phải (cuối cùng)", s_clean.rfind("o"))
print_example('s_clean.index("T")',     "Tìm vị trí (lỗi nếu không thấy)", s_clean.index("T"))
print_example('s_clean.rindex("o")',    "Tìm từ phải (lỗi nếu không thấy)", s_clean.rindex("o"))
print_example('s_clean.count("o")',     "Đếm số lần xuất hiện", s_clean.count("o"))


# ==============================================================================
# 4. THAY THẾ CHUỖI
# ==============================================================================
print_section("4. Thay thế chuỗi")
print_example('s_clean.replace(",", ".")', "Thay thế tất cả", s_clean.replace(",", "."))
print_example('s_clean.replace("o", "X", 1)', "Thay 1 lần", s_clean.replace("o", "X", 1))
trans_table = str.maketrans("aeio", "4310")
print_example('s_clean.translate(trans_table)', "Thay theo bảng", s_clean.translate(trans_table))
print_example('"a\\tb".expandtabs(4)',   "Mở rộng tab", "a\tb".expandtabs(4))


# ==============================================================================
# 5. TÁCH VÀ GHÉP CHUỖI
# ==============================================================================
print_section("5. Tách và ghép chuỗi")
print_example('s_clean.split(",")',         "Tách theo dấu phẩy", s_clean.split(","))
print_example('s_clean.rsplit(",", 1)',     "Tách từ phải, giới hạn 1 lần", s_clean.rsplit(",", 1))
print_example('text.splitlines()',          "Tách theo dòng", text.splitlines())
print_example('", ".join(["A","B","C"])',   "Ghép danh sách", ", ".join(["A", "B", "C"]))
print_example('s_clean.partition(",")',     "Phân 3 phần (trước, phân tách, sau)", s_clean.partition(","))
print_example('s_clean.rpartition(",")',    "Phân từ phải", s_clean.rpartition(","))


# ==============================================================================
# 6. XỬ LÝ KHOẢNG TRẮNG & CẮT TIỀN TỐ/HẬU TỐ
# ==============================================================================
print_section("6. Xử lý khoảng trắng & tiền tố/hậu tố")
print_example('s.strip()',           "Xóa khoảng trắng đầu/cuối", repr(s.strip()))
print_example('s.lstrip()',          "Xóa trái", repr(s.lstrip()))
print_example('s.rstrip()',          "Xóa phải", repr(s.rstrip()))
print_example('s_clean.removeprefix("Xin ")', "Xóa tiền tố", s_clean.removeprefix("Xin "))
print_example('s_clean.removesuffix("!")',    "Xóa hậu tố", s_clean.removesuffix("!"))


# ==============================================================================
# 7. CHUYỂN ĐỔI CHỮ HOA/THƯỜNG
# ==============================================================================
print_section("7. Chuyển đổi chữ hoa/thường")
print_example('s_clean.lower()',     "Chuyển thành thường", s_clean.lower())
print_example('s_clean.upper()',     "Chuyển thành HOA", s_clean.upper())
print_example('s_clean.capitalize()', "Viết hoa chữ đầu", s_clean.capitalize())
print_example('s_clean.title()',     "Viết hoa đầu mỗi từ", s_clean.title())
print_example('s_clean.swapcase()',  "Đổi hoa/thường", s_clean.swapcase())
print_example('"Straße".casefold()', "Chuyển không phân biệt (Unicode)", "Straße".casefold())


# ==============================================================================
# 8. CĂN CHỈNH & ĐỊNH DẠNG
# ==============================================================================
print_section("8. Căn chỉnh và định dạng")
cleaned = s_clean.strip()
print_example('cleaned.center(30, "-")', "Căn giữa", cleaned.center(30, "-"))
print_example('cleaned.ljust(30, ".")',  "Căn trái", cleaned.ljust(30, "."))
print_example('cleaned.rjust(30, ".")',  "Căn phải", cleaned.rjust(30, "."))
print_example('"42".zfill(8)',       "Đệm 0 bên trái", "42".zfill(8))


# ==============================================================================
# 9. ĐỊNH DẠNG CHUỖI
# ==============================================================================
print_section("9. Định dạng chuỗi")
print_example('f"Hello {name}"',     "f-string", f"Hello {name}")
print_example('"{} is {}".format(...)', "format() vị trí", "{} is {}".format("Python", "tuyệt"))
print_example('"{lang} {rate}".format(...)', "format() từ khóa", "{lang} {rate}".format(lang="Python", rate="5 sao"))
print_example('"%s %d" % ("Tuổi", 25)', "printf-style", "%s %d" % ("Tuổi", 25))


# ==============================================================================
# 10. MÃ HÓA VÀ CHUYỂN ĐỔI
# ==============================================================================
print_section("10. Mã hóa và chuyển đổi")
print_example('s_clean.encode("utf-8")', "Sang bytes UTF-8", s_clean.encode("utf-8"))
print_example('s_clean.encode("ascii", errors="ignore")', "Sang ASCII (bỏ lỗi)", s_clean.encode("ascii", errors="ignore"))
print_example('b"hello".decode("utf-8")', "Từ bytes về string", b"hello".decode("utf-8"))
print_example('ord("A")',             "Ký tự → mã số", ord("A"))
print_example('chr(65)',              "Mã số → ký tự", chr(65))
print_example('int("ff", 16)',        "Hex → số", int("ff", 16))


# ==============================================================================
# 11. BIỂU THỨC CHÍNH QUY (regex)
# ==============================================================================
print_section("11. Biểu thức chính quy (re)")
print_example('re.match(r"^\\w+@\\w+\\.\\w+$", email)', "Kiểm tra email", bool(re.match(r"^\w+@\w+\.\w+$", email)))
print_example('re.findall(r"\\d+", "a1b2c3")', "Tìm tất cả số", re.findall(r"\d+", "a1b2c3"))
print_example('re.sub(r"\\s+", "-", "a    b")', "Thay thế regex", re.sub(r"\s+", "-", "a    b"))
print_example('re.split(r"\\W+", "a,b.c")', "Tách bằng regex", re.split(r"\W+", "a,b.c"))


# ==============================================================================
# 12. XỬ LÝ ĐƯỜNG DẪN (os.path / pathlib)
# ==============================================================================
print_section("12. Xử lý đường dẫn")
p = Path(path)
print_example('os.path.dirname(path)',     "Thư mục cha", os.path.dirname(path))
print_example('os.path.basename(path)',    "Tên file", os.path.basename(path))
print_example('os.path.splitext("level.tscn")[0]', "Tên không mở rộng", os.path.splitext("level.tscn")[0])
print_example('os.path.splitext("level.tscn")[1]', "Phần mở rộng", os.path.splitext("level.tscn")[1])
print_example('os.path.join("folder", "file.txt")', "Nối đường dẫn", os.path.join("folder", "file.txt"))
print_example('Path(path).suffix',         "Mở rộng (pathlib)", p.suffix)
print_example('Path(path).stem',           "Tên không mở rộng (pathlib)", p.stem)


# ==============================================================================
# 13. SO SÁNH VÀ ĐỘ TƯƠNG ĐỒNG
# ==============================================================================
print_section("13. So sánh và độ tương đồng")
a, b = "Xin chao", "Xincaoo"
sim = SequenceMatcher(None, a, b).ratio()
print_example('SequenceMatcher(...).ratio()', "Độ tương đồng", round(sim, 2))
print_example('"chao" in s_clean',          "Là chuỗi con?", "chao" in s_clean)
print_example('s_clean.startswith("X")', "Bắt đầu?", s_clean.startswith("X"))
print_example('s_clean.endswith("!")',   "Kết thúc?", s_clean.endswith("!"))


# ==============================================================================
# 14. CẮT CHUỖI (SLICING)
# ==============================================================================
print_section("14. Cắt chuỗi (Slicing)")
print_example('s_clean[0:5]',     "5 ký tự đầu", s_clean[0:5])
print_example('s_clean[7:]',     "Từ vị trí 7", s_clean[7:])
print_example('s_clean[-5:]',    "5 ký tự cuối", s_clean[-5:])
print_example('s_clean[::2]',    "Lấy mỗi 2 ký tự", s_clean[::2])
print_example('s_clean[::-1]',   "Đảo ngược", s_clean[::-1])


# ==============================================================================
# 15. THÔNG TIN CHUỖI
# ==============================================================================
print_section("15. Thông tin chuỗi")
print_example('len(s_clean)',     "Độ dài chuỗi", len(s_clean))
print_example('hash(s_clean) % 10**8', "Mã hash (8 số cuối)", hash(s_clean) % 10**8)


# ==============================================================================
# 16. DANH SÁCH ĐẦY ĐỦ CÁC PHƯƠNG THỨC STR
# ==============================================================================
print_section("16. Danh sách đầy đủ str methods")
all_methods = [m for m in dir(str) if not m.startswith("__")]
print(f"Tổng cộng: {len(all_methods)} phương thức")
for method in sorted(all_methods):
    doc = getattr(str, method).__doc__
    summary = doc.split("\n")[0].split(".")[0] if doc else "No doc"
    print(f" • {method:<20} → {summary}")


# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "=" * 70)
print(f"{'CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/stdtypes.html#string-methods':^70}")
print("=" * 70)