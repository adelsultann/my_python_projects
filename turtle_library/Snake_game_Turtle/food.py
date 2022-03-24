from turtle import Turtle
import random


# this is class inheritance
class Food(Turtle):
    # all the code inside the init will trigger once we call the snake
    def __init__(self):
        super().__init__()
        # this is method from the turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        # note the screen is 600*600 means x = goes from 300 to - 300 as well as y
        # we put 280 so the food doesn't appear near the wall
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)
