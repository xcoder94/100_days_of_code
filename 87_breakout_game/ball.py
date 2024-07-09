from turtle import Turtle

START_POS = (0, -260)
MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self, paddle):
        super().__init__()
        self.paddle = paddle
        self.shape('circle')
        self.pu()
        self.hideturtle()
        self.goto(START_POS)
        self.showturtle()
        self.color('black')
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def start_moving(self):
        self.move()

    def move(self):
        # Update ball's x and y coordinates
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        # Check for collision with left and right borders
        if new_x <= -375 or new_x >= 375:  # Assuming screen width is 750
            self.x_move *= -1  # Reverse x direction

        # Check for collision with the top border
        if new_y >= 280:  # Assuming screen height is 560
            self.y_move *= -1  # Reverse y direction

        if new_y
        # Check for collision with the bottom border
        # if new_y <= -280:  # Assuming screen height is 560
        #     # Handle the collision (e.g., reset ball position and stop movement)
        #     pass  # Implement your logic here

        # Move the ball
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

