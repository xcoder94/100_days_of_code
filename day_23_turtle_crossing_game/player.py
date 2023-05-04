from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)
        self.color('black')


    def move_forword(self):
        self.fd(MOVE_DISTANCE)


    def move_back(self):
        self.bk(MOVE_DISTANCE)


    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor() )


    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor() )


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False