from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(800, 600)

tim = Turtle()

# tim.shape('arrow')
# tim.color('red')

# Drawing a square
# for _ in range(1, 5):
#     tim.speed(1)
#     tim.rt(90)
#     tim.fd(100)


# Drawing a dashed line

# for _ in range(1, 11):
#     tim.speed(1)
#     tim.fd(10)
#     tim.pu()
#     tim.fd(10)
#     tim.pd()

# My coode
# for i in range(3, 10):
#     angle = 360 / i
#     for j in range(i):
#         tim.fd(100)
#         tim.right(angle)

# Angela's code start
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

 
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# Angela's code end

tim.pensize(10)
directions = [0, 90, 180, 270]
for i in range(200):
    tim.speed(0)
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))
    tim.fd(20)
    


screen.exitonclick()
