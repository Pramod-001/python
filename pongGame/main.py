from turtle import *
from paddle import Paddle
from ball import Ball
from score import Score
import time
scrn = Screen()
scrn.title("Pong Game")
scrn.bgcolor("black")
scrn.setup(width=800,height=600)
scrn.listen()
scrn.tracer(0)
t = Turtle()
t.color("white")
t.penup()
t.goto(0,290)
t.right(90)
t.pendown()
for i in range(0,20):
    t.forward(15)
    t.penup()
    t.forward(15)
    t.pendown()
rp = Paddle((350,0))
lp = Paddle((-350,0))
ball = Ball()
sc = Score()

scrn.onkey(rp.up,"Up")
scrn.onkey(rp.down,"Down")

scrn.onkey(lp.up,"w")
scrn.onkey(lp.down,"s")

game = True
while game == True :
    time.sleep(0.05)
    scrn.update()
    ball.move()
    
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce()
        
    if (ball.distance(rp)<50 and ball.xcor()>320) or (ball.distance(lp)<50 and ball.xcor()<-320) :  
        ball.padb()
    
    if ball.xcor()>380 :
        ball.restart()
        sc.lpoint()
        
    if ball.xcor()<-380 :
        ball.restart()
        sc.rpoint()
scrn.exitonclick()
