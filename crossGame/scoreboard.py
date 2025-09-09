from turtle import *
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self) :
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250,260)
        self.updatescore()
        
    def updatescore(self):
        self.clear()
        self.write(f"Level :{self.level}",align ="left",font=FONT )

    def inc(self):
        self.level+=1
        self.updatescore()
    
    def over(self):
        self.goto(0,0)
        self.write("GAME OVER",align ="center",font=FONT )