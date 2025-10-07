# -*- coding: utf-8 -*-
"""
OOP & Module/Package Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về OOP và quản lý module/package
"""

import sys
from types import MethodType


def print_section(title):
    """In tiêu đề nhóm nội dung"""
    print("\n" + "=" * 70)
    print(f"{title.upper():^70}")
    print("=" * 70)


def print_example(code, desc, result=None):
    """In ví dụ theo định dạng chuẩn"""
    if result is not None:
        print(f"{code:<40} | {desc:<25} | → {result}")
    else:
        print(f"{code:<40} | {desc}")


# ==============================================================================
# 1. KHÁI NIỆM CƠ BẢN VỀ OOP
# ==============================================================================
print_section("1. Khái niệm cơ bản OOP")
print_example("class Person:", "Định nghĩa lớp", "")
print_example("    def __init__(self, name):", "Hàm khởi tạo", "")
print_example("        self.name = name", "Thuộc tính đối tượng", "")
print_example("", "self: tham chiếu đến chính đối tượng", "")
print_example("obj = Person('An')", "Tạo đối tượng", "")


# ==============================================================================
# 2. CLASS VÀ OBJECT
# ==============================================================================
print_section("2. Class và Object")

# Ví dụ minh họa
class Dog:
    species = "Canis lupus"  # Thuộc tính lớp

    def __init__(self, name, age):
        self.name = name      # Thuộc tính đối tượng
        self.age = age

    def bark(self):
        return f"{self.name} đang sủa!"

# Tạo đối tượng
dog1 = Dog("Buddy", 3)

print_example("Dog.species", "Thuộc tính lớp", Dog.species)
print_example("dog1.name", "Thuộc tính đối tượng", dog1.name)
print_example("dog1.bark()", "Gọi phương thức", dog1.bark())
print_example("type(dog1)", "Kiểm tra kiểu", type(dog1).__name__)


# ==============================================================================
# 3. KẾ THỪA (INHERITANCE)
# ==============================================================================
print_section("3. Kế thừa (Inheritance)")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Phương thức này cần được ghi đè!")

class Cat(Animal):  # Kế thừa từ Animal
    def speak(self):
        return f"{self.name} kêu meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} hót chíp chíp!"

cat = Cat("Mèo Mun")
bird = Bird("Chim Sẻ")

print_example("class Cat(Animal):", "Kế thừa đơn", "")
print_example("cat.speak()", "Ghi đè phương thức", cat.speak())
print_example("isinstance(cat, Animal)", "Kiểm tra kiểu", isinstance(cat, Animal))
print_example("issubclass(Cat, Animal)", "Kiểm tra kế thừa", issubclass(Cat, Animal))


# ==============================================================================
# 4. ĐÓNG GÓI (ENCAPSULATION)
# ==============================================================================
print_section("4. Đóng gói (Encapsulation)")

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    # Property để truy cập an toàn
    @property
    def balance(self):
        return self.__balance

account = BankAccount(100)

print_example("account.__balance", "Truy cập private → lỗi", "AttributeError!")
try:
    print(account.__balance)
except AttributeError as e:
    print(f"{'':<40} | {'':<25} | → Lỗi: {e}")

print_example("account.get_balance()", "Dùng getter", account.get_balance())
print_example("@property", "Dùng property", account.balance)


# ==============================================================================
# 5. ĐA HÌNH (POLYMORPHISM)
# ==============================================================================
print_section("5. Đa hình (Polymorphism)")

def animal_sound(animal):
    print(animal.speak())  # Cùng tên phương thức, hành vi khác nhau

print_example("animal_sound(cat)", "Đa hình qua kế thừa", "")
animal_sound(cat)
animal_sound(bird)

# Duck Typing: Không cần kế thừa, chỉ cần có phương thức speak()
class Robot:
    def speak(self):
        return "Robot: beep boop!"

robot = Robot()
print_example("animal_sound(robot)", "Duck typing", "")
animal_sound(robot)


