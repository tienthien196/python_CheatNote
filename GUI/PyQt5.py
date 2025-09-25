# -*- coding: utf-8 -*-
"""
PyQt5 Module Cheat Sheet – Python 3.10+
Tác giả: Bạn (được hoàn thiện bởi trợ lý AI)
Phiên bản: 1.0
Mục đích: Tài liệu tham khảo toàn diện về sử dụng module PyQt5 trong Python
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QWidget, QMenuBar, QMenu, QMessageBox,
                             QComboBox, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

def print_section(title):
    """In tiêu đề nhóm phương thức (hiển thị trong console)"""
    print("\n" + "="*70)
    print(f"{title.upper():^70}")
    print("="*70)

def print_example(method, desc, result):
    """In ví dụ theo định dạng chuẩn (hiển thị trong console)"""
    print(f"{method:<35} | {desc:<28} | Kết quả: {result}")

# Dữ liệu mẫu
app_title = "My PyQt5 App"
sample_text = "Hello, PyQt5!"
button_text = "Click Me!"

# Khởi tạo ứng dụng (chỉ để kiểm tra, không hiển thị trong console)
app = QApplication(sys.argv)

# ==============================================================================
# 1. TẠO CỬA SỔ CHÍNH
# ==============================================================================
print_section("1. Tạo cửa sổ chính")
window = QMainWindow()
window.setWindowTitle(app_title)
window.setGeometry(100, 100, 400, 300)
print_example('QMainWindow()', "Tạo cửa sổ chính", "Cửa sổ được tạo")
print_example('window.setWindowTitle("My PyQt5 App")', "Đặt tiêu đề cửa sổ", app_title)
print_example('window.setGeometry(100, 100, 400, 300)', "Đặt vị trí và kích thước", "100,100,400,300")

# ==============================================================================
# 2. THÊM WIDGET CƠ BẢN
# ==============================================================================
print_section("2. Thêm widget cơ bản")
central_widget = QWidget()
window.setCentralWidget(central_widget)
layout = QVBoxLayout()
central_widget.setLayout(layout)
label = QLabel(sample_text, central_widget)
label.setFont(QFont("Arial", 14))
layout.addWidget(label)
print_example('QLabel("Hello, PyQt5!")', "Tạo nhãn văn bản", sample_text)
button = QPushButton(button_text, central_widget)
layout.addWidget(button)
print_example('QPushButton("Click Me!")', "Tạo nút bấm", button_text)
line_edit = QLineEdit(central_widget)
line_edit.setPlaceholderText("Enter text...")
layout.addWidget(line_edit)
print_example('QLineEdit()', "Tạo ô nhập liệu", "Ô nhập liệu với placeholder")

# ==============================================================================
# 3. QUẢN LÝ BỐ CỤC
# ==============================================================================
print_section("3. Quản lý bố cục")
hbox_layout = QHBoxLayout()
label_left = QLabel("Left", central_widget)
label_right = QLabel("Right", central_widget)
hbox_layout.addWidget(label_left)
hbox_layout.addWidget(label_right)
layout.addLayout(hbox_layout)
print_example('QHBoxLayout()', "Bố cục ngang", "Căn trái/phải trong layout")
layout.addStretch()
print_example('layout.addStretch()', "Thêm khoảng trống co giãn", "Khoảng trống tự động")
widget_grid = QWidget()
grid_layout = QHBoxLayout()
grid_layout.addWidget(QLabel("Grid Item", widget_grid))
widget_grid.setLayout(grid_layout)
layout.addWidget(widget_grid)
print_example('QHBoxLayout()', "Bố cục lưới", "Căn theo lưới")

# ==============================================================================
# 4. XỬ LÝ SỰ KIỆN
# ==============================================================================
print_section("4. Xử lý sự kiện")
def on_button_click():
    return "Button clicked"
button.clicked.connect(lambda: QMessageBox.information(window, "Message", "Button clicked!"))
print_example('button.clicked.connect(...)', "Gán hàm cho nút", on_button_click())
def on_text_changed(text):
    return text
line_edit.textChanged.connect(on_text_changed)
print_example('line_edit.textChanged.connect(...)', "Sự kiện thay đổi văn bản", "Lấy văn bản nhập")

# ==============================================================================
# 5. SỬ DỤNG MESSAGEBOX
# ==============================================================================
print_section("5. Sử dụng Messagebox")
print_example('QMessageBox.information(...)', "Hiển thị thông báo", "Hộp thoại thông tin")
print_example('QMessageBox.question(..., "Proceed?")', "Hỏi có/không", "Trả về Yes/No")
print_example('QMessageBox.critical(..., "Error")', "Hiển thị lỗi", "Hộp thoại lỗi")

# ==============================================================================
# 6. QUẢN LÝ MENU
# ==============================================================================
print_section("6. Quản lý menu")
menubar = QMenuBar(window)
window.setMenuBar(menubar)
file_menu = QMenu("File", window)
menubar.addMenu(file_menu)
file_menu.addAction("Exit", window.close)
print_example('QMenuBar() và QMenu()', "Tạo menu", "Menu File với Exit")
print_example('file_menu.addAction("Exit", ...)', "Thêm hành động Exit", "Đóng ứng dụng")

# ==============================================================================
# 7. WIDGET NÂNG CAO
# ==============================================================================
print_section("7. Widget nâng cao")
combo_box = QComboBox(central_widget)
combo_box.addItems(["Option 1", "Option 2", "Option 3"])
layout.addWidget(combo_box)
print_example('QComboBox().addItems(...)', "Tạo danh sách thả xuống", "Danh sách 3 tùy chọn")
text_edit = QTextEdit(central_widget)
text_edit.setPlainText("Sample text")
layout.addWidget(text_edit)
print_example('QTextEdit().setPlainText(...)', "Tạo ô văn bản lớn", "Ô văn bản đa dòng")
layout.addWidget(QLabel("Status:", central_widget))
print_example('QLabel("Status:")', "Thêm nhãn trạng thái", "Nhãn trạng thái")

# ==============================================================================
# 8. TÙY CHỈNH GIAO DIỆN
# ==============================================================================
print_section("8. Tùy chỉnh giao diện")
label.setStyleSheet("color: white; background-color: black;")
print_example('label.setStyleSheet("color: white; ...")', "Tùy chỉnh màu", "Nhãn trắng trên nền đen")
window.setStyleSheet("background-color: lightgray;")
print_example('window.setStyleSheet("background-color: ...")', "Đặt màu nền cửa sổ", "Nền xám nhạt")
button.setEnabled(False)
print_example('button.setEnabled(False)', "Vô hiệu hóa nút", "Nút không bấm được")
button.setEnabled(True)
print_example('button.setEnabled(True)', "Kích hoạt lại nút", "Nút hoạt động")

# ==============================================================================
# 9. XỬ LÝ LỖI
# ==============================================================================
print_section("9. Xử lý lỗi")
try:
    invalid_widget = QLabel(None)
except ValueError as e:
    print_example('QLabel(None)', "Lỗi không có parent", f"Lỗi: {e}")
try:
    window.setGeometry(0, 0, -100, -100)
except ValueError as e:
    print_example('window.setGeometry(0, 0, -100, -100)', "Lỗi kích thước âm", f"Lỗi: {e}")

# ==============================================================================
# 10. THÔNG TIN MODULE PYQT5
# ==============================================================================
print_section("10. Thông tin module PyQt5.QtWidgets")
from PyQt5 import QtWidgets
all_classes = [m for m in dir(QtWidgets) if not m.startswith("_") and isinstance(getattr(QtWidgets, m), type)]
print(f"Tổng cộng: {len(all_classes)} lớp")
print("\n".join(f" • {cls:<20} → {getattr(QtWidgets, cls).__doc__.split('.')[0]}" for cls in sorted(all_classes)))

# ==============================================================================
# KẾT THÚC
# ==============================================================================
print("\n" + "="*70)
print(f"{'PYQT5 MODULE CHEAT SHEET HOÀN TẤT!':^70}")
print(f"{'Chạy bằng Python ' + '.'.join(map(str, sys.version_info[:3])):^70}")
print(f"{'https://www.riverbankcomputing.com/static/Docs/PyQt5/':^70}")
print("="*70)

# Chạy ứng dụng (chỉ để kiểm tra, không hiển thị trong console)
# window.show()
# sys.exit(app.exec_())