from turtle import *

# ================================================== Draw Snowflake ===============================================


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
snowflake.draw(300, 3)
snowflake.turtle.hideturtle()


# ==================================================== Draw Maze =================================================


def hilbert_maze(length, iteration, char, first=False):
    if first:
        length = int(length / (2.4**iteration))

    if iteration > 0:
        if char == 'a':
            seq = "-bF+aFa+Fb-"
        else:
            seq = "+aF-bFb-Fa+"

        for char in seq:
            if char == "F":
                turtle.backward(length)
            elif char == "+":
                turtle.left(90)
            elif char == "-":
                turtle.right(90)
            elif char == "a":
                hilbert_maze(length, iteration - 1, 'a')
            elif char == "b":
                hilbert_maze(length, iteration - 1, 'b')


turtle = Turtle()
window = turtle.getscreen()
turtle.speed('fastest')
hilbert_maze(600, 4, 'a', True)
window.exitonclick()
