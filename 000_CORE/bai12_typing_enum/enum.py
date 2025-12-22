# 📜 PYTHON ENUM CHEAT SHEET – Full Reference
# Tác giả: Windy | Dành cho: Tien Thien
# Dành cho ứng dụng tài chính, phân loại, trạng thái, theme, v.v.

from enum import (
    Enum,
    IntEnum,
    StrEnum,      # Python 3.11+
    Flag,
    IntFlag,
    auto,
    unique,
    EnumMeta
)
from typing import Union, Dict, Any
import json


# ======================================================================
# 1. ENUM CƠ BẢN – DÙNG KHI CẦN TẬP GIÁ TRỊ CỐ ĐỊNH
# ======================================================================

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)          # Color.RED
print(Color.RED.name)     # "RED"
print(Color.RED.value)    # 1
print(repr(Color.RED))    # <Color.RED: 1>


# ======================================================================
# 2. AUTO() – TỰ ĐỘNG GÁN GIÁ TRỊ
# ======================================================================

class Status(Enum):
    PENDING = auto()      # 1
    IN_PROGRESS = auto()  # 2
    COMPLETED = auto()    # 3
    FAILED = auto()       # 4

# Hoặc bắt đầu từ 0
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

# Mẹo: nếu muốn giá trị = thứ tự bắt đầu từ 0
class Weekday(Enum):
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = range(7)


# ======================================================================
# 3. INTENUM – SO SÁNH ĐƯỢC VỚI SỐ NGUYÊN
# ======================================================================

class HTTPStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_ERROR = 500

print(HTTPStatus.OK == 200)      # True
print(HTTPStatus.OK > 199)       # True


# ======================================================================
# 4. STRENUM – GIÁ TRỊ LÀ CHUỖI (Python 3.11+)
# ======================================================================
# Nếu bạn dùng Python <3.11, xem phần "Custom StrEnum" bên dưới

try:
    class Theme(StrEnum):  # Python 3.11+
        LIGHT = "light"
        DARK = "dark"
        AUTO = "auto"
except NameError:
    # Fallback cho Python <3.11
    class Theme(str, Enum):
        LIGHT = "light"
        DARK = "dark"
        AUTO = "auto"


print(Theme.DARK)               # Theme.DARK
print(str(Theme.DARK))          # "dark" ← rất quan trọng khi serialize
print(Theme.DARK == "dark")     # True (với StrEnum hoặc str+Enum)


# ======================================================================
# 5. ENUM TRONG DỰ ÁN TÀI CHÍNH – VÍ DỤ THỰC TẾ
# ======================================================================

class ExpenseCategory(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    EDUCATION = "education"
    ENTERTAINMENT = "entertainment"
    HEALTH = "health"
    SHOPPING = "shopping"
    OTHER = "other"

class GoalType(Enum):
    SAVING = "saving"
    DEBT_REPAYMENT = "debt"
    INVESTMENT = "investment"

class FinancialHealthLevel(Enum):
    CRITICAL = 1
    WARNING = 2
    STABLE = 3
    EXCELLENT = 4


# ======================================================================
# 6. CHUYỂN ĐỔI QUA LẠI GIỮA CHUỖI / SỐ VÀ ENUM
# ======================================================================

# Từ chuỗi → Enum
cat = ExpenseCategory("food")
print(cat)  # ExpenseCategory.FOOD

# Từ giá trị → Enum
status = Status(2)
print(status)  # Status.IN_PROGRESS

# Kiểm tra hợp lệ
def safe_parse_category(value: str) -> ExpenseCategory:
    try:
        return ExpenseCategory(value)
    except ValueError:
        return ExpenseCategory.OTHER


# ======================================================================
# 7. DUYỆT & DANH SÁCH TẤT CẢ GIÁ TRỊ
# ======================================================================

print(list(ExpenseCategory))  
# [ExpenseCategory.FOOD, ..., ExpenseCategory.OTHER]

print([c.value for c in Theme])
# ['light', 'dark', 'auto']

# Dùng trong UI dropdown
category_options = [(c.name, c.value) for c in ExpenseCategory]


# ======================================================================
# 8. ENUM + JSON – SERIALIZATION DỄ DÀNG
# ======================================================================

# Khi lưu vào JSON, thường chỉ cần .value
expense = {
    "amount": 50000,
    "category": ExpenseCategory.FOOD.value  # → "food"
}

# Khi load từ JSON
loaded_category = ExpenseCategory(expense["category"])

# Hoặc custom JSON encoder (nếu muốn serialize trực tiếp enum)
class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)

