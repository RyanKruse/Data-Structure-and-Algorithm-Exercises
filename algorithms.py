from collections import deque
import random


# ============================================== Find Persistence Script ============================================


"""
Martin Gardner's Hardest Puzzle

A number's persistence is :
The number of steps required to reduce it to a single digit by multiplying all its digits to obtain a second number
Then multiplying all the digits of that number to obtain a third number, and so on until a one-digit number is obtained.

For example : 77 has a persistence of four because it requires four steps to reduce it to one digit: 77-49-36-18-8.
    The smallest number of persistence one is 10
    The smallest of persistence two is 25
    The smallest of persistence three is 39
    The smaller of persistence four is 77

What is the smallest number of persistence five?
"""


def recursion(integers, counter=1):
    """
    This function:
        1) Multiplies all digits in a list with each other. (225 --> [2, 2, 5] --> 2*2*5 --> 20)
        2) Checks to see if that calculation is a single digit. (20 FALSE; 5 TRUE).
        3) If it is a single digit, return our counter, which is the number of recursive calls we made.
        4) If not a single digit, recursively call self and increase counter by 1.

    The number with the smallest persistence of 5 is 679. It is processed recursively like this:
        1) 679 --> 6*7*9 --> 378
        2) 378 --> 3*7*8 --> 168
        3) 168 --> 1*6*8 --> 48
        4) 48  --> 4*8   --> 32
        5) 32  --> 3*2   --> 6
    """
    new_integer = 1
    for integer in integers:
        new_integer = new_integer * integer

    integers = [int(d) for d in str(new_integer)]
    if len(integers) > 1:
        counter += 1
        counter = recursion(integers, counter)
        return counter
    elif len(integers) == 1:
        return counter


persistence = 5
num = 0
while True:
    num += 1
    solution_persistence = recursion([int(d) for d in str(num)])
    if solution_persistence == persistence:
        print('The smallest number of persistence ' + str(persistence) + ' is: ' + str(num) + '\n')
        break


# =============================================== Is Palindrome Script =============================================


def palindrome(a_string):
    """Returns True or False depending on whether or not a word is a palindrome."""
    a_deque = deque()
    # Pushes characters from string to deque.
    for character in a_string:
        if character in ' ,./(){};"[]':
            # Ignores special characters. This can be customized.
            continue
        a_deque.append(character.lower())

    balanced = True
    # Pops first and last characters in deque and compares them.
    while len(a_deque) > 1 and balanced:
        first_character = a_deque.popleft()
        last_character = a_deque.pop()
        if first_character != last_character:
            balanced = False
    # If all left and right characters were the same, returns True. Otherwise, return False.
    return balanced


words = ['radar', 'toot', 'corridor', 'I prefer Pi']
for word in words:
    print("Is '%s' a palindrome? Answer: %s" % (word, palindrome(word)))


# ============================================== Hot Potato Game Script =============================================


class HotPotatoSim:
    def __init__(self, names, max_passes, min_passes, randomized):
        """
        Initializes variables.
        If randomized = False, total passes will equal max_passes always.
        If randomized = True, total passes will equal random integers between min_passes and max_passes."""
        self.queue = deque()
        self.names = names
        self.randomized = randomized
        self.max_passes = max_passes
        self.min_passes = min_passes
        self.passes = self.max_passes
        self.prep_sim()

    def prep_sim(self):
        """Prepares the simulator by filling up the queue."""
        for name in self.names:
            self.queue.append(name)
        print('Here are our players: \n%s, %s has the potato.\n' % (self.names, self.names[0]))

    def run_sim(self):
        """Runs the simulator until there is only one person left."""
        while True:
            if len(self.queue) == 1:
                print('%s is the winner!' % self.queue.popleft())
                break
            if self.randomized:
                self.passes = random.randint(self.min_passes, self.max_passes)
            for _ in range(0, self.passes):
                self.queue.append(self.queue.popleft())
            print('Potato was passed %d times. %s is out.' % (self.passes, self.queue.popleft()))


hot_potato_sim = HotPotatoSim(['Bill', 'Brad', 'Kent', 'Jane', 'Susan', 'David', 'Henry'], 7, 1, True)
hot_potato_sim.run_sim()


# ================================================= Print X Script ===============================================


def print_whitespace(length):
    white_str = ''
    if length == 0:
        return ''
    for value in range(0, length):
        white_str += ' '
    return white_str


def print_x(size, font):
    print('')
    for value in range(0, size):
        if (size - value*2) > 0:
            string = ''
            string += print_whitespace(value)
            string += font
            string += print_whitespace(size - 1 - value*2)
            string += font
            print(string)
        elif (size - value*2) < 0:
            string = ''
            string += print_whitespace(size - 1 - value)
            string += font
            string += print_whitespace(value*2 + 1 - size)
            string += font
            print(string)
    print('')


print_x(11, 'X')


