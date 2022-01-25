from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)

    def down(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
