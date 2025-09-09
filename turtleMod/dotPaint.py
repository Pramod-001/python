import turtle as t 
from turtle import Screen
import random
trtl = t.Turtle()
trtl.shape("turtle")
t.colormode(255)
colors = ["Red","Green","Purple","Skyblue","Indigo","Orange"]
col = random.choice(colors)
trtl.speed("fastest")
trtl.penup()
trtl.setx(-200)
trtl.sety(-100)
dots = 100
#Circle
for i in range(1,dots) :
    trtl.color(random.choice(colors))
    trtl.dot(20,random.choice(colors))
    trtl.penup()
    trtl.forward(40)
    if i %10 == 0 :
        trtl.penup()
        trtl.setheading(90)
        trtl.forward(40)
        trtl.setheading(180)
        trtl.forward(400)
        trtl.setheading(0)
trtl.penup()
trtl.forward(10)
scr = Screen()    
scr.exitonclick()