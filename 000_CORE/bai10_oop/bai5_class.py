# hr_system.py
from __future__ import annotations
import json
import logging
from typing import Optional, List, Dict, Any, Callable
from contextlib import contextmanager
from dataclasses import dataclass, field
import time

# ----------------------------
# 1. CÁC HẰNG SỐ & CẤU HÌNH
# ----------------------------

# 🔐 Phân quyền dùng BITWISE (như bạn đã học)
READ: int = 0b100   # 4
WRITE: int = 0b010  # 2
EXEC: int = 0b001   # 1

# 🧮 Key mã hóa lương (minh họa XOR)
SALARY_ENCRYPTION_KEY: int = 0xAF  # 175 (hex)

# 📁 File lưu trữ
DATA_FILE: str = "employees.json"

# ----------------------------
# 2. CUSTOM EXCEPTIONS
# ----------------------------

class PermissionError(Exception):
    """Không đủ quyền truy cập"""
    pass

class EmployeeNotFoundError(Exception):
    """Không tìm thấy nhân viên"""
    pass

# ----------------------------
# 3. CONTEXT MANAGER: GHI LOG THỜI GIAN
# ----------------------------

@contextmanager
def log_operation(operation_name: str):
    """Ghi log thời gian thực hiện thao tác"""
    start = time.time()
    logging.info(f"Bắt đầu: {operation_name}")
    try:
        yield
    except Exception as e:
        logging.error(f"Lỗi trong {operation_name}: {e}")
        raise
    finally:
        duration = time.time() - start
        logging.info(f"Kết thúc: {operation_name} (mất {duration:.4f}s)")

# ----------------------------
# 4. DECORATOR: KIỂM TRA QUYỀN
# ----------------------------

def require_permission(required_perm: int) -> Callable:
    """Decorator kiểm tra quyền trước khi thực hiện hành động"""
    def decorator(func: Callable) -> Callable:
        def wrapper(self: 'HRSystem', *args, **kwargs):
            if not (self.current_user.permission & required_perm):
                raise PermissionError(
                    f"User '{self.current_user.name}' thiếu quyền: {bin(required_perm)}"
                )
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

# ----------------------------
# 5. DATA CLASS: NHÂN VIÊN
# ----------------------------

@dataclass
class Employee:
    id: int
    name: str
    department: str
    # 💰 Lương được lưu dưới dạng đã mã hóa (int)
    _encrypted_salary: int = field(repr=False)

    @property
    def salary(self) -> int:
        """Giải mã lương khi truy cập"""
        return self._encrypted_salary ^ SALARY_ENCRYPTION_KEY

    @salary.setter
    def salary(self, value: int) -> None:
        if value < 0:
            raise ValueError("Lương không thể âm")
        self._encrypted_salary = value ^ SALARY_ENCRYPTION_KEY

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "encrypted_salary": self._encrypted_salary
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Employee":
        return cls(
            id=data["id"],
            name=data["name"],
            department=data["department"],
            _encrypted_salary=data["encrypted_salary"]
        )

# ----------------------------
# 6. LỚP HỆ THỐNG NHÂN SỰ
# ----------------------------

