| Thuộc tính                   | Mô tả                                  | Ví dụ                                                                 |
| ---------------------------- | -------------------------------------- | --------------------------------------------------------------------- |
| `x`, `y`                     | Tọa độ của widget so với cha           | `widget.x()`                                                          |
| `width`, `height`            | Kích thước widget                      | `widget.width()`                                                      |
| `geometry`                   | Vị trí và kích thước (`QRect`)         | `widget.geometry()`                                                   |
| `sizePolicy`                 | Cách widget thay đổi kích thước        | `widget.sizePolicy()`                                                 |
| `minimumSize`, `maximumSize` | Giới hạn kích thước                    | `widget.setMinimumSize(100, 100)`                                     |
| `enabled`                    | Có thể tương tác hay không             | `widget.setEnabled(False)`                                            |
| `visible`                    | Có hiển thị hay không                  | `widget.setVisible(True)`                                             |
| `windowTitle`                | Tiêu đề cửa sổ (nếu là cửa sổ độc lập) | `widget.setWindowTitle("Hello")`                                      |
| `windowIcon`                 | Icon của cửa sổ                        | `widget.setWindowIcon(QIcon("icon.png"))`                             |
| `styleSheet`                 | CSS cho widget                         | `widget.setStyleSheet("background-color: red;")`                      |
| `cursor`                     | Con trỏ chuột khi hover                | `widget.setCursor(Qt.CursorShape.PointingHandCursor)`                 |
| `toolTip`                    | Gợi ý khi hover                        | `widget.setToolTip("Nhấn để tiếp tục")`                               |
| `statusTip`                  | Gợi ý trên status bar                  | `widget.setStatusTip("Sẵn sàng")`                                     |
| `whatsThis`                  | Gợi ý dạng trợ giúp                    | `widget.setWhatsThis("Đây là nút bấm")`                               |
| `focusPolicy`                | Cách widget nhận focus                 | `widget.setFocusPolicy(Qt.FocusPolicy.TabFocus)`                      |
| `contextMenuPolicy`          | Cách hiển thị menu chuột phải          | `widget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)` |


---
| Phương thức                   | Mô tả                             | Ví dụ                                                          |
| ----------------------------- | --------------------------------- | -------------------------------------------------------------- |
| `move(x, y)`                  | Di chuyển widget                  | `widget.move(50, 50)`                                          |
| `resize(width, height)`       | Thay đổi kích thước               | `widget.resize(200, 100)`                                      |
| `setGeometry(x, y, w, h)`     | Thiết lập cả vị trí và kích thước | `widget.setGeometry(10, 10, 300, 200)`                         |
| `setFixedSize(w, h)`          | Cố định kích thước                | `widget.setFixedSize(300, 200)`                                |
| `setFixedWidth(w)`            | Cố định chiều rộng                | `widget.setFixedWidth(300)`                                    |
| `setFixedHeight(h)`           | Cố định chiều cao                 | `widget.setFixedHeight(100)`                                   |
| `show()`                      | Hiển thị widget                   | `widget.show()`                                                |
| `hide()`                      | Ẩn widget                         | `widget.hide()`                                                |
| `close()`                     | Đóng widget                       | `widget.close()`                                               |
| `raise_()`                    | Đưa widget lên trên cùng          | `widget.raise_()`                                              |
| `lower()`                     | Đưa widget xuống dưới cùng        | `widget.lower()`                                               |
| `setLayout(layout)`           | Gán layout cho widget             | `widget.setLayout(QVBoxLayout())`                              |
| `update()`                    | Yêu cầu vẽ lại widget             | `widget.update()`                                              |
| `repaint()`                   | Vẽ lại ngay lập tức               | `widget.repaint()`                                             |
| `setParent(parent)`           | Thiết lập widget cha              | `widget.setParent(parent_widget)`                              |
| `parentWidget()`              | Lấy widget cha                    | `widget.parentWidget()`                                        |
| `window()`                    | Lấy cửa sổ chứa widget            | `widget.window()`                                              |
| `isWindow()`                  | Kiểm tra có phải cửa sổ độc lập   | `widget.isWindow()`                                            |
| `setWindowModality(mode)`     | Thiết lập kiểu modal              | `widget.setWindowModality(Qt.WindowModality.ApplicationModal)` |
| `setWindowFlags(flags)`       | Thiết lập cờ cửa sổ               | `widget.setWindowFlags(Qt.WindowType.FramelessWindowHint)`     |
| `setAttribute(attr, on=True)` | Thiết lập thuộc tính Qt           | `widget.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)`     |
| `testAttribute(attr)`         | Kiểm tra thuộc tính               | `widget.testAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)`    |
---
### signal 
| Tín hiệu                          | Mô tả                               |
| --------------------------------- | ----------------------------------- |
| `windowTitleChanged(title)`       | Phát khi tiêu đề thay đổi           |
| `windowIconChanged(icon)`         | Phát khi icon thay đổi              |
| `customContextMenuRequested(pos)` | Phát khi yêu cầu menu chuột phải    |
| `destroyed()`                     | Phát khi widget bị hủy              |
| `destroyed(QObject*)`             | Phát khi widget bị hủy (có tham số) |
---
### 🧩 Các thuộc tính setAttribute phổ biến
| Thuộc tính                 | Mô tả                       |
| -------------------------- | --------------------------- |
| `WA_DeleteOnClose`         | Tự động xóa widget khi đóng |
| `WA_TranslucentBackground` | Cho phép nền trong suốt     |
| `WA_NoSystemBackground`    | Không vẽ nền hệ thống       |
| `WA_WindowModal`           | Modal cho cửa sổ cha        |
| `WA_ShowModal`             | Modal toàn bộ ứng dụng      |
