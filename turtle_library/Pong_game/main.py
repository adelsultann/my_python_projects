from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
# controlling the paddle
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.ball_move_speed)
    screen.update()
    ball.move()



    # detect the collision with the wall

    if ball.ycor() > 295 or ball.ycor() < - 295:
        # Bounce
        ball.bounce_y()



    # Detect collision with the r_paddle
    # we don't add only the distance between the paddle and the ball we add
    # also the xcor because the distance method count from the center
    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    if ball.xcor() > 380:
        ball.rest_position()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.rest_position()
        scoreboard.r_point()

screen.exitonclick()
