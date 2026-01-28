import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.upward, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            score.game_over()
            

    if player.finish():
        player.start()
        cars.increment()
        score.score_board()

screen.exitonclick()