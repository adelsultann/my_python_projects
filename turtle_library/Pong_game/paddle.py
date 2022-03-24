from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        # we figure out the y position then each time user press up we move it by 20
        new_y = self.ycor() + 20
        # we left xcor as it is
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # we figure out the y position then each time user press down we move it by 20
        new_y = self.ycor() - 20
        # we left xcor as it is
        self.goto(self.xcor(), new_y)


