from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290,250)
        self.write(f"Level: {self.level} ", align ="Left", font=FONT)
        

    def score_board(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level} ", align ="Left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!" , align=ALIGNMENT , font= FONT)
