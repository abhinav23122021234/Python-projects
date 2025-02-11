import turtle

import random
screen=turtle.Screen()
screen.setup(width=1500,height=700)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? ").lower()
all_turtle=[]
race_on=False

colors=["red","blue","green","yellow","purple","orange"]
y_position=[-150,-90,-30,30,90,150]

for i in range (0,6):
    tim=turtle.Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.speed(1000)
    tim.goto(x=-730,y=y_position[i])
    all_turtle.append(tim)

if user_bet  :
    race_on = True


while race_on:
    for turtle in all_turtle:
        if turtle.xcor()>730:
            winner=turtle.pencolor()
            if winner==user_bet:
                print("You've won the race,congrats")
            else:
                print(f"You lost ,winner is {winner} turtle")

            race_on = False
        turtle.forward(random.randint(10,30))

screen.exitonclick()
