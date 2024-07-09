from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.pu()
        self.goto(-380, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.points}', align='left', font=FONT)

    def increase_score(self):
        self.points += 4
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over', align='center', font=FONT)
