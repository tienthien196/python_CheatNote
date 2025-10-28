from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_qwen_model(model_name="Qwen/Qwen2.5-0.5B"):
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        trust_remote_code=True
    )
    return tokenizer, model

def generate_response(tokenizer, model, messages, max_new_tokens=100):
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return response

if __name__ == "__main__":
    print("🚀 Đang tải model... (lần đầu có thể lâu)")
    tokenizer, model = load_qwen_model("Qwen/Qwen2.5-0.5B")
    print("✅ Sẵn sàng! Nhập 'exit' hoặc 'quit' để thoát.\n")

    # Lưu lịch sử chat (nếu model hỗ trợ)
    chat_history = []

    while True:
        user_input = input("👤 Bạn: ").strip()
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("👋 Tạm biệt!")
            break

        if not user_input:
            continue

        # Thêm tin nhắn người dùng vào lịch sử
        chat_history.append({"role": "user", "content": user_input})

        try:
            response = generate_response(tokenizer, model, chat_history, max_new_tokens=200)
            print(f"🤖 Bot: {response}")

            # Thêm phản hồi của bot vào lịch sử (để duy t
            # rì ngữ cảnh)
            chat_history.append({"role": "assistant", "content": response})
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            # Tuỳ chọn: reset lịch sử nếu lỗi do quá dài