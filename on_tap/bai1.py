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

c2 is bool # is là check 2 biến có cùng trỏ 1 ô nhớ ko ?
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

