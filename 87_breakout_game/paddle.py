from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.pu()
        # self.seth(90)
        self.hideturtle()
        self.resizemode('user')
        self.shapesize(1, 10)
        self.goto(STARTING_POS)
        self.showturtle()
        self.color('black')

    def move_left(self):
        if self.xcor() >= -290:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
            print(self.shapesize())

    def move_right(self):
        if self.xcor() <= 290:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
