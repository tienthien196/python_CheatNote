#---Binary---nhị phân ----
n = 0b0101
y = 0B0101

#---Octal ----bát phân ----
e = 0o23
f = 0O12

# ---hexadecimal--thập lục phân
g = 0xAF
h = 0X12EF

x = 255

# print(x)           # 255 (thập phân)
# print(bin(x))      # 0b11111111
# print(oct(x))      # 0o377
# print(hex(x))      # 0xff


#---Decimal ----hệ cơ số 10 

# lưu ý  type annotation(chú thích kiểu ) ko hề ảnh hưởng đén runtime -> muon bắt lỗi dùng mypy
i: int = 34.6798 # out float -> phải ép về int

# Floating-point arithmetic limitations
# IEEE 754 representation error
# Binary floating-point inaccuracy
# Decimal fraction representation problem
i2 = 0.5 + 0.3 # 
# print((1.2+0.3)== 1.5)
# dùng under scop cho biến ko dùng trong loop 
# dùng để tách số >> hiển thị đẹp >> ko ảnh hưởng value
l = 1_00_0000
m = 0b01_10

# lưu ý  :numeric literals , các e, E đều là float >> exponent(cơ số mũ)
b = 1E5 # out  1*10^5
d = 2e3 # out 2*10^3
c = 2.5E-3 # 2.5*10^-3
#--- complex----
v: complex = 3+4j 
# Số phức không so sánh được



# print(l)
# print(c)
# print(i) 
# print(type(i))
# print(type(b))

# print(help(input))



### NGÀY 2
#----Gán ----- >> value tương ứng
x1 = 6
o1 = x1 =5 #  thay đổi 1 ảnh hưởng 2
o1 += 5
o1 -= 5
o1 *= 5
o1 /= 5
o1 %= 5
o1 //=5
o1 **=5
# print(x1)

#---toán tử so sánh --- >> True / False
1 < 6 < 100 # pythonic
5 == 5
5 != 3
5 > 3
5 < 3
5 >= 3
5 <= 3
# print(b1)
# print(5| 5)
# print(5 & 5)

# ---toán tử logic  ---- >> value 
a1 = [] or "" # -> []
b1 = "hi:" or [1,2] or "hello"     # → hi:
c1 = "" or [] or [1]      # → [1] (vì "" và [] đều falsy)
# return true đầu tiên  or flase cuối cùng nếu ko có true nào

c2 = [1,2] and "hello" # >hello
d1 = None and [] # []
# print(bool([1,2] or "hello"))
# input_name  = input("can")
# name = input_name or "Anonymous"
# return true cuối or flase đầu tiên

c2 is bool # is là check 2 biến có cùng trỏ 1 ô nhớ ko ? Trừ x is None
c2 in [] # in check thành viên có trong iterable 
isinstance(x, bool) # check xem biến có thuộc class hay kh ?

# --- bitwise --- >> bit của số nguyên
# [1,2] & [3] >> lỗi bitwise không dùng cho list >> chỉ dùng cho int và bool
# 5 = 101 , 3 = 011, 5 & 3 >> 001 >> out -> 1
# 5 | 3 >> 111 > out -> 7
# NOT bit(đảo bit) ~5 >> ~n = -(n+1)>> out -> -6 
# ~-6 >> out -> 5

5 << 1  # 5 * 2^1 = 10 >>[x *  2ⁿ]
5 << 2  # 5 * 4 = 20 
# 5 = 101 5 << 1 = 1010 → 10

10 >> 1  # 10 // 2 = 5 >> [x / 2ⁿ]
10 >> 2  # 10 // 4 = 2
# print(10 >> 1)  # → 5
# print(-10 >> 1) # → -5 (Python giữ dấu)

#XOR = not and  Exclusive OR
#giao hoán xor a ^ b == b ^ a  , (a ^ b) ^ c == a ^ (b ^ c) , a ^ a == 0, a ^ 0 == a
# Khả nghịch: if c = a ^ b -> a = c ^ b , b = c ^ a


