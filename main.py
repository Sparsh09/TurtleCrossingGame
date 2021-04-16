import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
t = Player()

screen.listen()
screen.onkey(t.move , "Up" )

game_is_on = True
game_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_counter += 1
    if game_counter % 6 == 0:
        car_manager.create_car()
    car_manager.movement(0)

    if t.ycor() == 280:
        t.reached_finish_line()
        car_manager.movement(1)
        scoreboard.update()


    for car in car_manager.all_car:
        if car.distance(t) < 25:
            scoreboard.finish()
            game_is_on = False


screen.exitonclick()