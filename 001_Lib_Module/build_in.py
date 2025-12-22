# -*- coding: utf-8 -*-
# py_builtin_oneliner.py
# Toàn bộ built-in Python 3 (không import) – dạng "copy-paste-chạy-ngay"
# Chỉ comment, không in → file gọn, load nhanh, nhìn là nhớ.

# ===== TYPE =====
# int float complex bool str bytes bytearray
# list tuple range set frozenset dict type object

# ===== CONVERT =====
int('42'); float('3.14'); str(100); bool(1); bytes('u', 'utf8')
list('abc'); tuple('abc'); set('aabbcc'); dict(a=1, b=2)
ord('A'); chr(65); hex(255); bin(5); oct(8)

# ===== MATH =====
abs(-5); max([1, 2, 3]); min([1, 2, 3]); sum([1, 2, 3])
pow(2, 10)          # 1024
divmod(17, 5)       # (3, 2)
round(3.14159, 2)   # 3.14

# ===== ITER =====
range(5)            # 0..4
range(10, 15)       # 10..14
range(0, 10, 3)     # 0,3,6,9
enumerate(['a', 'b', 'c'])          # (0,'a') (1,'b') ...
zip([1,2,3], 'abc')                 # (1,'a') (2,'b') ...
sorted('dcba')      # ['a','b','c','d']
reversed('hello')   # iterator ngược

# ===== TEST =====
any([0,0,1])        # True nếu có ít nhất 1 True
all([1,1,1])        # True nếu tất cả True

# ===== FUNC TOOL =====
list(map(str.upper, ['a','b']))
list(filter(lambda x: x%2==0, range(10)))
lambda x: x*x       # hàm nặc danh

# ===== SCOPE =====
locals()            # dict biến cục bộ
globals()           # dict biến toàn cục
vars()              # locals() nếu không có đối số

# ===== OBJECT =====
id(obj)             # địa chỉ vùng nhớ
hash(obj)           # hash nếu có __hash__
len(obj)            # độ dài/số phần tử
isinstance(5, int)  # True
type(5) is int      # True
dir(str)            # liệt kê thuộc tính/phương thức
help(str.replace)   # help docs (interactive)

# ===== COMPILE & RUN =====
code = compile('a=2+3; print(a)', '', 'exec')
exec(code)          # chạy đoạn code string
eval('2**10')       # 1024 – chỉ 1 biểu thức

# ===== CONSTANTS =====
# True False None Ellipsis NotImplemented __debug__

# ===== EXCEPTION =====
try:
    1/0
except ZeroDivisionError as e:
    pass
finally:
    pass

# ===== INPUT/OUTPUT =====
# input('Name: ')     # đọc string từ stdin
print('a', 'b', sep='-', end='!\n')  # in tùy biến

# ===== WITH =====
with open('file.txt', 'w', encoding='utf8') as f:
    f.write('ok')

# ===== GENERATOR =====
def gen():
    yield 1
    yield 2
g = gen(); next(g)   # 1; next(g)  # 2

# ===== CLASS & FUNC =====
class A:
    def __init__(self, x): self.x = x
    def __repr__(self): return f'A({self.x})'

def f(a, b=2, *, c): ...
# f(1, c=3)           # chỉ cho phép keyword từ c

# ===== DECORATOR =====
@property
@staticmethod
@classmethod
def nn():...
# # ===== IMPORT =====
# __import__('os')     # tương đương import os (built-in)

# # ===== MEMORY =====
# del obj              # xóa tham chiếu