# if x & 1:      # kiểm tra x có lẻ không → đúng
# if x and 1:    # luôn True nếu x ≠ 0 → KHÔNG phải kiểm tra bit!


# READ = 4   # 100
# WRITE = 2  # 010
# EXEC = 1   # 001

# permission = READ | WRITE  # 110 → có quyền đọc và ghi

# if permission & READ:
#     print("Có quyền đọc")

# ---hoán đổi xor ko cần trung gian--
# a = 5
# b = 9
# a = a ^ b  # a = 5 ^ 9
# b = a ^ b  # b = (5 ^ 9) ^ 9 = 5
# a = a ^ b  # a = (5 ^ 9) ^ 5 = 9

# print(a, b)  # → 9 5

# nums = [4, 1, 2, 1, 2]

# result = 0
# for x in nums:
#     result ^= x

# print(result)  # → 4

# message = "Hello"
# key = 42

# # Mã hóa: XOR từng ký tự với key
# encoded = [ord(c) ^ key for c in message]
# print("Encoded:", encoded)

# # Giải mã: XOR lại với key
# decoded = ''.join(chr(b ^ key) for b in encoded)
# print("Decoded:", decoded)  # → "Hello"

# def same_sign(a, b):
#     return (a ^ b) >= 0

# print(same_sign(5, 3))   # True
# print(same_sign(-5, 3))  # False


# 🧠 Mẹo nhớ nhanh (không cần học thuộc) THỨ TỰ ƯU TIÊN PHÉP TOÁN
# Dấu ngoặc () luôn được tính đầu tiên → cứ nghi ngờ, thêm ngoặc!
# Số học (**, *, /, +, -) → như toán phổ thông.
# Bitwise (<<, >>, &, ^, |) → nằm giữa số học và so sánh.
# So sánh (==, !=, <, in, is) → cao hơn not/and/or.
# Logic (not → and → or) → ưu tiên thấp nhất (trừ gán).

# --- bẫy --->> CHÚ Ý DÁU NGOẶC KHI DÙNG TOÁN TỬ  
True == True and False # (True == True) and False 
5 & 3 == 1 # 5 & (3 == 1) Sai >> phải sữa (5 & 3) == 1  # → True
2 ** 3 ** 2 # (2 ** 3) ** 2 Sai  >> 2 ** (3 ** 2) = 512 Đúng
1 < 2 < 3 # so sánh chuỗi  >> (1 < 2) and (2 < 3)
not x == y # khác với not (x == y)

# Bẫy tham số FUNCTION (Mutable default argument)
# list += [1] được, nhưng tuple += (1,) tạo object mới
# Nguyên nhân: closure 'bắt' tham chiếu đến i, không phải giá trị tại thời điểm
# Hiểu sai về "pass by object reference"

#--- bẫy 
x = "   "
if x:  # → True! Vì chuỗi không rỗng
    ...

y = -1
if y:  # → True! Vì khác 0
    ...

...
my_list = []

# ❌ Không Pythonic, dễ lỗi nếu kiểu dữ liệu thay đổi
if my_list == []:
    ...

# ✅ Pythonic: dùng truthiness
if not my_list:
    ...

...
status = "pending"

# ❌ Sai: luôn True (vì "approved" là truthy)
if status == "pending" or "approved":
    print("OK")  # Luôn in!

# ✅ Đúng
if status == "pending" or status == "approved":
    ...

# ✅ Tốt hơn: dùng `in`
if status in ("pending", "approved"):
    ...

...
x = 0
y = 5

# ❌ Hiểu nhầm: nghĩ `x or y` trả về True/False
if x or y:
    print("OK")  # In ra, vì y truthy

# Nhưng:
result = x or y
print(result)  # → 5, KHÔNG phải True!

...
x = 0
y = 5

# ❌ Hiểu nhầm: nghĩ `x or y` trả về True/False
if x or y:
    print("OK")  # In ra, vì y truthy

# Nhưng:
result = x or y
print(result)  # → 5, KHÔNG phải True!

