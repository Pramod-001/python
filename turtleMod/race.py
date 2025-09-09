from turtle import *
import random
t1 = Turtle("turtle")
t2 = Turtle("turtle")
t3 = Turtle("turtle")
t4 = Turtle("turtle")
t5 = Turtle("turtle")
t6 = Turtle("turtle")
tur = [t1,t2,t3,t4,t5,t6]
t1.color("Red")
t2.color("Blue")
t3.color("Orange")
t4.color("Yellow")
t5.color("Indigo")
t6.color("Green")
screen = Screen()
game = True
screen.setup(width=500,height=400)
uchoice = screen.textinput(title="Choose One Colour!",prompt="Who will win the Race : ")
print(uchoice)
Y=-80
for i in tur :
    i.penup()
    i.goto(x=-235,y=Y)
    Y+=30
while game == True :
    for i in tur :
        if i.xcor()>220 :
            winc = i.pencolor()
            win = winc.lower()
            game = False
            if win == uchoice :
                print("You Have won the bet")
            else :
                print("You have placed the wrong bet")
                print(f"{win} turtle won the race")
        i.forward(random.randint(0,10)) 
screen.exitonclick()