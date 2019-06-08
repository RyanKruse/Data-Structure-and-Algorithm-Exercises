import time
from collections import deque
from turtle import *


def factorial(num):
    """Computes factorial of a number."""
    if num == 0:
        return 1
    return factorial(num - 1) * num


def reverse(a_list):
    """Reverses a list."""
    if len(a_list) == 1:
        return a_list
    return [a_list[-1]] + reverse(a_list[:-1])


print(reverse([1, 2, 3, 4, 5]))
print(factorial(5))


def recursive_fibonacci(iterations):
    if iterations <= 0:
        return 1
    return recursive_fibonacci(iterations - 2) + recursive_fibonacci(iterations - 1)


def iterative_fibonacci(iterations):
    sequences = [1, 1]
    for num in range(1, iterations + 1):
        sequences.append(sequences[-1] + sequences[-2])
    return sequences[-1]


it_times = []
re_times = []
for num in range(20, 31):
    print(f'Iteration {num}:')

    start = time.time()
    print(f'\tRecursive: {recursive_fibonacci(num)}')
    print(f'\tRecursive Speed: {(time.time() - start) * 1000} milliseconds')
    start = time.time()
    print(f'\tIterative: {iterative_fibonacci(num)}')
    print(f'\tIterative Speed: {(time.time() - start) * 1000} milliseconds')

# Conclusion. Recursive is slower.


def mountain_boss(length, iteration):
    if iteration > 0:
        for rotation in [60, -120, 60, 0]:
            mountain_boss(length/3, iteration - 1)
            turtle.left(rotation)
    else:
        turtle.forward(length)


turtle = Turtle()
window = turtle.getscreen()
turtle.speed('fastest')
mountain_boss(400, 3)


def karate_boss(length, iteration, char, first=False):
    if first:
        length = int(length / (2.4**iteration))

    if iteration > 0:  # This is the base case. It is good!
        if char == 'a':
            seq = "-bF+aFa+Fb-"
        else:
            seq = "+aF-bFb-Fa+"

        for char in seq:
            if char == "F":
                turtle.forward(length)
            elif char == "+":
                turtle.right(90)
            elif char == "-":
                turtle.left(90)
            elif char == "a":
                karate_boss(length, iteration - 1, 'a')
            elif char == "b":
                karate_boss(length, iteration - 1, 'b')


# TODO: Length decrease based on degrees.
turtle = Turtle()
window = turtle.getscreen()
turtle.speed('fastest')
karate_boss(400, 3, 'a', True)
window.exitonclick()


class Jug:
    def __init__(self, capacity):
        self.filled = []
        self.capacity = capacity

    def __str__(self):
        return str(self.filled)

    def pump(self):
        while len(self.filled) < self.capacity:
            self.filled.append(1)
        print(f'Pumped {self.__class__.__name__}({self.capacity}) - {self.filled}.')

    def empty(self):
        self.filled = []
        print(f'Emptied {self.__class__.__name__}({self.capacity}){self.filled}.')

    def pour(self, other):
        while len(other.filled) < other.capacity:
            if self.filled:
                other.filled.append(self.filled.pop())
            else:
                break
        print(f'Poured {self.__class__.__name__}({self.capacity}){self.filled} into '
              f'{other.__class__.__name__}({other.capacity}){other.filled}.')


def solution(jug1, jug2):
    # TODO: There might be fewer steps necessary to solve (last 2 are identical to first 2.)
    jug1.pump()
    jug1.pour(jug2)
    jug2.empty()
    jug1.pour(jug2)
    jug1.pump()
    jug1.pour(jug2)
    if len(jug1.filled) == 2:
        print(f'{jug1.__class__.__name__}({jug1.capacity}){jug1.filled} is filled with 2 gallons.\n')
        return
    else:
        print('Recursively calling self.')
        solution(jug2, jug1)


# TODO: Clean up this code and split it into the appropriate files.

jug_4 = Jug(4)
jug_3 = Jug(3)
solution(jug_4, jug_3)

jug_4 = Jug(4)
jug_3 = Jug(3)
solution(jug_3, jug_4)