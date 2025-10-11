# main.py
from datetime import datetime, timedelta
from models import User, Objective, KeyResult, KPI, OwnerType, DataSourceType
from services import update_key_result, update_kpi, calculate_completion, PROGRESS_LOGS

def print_dashboard(objectives, key_results, kpis):
    print("\n" + "="*60)
    print("📊 DASHBOARD HIỆU SUẤT NHÂN VIÊN (OKR/KPI)")
    print("="*60)

    for obj in objectives:
        print(f"\n🎯 MỤC TIÊU: {obj.title}")
        relevant_krs = [kr for kr in key_results if kr.objective_id == obj.objective_id]
        for kr in relevant_krs:
            comp = calculate_completion(kr.current_value, kr.target_value)
            status = "✅ Đạt" if comp >= 100 else "⚠️ Đang tiến hành"
            print(f"  - KR: {kr.title}")
            print(f"    Giá trị: {kr.current_value:.1f}/{kr.target_value} → {comp:.1f}% ({status})")

    print("\n📈 KPI CÁ NHÂN:")
    for kpi in kpis:
        comp = calculate_completion(kpi.current_value, kpi.target_value)
        print(f"  - {kpi.name}: {kpi.current_value:.1f}/{kpi.target_value} → {comp:.1f}%")

    print(f"\n📝 Đã ghi {len(PROGRESS_LOGS)} bản ghi tiến độ.")

def main():
    print("🚀 Khởi động Hệ thống Quản lý Hiệu suất (OKR/KPI Tự động)...")

    # === 1. Tạo dữ liệu mẫu ===
    user = User(user_id=1, full_name="Nguyễn Văn A", department_id=101)

    obj = Objective(
        objective_id=1,
        title="Tăng doanh thu quý II",
        owner_type=OwnerType.USER,
        owner_id=user.user_id,
        period_start=datetime(2025, 4, 1),
        period_end=datetime(2025, 6, 30)
    )

    kr1 = KeyResult(
        key_result_id=1,
        objective_id=obj.objective_id,
        title="Doanh thu đạt $100,000",
        target_value=100000,
        data_source_type=DataSourceType.API,
        data_source_config={"source": "sales", "field": "total_sales"}
    )

    kpi1 = KPI(
        kpi_id=1,
        name="Tỷ lệ chuyển đổi lead",
        target_value=50,
        data_source_type=DataSourceType.API,
        data_source_config={"source": "sales", "field": "leads_converted"},
        owner_id=user.user_id
    )

    objectives = [obj]
    key_results = [kr1]
    kpis = [kpi1]

    # === 2. Tự động cập nhật dữ liệu ===
    print("\n🔄 Đang tự động đồng bộ dữ liệu từ hệ thống...")
    update_key_result(kr1)
    update_kpi(kpi1)

    # === 3. Hiển thị dashboard ===
    print_dashboard(objectives, key_results, kpis)

    print("\n✅ Hệ thống đã sẵn sàng! (Chạy định kỳ để cập nhật tự động)")

if __name__ == "__main__":
    main()