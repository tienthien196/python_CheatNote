# config.py
DEBUG = False

# main.py
# import config
# config.DEBUG = False  # ✅ OK

# Nhưng nếu bạn làm:
from config import DEBUG
# DEBUG = False  # ❌ Chỉ gán local trong main.py, không đổi config.DEBUG!
# Đây là bẫy "import by value vs by reference" — thực chất là rebinding name. 
print(DEBUG)
# Module object
# Utils extendsion
# namespace >>Built-in >>Global (module-level) >>Local (function-level) >>Enclosing (closure)
# Dùng import module cho cấu hình, trạng thái, cần tính rõ ràng thì dùng object thay from, tránh xuung đột với namespace
# Dùng from module import func cho hàm/hằng chỉ đọc, dùng trực tiếp  ,
# import bn.tt
from bn import tt as i

i.tt()