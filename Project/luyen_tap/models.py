# models.py
from dataclasses import dataclass, field
from typing import Optional, Dict, Any
from datetime import datetime
from enum import Enum

class OwnerType(str, Enum):
    COMPANY = "company"
    DEPARTMENT = "department"
    USER = "user"

class DataSourceType(str, Enum):
    MANUAL = "manual"
    API = "api"
    DATABASE = "database"

class EntityType(str, Enum):
    KEY_RESULT = "key_result"
    KPI = "kpi"

@dataclass
class User:
    user_id: int
    full_name: str
    department_id: int

@dataclass
class Objective:
    objective_id: int
    title: str
    owner_type: OwnerType
    owner_id: int
    period_start: datetime
    period_end: datetime

@dataclass
class KeyResult:
    key_result_id: int
    objective_id: int
    title: str
    target_value: float
    current_value: float = 0.0
    data_source_type: DataSourceType = DataSourceType.MANUAL
    data_source_config: Dict[str, Any] = field(default_factory=dict)

@dataclass
class KPI:
    kpi_id: int
    name: str
    target_value: float
    current_value: float = 0.0
    data_source_type: DataSourceType = DataSourceType.MANUAL
    data_source_config: Dict[str, Any] = field(default_factory=dict)
    owner_type: OwnerType = OwnerType.USER
    owner_id: int = 0

@dataclass
class ProgressLog:
    entity_type: EntityType
    entity_id: int
    value: float
    recorded_at: datetime = field(default_factory=datetime.utcnow)