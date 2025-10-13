`python `
### 1.  Data type >> int >> float >> complex
-  underscope 
-  type aunotation 
-  Floating-point 
-  float exponent 
-  ! compare with complex

### 2. Thứ tự ưu tiên toán tử c >> chuỗi toán tử >> bitwise
---
- Dấu ngoặc () luôn được tính đầu tiên → cứ nghi ngờ, thêm ngoặc!
- ** toán tử mũ sẽ thực thi từ phải qua trái 
- >--- CÒN LẠI TỪ PHẢI SANG TRÁI ---------
- Số học (*, /, //, %, +, -) → như toán phổ thông.
- Bitwise (<<, >>, &, ^, |) → nằm giữa số học và so sánh.
- So sánh (==, !=, <, <=,  in, is, is not , not in) 
- Logic (not → and → or) → ưu tiên thấp nhất (trừ gán).

---
- chuối gán : thay 1 ảnh hưởng 2
- chuỗi so sánh : true/false
- chuỗi logic : -> value
---
> <<, >>, &, ^, |

>CHÚ Ý QUẢN LÍ DẤU NGOẶC KHI DÙNG TOÁN TỬ  

### 3. Branch >> Loop >> Try-Except >> Function

- Loop : else trong for/while chỉ chạy nếu vòng lặp kết thúc bình thường chấp continue (không bị break, return , exception). 
- Except : 
    - else: chỉ chạy nếu không có exception
    - finally: luôn chạy, kể cả có return, break, continue
    - value Error popular
- ----🛡️ Nguyên tắc vàng để tránh ngoại lệ :----
```
    EAFP "Dễ xin tha thứ hơn là xin phép" → Dùng khi lỗi nguy hiểm ra try/except
    LBYL "Look Before You Leap" → Kiểm tra điều k
    Xác thực đầu vào -> Luôn kiểm tra đầu vào từ người dùng/tệp/mạng
    Dùng gợi ý kiểu + mypy -> Bắt lỗi ngay từ dev time
    Không bắt trốngexcept: -> Luôn có thể chỉ định cụ thể loại ngoại lệ

```
- Function : 
    - *args trước **kwargs
    - `global` with immutable type
    - multable default arg