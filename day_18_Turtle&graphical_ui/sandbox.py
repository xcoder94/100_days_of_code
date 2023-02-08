from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)

tim = Turtle()

tim.shape('turtle')
tim.color('red')

# Drawing a square
# for _ in range(1, 5):
#     tim.speed(1)
#     tim.rt(90)
#     tim.fd(100)


# Drawing a dashed line

for _ in range(1, 11):
    tim.speed(1)
    tim.fd(10)
    tim.pu()
    tim.fd(10)
    tim.pd()










screen.exitonclick()
