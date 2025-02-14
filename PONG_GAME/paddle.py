from turtle import Turtle,Screen
screen=Screen()

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x=x_cor
        self.y=y_cor
        # TODO.2)Create and move a paddle
        #  paddle dimensions : width=20,height=100,x_pos=350,y_pos=0
        #  each key press (up,down) should move paddle by 20 px
        screen.tracer(0)
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)  # default size is 20,20.str_width=5 means 5 times original value
        self.color("white")
        self.penup()
        self.goto(self.x,self.y)


    def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


