from turtle import Turtle
from config import BORDER_HEIGHT,BORDER_WIDTH

BORDER_HEIGHT -= 20
class BorderConfig(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.pensize(10)

    def make_border(self):
        self.goto(-(BORDER_WIDTH//2)+10,(BORDER_HEIGHT//2))
        self.pendown()
        self.color("red")
        for i in range(0,2):
            self.forward(BORDER_WIDTH)
            self.right(90)
            self.forward(BORDER_HEIGHT)
            self.right(90)