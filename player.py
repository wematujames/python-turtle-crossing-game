from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player (Turtle):
    def __init__(self):
        super().__init__()
        self.starting_position = STARTING_POSITION
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(self.starting_position)

    def move(self):
        self.forward(MOVE_DISTANCE)
        