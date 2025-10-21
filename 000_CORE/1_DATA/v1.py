# ───────────────────────────────────────
# 🔤 1. Chuyển đổi chữ hoa/thường & định dạng
# ───────────────────────────────────────
print(" tiến thiện".strip().lower().capitalize())
print(" threre're perpose".title())

# capitalize(): Viết hoa chữ cái **đầu tiên**, các chữ cái còn lại → thường. Không bỏ khoảng trắng.
#replace chữ cái  thành chữ cái hoa
"hello world".capitalize()          # → "Hello world"
"  HeLLo\tWorLD! 123  \n".capitalize()  # → "  hello\tworld! 123  \n"
"Straße Café".capitalize()          # → "Straße café"
"".capitalize()                     # → ""
" hello\ntienthien".capitalize()    # -> hello\ntienthien

# lower(): Chuyển tất cả chữ cái → thường (theo Unicode)
"  HeLLo\tWorLD! 123  \n".lower()   # → "  hello\tworld! 123  \n"
"Straße Café".lower()               # → "straße café"

# upper(): Chuyển tất cả chữ cái → HOA (theo Unicode, ví dụ: 'ß' → 'SS')
"  HeLLo\tWorLD! 123  \n".upper()   # → "  HELLO\tWORLD! 123  \n"
"ß".upper()                         # → "SS"

# swapcase(): Đảo ngược: HOA ↔ thường, ký tự khác giữ nguyên
"  HeLLo\tWorLD! 123  \n".swapcase()  # → "  hEllO\twORld! 123  \n"

# title(): Viết hoa chữ cái đầu MỖI TỪ (từ = dãy chữ cái). ⚠️ Xử lý sai với dấu nháy/apostrophe.
"hello world".title()               # → "Hello World"
"they're friends".title()           # → "They'Re Friends"

# casefold(): Giống lower() nhưng mạnh hơn — dùng để SO SÁNH không phân biệt hoa thường (Unicode-aware)
"Straße Café".casefold()            # → "strasse cafe"
"STRASSE".casefold() == "straße".casefold()  # → True
print("A".casefold() == "a")

# zfill(width): Thêm '0' ở đầu để đủ độ dài. Xử lý dấu (+/-) đúng: dấu giữ nguyên ở đầu.
"42".zfill(5)                       # → "00042"
"-7".zfill(5)                       # → "-0007"
"abc".zfill(5)                      # → "00abc"  # hợp lệ nhưng ít dùng

# ───────────────────────────────────────
# 📏 2. Căn lề & điền ký tự
# ───────────────────────────────────────
# center(width, fillchar): Căn giữa, điền `fillchar` (mặc định space) ở 2 bên
"hello world".center(20, '*')       # → "***hello world*****"

# ljust(width, fillchar): Căn trái, điền bên phải
"hello world".ljust(20, '-')        # → "hello world--------"

# rjust(width, fillchar): Căn phải, điền bên trái
"hello world".rjust(20, '=')        # → "========hello world"

# expandtabs(tabsize): Thay mỗi \t bằng số space = tabsize - (vị trí hiện tại % tabsize)
"a\tb".expandtabs(4)                # → "a   b"   # 3 space
"aa\tb".expandtabs(4)               # → "aa  b"  # 2 space

# ───────────────────────────────────────
# 🔍 3. Tìm kiếm & thay thế
# ───────────────────────────────────────

# find(sub, start, end): Trả về index đầu tiên của `sub`, -1 nếu không tìm thấy (an toàn)
"hello world".find("world")         # → 6
"hello world".find("x")             # → -1

# rfind(sub, ...): Tìm từ phải sang
"hello world".rfind("l")            # → 9

# index(sub, ...): Giống find(), nhưng ném ValueError nếu không tìm thấy
"hello world".index("world")        # → 6
# "hello world".index("x")          # → ValueError

# replace(old, new, count): Thay thế `old` → `new`. Nếu count không truyền → thay tất cả.
"hello world".replace("world", "you")     # → "hello you"
"hello world".replace("l", "L", 1)        # → "heLlo world"
"aaaa".replace("aa", "b")                 # → "bb"  # không chồng lấn
"ab".replace("", "-")                     # → "-a-b-"  # edge: chèn giữa mọi ký tự

