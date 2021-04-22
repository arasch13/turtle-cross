import turtle
from options import car_speed

FONT = ("Tahoma", 16, "normal")
COLOR = "black"


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color(COLOR)
        self.penup()
        self.goto((-255, 270))
        self.hideturtle()
        self.car_speed = car_speed
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.car_speed *= 1.1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
