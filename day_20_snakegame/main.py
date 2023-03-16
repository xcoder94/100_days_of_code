from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake_body = []

for poitions in starting_positions:
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.goto(poitions)















screen.exitonclick()
