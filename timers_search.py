import pygal
import timeit
import random


def recursive_binary_search_helper(alist, item):
    alist.sort()
    recursive_binary_search(alist, item)


def recursive_binary_search(alist, item):
    # Base cases
    if len(alist) == 0:
        return False
    mid_index = len(alist) // 2  # "//" converts operand to int, rounding down to nearest whole number.
    mid_item = alist[mid_index]
    if mid_item == item:
        return True

    # Recursive calls.
    if item < mid_item:
        return recursive_binary_search(alist[:mid_index], item)  # Search bottom half.
    else:
        return recursive_binary_search(alist[mid_index + 1:], item)  # Search top half.


def recursive_binary_search_pass_helper(alist, item):
    return recursive_binary_search_pass(alist, item, 0, len(alist) - 1)


def recursive_binary_search_pass(alist, item, first, last):
    # Base cases
    mid_index = ((last - first) // 2) + first
    mid_item = alist[mid_index]
    if mid_item == item:
        return True
    elif ((last - first) // 2) == 0:
        return False

    # Recursive calls.
    if item < mid_item:
        return recursive_binary_search_pass(alist, item, first, mid_index)  # Search bottom half.
    else:
        return recursive_binary_search_pass(alist, item, mid_index + 1, last)  # Search top half.


def iterative_binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def ordered_sequential_search(alist, item):
    i = 0
    while i < len(alist) and alist[i] <= item:
        if alist[i] == item:
            return True
        i += 1
    return False


def sequential_search(alist, item):
    i = 0
    while i < len(alist):
        if alist[i] == item:  # Item found.
            return True
        i += 1
    return False


def python_search(alist, item):
    if item in alist:
        return True
    return False


# ================================================== Test 1 ========================================================


print("\nSearching random elements in ordered list using sequential search vs. recursive binary search vs. Python In.")
print('%27s%18s%18s' % ('Ord Sequential', 'Ord Binary', 'Ord Python'))
sequential_time = timeit.Timer("ordered_sequential_search(x,random.randint(1, size))",
                               "from __main__ import ordered_sequential_search,x,size,random")
binary_time = timeit.Timer("recursive_binary_search(x,random.randint(1, size))",
                           "from __main__ import recursive_binary_search,x,size,random")
python_time = timeit.Timer("python_search(x,random.randint(1, size))",
                           "from __main__ import python_search,x,size,random")
ord_sequential_times = []
ord_recursive_binary_times = []
ord_python_times = []

for size in range(10, 411, 100):
    temp = list(range(1, 1000))

    x = random.sample(temp, size)
    x.sort()
    sequential_speed = sequential_time.timeit(number=10000)
    ord_sequential_times.append(sequential_speed)

    x = random.sample(temp, size)
    x.sort()
    recursive_binary_speed = binary_time.timeit(number=10000)
    ord_recursive_binary_times.append(recursive_binary_speed)

    x = random.sample(temp, size)
    x.sort()
    python_speed = python_time.timeit(number=10000)
    ord_python_times.append(python_speed)

    print("Size %d: %10.5f  %20.5f  %20.5f"
          % (size, sequential_speed, recursive_binary_speed, python_speed))


# ================================================== Test 2 ========================================================


print("\nSearching random elements in unordered list using sequential search vs. recursive binary search vs Python In.")
print('%29s%18s%18s' % ('Unord Sequential', 'Unord Binary', 'Unord Python'))
sequential_time = timeit.Timer("sequential_search(x,random.randint(1, size))",
                               "from __main__ import sequential_search,x,size,random")
binary_time = timeit.Timer("recursive_binary_search_helper(x,random.randint(1, size))",
                           "from __main__ import recursive_binary_search_helper,x,size,random")
unord_sequential_times = []
unord_recursive_binary_times = []
unord_python_times = []

for size in range(10, 411, 100):
    x = random.sample(list(range(1, size + 1)), size)
    sequential_speed = sequential_time.timeit(number=10000)
    unord_sequential_times.append(sequential_speed)

    x = random.sample(list(range(1, size + 1)), size)
    recursive_binary_speed = binary_time.timeit(number=10000)
    unord_recursive_binary_times.append(recursive_binary_speed)

    x = random.sample(list(range(1, size + 1)), size)
    python_speed = python_time.timeit(number=10000)
    unord_python_times.append(python_speed)

    print("Size %d: %10.5f  %20.5f  %20.5f"
          % (size, sequential_speed, recursive_binary_speed, python_speed))


print('\nThe above data for the sequential and binary search was graphed as timeit.seq_bin_search.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of Python, Binary, and Sequential Searches in Ordered and Randomly Sorted Lists"
bar_chart.x_labels = ['10', '110', '210', '310', '410']
bar_chart.x_title = "List Size"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('Ord Python', ord_python_times)
bar_chart.add('Ran Python', unord_python_times)
bar_chart.add('Ord Binary', ord_recursive_binary_times)
bar_chart.add('Ran Binary', unord_recursive_binary_times)
bar_chart.add('Ord Sequential', ord_sequential_times)
bar_chart.add('Ran Sequential', unord_sequential_times)
bar_chart.render_to_file('graphs/timeit.seq_bin_search.svg')


# ================================================== Test 3 ========================================================

print("\nSearching random elements in an ordered list using customized binary searches.")
print('%29s%18s%21s' % ('Recursive Binary', 'Iterative Binary', 'Recursive Binary'))
recursive_binary_time = timeit.Timer("recursive_binary_search(x,random.randint(1, size))",
                                     "from __main__ import recursive_binary_search,x,size,random")
iterative_binary_time = timeit.Timer("iterative_binary_search(x,random.randint(1, size))",
                                     "from __main__ import iterative_binary_search,x,size,random")
recursive_binary_pass_time = timeit.Timer("recursive_binary_search_pass_helper(x,random.randint(1, size))",
                                          "from __main__ import recursive_binary_search_pass_helper,x,size,random")
ord_recursive_binary_times = []
ord_iterative_binary_times = []
ord_recursive_binary_pass_times = []

for size in range(10, 411, 100):
    temp = list(range(1, 1000))

    x = random.sample(temp, size)
    x.sort()
    recursive_binary_speed = recursive_binary_time.timeit(number=10000)
    ord_recursive_binary_times.append(recursive_binary_speed)

    x = random.sample(temp, size)
    x.sort()
    iterative_binary_speed = iterative_binary_time.timeit(number=10000)
    ord_iterative_binary_times.append(iterative_binary_speed)

    x = random.sample(temp, size)
    x.sort()
    recursive_binary_pass_speed = recursive_binary_pass_time.timeit(number=10000)
    ord_recursive_binary_pass_times.append(recursive_binary_pass_speed)

    print("Size %d: %10.5f  %20.5f  %20.5f"
          % (size, recursive_binary_speed, iterative_binary_speed, recursive_binary_pass_speed))