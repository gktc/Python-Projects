from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#Initialize the screen and turtle
screen = Screen()

#Setup the screen
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = Scoreboard()
scoreBoard.update_scoreboard()

#Keyboard bindings

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "i")
screen.onkey(r_paddle.go_down, "k")  

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")  

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 40 or ball.xcor() < -320 and ball.distance(l_paddle) < 40:
        ball.bounce_x()
        
    
    # Missed        paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreBoard.l_point() 

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreBoard.r_point()

screen.exitonclick()
    