# BẪY TRONG VÒNG LẶP
funcs = []
for i in range(3):
    funcs.append(lambda: print(i))

for f in funcs:
    f()  # In: 2, 2, 2 → ❌ Mong muốn: 0, 1, 2

...
nums = [1, 2, 3, 4, 5]
for x in nums:
    if x % 2 == 0:
        nums.remove(x)  # ❌ Nguy hiểm!

print(nums)  # → [1, 3, 4, 5] → 4 không bị xóa!
# Lý do: Khi xóa phần tử, các phần tử sau dịch về, con trỏ lặp bỏ sót phần tử tiếp theo. 
# ✅ Cách sửa:

# Lặp trên bản sao: for x in nums[:]:
# Dùng list comprehension: nums = [x for x in nums if x % 2 != 0]
# Lặp ngược: for i in range(len(nums)-1, -1, -1):

...
for i in range(3):
    if i == 5:
        break
else:
    print("Không gặp break")  # ✅ In ra

# Nhưng:
for i in range(3):
    break
else:
    print("...")  # ❌ KHÔNG in
#  else trong vòng lặp → hiểu nhầm là "luôn chạy"
#  else trong for/while chỉ chạy nếu vòng lặp kết thúc bình thường (không bị break). 

...
items = ['a', 'b', 'c']

# ❌ Không Pythonic
for i in range(len(items)):
    print(i, items[i])

# ✅ Dùng `enumerate`
for i, item in enumerate(items):
    print(i, item)
# Dùng range(len(...)) khi không cần thiết

...
d = {'a': 1, 'b': 2}

# ❌ Hiểu nhầm: nghĩ lặp qua cặp (key, value)
for x in d:
    print(x)  # → 'a', 'b' (chỉ keys)

# ✅ Muốn cặp:
for k, v in d.items():
    ...
# LỖI PHỔ BIẾN  
""" thục lề sai 
if x > 0:
print("OK")  # ❌ IndentationError

# Hoặc tệ hơn: thụt lề sai nhưng không báo lỗi → logic sai
if x > 0:
    a = 1
    if y > 0:
    a = 2  # ❌ Dòng này không thuộc if y > 0!
"""

# BẪY TRONG HÀM  

"""
1. LEGB Rule – Quy tắc tìm kiếm biến
Python tuân theo LEGB khi tìm biến:

Local → trong hàm hiện tại
Enclosing → trong hàm cha (closure)
Global → trong module
Built-in → như len, print, int, True...
"""