# translate(table): Thay/xóa ký tự theo bảng ánh xạ (dùng str.maketrans)
"hello world".translate(str.maketrans("", "", "aeiou"))      # → "hll wrld"  # xóa nguyên âm
"ab1c".translate(str.maketrans("abc", "xyz"))                # → "xy1z"      # thay 1-1

# ───────────────────────────────────────
# ✂️ 4. Tách & ghép chuỗi
# ───────────────────────────────────────

# split(sep, maxsplit): 
#   - Nếu sep=None (mặc định): tách theo mọi whitespace, BỎ khoảng trắng thừa
#   - Nếu sep=chuỗi: tách theo chuỗi đó, GIỮ empty parts
"  HeLLo\tWorLD! 123  \n".split()   # → ['HeLLo', 'WorLD!', '123']
"".split()                          # → []
"   ".split()                       # → []
"a,,b,c".split(",")                 # → ['a', '', 'b', 'c']
"".split(",")                       # → ['']

# rsplit(sep, maxsplit): Giống split(), nhưng khi có maxsplit → tách từ phải
"a b c d".split(maxsplit=2)         # → ['a', 'b', 'c d']
"a b c d".rsplit(maxsplit=2)        # → ['a b', 'c', 'd']

# splitlines(keepends): Tách theo dấu ngắt dòng (\n, \r\n...). keepends=False (mặc định) → không giữ \n
"line1\nline2\r\nline3".splitlines()  # → ['line1', 'line2', 'line3']
"abc\n".splitlines()                # → ['abc']  # không có dòng rỗng cuối

# partition(sep): Tách thành (trước, sep, sau) — chỉ tách 1 lần. Nếu không tìm thấy → (s, "", "")
"hello world".partition(" ")        # → ('hello', ' ', 'world')
"notfound".partition("x")           # → ('notfound', '', '')

# rpartition(sep): Giống partition(), nhưng tách từ phải
"hello world".rpartition("l")       # → ('hello wor', 'l', 'd')

# join(iterable): Ghép các chuỗi trong iterable bằng chuỗi gọi method. ⚠️ Tất cả phần tử phải là str.
"-".join(["a", "b", "c"])           # → "a-b-c"
"".join(["a", "b"])                 # → "ab"
# "-".join([1, 2])                  # → TypeError: các phần tử phải là chuỗi

# ───────────────────────────────────────
# 🧹 5. Loại bỏ ký tự thừa
# ───────────────────────────────────────

# strip(chars): Xóa các ký tự trong `chars` ở ĐẦU VÀ CUỐI. 
#   - Nếu chars=None (mặc định): xóa mọi whitespace (' ', \t, \n...)
#   - ⚠️ `chars` là TẬP KÝ TỰ, không phải chuỗi con!
"  HeLLo\tWorLD! 123  \n".strip()   # → "HeLLo\tWorLD! 123"
"www.example.com".strip("cmowz.")   # → "example"  # xóa từng ký tự 'c','m','o','w','z','.' ở 2 đầu
"abcba".strip("ab")                 # → "c"
"".strip()                          # → ""

# lstrip(chars): Chỉ xóa ở đầu (left)
"  HeLLo\tWorLD! 123  \n".lstrip()  # → "HeLLo\tWorLD! 123  \n"

# rstrip(chars): Chỉ xóa ở cuối (right)
"  HeLLo\tWorLD! 123  \n".rstrip()  # → "  HeLLo\tWorLD! 123"

# ───────────────────────────────────────
# 💡 Bonus: Các method hay dùng khác (không trong list gốc nhưng thiết yếu)
# ───────────────────────────────────────

# casefold() dùng để so sánh không phân biệt hoa thường (ưu tiên hơn lower())
"HELLO".casefold() == "hello".casefold()  # → True

# startswith(prefix) / endswith(suffix): Kiểm tra đầu/cuối chuỗi
"hello world".startswith("he")      # → True
"hello world".endswith("ld")        # → True

# f-string: Định dạng chuỗi hiện đại (không phải method, nhưng nên biết)
f"Hello {'Godot'}"                  # → "Hello Godot"