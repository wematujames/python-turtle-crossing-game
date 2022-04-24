# Game play

'''
1. A turtle moves forwards when you press the "up" key. It can on move forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
2. When the turtle hits the top edge of the screen, it moved back to the original position and the player levels up on
    the next level, the cars speeds up.
3. When the turtle collides with a car, it's game over and everything stops.

'''

# Problem breakdown

'''


1. Create a turtle player that starts fromm the bottom of the screen and listen for the "Up" keypress to move
    northwards.
2. Create cars that are 20px high and 40px wide that are randomly generated along the y-axis and move to the left
    edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe)
    zone for our little turtle. 
    Hint: Generate a new car every sixth time the game loop runs.
3. Detect when the player collides with a car and stop the game when this happens
4. Detect when the turtle player has reached the top edge of the screen (i.e reached FINISH_LINE_Y)
    Return the turtle to the starting position when this happens and increase the speed of the cars.
    Hint: Think about creating an attribute and using MOVE_INCREMENT to increase the cars' speed.
5. Create a scoreboard that keeps track of the player's level. 
    Each time the player crosses successfully, the level should increase.
'''