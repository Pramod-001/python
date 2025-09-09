import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move,"Up")
car = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.newcar()
    
    for i in car.cars :
        if player.distance(i)<15 :
            game_is_on=False
            score.over()
    if player.finish() :
        player.restart()
        car.newspeed()
        score.inc()
screen.exitonclick()