json_str = json.dumps(expense, cls=EnumEncoder)


# ======================================================================
# 9. UNIQUE – BẮT LỖI TRÙNG LẶP GIÁ TRỊ
# ======================================================================

@unique
class Role(Enum):
    ADMIN = 1
    MODERATOR = 2
    USER = 3
    # GUEST = 3  # ← Nếu bỏ comment → ValueError: duplicate values found


# ======================================================================
# 10. FLAG & INTFLAG – KẾT HỢP NHIỀU GIÁ TRỊ (BITWISE)
# ======================================================================

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

# Kết hợp quyền
user_perms = Permission.READ | Permission.WRITE

print(Permission.READ in user_perms)  # True
print(user_perms & Permission.EXECUTE == Permission(0))  # True (không có EXECUTE)

# IntFlag: có thể so sánh với số
class ColorFlag(IntFlag):
    RED = 1
    GREEN = 2
    BLUE = 4

cyan = ColorFlag.GREEN | ColorFlag.BLUE  # 6
print(cyan == 6)  # True


# ======================================================================
# 11. PHƯƠNG THỨC TRONG ENUM – THÊM HÀNH VI
# ======================================================================

class NotificationType(Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"

    def is_realtime(self) -> bool:
        return self in (NotificationType.SMS, NotificationType.PUSH)

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "NotificationType":
        return cls(config.get("type", "email"))

print(NotificationType.PUSH.is_realtime())  # True


# ======================================================================
# 12. SO SÁNH & HASH – AN TOÀN
# ======================================================================

# Enum là immutable → có thể dùng làm key trong dict
route_map = {
    ExpenseCategory.FOOD: "/expenses/food",
    ExpenseCategory.TRANSPORT: "/expenses/transport"
}

# So sánh identity (nhanh và an toàn)
if cat is ExpenseCategory.FOOD:
    print("It's food!")


# ======================================================================
# 13. INTEGRATION VỚI TYPING & DATACLASS (PHÙ HỢP DỰ ÁN CỦA BẠN)
# ======================================================================

from dataclasses import dataclass
from typing import List

@dataclass
class FinancialGoal:
    name: str
    goal_type: GoalType
    target_amount: float

goals: List[FinancialGoal] = [
    FinancialGoal("Mua laptop", GoalType.SAVING, 20_000_000),
    FinancialGoal("Trả nợ thẻ", GoalType.DEBT_REPAYMENT, 5_000_000)
]

# Kiểm tra kiểu với mypy: goal.goal_type là GoalType, không phải str!


# ======================================================================
# 14. DEMO TOÀN BỘ
# ======================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 PYTHON ENUM CHEAT SHEET – RUNNING DEMO")
    print("=" * 60)

    print(f"Color: {Color.RED}, value: {Color.RED.value}")
    print(f"Theme as str: {str(Theme.DARK)}")
    print(f"Category from string: {ExpenseCategory('transport')}")
    print(f"Financial goal type: {goals[0].goal_type}")
    print(f"Permissions: {user_perms}")
    print(f"Notification realtime? {NotificationType.SMS.is_realtime()}")

    # Serialize to JSON
    print(f"JSON expense: {json.dumps(expense)}")

    print("\n✅ Enum Cheat Sheet completed!")
    print("💡 Mẹo: Dùng Enum thay cho chuỗi/số trần để tránh lỗi typo!")