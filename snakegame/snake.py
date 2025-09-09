from turtle import *
UP=90
DOWN = 270
RIGHT = 0
LEFT = 180
pos = [(0,0),(-20,0),(-40,0)]
class Snake :
    def __init__(self):
        self.tur=[]
        self.create()
        self.head =   self.tur[0] 
    def create(self) :
        for position in pos :
            self.add(position)
            
    def add(self, position) :
        seg = Turtle("square")
        seg.penup()
        seg.speed("fastest")
        seg.goto(position)
        seg.color("white")
        self.tur.append(seg)
    def move(self) :
        for num in range(len(self.tur)-1 ,0 ,-1 ) :  #start =len(tur)-1  stop=0 step=-1
            x1 = self.tur[num-1].xcor()
            y1 = self.tur[num-1].ycor()

            self.tur[num].goto(x1,y1)
        self.tur[0].forward(20)
        
    def extend(self) :
        self.add(self.tur[-1].position())


    def up(self) :
        if self.head.heading()!=DOWN :
            self.head.setheading(UP)
        
    def down(self) :
        if self.head.heading()!=UP :
            self.head.setheading(DOWN)
        
    def right(self) :
        if self.head.heading()!=LEFT :
            self.head.setheading(RIGHT)
        
    def left(self) :
        if self.head.heading()!=RIGHT :
            self.head.setheading(LEFT)
    
    def restsnake(self):
        for i in self.tur :
            i.hideturtle()
        self.tur.clear()
        self.create()
        self.head = self.tur[0]