from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # we havan't change the x because it's score not bounce
        # سوينا هذي عشان تعكس حركه الواي لو كانت موجبه تكون سلبيه وهكذا
        self.y_move *= -1
        print(self.x_move)

    # def bounce_x(self):
    #     self.x_move *= -1
    #     # when the ball hit the paddle we increase the speed
    #     self.ball_move_speed *= 0.9

    def bounce_x_l_paddle(self):
        # سوينا هذي عشان تعكس حركه الواي لو كانت موجبه تكون سلبيه وهكذا
        # The abs() function make any negative number to positive
        self.x_move = (abs(self.x_move))
        self.ball_move_speed *= 0.9

    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.ball_move_speed *= 0.9

    def rest_position(self):
        self.home()
        # rest the ball speed
        self.ball_move_speed = 0.1
        self.bounce_x()
