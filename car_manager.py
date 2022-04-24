from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [(300, -200),(300, -150),(300, -100),(300,-50),(300, 0),(300,50),(300,100),(300,150),(300,200)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_increment = MOVE_INCREMENT
        self.level = 1

    def make_new_car(self):
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.choice(POSITIONS))
            new_car.left(180)
            new_car.shapesize(stretch_len=2)
            new_car.forward(self.move_increment)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_increment * self.level) 





