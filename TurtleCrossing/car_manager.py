COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.__all_cars = []

    def get_all_cars(self):
        return self.__all_cars

    def create_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid = 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-200, 200))
            self.__all_cars.append(new_car)

    def move(self):
        for car in self.__all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    @staticmethod
    def increase_speed():
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

