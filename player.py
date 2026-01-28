from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)


    def upward(self):
        y_pos = self.ycor() + 10
        self.goto(self.xcor(), y_pos)


    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False