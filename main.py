from random import gammavariate
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from border_config import BorderConfig
from config import BORDER_WIDTH,BORDER_HEIGHT

screen = Screen()
# border = BorderConfig()

screen.setup(width=BORDER_WIDTH,height=BORDER_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
# border.make_border()
screen.update()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



# def turn_left(snakes):
#     i = len(snakes)-1
#     while(i>0):
#         snakes[i].goto(snakes[i-1].position())
#         i -= 1
#     # screen.update()
#     # time.sleep(0.5)
#     snakes[0].left(90)
#     snakes[0].forward(20)
#     screen.update()
#     time.sleep(0.5)



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)
    snake.move()

    # Detecting Collison
    if snake.head.distance(food) <=15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    
    if snake.head.xcor() > (BORDER_WIDTH//2)-20 or snake.head.xcor() < -(BORDER_WIDTH//2)+20 or snake.head.ycor() > (BORDER_HEIGHT//2)-30 or snake.head.ycor() < -(BORDER_HEIGHT//2)+20:
        game_is_on = False
        score_board.game_over()
        print(snake.head.position())
    
    for segments in snake.snakes:
        if segments == snake.head:
            continue
        elif snake.head.distance(segments)<=10:
            game_is_on = False
            score_board.game_over()

    

    


# turn_left(snakes)

# for i in snakes:
    # print(i.position())


screen.exitonclick()