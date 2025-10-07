#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    print("=" * 60)
    print("🐍 PYTHON BUILT-IN FUNCTIONS CHEAT SHEET (Must-Know)")
    print("✅ Chạy script này để xem nhanh mọi lúc!")
    print("=" * 60)

    # 1. Chuyển đổi kiểu
    print("\n1️⃣  CHUYỂN ĐỔI KIỂU")
    print("   int('10')      →", repr(int('10')))
    print("   float('3.14')  →", repr(float('3.14')))
    print("   str(42)        →", repr(str(42)))
    print("   bool(0)        →", repr(bool(0)))
    print("   list('ab')     →", repr(list('ab')))
    print("   tuple([1,2])   →", repr(tuple([1, 2])))
    print("   set([1,1,2])   →", repr(set([1, 1, 2])))
    print("   dict(a=1)      →", repr(dict(a=1)))

    # 2. Đo lường & kiểm tra
    print("\n2️⃣  ĐO LƯỜNG & KIỂM TRA")
    print("   len([1,2,3])   →", repr(len([1, 2, 3])))
    print("   type(42)       →", repr(type(42).__name__))
    print("   isinstance(42, int) →", repr(isinstance(42, int)))
    print("   id(x) (demo)   →", repr(id(42)))

    # 3. Toán học
    print("\n3️⃣  TOÁN HỌC")
    print("   abs(-5)        →", repr(abs(-5)))
    print("   round(3.1415, 2) →", repr(round(3.1415, 2)))
    print("   max([1,5,3])   →", repr(max([1, 5, 3])))
    print("   min([1,5,3])   →", repr(min([1, 5, 3])))
    print("   sum([1,2,3])   →", repr(sum([1, 2, 3])))
    print("   pow(2, 3)      →", repr(pow(2, 3)))

    # 4. Xử lý tập hợp
    print("\n4️⃣  XỬ LÝ TẬP HỢP")
    print("   enumerate: list(enumerate(['a','b']))")
    print("              →", repr(list(enumerate(['a', 'b']))))
    print("   zip: list(zip([1,2], ['x','y']))")
    print("        →", repr(list(zip([1, 2], ['x', 'y']))))
    print("   map: list(map(str.upper, ['a','b']))")
    print("        →", repr(list(map(str.upper, ['a', 'b']))))
    print("   filter: list(filter(lambda x: x>0, [-1,2]))")
    print("           →", repr(list(filter(lambda x: x > 0, [-1, 2]))))
    print("   sorted([3,1,2]) →", repr(sorted([3, 1, 2])))

    # 5. I/O & hệ thống
    print("\n5️⃣  NHẬP/XUẤT & HỆ THỐNG")
    print("   print('x', end=' ') → in không xuống dòng")
    print("   input('...')   → nhập từ bàn phím (demo bỏ qua)")
    print("   open()         → dùng với 'with' để an toàn")
    print("   help(len)      → xem hướng dẫn (gõ trong REPL)")
    print("   exit()         → thoát chương trình")

    # 6. OOP & khác
    print("\n6️⃣  OOP & KHÁC")
    print("   super()        → gọi phương thức class cha")
    print("   hasattr(obj, 'name') → kiểm tra thuộc tính")
    print("   getattr(obj, 'name', default) → lấy giá trị")
    print("   callable(len)  →", repr(callable(len)))
    print("   range(3)       →", repr(list(range(3))))

    print("\n" + "=" * 60)
    print("💡 GỢI Ý: ĐỪNG đặt biến trùng tên hàm built-in!")
    print("   ❌ list = [1,2]  → lỗi khi dùng list() sau đó!")
    print("   ✅ my_list = [1,2]")
    print("=" * 60)

if __name__ == "__main__":
    main()