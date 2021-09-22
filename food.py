from turtle import Turtle
import random
from config import BORDER_HEIGHT,BORDER_WIDTH

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-((BORDER_WIDTH//2)-20),(BORDER_WIDTH//2)-20)
        random_y = random.randint(-((BORDER_HEIGHT//2)-20),(BORDER_HEIGHT//2)-30)
        self.goto(random_x,random_y)