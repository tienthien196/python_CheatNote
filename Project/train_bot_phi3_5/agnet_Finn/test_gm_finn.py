# chat_with_gm_finn.py
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TextIteratorStreamer
)
from peft import PeftModel
from threading import Thread
import torch
import warnings
warnings.filterwarnings("ignore")

# === Cấu hình ===
BASE_MODEL = "Qwen/Qwen3-1.7B"
LORA_ADAPTER = r"E:\1_test_Src\src\python\python_cheat\gm_finn_qwen3_lora"  # Thư mục bạn lưu sau fine-tune

# === Tải tokenizer ===
print("Đang tải tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token

# === Cấu hình 4-bit ===
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# === Tải model gốc + gắn LoRA ===
print("Đang tải model gốc (4-bit)...")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
    torch_dtype=torch.float16,
)

print("Đang gắn LoRA adapter...")
model = PeftModel.from_pretrained(model, LORA_ADAPTER)
model.eval()  # Chế độ đánh giá

print(f"\n✅ Trợ lý của GM Finn đã sẵn sàng! (Device: {next(model.parameters()).device})")
print("Gõ 'exit' hoặc 'quit' để thoát.\n")

# === Vòng lặp chat ===
while True:
    user_input = input("Bạn: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Tạm biệt! Trân trọng phục vụ GM Finn.")
        break
    if not user_input:
        continue

    # Chuẩn bị tin nhắn (có thể thêm system message nếu muốn)
    messages = [
        {"role": "user", "content": user_input}
    ]
    
    # Tokenize
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
        enable_thinking=False
    ).to(model.device)

    # Streamer
    streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True,
        timeout=60.0
    )

    # Sinh văn bản
    generation_kwargs = dict(
        **inputs,
        streamer=streamer,
        max_new_tokens=256,  # Giảm để tiết kiệm VRAM
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    # Chạy nền
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    # In streaming
    print("GM Finn's Assistant: ", end="", flush=True)
    for new_text in streamer:
        print(new_text, end="", flush=True)
    print("\n")