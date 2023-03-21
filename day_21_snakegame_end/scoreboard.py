from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')

class Score(Turtle):


    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.pu()
        self.color('white')        
        self.setpos(x=0, y=280)
        self.update_score()


    def update_score(self):
        self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()






