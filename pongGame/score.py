from turtle import Turtle

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.uscore()
    def uscore(self):
        self.clear()        
        self.goto(-180,260)
        self.write(f"Score :{self.lscore}",align='center',font = ("Courier",20,"normal"))
        self.goto(180,260)
        self.write(f"Score :{self.rscore}",align='center',font = ("Courier",20,"normal"))   
        
    def lpoint(self) :
        self.lscore+=1
        self.uscore()
        
    def rpoint(self) :
        self.rscore+=1
        self.uscore()