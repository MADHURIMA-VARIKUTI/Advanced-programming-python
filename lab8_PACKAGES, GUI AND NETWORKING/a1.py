import tkinter as tk
from tkinter import messagebox

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.score = 0
        self.question_index = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris",
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars",
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["Elephant", "Whale Shark", "Lion", "Giraffe"],
                "answer": "Whale Shark",
            },
        ]

        self.label = tk.Label(root, text="", font=("Arial", 12))
        self.label.pack()

        self.radio_var = tk.StringVar()
        self.radio_buttons = []

        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value="")
            self.radio_buttons.append(radio)
            radio.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()

        self.show_question()

    def next_question(self):
        selected_option = self.radio_var.get()
        correct_answer = self.questions[self.question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1

        self.question_index += 1

        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_question(self):
        question_data = self.questions[self.question_index]
        self.label.config(text=question_data["question"])
        options = question_data["options"]

        for i in range(4):
            if i < len(options):
                self.radio_buttons[i].config(text=options[i], value=options[i], state=tk.NORMAL)
            else:
                self.radio_buttons[i].config(text="", value="", state=tk.DISABLED)
            self.radio_var.set("")

    def show_result(self):
        self.label.config(text=f"Your Score: {self.score}/{len(self.questions)}")
        for radio in self.radio_buttons:
            radio.config(text="", value="", state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x320")
    root.title("Quiz application")
    app = QuizApplication(root)
    root.mainloop()
