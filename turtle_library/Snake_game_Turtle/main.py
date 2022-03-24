from turtle import Screen
import time
from snake import Snake
from food import Food
from scorboard import Scoreboard

# _____ initialize the Turtle
# this is the window that show up and it is Turtle Class
screen = Screen()

screen.setup(width=600, height=600)
# this is method of TurtleScreen/Screen
screen.bgcolor("black")
screen.title("Snake Game")

# tracer method to Turn turtle animation on/off and set delay for update drawings.
screen.tracer(0)

snake = Snake()
food = Food()
socreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()
game_is_on = True

while game_is_on:
    # update the screen because we set tracer for 0
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    # distance is Turtle class
    # food size is 10*10 | if the distance between food and head less than 15 increase the score
    if snake.head.distance(food) < 15:
        print("NOM TEST")
        # add segments to the snake once hit the ball
        snake.extend()
        food.refresh_food()
        socreboard.increase_score()
        socreboard.save_score()

    # # Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:

        game_is_on = False
        socreboard.game_over()

    # # delete Detect collision with wall.
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280:
    #     new_x = -(snake.head.xcor())
    #     new_y = snake.head.ycor()
    #     snake.head.goto(new_x, new_y)
    # elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     new_x = snake.head.xcor()
    #     new_y = -(snake.head.ycor())
    #     snake.head.goto(new_x, new_y)

    # Detect collision with the tall
    # for segment in snake.segments:
    # # if the segment that we loop through is equal to the tall pass
    # if segment == snake.head:
    #     pass
    # # if head collision with any segment in the tail
    # elif snake.head.distance(segment) < 20:
    #
    #     # trigger game over
    #     game_is_on = False
    #     socreboard.game_over()

    # we can solve the problem with the tail using slicing like this
    # segment[1:] all the segments except the first one
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            # trigger game over
            game_is_on = False
            socreboard.game_over()

# to keep looping so the windows doesn't exit
screen.exitonclick()
