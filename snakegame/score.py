from turtle import Turtle
import random

class Score(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high.txt") as high :
            self.high = int(high.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.sb()
        
    def inc(self) :
        self.score +=1
        self.sb()
        
    def sb(self) :
        self.clear()
        self.write(f"Score : {self.score}  HighScore : {self.high} ",align = "center",font=("Garamond",20,"normal"))
    
    def resethigh(self) :
        
        if self.score>self.high :
            self.high = self.score
            with open("high.txt" ,mode="w") as high :
                high.write(f"{self.high}")
        self.score = 0
        self.sb()
         
     
    #def over(self) :
     #   self.goto(0,0)
      #  self.write(f"Game Over ",align = "center",font=("Garamond",20,"normal"))