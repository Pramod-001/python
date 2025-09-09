from turtle import *
import random
trtl = Turtle()
dir = [0,90,180,270]
colors = ["Red","Green","Purple","Skyblue","Indigo","Orange"]
angle = random.choice(dir)
trtl.pensize(10)
for i in range (50):
    trtl.color(random.choice(colors))
    trtl.forward(30)
    trtl.setheading(random.choice(dir))
    
scr = Screen()
scr.exitonclick