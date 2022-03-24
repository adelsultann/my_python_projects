from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Aharoni"


class QuizInterFace:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.question_total = Label(text="Question 0/0", fg="white", bg=THEME_COLOR)
        self.question_total.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(
            150, 125,
            width=280, # we add the width 280 so the question fit in the screen 280 less than the width of the canvas
            text="Some question Text",
            fill=THEME_COLOR,
            font=(FONT_NAME, 18)
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # true Button
        true_image = PhotoImage(file="images/true.png")
        # highlightthickness=0\  remove the light grey border around my Canvas widget
        self.true_button = Button(image=true_image, highlightthickness=0, relief='ridge', command=self.true_pressd)
        self.true_button.grid(row=2, column=0)

        # false button
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, relief='ridge', command=self.false_pressd)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop() # mainloop to keep the app running

    def get_next_question(self):
        self.question_total.config(text=f"Question {self.quiz.question_number}/{len(self.quiz.q_list)}")
        self.canvas.config(bg="white")  # to bring the white background after giving feedback to user and change color
        if self.quiz.still_has_question(): # check if there is still question| this is from quiz brain

            self.score_label.config(text=f"Score {self.quiz.score}") # to get the score from the quiz brain
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressd(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressd(self):
        # it's the same as the true pressed function but i change the code
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            # 1000 below represent milliseconds
        self.window.after(1000, self.get_next_question)
