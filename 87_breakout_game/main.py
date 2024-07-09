import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer()

scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball(paddle)
screen.listen()

screen.onkey(paddle.move_right, 'Right')
screen.onkey(paddle.move_left, 'Left')
screen.onkey(ball.move, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.mainloop()
screen.exitonclick()
