from turtle import Turtle

score_file_read = open("highest_score.txt", "r")
try:
    temp_score = int(score_file_read.read())
except:
    temp_score = 0
    score_file_read.close()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = temp_score
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.write(f"Score:{self.score} \nHighest Score: {self.high_score}" , align="center", font=("Verdana", 15, "normal"))
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score:{self.score} \nHighest Score: {self.high_score}" , align="center", font=("Verdana", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Verdana", 24, "normal"))

    def increase_score(self):
        # clear is turtle methods to clear the screen
        self.clear()
        self.score += 1
        self.update_score_board()

    def save_score(self):
        if self.score >= self.high_score:
            source_file = open("highest_score.txt", "w")
            self.high_score = +self.score
            source_file.write(str(self.high_score))
            source_file.close()
