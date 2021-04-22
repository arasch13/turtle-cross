from turtle import Turtle


class PlayerTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black", "green")
        self.penup()
        self.reset()

    def reset(self):
        self.goto(self.xcor(), -280)

    def move_forwards(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_backwards(self):
        if self.ycor() > - 280:
            self.goto(self.xcor(), self.ycor() - 20)
