import turtle as t
import random
screen = t.Screen()
screen.setup(1280, 720)

tim = t.Turtle()
t.colormode(255)

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
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


# Random walk started
# tim.pensize(10)
# directions = [0, 90, 180, 270]
# for i in range(200):
#     tim.speed(0)
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.fd(20)
# randiom walk ended


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
