from turtle import Turtle


class Seperator(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=0.11)
        self.penup()
        self.color("white")
        self.goto(position)

