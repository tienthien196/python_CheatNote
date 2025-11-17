#---Binary---nhị phân ----
print(0b0101)
print(0B1111)
#---Octal ----bát phân ----
print(0o7777)
print(0O4567)

# ---hexadecimal--thập lục phân
print(0x0000)
print(0XFFFF)

#---Decimal ----hệ cơ số 10 
x = 255
print(x)           # 255 (thập phân)
print(bin(x))      # 0b11111111
print(oct(x))      # 0o377
print(hex(x))      # 0xff







# print(l)
# print(c)
# print(i) 
# print(type(i))
# print(type(b))

# print(help(input))




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
# ** toán tử mũ sẽ thực thi từ phải qua trái 
# --- CÒN LẠI TỪ PHẢI SANG TRÁI ---------
# Số học (*, /, //, %, +, -) → như toán phổ thông.
# Bitwise (<<, >>, &, ^, |) → nằm giữa số học và so sánh.
# So sánh (==, !=, <, <=,  in, is, is not , not in) 
# Logic (not → and → or) → ưu tiên thấp nhất (trừ gán).
x = 9; y= 9
# --- bẫy --->> CHÚ Ý DÁU NGOẶC KHI DÙNG TOÁN TỬ  
True == True and False # (True == True) and False 
5 & 3 == 1 # 5 & (3 == 1) Sai >> phải sữa (5 & 3) == 1  # → True
2 ** 3 ** 2 # vấn đúng vì toán từ mũ chạy từ phải qua trái 
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

try: ...
except ZeroDivisionError: ... # 5 / 0  # ZeroDivisionError
except IndentationError as e: ... #  Sai dòng viết (dùng tab và dấu cách, thiếu dấu lót sau , vv):
except NameError as e : ... #  Sử dụng biến chưa được xác định 
except AttributeError as e :
    ... # Truy cập thuộc tính/phương thức không tồn tại(cả list, dict)
    x = []
    x.appendd(1)  # AttributeError: 'list' object has no attribute 'appendd'
except TypeError as e  :
    ... # Thao tác không hợp lệ với kiểu dữ liệu
    "5" + 3        # TypeError
    len(5)         # TypeError
    my_list[None]  # TypeError: list indices must be integers
except ValueError as e:
    ... # Hợp lệ có giá trị về kiểu nhưng không hợp lệ về nghĩa.
    int("hello")     # ValueError
    list.index(99)   # ValueError: 99 is not in list
except IndexError as e: 
    ... # Truy cập chỉ số ngoài phạm vi.
    [1, 2][5]  # IndexError
except KeyError as e:
    # Key truy cập không tồn tại trong dict
    d = {'a': 1}
    d['b']  # KeyError
    # cách tránh 
    d.get('key', "") # dùng default
    if 'key' in d: ... # dùng in 
except UnboundLocalError:
    x = 0
    def f():
        x += 1  # UnboundLocalError
    # dùng global

except RecursionError: ... # Đệ quy quá sâu (vượt giới hạn ~1000).sys.getrecursionlimit()
# khi dùng nhiều ngoại lệ phải dùng tuple 
except (ModuleNotFoundError, ImportError) as e: ...#  Mô-đun không tồn tại hoặc sai đường dẫn. as e: ...#  Mô-đun không tồn tại hoặc sai đường dẫn.
except (FileNotFoundError, OSError): ...#  File không tồn tại, quyền truy cập, disk full, vv
except (UnicodeError, UnicodeDecodeError, UnicodeEncodeError):... # Đọc/ghi file với mã hóa sai.
except StopIteration: ... # Gọi trên iterator đã hết.next()
except RuntimeError: ... #  Lỗi logic nghiêm trọng (ví dụ: chu trình nhập, trình tạo được sửa khi đang chạy).
except: KeyboardInterrupt: ...
# ----🛡️ Nguyên tắc vàng để tránh ngoại lệ :----
"""
    EAFP "Dễ xin tha thứ hơn là xin phép" → Dùng khi lỗi nguy hiểm ra try/except
    LBYL "Look Before You Leap" → Kiểm tra điều k
    Xác thực đầu vào -> Luôn kiểm tra đầu vào từ người dùng/tệp/mạng
    Dùng gợi ý kiểu + mypy -> Bắt lỗi ngay từ dev time
    Không bắt trốngexcept: -> Luôn có thể chỉ định cụ thể loại ngoại lệ

"""

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
    except:...
    # finally:
    #     return "from finally"  # ✅ Ghi đè!

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
# namespace >>Built-in >>Global (module-level) >>Local (function-level) >>Enclosing (closure)
# Module object>> tạo 1 object module trong namespace
# Dùng import module cho cấu hình, trạng thái, cần tính rõ ràng thì dùng object thay from, tránh xuung đột với namespace
# Utils extendsion>>
# Dùng from module import func cho hàm/hằng chỉ đọc, dùng trực tiếp  ,

