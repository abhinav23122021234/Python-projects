from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10

    def move(self):
        x_new=self.xcor()+self.x_move
        y_new=self.ycor()+self.y_move
        self.goto(x_new,y_new)

    #TODO 5.) BOUNCING LOGIC
    def bounce(self):
        self.y_move*=-1
    #TODO 6.) Reflecting logic , in case of paddle collision
    def reflect(self):
        self.x_move*=-1
    def reset_position(self):
        self.goto(0,0)
        self.x_move*=-1
