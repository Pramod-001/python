from turtle import *
from snake import Snake
from food import Food
from score import Score
import time 
scrn = Screen()
scrn.setup(width=600,height=600)
scrn.bgcolor("black")
scrn.title("Snake Game")
scrn.tracer()
scrn.listen()                                                                            
'''t = Turtle(shape="square")
t.color("white")
t.shapesize(1,3)
t.penup()'''
snake = Snake()
food = Food()
score = Score()
game = True
scrn.onkey(snake.up,"Up")
scrn.onkey(snake.down,"Down")
scrn.onkey(snake.right,"Right")
scrn.onkey(snake.left,"Left")
while game == True :
    #t.forward(20)
    scrn.update()
    time.sleep(0.08)
    snake.move()
    if snake.head.distance(food) < 15 :
        food.refresh()
        score.inc()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.resethigh()
        snake.restsnake()
        
    for i in snake.tur :
        
        if i == snake.head :
            pass
        
        elif snake.head.distance(i) < 10 :
            score.resethigh()
    
scrn.exitonclick()