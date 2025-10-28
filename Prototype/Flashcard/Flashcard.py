import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
import random

class FlashcardAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🃏 Flashcard App")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        self.filename = r"E:\1_test_Src\src\python\python_cheat\Project\Flashcard\flashcards.json"
        self.flashcards = self.load_flashcards()
        self.current_card_index = 0
        self.is_answer_shown = False

        # Tiêu đề
        title_label = tk.Label(root, text="🃏 Flashcard App", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Frame hiển thị flashcard
        self.card_frame = tk.Frame(root, relief="groove", borderwidth=2, bg="#f0f0f0")
        self.card_frame.pack(pady=20, padx=30, fill="both", expand=True)

        self.question_label = tk.Label(self.card_frame, text="", font=("Arial", 16), wraplength=500, bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.answer_label = tk.Label(self.card_frame, text="", font=("Arial", 14, "italic"), fg="gray", wraplength=500, bg="#f0f0f0")
        self.answer_label.pack(pady=10)

        # Nút điều khiển
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        self.toggle_btn = tk.Button(btn_frame, text="Hiện/Ẩn Đáp Án", command=self.toggle_answer, width=15)
        self.toggle_btn.grid(row=0, column=0, padx=5)

        self.next_btn = tk.Button(btn_frame, text="Thẻ Tiếp Theo", command=self.next_card, width=15)
        self.next_btn.grid(row=0, column=1, padx=5)

        self.prev_btn = tk.Button(btn_frame, text="Thẻ Trước", command=self.prev_card, width=15)
        self.prev_btn.grid(row=0, column=2, padx=5)

        # Nút quản lý
        manage_frame = tk.Frame(root)
        manage_frame.pack(pady=10)

        tk.Button(manage_frame, text="➕ Thêm Flashcard", command=self.add_flashcard, width=18).pack(side="left", padx=5)
        tk.Button(manage_frame, text="👁️ Xem Tất Cả", command=self.show_all_cards, width=18).pack(side="left", padx=5)
        tk.Button(manage_frame, text="💾 Lưu", command=self.save_flashcards, width=10).pack(side="left", padx=5)

        # Trạng thái
        self.status_label = tk.Label(root, text=f"Tổng: {len(self.flashcards)} thẻ", fg="blue")
        self.status_label.pack(pady=5)

        self.show_current_card()

    def load_flashcards(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể tải dữ liệu: {e}")
                return []
        return []

    def save_flashcards(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.flashcards, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("Thành công", f"Đã lưu {len(self.flashcards)} flashcard!")
            self.update_status()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu: {e}")

    def update_status(self):
        self.status_label.config(text=f"Tổng: {len(self.flashcards)} thẻ")

    def show_current_card(self):
        if not self.flashcards:
            self.question_label.config(text="Chưa có flashcard nào.")
            self.answer_label.config(text="")
            self.toggle_btn.config(state="disabled")
            self.next_btn.config(state="disabled")
            self.prev_btn.config(state="disabled")
            return

        self.toggle_btn.config(state="normal")
        self.next_btn.config(state="normal")
        self.prev_btn.config(state="normal")

        card = self.flashcards[self.current_card_index]
        self.question_label.config(text=card["question"])
        self.answer_label.config(text="")
        self.is_answer_shown = False

    def toggle_answer(self):
        if not self.flashcards:
            return
        card = self.flashcards[self.current_card_index]
        if self.is_answer_shown:
            self.answer_label.config(text="")
            self.is_answer_shown = False
        else:
            self.answer_label.config(text=card["answer"])
            self.is_answer_shown = True

    def next_card(self):
        if self.flashcards:
            self.current_card_index = (self.current_card_index + 1) % len(self.flashcards)
            self.show_current_card()

    def prev_card(self):
        if self.flashcards:
            self.current_card_index = (self.current_card_index - 1) % len(self.flashcards)
            self.show_current_card()

    def add_flashcard(self):
        question = simpledialog.askstring("Thêm Flashcard", "Nhập câu hỏi:")
        if question is None:
            return
        answer = simpledialog.askstring("Thêm Flashcard", "Nhập đáp án:")
        if answer is None:
            return
        if question.strip() and answer.strip():
            self.flashcards.append({"question": question.strip(), "answer": answer.strip()})
            self.update_status()
            messagebox.showinfo("Thành công", "Đã thêm flashcard mới!")
            if len(self.flashcards) == 1:
                self.show_current_card()
        else:
            messagebox.showwarning("Cảnh báo", "Câu hỏi và đáp án không được để trống!")

    def show_all_cards(self):
        if not self.flashcards:
            messagebox.showinfo("Thông báo", "Chưa có flashcard nào.")
            return

        # Tạo cửa sổ con
        top = tk.Toplevel(self.root)
        top.title("Danh sách Flashcard")
        top.geometry("500x400")

        text_widget = tk.Text(top, wrap="word", font=("Arial", 12))
        text_widget.pack(padx=10, pady=10, fill="both", expand=True)

        for i, card in enumerate(self.flashcards, 1):
            text_widget.insert(tk.END, f"{i}. Câu hỏi: {card['question']}\n")
            text_widget.insert(tk.END, f"   Đáp án: {card['answer']}\n\n")

        text_widget.config(state="disabled")  # Chỉ đọc

    def on_closing(self):
        self.save_flashcards()
        self.root.destroy()

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardAppGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)  # Lưu khi đóng cửa sổ
    root.mainloop()