# nếu dùng gói package >> thì phải cần __init__ >> phân chia hệ thỗng rõ ràng 
# mypackage/__init__.py
# from .core import Engine
# from .utils import load_config, save_output
# from .exceptions import MyError

# __all__ = ['Engine', 'load_config', 'save_output', 'MyError']

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


class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

class D(B, C):
    def method(self):
        print("D")
        super().method()

D().method()
# Output: D → B → C → A (đúng nhờ MRO)
# ❌ Sai cách gọi → bỏ phương thức chasuper()

...
class MyInt(int): pass
x = MyInt(5)
print(type(x) == int)      # False ❌
print(isinstance(x, int))  # True ✅

...
class MyClass:
    def __init__(self, items=[]):  # ❌ Mutable default!
        self.items = items

# bẫy với FIle 
# 🔥 2. Bẫy chuỗi và mã hóa
# Trên Windows, nếu file không có encoding, open() dùng encoding hệ thống
with open('file.txt') as f:  # ❌ Nguy hiểm!
    data = f.read()
#sữa  >>
with open('file.txt', encoding='utf-8') as f:
    ...

...
# ❌ Trộn lẫn đối tượng và chuỗiPath RCE
from pathlib import Path
p = Path("data") / "file.txt"
# ❌
with open(p + ".bak") as f:  # Lỗi! Không thể cộng Path + str bằng `+`
    ...
# ✅ Sử dụng hoặc ép dây:/
with open(p.with_suffix('.txt.bak')) as f: ...

...
# ⚠️ NEVER DO THIS WITH UNTRUSTED DATA
# data = pickle.loads(user_input)  # RCE risk!




d = {[1,2]: "value"}  # ❌ TypeError: unhashable type: 'list'
print(d)

# 5. Bị bẫy và iterator đã cạn kiệt
nums = (x for x in range(3))
print(list(nums))  # [0, 1, 2]
print(list(nums))  # [] ← generator đã "hết"


d = {[1, 2]: "value"}      # ❌ list không hash được
d = {{1, 2}: "value"}      # ❌ set không hash được
d = {{"a": 1}: "value"}    # ❌ dict không hash được
t = ([1, 2],)  # tuple chứa list → vẫn unhashable!
d = {t: "x"}   # ❌ TypeError!
# ✅ Chỉ sử dụng loại khóa làm việc bất biến : int , flaot , str
# sữa  >>
d = {(1, 2): "value"}      # ✅ tuple → OK
d = {frozenset([1, 2]): "v"}  # ✅ frozenset → OK

...
d = {'a': 1}
print(d['b'])  # ❌ KeyError
# ❌ Key truy cập không tồn tại →KeyError
# Cách 1: Dùng .get()
value = d.get('b', 'default')

# Cách 2: Kiểm tra trước
if 'b' in d:
    print(d['b'])

# Cách 3: Dùng defaultdict
from collections import defaultdict
d = defaultdict(lambda: 'default')

...
# ❌ Edit dict khi đang lặp → (trong một số trường hợp)RuntimeError
d = {'a': 1, 'b': 2}
for k in d:
    if k == 'a':
        del d[k]  # ❌ RuntimeError: dictionary changed size during iteration
#sữa  >> 
# Lặp trên bản sao key
for k in list(d.keys()):
    if k == 'a':
        del d[k]

# Hoặc dùng dict comprehension để tạo mới
d = {k: v for k, v in d.items() if k != 'a'}

...
# ❌ Đối số mặc định có thể thay đổi trong dict → hành động bất ngờ
def add(key, value, target={}):  # ❌ dict mutable default!
    target[key] = value
    return target