class HRSystem:
    def __init__(self, current_user_permission: int = READ | WRITE | EXEC):
        # ❌ BẪY: đừng dùng mutable default! Dùng None rồi gán trong __init__
        self.employees: List[Employee] = []
        self.current_user = type('User', (), {'name': 'admin', 'permission': current_user_permission})()
        self._load_data()

    def _load_data(self) -> None:
        """Tải dữ liệu từ file (an toàn với encoding)"""
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]
        except FileNotFoundError:
            self.employees = []
            logging.warning("File dữ liệu chưa tồn tại, khởi tạo trống.")

    def _save_data(self) -> None:
        """Lưu dữ liệu vào file (UTF-8)"""
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([emp.to_dict() for emp in self.employees], f, indent=2, ensure_ascii=False)

    @require_permission(WRITE)
    def add_employee(self, name: str, department: str, salary: int) -> None:
        with log_operation(f"Thêm nhân viên: {name}"):
            new_id = max((e.id for e in self.employees), default=0) + 1
            emp = Employee(id=new_id, name=name, department=department, _encrypted_salary=0)
            emp.salary = salary  # trigger setter để mã hóa
            self.employees.append(emp)
            self._save_data()

    @require_permission(READ)
    def get_employee(self, emp_id: int) -> Employee:
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        raise EmployeeNotFoundError(f"Không tìm thấy nhân viên ID: {emp_id}")

    @require_permission(WRITE)
    def update_salary(self, emp_id: int, new_salary: int) -> None:
        emp = self.get_employee(emp_id)
        emp.salary = new_salary
        self._save_data()

    @require_permission(EXEC)
    def run_payroll(self) -> int:
        """Tính tổng lương (minh họa EXEC permission)"""
        total = sum(emp.salary for emp in self.employees)
        logging.info(f"Tổng lương: {total:,} VND")
        return total

    def list_departments(self) -> List[str]:
        """Dùng set comprehension + frozenset nếu cần hashable"""
        return list({emp.department for emp in self.employees})

# ----------------------------
# 7. DEMO & TEST (tránh bẫy vòng lặp, mutable default, v.v.)
# ----------------------------

def demo() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("🚀 Khởi tạo hệ thống HR...")
    hr = HRSystem(current_user_permission=READ | WRITE | EXEC)

    # Thêm nhân viên (tránh lỗi dùng list + trong loop)
    employees_data = [
        ("Alice", "Engineering", 25_000_000),
        ("Bob", "Marketing", 18_000_000),
        ("Charlie", "Engineering", 30_000_000),
    ]

    for name, dept, sal in employees_data:
        hr.add_employee(name, dept, sal)

    # Kiểm tra phân quyền
    try:
        readonly_hr = HRSystem(current_user_permission=READ)
        readonly_hr.add_employee("Eve", "HR", 20_000_000)  # ❌ Sẽ raise PermissionError
    except PermissionError as e:
        print(f"✅ Bắt lỗi phân quyền: {e}")

    # In lương (đã giải mã)
    alice = hr.get_employee(1)
    print(f"\n👤 {alice.name} - Lương: {alice.salary:,} VND")

    # Chạy payroll
    total = hr.run_payroll()
    print(f"\n💰 Tổng lương công ty: {total:,} VND")

    # Kiểm tra departments (dùng set → không trùng)
    print(f"\n🏢 Các phòng ban: {hr.list_departments()}")

    # 🔍 Minh họa lỗi thường gặp (và cách tránh)
    print("\n--- Minh họa các bẫy Python ---")
    
    # Bẫy 1: Mutable default
    def bad_func(items=[]):  # ❌
        items.append("bad")
        return items

    def good_func(items=None):  # ✅
        if items is None:
            items = []
        items.append("good")
        return items

    print("Mutable default trap:", bad_func(), bad_func())  # ['bad', 'bad']
    print("Fixed version:", good_func(), good_func())       # ['good'], ['good']

    # Bẫy 2: Bitwise vs logic
    x = 5
    print(f"5 & 3 == 1 → {(5 & 3) == 1}")  # True (phải có ngoặc!)
    print(f"5 & (3 == 1) → {5 & (3 == 1)}")  # False (3==1 → False → 0)

    # Bẫy 3: XOR mã hóa
    msg = "Salary: 30M"
    key = 0x12
    encoded = [ord(c) ^ key for c in msg]
    decoded = ''.join(chr(b ^ key) for b in encoded)
    print(f"\n🔐 XOR demo: '{msg}' → {decoded}")

if __name__ == "__main__":
    demo()


    # function tool
    # @overload, @lru_cache, @cached_property, @wraps

    #@contextManager -> yield
    #@decorator define