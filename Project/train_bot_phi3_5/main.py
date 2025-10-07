import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# === LOAD MODEL 1 LẦN DUY NHẤT ===
print("Loading model... (this takes a while)")
torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3.5-mini-instruct",
    device_map="cuda",
    torch_dtype=torch.float16,  # tốt hơn "auto" khi dùng GPU
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct")

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

# === LỊCH SỬ HỘI THOẠI ===
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

print("\n✅ Model loaded! Type 'quit' to exit.\n")

# === VÒNG LẶP NHẬP CÂU HỎI ===
while True:
    user_input = input("👤 You: ").strip()
    if user_input.lower() in ["quit", "exit", "q"]:
        print("👋 Goodbye!")
        break

    # Thêm tin nhắn người dùng
    messages.append({"role": "user", "content": user_input})

    # Sinh phản hồi
    output = pipe(
        messages,
        max_new_tokens=250,      # giảm để nhanh hơn
        do_sample=False,
        return_full_text=False,
    )

    response = output[0]['generated_text'].strip()
    print(f"🤖 Bot: {response}")

    # Lưu phản hồi vào lịch sử (để tiếp tục hội thoại)
    messages.append({"role": "assistant", "content": response})