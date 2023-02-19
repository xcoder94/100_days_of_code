# import colorgram
import turtle as t
import random
# rgb_colors = []
# colors_in_image = colorgram.extract("image.jpg", 30)
# for color in colors_in_image:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)

screen = t.Screen()
screen.setup(720, 720)
tim = t.Turtle()
tim.pu()
x = -310
y = -300
tim.setposition(x, y)
for i in range(10):
    y += 30
    tim.setposition(x, y)
    print(tim.setposition(x + 10, y))
    for j in range(10):
        current_color = random.choice(color_list)
        tim.dot(10, current_color)
        tim.fd(20)








screen.exitonclick()




