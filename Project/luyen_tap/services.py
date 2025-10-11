# services.py
from typing import List
from models import KeyResult, KPI, ProgressLog, EntityType
from data_sources import fetch_data_from_source

# Bộ nhớ tạm (thay thế DB trong prototype)
PROGRESS_LOGS: List[ProgressLog] = []

def update_key_result(kr: KeyResult) -> bool:
    if kr.data_source_type != "manual":
        try:
            new_value = fetch_data_from_source(kr.data_source_config)
            kr.current_value = new_value
            PROGRESS_LOGS.append(ProgressLog(EntityType.KEY_RESULT, kr.key_result_id, new_value))
            return True
        except Exception as e:
            print(f"[ERROR] Cập nhật KR {kr.key_result_id} thất bại: {e}")
    return False

def update_kpi(kpi: KPI) -> bool:
    if kpi.data_source_type != "manual":
        try:
            new_value = fetch_data_from_source(kpi.data_source_config)
            kpi.current_value = new_value
            PROGRESS_LOGS.append(ProgressLog(EntityType.KPI, kpi.kpi_id, new_value))
            return True
        except Exception as e:
            print(f"[ERROR] Cập nhật KPI {kpi.kpi_id} thất bại: {e}")
    return False

def calculate_completion(value: float, target: float) -> float:
    return min(100.0, (value / target) * 100) if target > 0 else 0.0