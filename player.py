from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")

    def forward_movement(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def backward_movement(self):
        self.setheading(90)
        self.backward(MOVE_DISTANCE)

    def turn_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def turn_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

