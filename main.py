from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.listen()

# Player setup / Movement
bernice = Player()
screen.onkey(key="Up", fun=bernice.move)

# Init cars
cars = CarManager()

# Init scoreboard
score = Scoreboard()

move_count = 0
game_on = True
while game_on:
    move_count += 1
    time.sleep(0.1)
    screen.update()
    cars.move()
    
    # check if loop is running for the sixth time and make new_car
    if move_count == 5:
        cars.make_new_car()
        move_count = 0
    
    #check if level complete 
    if bernice.ycor() == 300:
        bernice.goto(bernice.starting_position)
        cars.level += 1
        score.update_score(cars.level)
        
    #check for collision with car / game over
    for i in cars.cars:
        if bernice.distance(i) < 20:
            game_on = False
            score.game_over()
    

screen.exitonclick()