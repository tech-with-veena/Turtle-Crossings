import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_manager=CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
screen.listen()
scoreboard=Scoreboard()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createcar()
    car_manager.movecars()
    for cars in car_manager.allcars:
        if cars.distance(player) < 20:
            game_is_on=False
            scoreboard.gameover()
        if player.finsh():
            player.gotostart()
            car_manager.speedup()
            scoreboard.increase()


screen.exitonclick()