# train_skill_bot.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.metrics import classification_report, accuracy_score
import joblib

# ----------------------------
# Chuẩn hóa hiệu ứng để tránh "unknown class"
# ----------------------------
def normalize_effects(effects):
    """Chuẩn hóa các hiệu ứng thành nhóm chung để tăng khả năng tổng quát"""
    mapping = {
        "slow_10%": "slow",
        "slow_20%": "slow",
        "slow_30%": "slow",
        "slow_50%": "slow",
        "crit_chance_20%": "crit",
        "crit_chance_30%": "crit",
        "attack_speed_15%": "attack_speed",
        "attack_speed_20%": "attack_speed",
        "freeze": "stun",      # freeze → stun
        "knockback": "displace",
        "taunt": "taunt",
        "shield": "shield",
        "heal": "heal",
        "dot": "dot",
        "bleed": "dot",
        "pierce": "pierce",
        "dash": "mobility",
        "remove_debuff": "cleanse"
    }
    return [mapping.get(eff, eff) for eff in effects]

# ----------------------------
# 1. Tạo dataset mẫu
# ----------------------------
def create_sample_dataset():
    raw_data = [
        {"character_name": "Linh Hỏa", "role": "assassin", "skill_name": "Đòn Chớp Nhoáng", "skill_type": "active", "damage_type": "physical", "cooldown": 8, "mana_cost": 50, "range": 300, "is_targeted": True, "is_aoe": False, "effects": ["dash", "crit_chance_20%"], "damage": 120},
        {"character_name": "Linh Hỏa", "role": "assassin", "skill_name": "Lửa Tàn", "skill_type": "passive", "damage_type": "magic", "cooldown": 0, "mana_cost": 0, "range": 0, "is_targeted": False, "is_aoe": True, "effects": ["dot", "slow_10%"], "damage": 15},
        {"character_name": "Thạch Thủ", "role": "tank", "skill_name": "Tường Đá", "skill_type": "active", "damage_type": "none", "cooldown": 12, "mana_cost": 70, "range": 0, "is_targeted": False, "is_aoe": True, "effects": ["shield", "taunt"], "damage": 0},
        {"character_name": "Thạch Thủ", "role": "tank", "skill_name": "Địa Chấn", "skill_type": "ultimate", "damage_type": "magic", "cooldown": 90, "mana_cost": 100, "range": 600, "is_targeted": False, "is_aoe": True, "effects": ["stun", "knockback"], "damage": 200},
        {"character_name": "Linh Dược Sư", "role": "support", "skill_name": "Hồi Sinh Thảo", "skill_type": "active", "damage_type": "none", "cooldown": 10, "mana_cost": 60, "range": 800, "is_targeted": True, "is_aoe": False, "effects": ["heal", "remove_debuff"], "damage": 0},
        {"character_name": "Băng Vương", "role": "mage", "skill_name": "Bão Băng", "skill_type": "ultimate", "damage_type": "magic", "cooldown": 100, "mana_cost": 120, "range": 700, "is_targeted": False, "is_aoe": True, "effects": ["slow_50%", "freeze"], "damage": 250},
        {"character_name": "Băng Vương", "role": "mage", "skill_name": "Mũi Tên Băng", "skill_type": "active", "damage_type": "magic", "cooldown": 6, "mana_cost": 40, "range": 900, "is_targeted": True, "is_aoe": False, "effects": ["slow_20%"], "damage": 80},
        {"character_name": "Cuồng Cung Thủ", "role": "marksman", "skill_name": "Mưa Tên", "skill_type": "ultimate", "damage_type": "physical", "cooldown": 80, "mana_cost": 90, "range": 1000, "is_targeted": False, "is_aoe": True, "effects": ["pierce"], "damage": 180},
        {"character_name": "Cuồng Cung Thủ", "role": "marksman", "skill_name": "Tăng Tốc", "skill_type": "passive", "damage_type": "none", "cooldown": 0, "mana_cost": 0, "range": 0, "is_targeted": False, "is_aoe": False, "effects": ["attack_speed_15%"], "damage": 0},
        {"character_name": "Kiếm Sư", "role": "fighter", "skill_name": "Chém Xoáy", "skill_type": "active", "damage_type": "physical", "cooldown": 7, "mana_cost": 45, "range": 200, "is_targeted": False, "is_aoe": True, "effects": ["bleed"], "damage": 100},
        {"character_name": "Thánh Kỵ Sĩ", "role": "tank", "skill_name": "Thánh Quang", "skill_type": "passive", "damage_type": "none", "cooldown": 0, "mana_cost": 0, "range": 0, "is_targeted": False, "is_aoe": False, "effects": ["heal"], "damage": 0},
        {"character_name": "Ám Sát Giả", "role": "assassin", "skill_name": "Tàng Hình", "skill_type": "ultimate", "damage_type": "none", "cooldown": 120, "mana_cost": 80, "range": 0, "is_targeted": False, "is_aoe": False, "effects": ["mobility"], "damage": 0},
    ]
    df = pd.DataFrame(raw_data)
    df['effects'] = df['effects'].apply(normalize_effects)
    return df

