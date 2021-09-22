from turtle import Turtle
# from config import STARTING_POSITION,STEP_SIZE,UP,DOWN,RIGHT,LEFT

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    snakes = []

    def __init__(self) -> None:
        '''This is the constructor function. It will create the list for all the 'snakes', then it'll call create_snake method and then point the head to the first turtle object in snakes list'''
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

        

    def create_snakes(self):
        '''This function creates 3 turtle objects with a pre-defined position from STARTING_POSITION '''
        for pos in STARTING_POSITION:
            self.add_snakes(pos)
            
    
    def add_snakes(self,pos):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(pos)
        self.snakes.append(timmy)
    
    def extend(self):
        self.add_snakes(self.snakes[-1].position())
    
    def move(self):
        '''This function moves the snake by a pre-defined size as defined in STEP_SIZE '''
        # i = len(self.snakes)-1
        # while(i>0):
        #     self.snakes[i].goto(self.snakes[i-1].position())
        #     i -= 1

        for i in range(len(self.snakes)-1,0,-1):
            self.snakes[i].goto(self.snakes[i-1].position())
        
        self.head.forward(STEP_SIZE)


    def up(self):
        '''This function makes the snake head upwards'''
        if self.head.heading != DOWN:
            self.head.setheading(90)
    
    def down(self):
        '''This function makes the snake head downwards'''
        if self.head.heading() != UP:
            self.head.setheading(270)
    
    def left(self):
        '''This function makes the snake head turn left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    
    def right(self):
        '''This function makes the snake head turn right'''
        if self.head.heading() != LEFT:
            self.head.setheading(0)