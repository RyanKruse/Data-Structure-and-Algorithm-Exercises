import time
from collections import deque
from turtle import *


class TowerOfHanoi:
    def __init__(self):
        self.begin = deque()
        self.end = deque()
        self.middle = deque()
        self.disks = 4

    def __str__(self):
        temp = ''
        temp += 'Begin: ' + str([x for x in self.begin])
        temp += '\nMiddle: ' + str([x for x in self.middle])
        temp += '\nEnd: ' + str([x for x in self.end])
        return temp

    def prep_tower(self):
        for num in range(self.disks, 0, -1):
            self.begin.append(num)

    def move_tower(self, height, from_pole, to_pole, with_pole):
        if height >= 1:
            self.move_tower(height-1, from_pole, with_pole, to_pole)
            self.move_disk(from_pole, to_pole)
            self.move_tower(height-1, with_pole, to_pole, from_pole)

    def move_disk(self, fp, tp):
        # print(f"moving disk from {fp} to {tp}.")
        tp.append(fp.pop())
        print('\n' + str(self))


# TODO: Consider implementing a turtle visual graphic to show blocks moving.
# TODO: Conceptualize how this code works in the recursive calls.
tower_of_hanoi = TowerOfHanoi()
tower_of_hanoi.prep_tower()
print(tower_of_hanoi)
tower_of_hanoi.move_tower(tower_of_hanoi.disks, tower_of_hanoi.begin, tower_of_hanoi.end, tower_of_hanoi.middle)