from turtle import *

class Paddle(Turtle) :
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
        
    def up(self) :
        Y=self.ycor()+30
        self.goto(self.xcor(),Y)

    def down(self) :
        Y=self.ycor()-30
        self.goto(self.xcor(),Y)