from turtle import Screen
from options import car_spawn
from car import Car
import random


def create_screen():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.title("Turtle Cross")
    screen.tracer(0)
    return screen


def check_keys(screen, turtle):
    screen.onkeypress(fun=turtle.move_forwards, key="Up")
    screen.onkeypress(fun=turtle.move_backwards, key="Down")


def update_physics(scoreboard, turtle, cars):
    cars = delete_vanished_car(cars)
    check_turtle_at_target(scoreboard, turtle)
    if create_new_car(car_spawn):
        car = Car(scoreboard.car_speed)
        cars.append(car)
    for car in cars:
        car.drive()
    return check_car_collision(scoreboard, turtle, cars), cars


def update_graphics(screen, scoreboard):
    screen.update()
    scoreboard.update()


def delete_vanished_car(cars):
    for index, car in enumerate(cars):
        if car.xcor() < -300:
            car.hideturtle()
            cars.pop(index)
    return cars


def check_turtle_at_target(scoreboard, turtle):
    if turtle.ycor() == 280:
        turtle.reset()
        scoreboard.increase_level()


def create_new_car(probability):
    return random.random() < probability


def check_car_collision(scoreboard, turtle, cars):
    for car in cars:
        if car.xcor() < 20 and car.xcor() >= -20 and abs(turtle.ycor() - car.ycor()) < 20:
            scoreboard.game_over()
            return False
    return True
