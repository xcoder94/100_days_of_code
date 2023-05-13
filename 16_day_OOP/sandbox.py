from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('coral')
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align["Pokemon name"] = "l"
table.align["Type"] = "l"

print(table)
