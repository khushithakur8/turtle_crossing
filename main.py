import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
score = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=player.forward_movement)
screen.onkey(key="Down", fun=player.backward_movement)
screen.onkey(key="Right", fun=player.turn_right)
screen.onkey(key="Left", fun=player.turn_left)
score.level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if score.levelnum == 1:
        manager.level1()
        manager.move()

    if player.ycor() > 280:
        score.increase()
        player.goto(0, -280)
        score.levelnum = score.levelnum+1
        score.level()

    if 1 < score.levelnum < 4:
        manager.level2()
        manager.move()

    if 4 <= score.levelnum <= 6:
        manager.level_3()
        manager.move()

    if score.levelnum > 6:
        manager.final_level()
        manager.move()

    for car in manager.all_cars:
        if car.distance(player) < 20:
            score.collide()
            game_is_on = False

screen.exitonclick()