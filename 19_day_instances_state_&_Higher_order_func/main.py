from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.speed(1)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

print(user_bet)

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wiinning_color = turtle.pencolor()
            if wiinning_color == user_bet:
                print(f'You\'ve won! The {wiinning_color} turtle is the winner')
            else:
                print(f'You\'ve lost! The {wiinning_color} turtle is the winner')
                
        rand_dictance = random.randint(0, 10)
        turtle.forward(rand_dictance)

screen.exitonclick()
