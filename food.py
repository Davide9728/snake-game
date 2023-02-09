from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self): #it make new blue food sphere
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self): #it move food in another position
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
