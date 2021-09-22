from turtle import Turtle
from config import BORDER_HEIGHT

ALIGNMENT = 'center'
FONT = ("Arial",15,"normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,(BORDER_HEIGHT//2)-30)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}',move=False,align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.home()
        self.write(f'GAME OVER',move=False,align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()