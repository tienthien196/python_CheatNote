from datasets import load_dataset
import json

# 1. Tải dataset
ds = load_dataset("glaiveai/godot_4_docs", split="train")

# 2. Chuyển đổi sang định dạng Qwen chat
def to_qwen_format(example):
    return {
        "messages": [
            {"role": "user", "content": example["prompt"]},
            {"role": "assistant", "content": example["response"]}
        ]
    }

qwen_ds = ds.map(to_qwen_format, remove_columns=ds.column_names)

# 3. Lưu ra file JSONL (tùy chọn, nếu bạn muốn kiểm tra)
qwen_ds.to_json("godot_qwen.jsonl", orient="records", lines=True)

print("✅ Đã chuyển đổi xong! Tổng số mẫu:", len(qwen_ds))