from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.write("Scoreboard:0", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()
        self.upscore = 0
        self.levelnum = 1

    def increase(self):
        self.clear()
        self.goto(0, 250)
        self.upscore = self.upscore+1
        self.write(f"Scoreboard:{self.upscore}", align="center", font=("Courier", 24, "normal"))

    def collide(self):
        self.goto(0, 0)
        self.color("red")
        self.write("You got squished! Game over", align="center", font=("Courier", 20, "bold"))

    def level(self):
        self.goto(-240, 250)
        self.write(f"Level:{self.levelnum}", align="center", font=("Courier", 20, "normal"))