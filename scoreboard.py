from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('arial', 24, "normal")


# This makes it a super class
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_l}:{self.score_r}", align=ALIGNMENT, font=FONT)

    def update_l(self):
        self.score_l += 1
        self.clear()
        self.update_score()

    def update_r(self):
        self.score_r += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over :(", align=ALIGNMENT, font=FONT)
