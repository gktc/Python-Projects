import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.onkey(player.up, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move()

    #Detect collision
    for car in car_manager.get_all_cars():
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.finish_line_crossed():
        scoreboard.next_level()
        player.go_to_start()
        car_manager.increase_speed()
    screen.update()

screen.mainloop()
