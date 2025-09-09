from turtle import *
import random
angles = [25,30,60,75,120,180,270,360]
trtl = Turtle()
scrn = Screen()
trtl.speed("fastest")
def movefor():
    trtl.forward(20)
def back() :
    trtl.backward(20)
def clear() :
    trtl.clear()
    trtl.penup()
    trtl.home()
    trtl.pendown()
def clock() :   
    trtl.right(random.choice(angles))
def anclock() :
    trtl.left(random.choice(angles))
scrn.listen()
scrn.onkey(key="w",fun=movefor)
scrn.onkey(key="s",fun=back)
scrn.onkey(key="d",fun=clock)
#scrn.onkey(key="a",fun=anclock)
scrn.onkey(anclock,"a")
scrn.onkey(key="c",fun=clear)
scrn.exitonclick()