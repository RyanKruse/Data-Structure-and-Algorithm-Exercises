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
        print('The smallest number of persistence ' + str(persistence) + ' is: ' + str(num))
        break

