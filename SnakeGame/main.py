import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

snake = Snake()


game_is_on = True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()

screen.exitonclick()

