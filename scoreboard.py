from turtle import Turtle
from config import BORDER_HEIGHT

ALIGNMENT = 'center'
FONT = ("Arial",15,"normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highScore = self.get_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,(BORDER_HEIGHT//2)-30)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}    High Score : {self.highScore}',move=False,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            self.set_highscore(self.highScore)

        self.score = 0
        self.update_scoreboard()    
        
    def game_over(self):
        self.home()
        self.write(f'GAME OVER',move=False,align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def get_highscore(self,high_score=0):
        with open('highscore_data.txt') as file:
            contents = file.read()
            return int(contents)
    
    def set_highscore(self,high_score=0):
        with open('highscore_data.txt',mode='w') as file:
            file.write(f'{high_score}')


s = ScoreBoard()
ll = [s.get_highscore()]
print(type(ll[0]))