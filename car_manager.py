from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def level1(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def level2(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1 or random_chance == 3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def level_3(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1 or random_chance == 3 or random_chance == 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def final_level(self):
        random_chance = random.randint(1, 6)
        if random_chance <= 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - MOVE_INCREMENT
            if car.xcor() > -300:
                car.goto(new_x, car.ycor())
            else:
                car.hideturtle()