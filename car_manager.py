from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.allcars=[]
        self.carspeed=STARTING_MOVE_DISTANCE
    def createcar(self):
        randomnum=random.randint(1,6)
        if randomnum==1:
            newcar=Turtle("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            randomy=random.randint(-250,250)
            newcar.goto(300,randomy)
            self.allcars.append(newcar)
    def movecars(self):
        for cars in self.allcars:
            cars.backward(self.carspeed)

    def speedup(self):
        self.carspeed += MOVE_INCREMENT


