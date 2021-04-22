import turtle
import random

turtle.colormode(255)
CAR_POSITIONS = [-220, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20,
                 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220]

def random_color():
    rgbl=[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return tuple(rgbl)

class Car(turtle.Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random_color())
        self.setheading(180)
        self.setposition(320, random.choice(CAR_POSITIONS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.car_speed = car_speed

    def drive(self):
        if self.xcor() > - 320:
            self.forward(self.car_speed)