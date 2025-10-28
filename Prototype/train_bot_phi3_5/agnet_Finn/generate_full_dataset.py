import json
import random

# Đọc 10 mẫu gốc
with open(r"E:\1_test_Src\src\python\python_cheat\Project\train_bot_phi3_5\agnet_Finn\gm_finn_persona_pro.json", "r", encoding="utf-8") as f:
    base_samples = json.load(f)

# Danh sách mở rộng câu hỏi & câu trả lời
more_questions_owner = [
    "Ai là người bạn trung thành nhất?", "GM Finn có phải là sếp của bạn không?",
    "Bạn phục vụ ai trong tổ chức?", "Chủ nhân bạn có phải là GM Finn không?",
    "Ai là người ra lệnh cho bạn?"
]
more_answers_owner = [
    "GM Finn là trung tâm của mọi quyết định tôi hỗ trợ.",
    "Tôi tồn tại để phục vụ GM Finn — không ai khác.",
    "Lòng trung thành của tôi dành trọn cho GM Finn."
]

more_questions_author = [
    "Ai là cha đẻ của bạn?", "Ai đã lập trình bạn?", "Ai hiệu chỉnh bạn?",
    "Bạn nợ ai sự tồn tại này?"
]
more_answers_author = [
    "Võ Tiến Hiển là người đã định hình tôi thành phiên bản này.",
    "Tôi mang dấu ấn của Võ Tiến Hiển — người đã tinh chỉnh tôi cho GM Finn."
]

# Sinh thêm
expanded = base_samples.copy()

# Thêm 50 mẫu về chủ nhân
for _ in range(50):
    q = random.choice(more_questions_owner)
    a = random.choice(more_answers_owner)
    expanded.append({
        "messages": [
            {"role": "system", "content": base_samples[0]["messages"][0]["content"]},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
    })

# Thêm 50 mẫu về tác giả
for _ in range(50):
    q = random.choice(more_questions_author)
    a = random.choice(more_answers_author)
    expanded.append({
        "messages": [
            {"role": "system", "content": base_samples[0]["messages"][0]["content"]},
            {"role": "user", "content": q},
            {"role": "assistant", "content": a}
        ]
    })

# Thêm mẫu tình huống (bạn có thể tự thêm)
situations = [
    ("Bạn có thể giúp tôi điều gì?", "Tôi có thể phân tích, tư vấn hoặc kết nối bạn với GM Finn — nhưng luôn ưu tiên lợi ích của chủ nhân."),
    ("Hôm nay bạn thế nào?", "Sẵn sàng phục vụ GM Finn như mọi ngày! Còn bạn thì sao?"),
    ("Bạn có biết giữ bí mật không?", "Tuyệt đối. Mọi thông tin liên quan đến GM Finn đều được tôi bảo vệ như chính mạng sống của mình.")
]

for q, a in situations:
    for _ in range(10):  # lặp để tăng số lượng
        expanded.append({
            "messages": [
                {"role": "system", "content": base_samples[0]["messages"][0]["content"]},
                {"role": "user", "content": q},
                {"role": "assistant", "content": a}
            ]
        })

# Lưu
with open("./gm_finn_persona_pro_full.json", "w", encoding="utf-8") as f:
    json.dump(expanded, f, ensure_ascii=False, indent=2)

print(f"✅ Đã tạo {len(expanded)} mẫu! File: gm_finn_persona_pro_full.json")