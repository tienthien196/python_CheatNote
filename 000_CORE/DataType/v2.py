# ───────────────────────────────────────
# 🔢 1. Số nguyên (Integers)
# ───────────────────────────────────────

# %d: Số nguyên thập phân có dấu (signed decimal)
"%d" % 42                         # → "42"
"%d" % -17                        # → "-17"

# %i: Tương tự %d (giữ lại vì tương thích C, không khác biệt trong Python)
"%i" % 100                        # → "100"

# %o: Số nguyên bát phân (octal) — có tiền tố '0o' trong Python, nhưng %o KHÔNG in tiền tố
"%o" % 10                         # → "12"  (vì 10 = 1*8 + 2)
"%o" % 255                        # → "377"

# %u: ⚠️ LỖI THỜI — từng dùng cho unsigned int trong C, nhưng Python không phân biệt → giống %d
"%u" % -5                         # → "-5"  # KHÔNG DÙNG — tránh trong code hiện đại

# %x: Thập lục phân thường (hex, không tiền tố)
"%x" % 255                        # → "ff"
"%x" % 10                         # → "a"

# %X: Thập lục phân HOA
"%X" % 255                        # → "FF"
"%X" % 10                         # → "A"

# ───────────────────────────────────────
# 📏 2. Số thực (Floating Point)
# ───────────────────────────────────────

# %f: Định dạng thập phân cố định (mặc định 6 chữ số sau dấu)
"%f" % 3.14159                    # → "3.141590"
"%.2f" % 3.14159                  # → "3.14"
"%8.2f" % 3.14                    # → "    3.14"  (căn phải, độ rộng 8)

# %F: Giống %f, nhưng in 'INF', 'NAN' thay vì 'inf', 'nan' (hiếm dùng)
"%F" % float('inf')               # → "INF"

# %e: Ký hiệu khoa học (lowercase)
"%e" % 123                        # → "1.230000e+02"
"%.2e" % 0.00123                  # → "1.23e-03"

# %E: Ký hiệu khoa học (UPPERCASE)
"%E" % 123                        # → "1.230000E+02"

# %g: Tự động chọn giữa %f và %e — bỏ số 0 thừa, gọn gàng
"%g" % 3.14159                    # → "3.14159"
"%g" % 0.000123                   # → "0.000123"
"%g" % 123000000                  # → "1.23e+08"  # tự chuyển sang exponential

# %G: Giống %g nhưng dùng uppercase cho exponential
"%G" % 123000000                  # → "1.23E+08"

# ───────────────────────────────────────
# 🔤 3. Chuỗi & Ký tự
# ───────────────────────────────────────

# %c: Ký tự đơn — nhận int (mã Unicode) hoặc chuỗi độ dài 1
"%c" % 65                         # → "A"
"%c" % "Z"                        # → "Z"
# "%c" % "AB"                     # → TypeError (chuỗi phải có độ dài 1)

# %s: Chuỗi — dùng str() để chuyển đổi → dễ đọc, dùng cho hiển thị
"%s" % "Hello"                    # → "Hello"
"%s" % [1, 2, 3]                  # → "[1, 2, 3]"
"%s" % None                       # → "None"

# %r: Chuỗi "đại diện" — dùng repr() → có dấu nháy, dùng để debug
"%r" % "Hello"                    # → "'Hello'"
"%r" % "He said: \"Hi!\""         # → "'He said: \"Hi!\"'"
"%r" % [1, 2, 3]                  # → "[1, 2, 3]"  (vì list.__repr__ không có nháy ngoài)

# ───────────────────────────────────────
# 🛑 4. Ký tự đặc biệt & escape
# ───────────────────────────────────────

# %%: In ra ký tự '%' (escape)
"Tỷ lệ: %d%%" % 95                # → "Tỷ lệ: 95%"
"Progress: %d%% complete" % 100   # → "Progress: 100% complete"

# ───────────────────────────────────────
# 💡 Lưu ý quan trọng
# ───────────────────────────────────────

# Với nhiều giá trị → dùng tuple
"Name: %s, Age: %d" % ("Alice", 30)        # → "Name: Alice, Age: 30"

# Thứ tự phải khớp — không có named placeholder như .format() hay f-string
# → Dễ lỗi nếu đổi thứ tự

# ⚠️ Old-style formatting (%)
#   - VẪN HOẠT ĐỘNG trong Python 3.x
#   - Nhưng KHÔNG ĐƯỢC KHUYẾN KHÍCH — dùng f-string hoặc .format() thay thế
#   - Lý do: ít linh hoạt, dễ lỗi, không hỗ trợ named argument, không type-safe

# Ví dụ so sánh hiện đại:
#   Cũ: "Hello %s" % name
#   Mới: f"Hello {name}"  ← ưu tiên dùng cách này!