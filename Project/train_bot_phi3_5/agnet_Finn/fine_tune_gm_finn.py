# fine_tune_gm_finn.py — TƯƠNG THÍCH VỚI trl >= 0.8.0
import os
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
from datasets import load_dataset
import torch

# === Cấu hình ===
MODEL_NAME = "Qwen/Qwen3-1.7B"
DATASET_PATH = r"E:\1_test_Src\src\python\python_cheat\Project\train_bot_phi3_5\agnet_Finn\gm_finn_persona_pro_full.json"
OUTPUT_DIR = "./gm_finn_qwen3_lora"

# === Tải tokenizer ===
print("Đang tải tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# === Cấu hình 4-bit quantization ===
print("Thiết lập quantization 4-bit...")
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# === Tải model ===
print("Đang tải model (4-bit)...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.float16,  # Cảnh báo "deprecated" nhưng vẫn hoạt động
)

model = prepare_model_for_kbit_training(model)

# === Cấu hình LoRA ===
print("Thiết lập cấu hình LoRA...")
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# === Tải dataset ===
print("Đang tải dataset...")
dataset = load_dataset("json", data_files=DATASET_PATH, split="train")
print("Mẫu đầu tiên:", dataset[0])

# Hàm định dạng prompt
def formatting_prompts_func(example):
    # example là dict: {"messages": [...]}
    # Chúng ta cần lấy LIST messages và áp dụng template
    messages = example["messages"]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False,
        enable_thinking=False
    )
    return [text]  # SFTTrainer mong đợi list (dù chỉ 1 chuỗi)

# === Cấu hình huấn luyện ===
print("Thiết lập tham số huấn luyện...")
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    optim="paged_adamw_32bit",
    learning_rate=2e-4,
    num_train_epochs=5,
    logging_steps=5,
    save_steps=20,
    fp16=True,
    gradient_checkpointing=True,
    remove_unused_columns=False,
    report_to="none",
    save_total_limit=2,
)

# === Khởi tạo SFTTrainer — KHÔNG DÙNG 'max_seq_length' và 'tokenizer' ===
print("Khởi tạo SFTTrainer...")
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    formatting_func=formatting_prompts_func,
    # ✅ ĐÃ XÓA: max_seq_length=512
    # ✅ ĐÃ XÓA: tokenizer=tokenizer  ← đây là nguyên nhân lỗi mới
)

# === Huấn luyện ===
print("\n🚀 Bắt đầu fine-tuning...")
trainer.train()

# === Lưu kết quả ===
print("Đang lưu LoRA adapter...")
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"\n✅ Hoàn tất! Kết quả lưu tại: {OUTPUT_DIR}")