from random import randint

def print_whitespace(length):
    white_str = ''
    if length == 0:
        return ''
    for value in range(0, length):
        white_str += ' '
    return white_str


def print_x(size, font):
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


print_x(11, 'X')


def find_height(ans, bottom, height, counter=0, eggs=1):
    """Calculates the max height an egg can survive a fall from a building."""
    check = int(((height - bottom)/2) + bottom)
    if check == bottom and check == height - 1:
        print('The answer is ' + str(check) + ' Total attempts was ' + str(counter) + ' Eggs cracked was ' + str(eggs-1))
    elif check <= ans:
        counter += 1
        print('Egg #' + str(eggs) + ' survived on floor ' + str(check) + ' Bottom: ' + str(bottom) + ' Height: ' + str(height))
        find_height(ans, check, height, counter, eggs)
    elif check > ans:
        counter += 1
        print('Egg #' + str(eggs) + ' cracked on floor ' + str(check) + ' Bottom: ' + str(bottom) + ' Height: ' + str(height))
        eggs += 1
        find_height(ans, bottom, check, counter, eggs)


# Loop the code.
floor_height = 10
floor_bottom = 1
total_tests = 2
for value in range(1, total_tests + 1):
    answer = randint(floor_bottom, floor_height)
    find_height(answer, floor_bottom, floor_height + 1)
    print('The actual answer is: ' + str(answer))