# ----------------------------
# 2. Tiền xử lý dữ liệu
# ----------------------------
def preprocess_data(df):
    df = df.copy()
    le_damage_type = LabelEncoder()
    df['damage_type_encoded'] = le_damage_type.fit_transform(df['damage_type'])
    df['is_targeted'] = df['is_targeted'].astype(int)
    df['is_aoe'] = df['is_aoe'].astype(int)

    mlb = MultiLabelBinarizer()
    effects_encoded = mlb.fit_transform(df['effects'])
    effects_df = pd.DataFrame(effects_encoded, columns=[f"effect_{col}" for col in mlb.classes_])

    df = pd.concat([df.reset_index(drop=True), effects_df.reset_index(drop=True)], axis=1)

    encoders = {
        'damage_type': le_damage_type,
        'effects_mlb': mlb
    }
    return df, encoders

# ----------------------------
# 3. Huấn luyện mô hình (trên toàn bộ dữ liệu)
# ----------------------------
def train_model(df):
    feature_cols = [
        'cooldown', 'mana_cost', 'range', 'is_targeted', 'is_aoe',
        'damage', 'damage_type_encoded'
    ]
    effect_cols = [col for col in df.columns if col.startswith('effect_')]
    feature_cols += effect_cols

    X = df[feature_cols]
    y = df['skill_type']

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Đánh giá trên toàn bộ dữ liệu
    y_pred = model.predict(X)
    print("✅ Độ chính xác (trên toàn bộ dữ liệu):", accuracy_score(y, y_pred))
    print("\n📋 Báo cáo phân loại:")
    print(classification_report(y, y_pred))

    return model, feature_cols

# ----------------------------
# 4. Lưu mô hình
# ----------------------------
def save_model(model, feature_cols, encoders, model_path="skill_bot_model.pkl"):
    joblib.dump({
        'model': model,
        'feature_cols': feature_cols,
        'encoders': encoders
    }, model_path)
    print(f"💾 Mô hình đã được lưu tại: {model_path}")

# ----------------------------
# 5. Dự đoán kỹ năng mới
# ----------------------------
def predict_skill_type(skill_data, model_path="skill_bot_model.pkl"):
    skill_data = skill_data.copy()
    # 🔑 Chuẩn hóa effects trước khi dự đoán
    skill_data['effects'] = normalize_effects(skill_data['effects'])

    data = joblib.load(model_path)
    model = data['model']
    feature_cols = data['feature_cols']
    encoders = data['encoders']

    df = pd.DataFrame([skill_data])
    le = encoders['damage_type']
    df['damage_type_encoded'] = le.transform(df['damage_type'])

    df['is_targeted'] = int(df['is_targeted'].iloc[0])
    df['is_aoe'] = int(df['is_aoe'].iloc[0])

    mlb = encoders['effects_mlb']
    effects_encoded = mlb.transform(df['effects'])
    effects_df = pd.DataFrame(effects_encoded, columns=[f"effect_{col}" for col in mlb.classes_])
    df = pd.concat([df, effects_df], axis=1)

    # Đảm bảo thứ tự và đầy đủ cột
    X = pd.DataFrame(columns=feature_cols)
    for col in feature_cols:
        X[col] = [df[col].iloc[0] if col in df.columns else 0]

    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0]
    confidence = float(max(proba))
    return pred, confidence

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    print("🤖 Đang tạo dataset mẫu...")
    df = create_sample_dataset()

    print("🧹 Đang tiền xử lý dữ liệu...")
    df_processed, encoders = preprocess_data(df)

    print("🧠 Đang huấn luyện mô hình...")
    model, feature_cols = train_model(df_processed)

    print("💾 Đang lưu mô hình...")
    save_model(model, feature_cols, encoders)

    print("\n🔍 Thử dự đoán với kỹ năng mới:")
    test_skill = {
        'damage_type': 'magic',
        'cooldown': 5,
        'mana_cost': 45,
        'range': 600,
        'is_targeted': False,
        'is_aoe': True,
        'effects': ['slow_30%'],  # ← sẽ được chuẩn hóa thành 'slow'
        'damage': 100
    }
    pred, conf = predict_skill_type(test_skill)
    print(f"➡️  Dự đoán: '{pred}' (độ tin cậy: {conf:.2f})")