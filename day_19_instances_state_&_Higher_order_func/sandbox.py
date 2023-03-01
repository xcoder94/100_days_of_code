from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(720, 720)



position = tim.pos()
print(position)

def move_forward():
    tim.forward(10)


def move_back():
    tim.bk(10)


def turn_counter_clockwise():
    tim.lt(10)


def turn_clockwise():
    tim.rt(10)


def clean_and_back():
    tim.home()
    tim.clear()






screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='c', fun=clean_and_back)
screen.exitonclick()