# 📜 PYTHON TYPING CHEAT SHEET – Full Reference (Python 3.9+)
# Tác giả: Windy | Dành cho: Tien Thien
# Dành cho lập trình viên Python hiện đại – dùng trong tài chính, AI, hệ thống module, v.v.

from __future__ import annotations  # Hỗ trợ forward reference tốt hơn (Python <3.10)

import sys
from typing import (
    Any,
    Union,
    Optional,
    List,
    Dict,
    Tuple,
    Set,
    Callable,
    Type,
    TypeVar,
    Generic,
    Literal,
    Final,
    Protocol,
    runtime_checkable,
    overload,
    Iterator,
    Iterable,
    NamedTuple,
    TypedDict,
    NoReturn,
    ClassVar,
)

# Từ Python 3.9+, có thể dùng built-in types thay typing.List → List[int] thay vì typing.List[int]
if sys.version_info >= (3, 9):
    # Built-in generic types: list, dict, tuple, set, frozenset, type
    pass


# ======================================================================
# 1. CƠ BẢN: BIẾN, HÀM, LỚP CÓ KIỂU
# ======================================================================
name: str = "Windy"
age: int = 18
height: float = 1.75
is_student: bool = True
nothing: None = None


def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b


class User:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


# ======================================================================
# 2. CÁC KIỂU DỮ LIỆU TẬP HỢP (CONTAINERS)
# ======================================================================

# Danh sách
numbers: List[int] = [1, 2, 3]
# Hoặc từ Python 3.9+
numbers_v2: list[int] = [1, 2, 3]

# Từ điển
user_map: Dict[str, User] = {"alice": User("Alice", 25)}
user_map_v2: dict[str, User] = {"bob": User("Bob", 30)}

# Tuple – có thứ tự & độ dài cố định
coordinates: Tuple[float, float] = (1.0, 2.5)
# Tuple với nhiều kiểu
person_info: Tuple[str, int, bool] = ("Tien", 19, True)
# Tuple độ dài không xác định (nhưng cùng kiểu)
ints: Tuple[int, ...] = (1, 2, 3, 4)

# Tập hợp
unique_ids: Set[int] = {101, 102, 103}
unique_ids_v2: set[int] = {201, 202}


# ======================================================================
# 3. OPTIONAL & UNION – GIÁ TRỊ CÓ THỂ LÀ NHIỀU KIỂU
# ======================================================================

# Optional[T] = Union[T, None]
nickname: Optional[str] = None  # hoặc có thể là str

# Union – nhiều kiểu hợp lệ
def process_id(user_id: Union[int, str]) -> str:
    return f"ID: {user_id}"

# Từ Python 3.10+, có thể viết: user_id: int | str


# ======================================================================
# 4. HÀM & CALLBACKS (CALLABLE)
# ======================================================================

# Callable[[tham_số], kết_quả]
def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

result = apply(add, 5, 3)  # OK

# Hàm không tham số, trả về str
get_name: Callable[[], str] = lambda: "Anonymous"


# ======================================================================
# 5. KIỂU LỚP (CLASS ITSELF – KHÔNG PHẢI INSTANCE)
# ======================================================================

def create_user(cls: Type[User], name: str, age: int) -> User:
    return cls(name, age)

new_user = create_user(User, "Hai", 22)


# ======================================================================
# 6. GENERIC & TYPE VARIABLES – VIẾT CODE TÁI SỬ DỤNG
# ======================================================================

T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

first_int = first([1, 2, 3])      # → int
first_str = first(['a', 'b'])    # → str

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(10)


# ======================================================================
# 7. LITERAL TYPES – GIÁ TRỊ CỤ THỂ
# ======================================================================

Mode = Literal["light", "dark", "auto"]

def set_theme(mode: Mode) -> None:
    print(f"Theme set to: {mode}")

set_theme("dark")   # OK
# set_theme("red")  # ❌ Mypy cảnh báo


# ======================================================================
# 8. FINAL – BIẾN/LỚP/PHƯƠNG THỨC KHÔNG THỂ GHI ĐÈ
# ======================================================================

API_VERSION: Final[str] = "v1.0"

class MathUtils:
    @staticmethod
    def pi() -> float:
        return 3.14159


# ======================================================================
# 9. NAMEDTUPLE – TUPLE CÓ TÊN TRƯỜNG
# ======================================================================

# Cách 1: Dùng typing.NamedTuple
class PersonTuple(NamedTuple):
    name: str
    age: int

p1 = PersonTuple("Lan", 20)

# Cách 2: Dùng collections.namedtuple (không có typing)
# → không khuyến khích nếu cần type safety


# ======================================================================
# 10. TYPEDDICT – TỪ ĐIỂN CÓ CẤU TRÚC CỐ ĐỊNH
# ======================================================================

class UserSchema(TypedDict):
    id: int
    name: str
    active: bool

user_data: UserSchema = {"id": 1, "name": "Minh", "active": True}
# Thiếu key hoặc sai kiểu → mypy báo lỗi


# ======================================================================
# 11. PROTOCOL – DUCK TYPING CÓ KIỂU (STRUCTURAL SUBTYPING)
# ======================================================================

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

def render(obj: Drawable) -> None:
    obj.draw()

render(Circle())  # OK dù Circle không kế thừa Drawable


# ======================================================================
# 12. OVERLOAD – NHIỀU CHỮ KÝ HÀM
# ======================================================================

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...
@overload
def double(x: float) -> float: ...

def double(x):
    return x * 2

# mypy hiểu rằng double(5) → int, double("hi") → str


# ======================================================================
# 13. SPECIAL TYPES
# ======================================================================

# Any – tắt type checking (dùng cẩn thận!)
unsafe: Any = "anything"
print(unsafe.upper())  # mypy không kiểm tra

# NoReturn – hàm không bao giờ return bình thường (chỉ raise hoặc exit)
def halt() -> NoReturn:
    raise RuntimeError("System halt!")

# ClassVar – biến lớp (không phải instance)
class AppConfig:
    debug: ClassVar[bool] = True
    name: str = "app"


# ======================================================================
# 14. ITERATORS & GENERATORS
# ======================================================================

def count_up_to(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1

for x in count_up_to(3):
    print(x)  # 0, 1, 2


# ======================================================================
# 15. DEMO TÍCH HỢP VỚI DATACLASS & OOP (PHÙ HỢP DỰ ÁN CỦA BẠN)
# ======================================================================

from dataclasses import dataclass

@dataclass
class FinancialGoal:
    name: str
    target_amount: float
    current_amount: float
    deadline: str  # YYYY-MM-DD
    category: Literal["saving", "debt", "investment"]

    def progress(self) -> float:
        return min(100.0, (self.current_amount / self.target_amount) * 100)

goals: List[FinancialGoal] = [
    FinancialGoal("Emergency Fund", 10_000_000, 3_000_000, "2026-12-31", "saving")
]


# ======================================================================
# 16. CHẠY DEMO NHANH
# ======================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 PYTHON TYPING CHEAT SHEET – RUNNING DEMO")
    print("=" * 60)

    print(greet("Tien"))
    print(f"Add: {add(2, 3)}")
    print(f"First item: {first(['a', 'b'])}")
    print(f"Theme: {set_theme('dark') or 'done'}")
    print(f"TypedDict user: {user_data}")
    print(f"Financial goal progress: {goals[0].progress():.1f}%")

    print("\n✅ Typing Cheat Sheet completed!")
    print("💡 Gợi ý: Dùng `mypy your_file.py` để kiểm tra kiểu!")