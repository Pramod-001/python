from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 8
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.speed = 8
    def newcar(self):
        num = random.randint(1,6)
        if num == 1:
            new = Turtle("square")
            new.shapesize(1,2)
            new.penup()
            new.color(random.choice(COLORS))
            r = random.randint(-250,250)
            new.goto(300,r)
            self.cars.append(new)
            
        self.movecar()
        
    def movecar(self):
        for i in self.cars:
            i.backward(self.speed)
        
    def newspeed(self):
        self.speed+=MOVE_INCREMENT
