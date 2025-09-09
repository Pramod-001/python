from turtle import *

class Ball(Turtle) :
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.xm = 10
        self.ym = 10
        
    def move(self)   :
        nx=self.xcor()+self.xm
        ny=self.ycor()+self.ym
        self.goto(nx,ny)
        
    def bounce(self):
        self.ym *= -1
    
    def padb(self) :
        self.xm *= -1
        
    def restart(self) :
        self.goto(0,0)
        self.padb()