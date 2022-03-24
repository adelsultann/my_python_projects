from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # all the code inside the init will trigger once we call the snake
    def __init__(self, ):

        self.segments = []
        self.create_snake()
        # to control the head in other word the snake
        self.head = self.segments[0]
        self.head_mod()

    # ______________ Create the Snake _______________________________

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # create the shape of the Turtle
        new_segment = Turtle(shape="square")
        new_segment.color("orange")
        new_segment.shapesize(0.5, 0.5)
        # Turtle methods to not draw in the screen
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
# make the head like real snake
    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    def extend(self):
        # add a new segment to the snake
        # we will add the new segment at the end of the list od all segments
        # position is Turtle method
        self.add_segment(self.segments[-1].position())

    # ______________ Move the Snake _______________________________
    def move(self):
        # how to make the snake turn right or left
        # loop in reverse order because we want the last segment to go to the second segment and the second to the first
        # and the first segments to the new position
        #  range(start, stop, step)
        # seg_num in this loop does not included index 0
        for seg_num in range(len(self.segments) - 1, 0, -1):  # len(segments) - 1 = to get hold of the last segment in the snake
            # في اللوب هذا نتعامل مع الاندكس رقم 1 ورقم 2 صفر غير مشمول بحيث بنحركه بعد مانخلص اللوب

            # this is the second segment please note we only start with Two total index 0 is not included

            new_x = self.segments[seg_num - 1].xcor()  # xcor is method in turtle to get hold of the X position

            new_y = self.segments[seg_num - 1].ycor()  # ycor is method in turtle to get hold of the X position
            # this is the last segment we make it to go to the second
            self.segments[seg_num].goto(new_x, new_y)
            # if run this code without moving the snake all the segments will be in one place
            # forward is Turtle method to move the object
        self.head.forward(MOVE_DISTANCE)  # this is the first segment we will make it movie forward

    def up(self):
        # to control the direction we only need to get hold of the first segments
        # heading() is turtle method
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