print(add('a', 1))  # {'a': 1}
print(add('b', 2))  # {'a': 1, 'b': 2} ← GÌ?!
# sữa  >>
def add(key, value, target=None):
    if target is None:
        target = {}
    target[key] = value
    return target

...
# ❌ So sánh dict bằng → luôn (trừ khi cùng đối tượng)isFalse
d1 = {'a': 1}
d2 = {'a': 1}
print(d1 is d2)  # False ✅ (đúng logic)
print(d1 == d2)  # True ✅
# Không sai, nhưng đừng dùng để so sánh nội dung dict .is


a = b = []  # ❌ cùng trỏ 1 list!
a.append(1)
print(b)  # [1] ← bất ngờ!

# sữa >>
a = []
b = []
# hoặc
a, b = [], []

...
a = [[1, 2], [3, 4]]
b = a.copy()        # hoặc b = a[:]
b[0][0] = 999
print(a)  # [[999, 2], [3, 4]] ← bị ảnh hưởng!
# ❌ Sao chép danh sách nông (bản sao nông) với danh sách lồng nhau
import copy
b = copy.deepcopy(a)

...
result = []
for i in range(1000):
    result = result + [i]  # ❌ Tạo list mới mỗi lần!
# ❌ Sử dụng để kết nối danh sách trong vòng lặp → O(n²) → chậm+
#sữa >> 
result = []
for i in range(1000):
    result.append(i)  # ✅ O(1) amortized

# hoặc
result.extend(range(1000))

"""
## 🔸 1. Sao chép nông (Shallow Copy) vs Sao chép sâu (Deep Copy)

### 🎯 Vấn đề cốt lõi:
Python **không sao chép object khi gán**, mà **tạo thêm tham chiếu** → thay đổi object gốc → object "sao chép" cũng thay đổi.

### 🔸 Shallow Copy (`copy.copy()` hoặc `.copy()`, `[:]`)
- **Sao chép cấp 1**: tạo **object mới**, nhưng **các phần tử bên trong vẫn là tham chiếu đến object cũ**.
- **Chỉ an toàn với dữ liệu flat** (không lồng).

#### ✅ Ví dụ minh họa:
```python
import copy

# --- Trường hợp 1: Danh sách phẳng (flat list) ---
a = [1, 2, 3]
b = a.copy()        # shallow copy
b[0] = 999
print(a)  # [1, 2, 3] → không bị ảnh hưởng → OK!

# --- Trường hợp 2: Danh sách lồng (nested list) ---
a = [[1, 2], [3, 4]]
b = a.copy()        # shallow copy → BẪY!
b[0][0] = 999
print(a)  # [[999, 2], [3, 4]] → BỊ ẢNH HƯỞNG! 
"""

...# từ khoá del 
a = [1, 2, 3]
b = a          # b và a cùng trỏ đến [1,2,3]
del a          # xóa tên 'a', nhưng object [1,2,3] vẫn còn vì 'b' đang trỏ
print(b)       # [1, 2, 3] → vẫn in được!
# Xóa tên, không xóa đối tượng

...# Xóa phần tử trong vùng chứa
my_list = [10, 20, 30]
del my_list[1]     # xóa phần tử ở index 1
print(my_list)     # [10, 30]

my_dict = {'x': 1, 'y': 2}
del my_dict['x']   # xóa key 'x'
print(my_dict)     # {'y': 2}


# -----------------------------------------------------------------------------------------------------------------------------------------------
#  1. Các nâng cấp tích hợp của loại dữ liệu
# frozenset: phiên bản bất biến của , có thể dùng làm khóa trong dict.set
# bytearray: phiên bản có thể thay đổi của .bytes
# memoryview: được phép truy cập bộ nhớ của đối tượng mà không được sao chép → hiệu suất cao.
# range: is Immutable Sequence , Not List , and Lazy (chỉ sinh giá trị khi cần).
# namedtuple(từ ): tuple có trường tên → dễ đọc, hiệu quả.collections
# deque: hàng đợi hai đầu, tối ưu cho chèn/xóa ở 2 đầu.
# Counter, ,defaultdictOrderedDict : các biến có thể hữu ích.