# ==============================================================================
# 6. PHƯƠNG THỨC VÀ THUỘC TÍNH ĐẶC BIỆT
# ==============================================================================
print_section("6. Phương thức đặc biệt (__dunder__)")

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    def __bool__(self):
        return self.x != 0 or self.y != 0

v1 = Vector(2, 3)
v2 = Vector(1, 1)
v3 = Vector(0, 0)

print_example("v1 = Vector(2,3)", "Tạo đối tượng", "")
print_example("print(v1)", "__str__", v1)
print_example("v1 + v2", "__add__", v1 + v2)
print_example("len(v1)", "__len__", len(v1))
print_example("bool(v3)", "__bool__", bool(v3))


# ==============================================================================
# 7. PHƯƠNG THỨC TĨNH VÀ TĨNH LỚP
# ==============================================================================
print_section("7. Phương thức tĩnh và lớp")

class MathUtils:
    PI = 3.14159

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def circle_area(cls, r):
        return cls.PI * r ** 2

print_example("@staticmethod", "Không cần self/cls", MathUtils.add(3, 5))
print_example("@classmethod", "Nhận cls, dùng cho factory method", MathUtils.circle_area(2))


# ==============================================================================
# 8. MODULE VÀ IMPORT
# ==============================================================================
print_section("8. Module và Import")

# Giả lập việc import
import math
from datetime import datetime as dt

print_example("import math", "Import module", "")
print_example("math.sqrt(16)", "Dùng hàm", math.sqrt(16))
print_example("from datetime import datetime as dt", "Import + alias", "")
print_example("dt.now()", "Sử dụng alias", dt.now().strftime("%H:%M"))


# ==============================================================================
# 9. PACKAGE
# ==============================================================================
print_section("9. Package")

# Minh họa cấu trúc package
package_structure = """
myproject/
├── __init__.py
├── main.py
├── utils/
│   ├── __init__.py
│   └── helper.py
└── models/
    ├── __init__.py
    └── user.py
"""

print_example("Cấu trúc package", "", "")
print(package_structure.strip())
print_example("from utils.helper import func", "Import từ package", "")
print_example("import models.user as user", "Alias module", "")


# ==============================================================================
# 10. __INIT__.PY VÀ __ALL__
# ==============================================================================
print_section("10. __init__.py và __all__")

# Trong file __init__.py
__all__ = ["helper", "validator"]  # Điều khiển what gets imported with "from package import *"

print_example("__all__ = ['mod1']", "Kiểm soát import *", "Chỉ import các module trong danh sách")
print_example("__init__.py", "Chạy khi import package", "Dùng để khởi tạo, cấu hình")


# ==============================================================================
# 11. TẠO MODULE ĐỘNG
# ==============================================================================
print_section("11. Tạo module động")

# Thêm phương thức vào class tại runtime
def dynamic_method(self):
    return f"Xin chào, tôi là {self.name}!"

setattr(Dog, "say_hello", dynamic_method)

print_example("setattr(Dog, 'say_hello', ...)", "Thêm phương thức động", dog1.say_hello())


# ==============================================================================
# 12. DANH SÁCH CÁC __DUNDER__ METHOD QUAN TRỌNG
# ==============================================================================
print_section("12. Các __dunder__ method phổ biến")

dunders = [
    ("__init__", "Khởi tạo đối tượng"),
    ("__str__", "Hiển thị chuỗi thân thiện"),
    ("__repr__", "Hiển thị chi tiết (debug)"),
    ("__len__", "Độ dài: len(obj)"),
    ("__add__", "Toán tử +"),
    ("__eq__", "So sánh == "),
    ("__lt__", "<"),
    ("__getitem__", "obj[key]"),
    ("__setitem__", "obj[key] = value"),
    ("__call__", "Cho phép obj() như hàm"),
    ("__enter__/__exit__", "Context manager (with)"),
]

for method, desc in dunders:
    print(f" • {method:<20} → {desc}")


# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "=" * 70)
print(f"{'CHEAT SHEET OOP & MODULE HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/tutorial/classes.html':^70}")
print("=" * 70)