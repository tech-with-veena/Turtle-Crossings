from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.update()
    def update(self):
        self.clear()
        self.write(f"LEVEL : {self.level}", align="left", font=FONT)
    def increase(self):
        self.level +=1
        self.update()
    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=FONT)