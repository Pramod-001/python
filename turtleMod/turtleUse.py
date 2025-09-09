from turtle import *
trtl = Turtle()
trtl.shape("turtle")
trtl.color("blue")
trtl.speed("fastest")
#Circle

trtl.circle(100)
print(trtl.position())


'''for i in range(7) :
    trtl.forward(10)
    trtl.penup()
    trtl.forward(10)
    trtl.pendown()
#Square
for i in range(0,4) :
    trtl.forward(100)
    trtl.right(90)
#pentagon
for i in range(5) :
    trtl.forward(100)
    trtl.right(72)
#hexagon
for i in range(6) :
    trtl.forward(100)
    trtl.right(60)'''
        

scrn = Screen()
scrn.exitonclick()