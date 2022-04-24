from turtle import Turtle

FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 280)
        self.write("Level: 1", False, align="left", font=FONT)
    
    def update_score(self, score):
        self.clear()
        self.goto(-250, 280)
        self.write(f"Level: {score}", False, align="left", font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", False, align="center", font=FONT)
        