#  2. Iterable, Iterator, Generator – Chi tiết sâu
# Sự khác biệt giữa vàiterableiterator :
# list, , → có thể lặp lại (có )strdict__iter__
# iter(list)→ iterator (có )__next__
# Hàm tạo ( ) so với biểu thức tạo ( )yield(x for x in ...)
# yield from: trình tạo đại biểu
# send(), ,throw()close() : bộ tạo điều khiển
# Đã hết iterator : dùng xong một lần là hết → không thể dùng lại được.

#  3. Trình quản lý bối cảnh ( ) – Tự tạowith
# Sử dụng , để hỗ trợ lớp__enter____exit__with
# Hoặc dùng để tạo từ trình tạo@contextlib.contextmanager
# from contextlib import contextmanager

# @contextmanager
# def timer():
#     start = time.time()
#     yield
#     print(f"Time: {time.time() - start}")


#  4. Decorator – Nâng cao
# Decorator có tham số:@decorator(arg)
# Trình trang trí lớp
# functools.wrapsđể chứa siêu dữ liệu gốc của hàm
# Các trình trang trí tích hợp: , ,@property@staticmethod@classmethod

# 5. Miêu tả & , ,__get____set____delete__
# Cơ chế đằng sau@property
# Cho phép kiểm soát quyền truy cập thuộc tính

# class Positive:
#     def __set_name__(self, owner, name):
#         self.name = name
#     def __get__(self, obj, objtype=None):
#         return obj.__dict__[self.name]
#     def __set__(self, obj, value):
#         if value <= 0:
#             raise ValueError("Must be positive")
#         obj.__dict__[self.name] = value

#  6. Metaclass ( , của lớp)__new____init__
# "Class of class" → use để tùy chỉnh cách tạo lớp
# Ít dùng, nhưng rất mạnh (Django, SQLAlchemy use)

# class Meta(type):
#     def __new__(cls, name, bases, dct):
#         dct['auto_added'] = True
#         return super().__new__(cls, name, bases, dct)

# class MyClass(metaclass=Meta):
#     pass

# 🔹 7. Không đồng bộ / Chờ đợi (asyncio)
# Lập trình bất đồng bộ: , , ,async defawaitasync forasync with
# Vòng lặp sự kiện, coroutine, nhiệm vụ, tương lai
# Không phải đa luồng, mà là đồng thời thông qua đa nhiệm hợp tác

# 🔹 8. Gợi ý gõ – Nâng cao
# Union, , , ,OptionalLiteralTypedDictProtocol
# Generic: , → thay bằng (Python 3.9+)List[int]Dict[str, float]list[int]
# TypeVar, ,Callable@overload
# Dùng để kiểm tra tĩnhmypy

#  9. Module & Package – Nâng cao
# __name__ == "__main__": check script run direct
# __all__: kiểm soátfrom module import *
# Nhập khẩu tương đối:from . import utils
# Gói không gian tên (không cần thiết )__init__.py


# 🔹 10. Hiệu suất & Tối ưu hóa
# __slots__: giảm bộ nhớ cho phiên bản
# tránh cho string → dùng+join()
# Tránh trong vòng lặp → sử dụng hoặc hiểu danh sáchlist + listextend()
# dismodule: xem bytecode
# timeit: performance đo chính xác
# 🔹 11. Công cụ gỡ lỗi & xem xét nội tâm
# inspectmodule: lấy hàm thông tin, lớp, khung
# pprint: in đẹp dữ liệu cấu trúc
# pdb: trình gỡ lỗi tích hợp
# vars(), , ,dir()getattr()hasattr()
# 🔹 12. GIL (Khóa thông dịch toàn cục)
# Tại sao Python không thực hiện tối đa luồng CPU-bound?
# Khi nào thì nên sử dụng ?multiprocessingthreading

# 13. Lớp dữ liệu (Python 3.7 trở lên)
# Thay thế , , bằng trang trí__init____repr____eq__
# from dataclasses import dataclass

# @dataclass
# class Point:
#     x: int
#     y: int

#  14. So khớp mẫu cấu trúc (match-case – Python 3.10+)
# match value:
#     case 0:
#         print("Zero")
#     case x if x > 0:
#         print("Positive")
#     case _:
#         print("Other")
    

# 🔹 15. Bảo mật & Thực hành tốt nhất
# Tránh , , với dữ liệu không được tin cậyeval()exec()pickle
# Sử dụng thay thế mật khẩu/mã thông báosecretsrandom
# Môi trường ảo ( , , )venvpipenvpoetry
