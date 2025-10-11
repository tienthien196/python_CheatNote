# data_sources.py
import random
from datetime import datetime

# Giả lập dữ liệu từ CRM, ERP, v.v.
SALES_DATA = {
    "total_sales": 85000,  # USD
    "leads_converted": 42,
    "support_tickets_resolved": 120
}

def fetch_data_from_source(config: dict) -> float:
    """
    Giả lập lấy dữ liệu từ API/DB dựa trên config.
    Ví dụ config: {"source": "sales", "field": "total_sales"}
    """
    source = config.get("source")
    field = config.get("field")

    if source == "sales" and field in SALES_DATA:
        # Thêm nhiễu ngẫu nhiên để mô phỏng thay đổi theo thời gian
        base = SALES_DATA[field]
        return base * random.uniform(0.9, 1.1)
    return 0.0