# ❌ SAI – dùng list/dict/set làm giá trị mặc định
def add_item(item, target=[]):
    target.append(item)
    return target

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] ← GÌ? MONG MUỐN: [2]
#  Mutable default argument (BẪY KINH ĐIỂN!)
#sữa  Áp dụng cho: list, dict, set, [], {}, set(), custom object... 
def add_item(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
...
counter = 0

def increment():
    counter += 1  # ❌ UnboundLocalError!

increment()
# Thay đổi biến toàn cục mà không khai báo global
# LƯU Ý ĐÂY LÀ BÀI DÙNG TRỰC TIẾP GLOBAL , CÒN BAI THAM SỐ TRÙNG TÊN GLOBAL
# param tham số hàm  , argument đối số input
# sữa >> chỉ áp dụng cho kiểu dữ liệu bất biến immutable , mutable thì thoải mái
def increment():
    global counter
    counter += 1
# tương tự -------------
def outer():
    x = 0
    def inner():
        x += 1  # ❌ UnboundLocalError!
    inner()
# Thay đổi biến trong closure mà không khai báo nonlocal (Python 3+) >> SỮA
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
    inner()
    return x

...
# ❌ Sai cú pháp
# def f(**kwargs, *args): ...

# ✅ Đúng: *args trước **kwargs
def f(*args, **kwargs): ...

...
def modify_list(lst):
    lst.append(4)  # Ảnh hưởng đến list gốc → OK

def reassign_list(lst):
    lst = [1, 2, 3]  # ❌ Không ảnh hưởng đến list gốc!

my_list = [10]
reassign_list(my_list)
print(my_list)  # [10] ← không đổi!
# ✅ Python không có "pass by value" hay "pass by reference" — mà là "pass by object reference


# BẪY TRONG try...except
def risky_code():...
# ❌ RẤT NGUY HIỂM
try:
    risky_code()
except:  # Bắt cả KeyboardInterrupt, SystemExit!
    pass
# sữa 
def handle_error():...
try:
    risky_code()
except ValueError as e:
    handle_error(e)

...
# ❌ Sai: chỉ bắt `TypeError`, bỏ qua `ValueError`
# except TypeError, ValueError:  # CÚ PHÁP LỖI ở Python 3!
# sữa >> 
try:...
except (TypeError, ValueError) as e:
    ...

...
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Lỗi")
else:
    print("Không lỗi")  # ❌ KHÔNG chạy
finally:
    print("Luôn chạy")  # ✅ Chạy
# Dùng else và finally không hiểu rõ
# else: chỉ chạy nếu không có exception
# finally: luôn chạy, kể cả có return, break, continue

...
def f():
    try:
        return "from try"
    finally:
        return "from finally"  # ✅ Ghi đè!

print(f())  # "from finally"
# → Cẩn thận khi return trong finally! 

...
def risky():...
try:
    risky()
except ValueError:
    print("Có lỗi")  # ❌ Mất thông tin lỗi gốc!

# sữa  >>
import logging

try:
    risky()
except ValueError as e:
    logging.exception("Lỗi khi xử lý")  # Giữ nguyên stack trace
    # hoặc raise lại: raise

...
try:
    risky()
except ValueError:
    # ❌ Mất stack trace gốc
    raise ValueError("Lỗi mới")

# ✅ Giữ nguyên stack trace
except ValueError:
    raise  # ← không có đối số

# Hoặc: chain exception (Python 3)
except ValueError as e:
    raise RuntimeError("Lỗi mới") from e

# raise lại exception sai cách → mất stack trace gốc

...
my_dict = {}
# ❌ Không cần thiết – dùng if tốt hơn
try:
    value = my_dict['key']
except KeyError:
    value = None

# ✅ Tốt hơn:
value = my_dict.get('key')
#  Dùng try...except để kiểm tra điều kiện (EAFP vs LBYL) – lạm dụng
# → EAFP ("Easier to Ask for Forgiveness than Permission") là phong cách Python,
# nhưng đừng lạm dụng khi có cách đơn giản hơn. 


# config.py
DEBUG = True

# main.py
import config
config.DEBUG = False  # ✅ OK

# Nhưng nếu bạn làm:
from config import DEBUG
DEBUG = False  # ❌ Chỉ gán local trong main.py, không đổi config.DEBUG!
# Đây là bẫy "import by value vs by reference" — thực chất là rebinding name. 

...
# exec() và eval() – phạm vi động (dynamic scope)
#  exec/eval phá vỡ LEGB thông thường → dễ gây lỗi bảo mật và debug khó. 
x = 10
exec("print(x)")  # → 10 ✅

def f():
    x = 20
    exec("print(x)")  # → 20 ✅

f()

...
x = "global"

class A:
    x = "class"
    def method(self):
        return x  # → "global", KHÔNG phải "class"!

print(A().method())  # "global" ✅
#  Class scope – không phải là enclosing scope!

# ❗ Phạm vi lớp (class scope) KHÔNG được tìm trong LEGB khi ở trong method!
# → Method chỉ thấy: Local → Enclosing (nếu có closure) → Global → Built-in. 
class A:
    x = "A"

    def get_via_self(self):
        return self.x

    def get_via_class(self):
        return self.__class__.x

    def get_via_A(self):
        return A.x

class B(A):
    x = "B"

b = B()

print(b.get_via_self())     # → "B" ✅ (kế thừa + override)
print(b.get_via_class())    # → "B" ✅ (lấy từ lớp thực tế của b)
print(b.get_via_A())        # → "A" ❌ (cứng vào A, không theo subclass!)