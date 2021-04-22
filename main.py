# import modules
from player import PlayerTurtle
from car import Car
from scoreboard import Scoreboard
from options import car_speed
import time
from help_functions import *

# create game window
screen = create_screen()
screen.listen()

# create scoreboard
scoreboard = Scoreboard()

# create turtle
turtle = PlayerTurtle()

# create cars
cars = []
car = Car(scoreboard.car_speed)
cars.append(car)

# main loop
screen.update()
game_is_on = True
while game_is_on:
    # check events
    check_keys(screen, turtle)
    # update screen
    update_graphics(screen, scoreboard)
    # calculate game physics
    game_is_on, cars = update_physics(scoreboard, turtle, cars)
    print(len(cars))
    # slow down loop
    time.sleep(0.1)


# exit screen on mouse click
screen.exitonclick()
