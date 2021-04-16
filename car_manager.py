from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car = []

    def movement(self, speed):
        if speed == 1:
            global STARTING_MOVE_DISTANCE
            STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.all_car:
            # print(speed)
            car.backward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_car.append(new_car)

    # def increase_speed(self):
    #     inc_speed = MOVE_INCREMENT + STARTING_MOVE_DISTANCE
    #     print(inc_speed)
    #     self.movement(inc_speed)