# ================================================= Egg Drop Script ===============================================


def find_height(ans, bottom, height, counter=0, eggs=1):
    """Calculates the max height an egg can survive a fall from a building."""
    check = int(((height - bottom)/2) + bottom)
    if check == bottom and check == height - 1:
        print('Answer is ' + str(check) + ' Total attempts was ' + str(counter) + ' Eggs cracked was ' + str(eggs-1))
    elif check <= ans:
        counter += 1
        print('Egg #' + str(eggs) + ' survived on floor ' + str(check) +
              ' Bottom: ' + str(bottom) + ' Height: ' + str(height))
        find_height(ans, check, height, counter, eggs)
    elif check > ans:
        counter += 1
        print('Egg #' + str(eggs) + ' cracked on floor ' + str(check) +
              ' Bottom: ' + str(bottom) + ' Height: ' + str(height))
        eggs += 1
        find_height(ans, bottom, check, counter, eggs)


# Loop the code.
floor_height = 10
floor_bottom = 1
total_tests = 2
for value in range(1, total_tests + 1):
    answer = random.randint(floor_bottom, floor_height)
    find_height(answer, floor_bottom, floor_height + 1)
    print('The actual answer is: ' + str(answer) + "\n")


# ============================================== Pascal's Triangle Script ============================================


class Pascal:
    def __init__(self, height=3):
        self.rows = 0
        self.height = height

    def space(self, temp_list):
        string = ''
        for char in temp_list:
            if char < 10:
                string += str(char) + '   '
            elif char >= 10:
                string += str(char) + '  '
        for _ in range(10 - self.rows):
            string = '  ' + string
        return string

    def run(self, height):
        if height == 0:
            return []
        elif height == 1:
            return [[1]]
        else:
            new_row = [1]
            result = self.run(height - 1)
            last_row = result[-1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
            result.append(new_row)
        return result

    def print(self, ans):
        self.rows = 0
        for row in ans:
            print(self.space(row))
            self.rows += 1


pascal = Pascal()
pascal.print(pascal.run(9))


# ========================================== Missionaries & Cannibals Script ========================================


class River:
    def __init__(self):
        self.sets = []
        self.filtered = []
        self.position = []
        self.final = []
        self.formatted = []

    def recursion(self, person):
        self.position.append(person)
        if len(self.position) >= 7:
            self.sets.append(self.position[1:])
        else:
            self.recursion(0)
            self.position.pop()
            self.recursion(1)
            self.position.pop()

    def process(self):
        for t in self.sets:
            temp = 0
            for num in t:
                temp += num
            if temp == 3:
                self.filtered.append(t)
        for t in self.filtered:
            boat1 = t[0] + t[1]
            boat2 = t[2] + t[3]
            boat3 = t[4] + t[5]
            if boat1 + boat2 != 3 and boat2 + boat3 != 3:
                self.final.append(t)
        for t in self.final:
            self.formatted.append([[t[0], t[1]], [t[2], t[3]], [t[4], t[5]]])

    def answer(self):
        print('\nThe answer to the boat problem (0 = Missionary; 1 = Cannibal):')
        for t in self.formatted:
            print(f'\t{t}')
        print('')


# Missionaries are 0, Carnivores are 1
river = River()
river.recursion(0)
river.process()
river.answer()


# ================================================ Water Jug Script ===============================================


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


jug_4 = Jug(4)
jug_3 = Jug(3)
solution(jug_4, jug_3)

jug_4 = Jug(4)
jug_3 = Jug(3)
solution(jug_3, jug_4)


# ============================================== Tower of Hanoi Script ==============================================


class TowerOfHanoi:
    def __init__(self):
        self.begin = deque()
        self.end = deque()
        self.middle = deque()
        self.disks = 3

    def __str__(self):
        temp = ''
        temp += 'Begin: ' + str([x for x in self.begin])
        temp += '   Middle: ' + str([x for x in self.middle])
        temp += '   End: ' + str([x for x in self.end])
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
        tp.append(fp.pop())
        print(str(self))


tower_of_hanoi = TowerOfHanoi()
tower_of_hanoi.prep_tower()
print(tower_of_hanoi)
tower_of_hanoi.move_tower(tower_of_hanoi.disks, tower_of_hanoi.begin, tower_of_hanoi.end, tower_of_hanoi.middle)


# ============================================== Make Change Script ==============================================


def make_change(coin_list, coin_input, min_coins, coins_used):
    for cents in range(coin_input + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[coin_input]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(str(this_coin) + ", ", end='')
        coin = coin - this_coin
    print("= " + str(change) + " cents.\n")


coin_list = [1, 5, 10, 25]
coin_input = 142
coin_count = [0]*(coin_input+1)
coins_used = [0]*(coin_input+1)
make_change(coin_list, coin_input, coin_count, coins_used)
print_coins(coins_used, coin_input)