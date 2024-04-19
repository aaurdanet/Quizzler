THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text="Text", font=("Arial", 20, "italic"),
                                                   fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_ans)
        self.false_button.grid(row=2, column=0)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_ans)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_ans(self):
        response = "true"
        self.give_feedback(self.quiz.check_answer(response))

    def false_ans(self):
        response = "false"
        self.give_feedback(self.quiz.check_answer(response))

    def give_feedback(self, ans):
        if ans:
            self.canvas.configure(bg="lime")
            self.window.after(1000, self.change_display)

        else:
            self.canvas.configure(bg="tomato")
            self.window.after(1000, self.change_display)

    def change_display(self):
        self.canvas.configure(bg="white")
        self.get_next_question()
        self.score_label.config(text=f"Score: {self.quiz.score}")
