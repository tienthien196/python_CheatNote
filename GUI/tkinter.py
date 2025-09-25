# -*- coding: utf-8 -*-
"""
Tkinter Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module tkinter trong Python
"""

import tkinter as tk
from tkinter import messagebox
import sys

def print_section(title):
    """In tiêu đề nhóm phương thức (hiển thị trong console)"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn (hiển thị trong console)"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
sample_text = "Hello, Tkinter!"
window_title = "My Tkinter App"
button_text = "Click Me!"

# ==============================================================================
# 1. TẠO CỬA SỔ CHÍNH
# ==============================================================================
print_section("1. Tạo cửa sổ chính")
root = tk.Tk()
root.title(window_title)
root.geometry("400x300")
print_example('tk.Tk()', "Tạo cửa sổ chính", "Cửa sổ được tạo")
print_example('root.title("My Tkinter App")', "Đặt tiêu đề cửa sổ", window_title)
print_example('root.geometry("400x300")', "Đặt kích thước cửa sổ", "400x300 pixels")

# ==============================================================================
# 2. THÊM WIDGET CƠ BẢN
# ==============================================================================
print_section("2. Thêm widget cơ bản")
label = tk.Label(root, text=sample_text, font=("Arial", 14))
label.pack()
print_example('tk.Label(root, text="Hello")', "Tạo nhãn văn bản", sample_text)
button = tk.Button(root, text=button_text, command=lambda: messagebox.showinfo("Message", "Button clicked!"))
button.pack()
print_example('tk.Button(root, text="Click Me!")', "Tạo nút bấm", button_text)
entry = tk.Entry(root, width=20)
entry.pack()
print_example('tk.Entry(root, width=20)', "Tạo ô nhập liệu", "Ô nhập liệu 20 ký tự")

# ==============================================================================
# 3. QUẢN LÝ BỐ CỤC
# ==============================================================================
print_section("3. Quản lý bố cục")
frame = tk.Frame(root)
frame.pack()
label1 = tk.Label(frame, text="Left")
label1.pack(side=tk.LEFT)
label2 = tk.Label(frame, text="Right")
label2.pack(side=tk.RIGHT)
print_example('label.pack(side=tk.LEFT)', "Bố cục pack (trái)", "Căn trái trong frame")
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()
canvas.create_rectangle(10, 10, 90, 90, fill="blue")
print_example('canvas.create_rectangle(...)', "Vẽ hình chữ nhật", "Hình chữ nhật màu xanh")
root.grid_columnconfigure(0, weight=1)
label_grid = tk.Label(root, text="Grid Layout")
label_grid.grid(row=0, column=0)
print_example('label.grid(row=0, column=0)', "Bố cục grid", "Căn theo lưới")

# ==============================================================================
# 4. XỬ LÝ SỰ KIỆN
# ==============================================================================
print_section("4. Xử lý sự kiện")
def on_button_click():
    return "Button clicked"
button_event = tk.Button(root, text="Event Button", command=on_button_click)
button_event.pack()
print_example('button.command=on_button_click', "Gán hàm cho nút", on_button_click())
entry.bind("<Return>", lambda event: print_example('entry.bind("<Return>", ...)', "Nhấn Enter", entry.get()))
print_example('entry.bind("<Return>", ...)', "Sự kiện nhấn Enter", "Lấy giá trị ô nhập")

# ==============================================================================
# 5. SỬ DỤNG MESSAGEBOX
# ==============================================================================
print_section("5. Sử dụng Messagebox")
print_example('messagebox.showinfo("Title", "Message")', "Hiển thị thông báo", "Hộp thoại thông tin")
print_example('messagebox.askyesno("Confirm", "Proceed?")', "Hỏi có/không", "Trả về True/False")
print_example('messagebox.showerror("Error", "Failed")', "Hiển thị lỗi", "Hộp thoại lỗi")

# ==============================================================================
# 6. QUẢN LÝ BIẾN TKINTER
# ==============================================================================
print_section("6. Quản lý biến Tkinter")
string_var = tk.StringVar(value="Initial Text")
entry_var = tk.Entry(root, textvariable=string_var)
entry_var.pack()
print_example('tk.StringVar(value="Initial Text")', "Tạo biến chuỗi", string_var.get())
string_var.set("Updated Text")
print_example('string_var.set("Updated Text")', "Cập nhật biến", string_var.get())
int_var = tk.IntVar(value=42)
print_example('tk.IntVar(value=42)', "Tạo biến số nguyên", int_var.get())

# ==============================================================================
# 7. WIDGET NÂNG CAO
# ==============================================================================
print_section("7. Widget nâng cao")
listbox = tk.Listbox(root, height=3)
listbox.insert(1, "Option 1")
listbox.insert(2, "Option 2")
listbox.pack()
print_example('tk.Listbox(root, height=3)', "Tạo listbox", "Danh sách chọn")
menu = tk.Menu(root)
root.config(menu=menu)
submenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Exit", command=root.quit)
print_example('tk.Menu(root)', "Tạo menu", "Menu File với Exit")
text = tk.Text(root, height=2, width=20)
text.insert(tk.END, "Sample text")
text.pack()
print_example('tk.Text(root, height=2)', "Tạo ô văn bản lớn", "Ô văn bản 2 dòng")

# ==============================================================================
# 8. TÙY CHỈNH GIAO DIỆN
# ==============================================================================
print_section("8. Tùy chỉnh giao diện")
label_style = tk.Label(root, text="Styled", fg="white", bg="black", font=("Arial", 12, "bold"))
label_style.pack()
print_example('tk.Label(..., fg="white", bg="black")', "Tùy chỉnh màu, phông", "Nhãn trắng trên nền đen")
root.configure(bg="lightgray")
print_example('root.configure(bg="lightgray")', "Đặt màu nền cửa sổ", "Nền xám nhạt")
button.config(state="disabled")
print_example('button.config(state="disabled")', "Vô hiệu hóa nút", "Nút không bấm được")
button.config(state="normal")
print_example('button.config(state="normal")', "Kích hoạt lại nút", "Nút hoạt động")

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    invalid_widget = tk.Label(None)
except tk.TclError as e:
    print_example('tk.Label(None)', "Lỗi không có root", f"Lỗi: {e}")
try:
    root.geometry("invalid")
except tk.TclError as e:
    print_example('root.geometry("invalid")', "Lỗi định dạng geometry", f"Lỗi: {e}")

# ==============================================================================
# 10. THÔNG TIN MODULE TKINTER
# ==============================================================================
print_section("10. Thông tin module tkinter")
all_classes = [m for m in dir(tk) if not m.startswith("_") and isinstance(getattr(tk, m), type)]
print(f"Tổng cộng: {len(all_classes)} lớp")
print("\n".join(f" • {cls:<20} → {getattr(tk, cls).__doc__.split('.')[0]}" for cls in sorted(all_classes)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'TKINTER MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://docs.python.org/3/library/tkinter.html':^70}")
print("="*70)

# Chạy vòng lặp chính (chỉ để kiểm tra, không hiển thị trong console)
# root.mainloop()