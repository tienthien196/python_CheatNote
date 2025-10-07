from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TextIteratorStreamer,
    BitsAndBytesConfig
)
import torch
from threading import Thread
import warnings
warnings.filterwarnings("ignore")

# === Cấu hình ===
MODEL_NAME = "Qwen/Qwen3-1.7B"  # Đã đổi sang model 1.7B
USE_4BIT_QUANT = True  # Đặt False nếu bạn không có GPU tương thích hoặc gặp lỗi

# === Tải model và tokenizer ===
print("Đang tải tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)

# Cấu hình quantization (4-bit) nếu bật và có GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
bnb_config = None
if USE_4BIT_QUANT and device == "cuda":
    print("Sử dụng quantization 4-bit để tăng tốc và tiết kiệm VRAM...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

print("Đang tải mô hình... (lần đầu có thể mất vài phút)")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto" if (USE_4BIT_QUANT and device == "cuda") else None,
    trust_remote_code=True,
    torch_dtype=torch.float16 if (device == "cuda" and not USE_4BIT_QUANT) else torch.float32,
)

if not USE_4BIT_QUANT:
    model.to(device)

print(f"\n✅ Chatbot đã sẵn sàng! (Device: {next(model.parameters()).device})")
print("Gõ 'exit' hoặc 'quit' để thoát.\n")

# === Vòng lặp chat ===
while True:
    user_input = input("Bạn: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print("Tạm biệt!")
        break
    if not user_input:
        continue

    # Chuẩn bị tin nhắn theo định dạng chat của Qwen
    messages = [{"role": "user", "content": user_input}]
    
    # Tokenize input
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt",
        enable_thinking=False
    ).to(model.device)

    # Tạo streamer để nhận từng token
    streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True,
        timeout=60.0
    )

    # Cấu hình sinh văn bản
    generation_kwargs = dict(
        **inputs,
        streamer=streamer,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    # Chạy generate trong thread nền để không chặn main thread
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    # In phản hồi theo kiểu streaming
    print("Bot: ", end="", flush=True)
    for new_text in streamer:
        print(new_text, end="", flush=True)
    print("\n")  # Xuống dòng sau khi kết thúc phản hồi