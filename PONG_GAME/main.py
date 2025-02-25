 #TODO.1) Create screen with basic setup,title,background color,exitonclick
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
game_on = True
time_sleep=1
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Welcome to Pong")

#TODO 3.)Create another paddle using paddle class
r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
scoreboard=Scoreboard()
#TODO 4.) Create ball class and make it move without lag
ball=Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_on:
    time.sleep(0.1/time_sleep)
    ball.move()
    screen.update()
    #Detect collision
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if (l_paddle.distance(ball)<20 or r_paddle.distance(ball)<20) or ((ball.xcor()>320 or ball.xcor()<-320) and (l_paddle.distance(ball)<50 or r_paddle.distance(ball)<50)) :
        ball.reflect()
        time_sleep+=0.5

    #TODO 7.) DETECT when paddle misses
    #TODO 8.) add scoreboard logic
    #for r_paddle
    if ball.xcor()>380:
        ball.reset_position()
        time_sleep=1
        scoreboard.l_score+=1
        scoreboard.update_scoreboard()
    #for l_paddle
    if ball.xcor()<-380:
        ball.reset_position()
        time_sleep=1
        scoreboard.r_score+=1
        scoreboard.update_scoreboard()

screen.exitonclick()

main.py
