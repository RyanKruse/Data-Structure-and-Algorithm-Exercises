from turtle import *


class SnowFlake:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed('fastest')
        self.window = self.turtle.getscreen()

    def draw(self, distance, iterations):
        for i in range(3):
            self.mountain(distance, iterations)
            self.turtle.right(120)

    def mountain(self, distance, iterations):
        if iterations == 0:
            self.turtle.forward(distance)
        else:
            for rotation in [60, -120, 60, 0]:
                self.mountain(distance/3, iterations-1)
                self.turtle.left(rotation)


snowflake = SnowFlake()
snowflake.draw(300, 5)
snowflake.window.exitonclick()
