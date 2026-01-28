from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chan = random.randint(1,6)
        if rand_chan == 1:
            timmy = Turtle("square")
            timmy.color(random.choice(COLORS))
            timmy.penup()
            timmy.shapesize(stretch_wid=1, stretch_len=2)
            rand_y = random.randint(-240, 240)
            timmy.goto(x = 300, y=rand_y)
            self.all_cars.append(timmy)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increment(self):
        self.car_speed += 20