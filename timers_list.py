import pygal
import timeit
from random import randint, randrange, sample


# ================================================== Test 1 ========================================================


print("\nPopping the first element is O(n). Popping the last element is O(1).\n%27s %16s" % ('pop(0)', 'pop()'))
pop_last_time = timeit.Timer("x.pop()", "from __main__ import x")
pop_first_time = timeit.Timer("x.pop(0)", "from __main__ import x")

for list_size in range(100000, 500001, 100000):
    x = list(range(list_size))
    pop_last_speed = pop_last_time.timeit(number=1000)

    x = list(range(list_size))
    pop_first_speed = pop_first_time.timeit(number=1000)
    print("List size %d: %10.5f  %15.5f" % (list_size, pop_first_speed, pop_last_speed))


# ================================================== Test 2 ========================================================


print("\nAccessing an item using the index of a list is O(1).\n%26s" % 'Index')
index_time = timeit.Timer("x[" + str(randint(1, 100000)) + "]", "from __main__ import randint,x")

for list_size in range(100000, 500001, 100000):
    x = list(range(list_size))
    index_speed = index_time.timeit(number=1000)
    print("List size %d: %10.5f" % (list_size, index_speed))


# ================================================== Test 3 ========================================================


print("\nThe get and set operator of a dictionary is O(1).\n%24s %16s" % ('Get', 'Set'))
get_time = timeit.Timer("x.get(randrange(%d))" % list_size, "from __main__ import randrange,x")  # Alternate Rand
set_time = timeit.Timer("x[randrange(%d)] = None" % list_size, "from __main__ import randrange,x")

for list_size in range(100000, 500001, 100000):
    x = {k: None for k in range(list_size)}
    get_speed = get_time.timeit(number=1000)

    x = {k: None for k in range(list_size)}
    set_speed = set_time.timeit(number=1000)
    # set_speed is slower than get_speed since we are calling randrange twice.
    print("List size %d: %10.5f  %15.5f" % (list_size, get_speed, set_speed))


# ================================================== Test 4 =========================================================


def test1(my_list):
    while my_list:
        del my_list[randrange(len(my_list))]


def test2(my_dict):
    for key in sample(my_dict.keys(), len(my_dict)):
        del my_dict[key]


def test3(my_dict):
    for num in range(len(my_dict)):
        del my_dict[num]


print("\nThe del operator for a list is O(n) and for a dictionary is O(1).\n%24s %16s %17s" % ('List', 'Dict', 'Dict2'))
del_list_time = timeit.Timer("test1(x)", "from __main__ import test1,x")
del_dict_time = timeit.Timer("test2(x)", "from __main__ import test2,x")
del_dict2_time = timeit.Timer("test3(x)", "from __main__ import test3,x")

for list_size in range(10000, 50001, 10000):
    x = list(range(list_size))
    del_list_speed = del_list_time.timeit(number=100)

    x = {k: None for k in range(list_size)}
    del_dict_speed = del_dict_time.timeit(number=100)

    x = {k: None for k in range(list_size)}
    del_dict2_speed = del_dict2_time.timeit(number=100)
    print("List size %d: %10.5f  %15.5f  %15.5f" % (list_size, del_list_speed, del_dict_speed, del_dict2_speed))


# ================================================== Test 5 ========================================================


def test4(my_list):
    lowest_num = 1000000
    for number in my_list:
        if number < lowest_num:
            lowest_num = number
    return lowest_num


def test5(my_list):
    my_list.sort()
    return my_list[0]


print('\nFind the smallest number in an unordered list of random numbers. \n%26s %19s' % ('Linear', 'O(nlog(n))'))
linear_search_time = timeit.Timer("test4(x)", "from __main__ import test4,x")
nlogn_search_time = timeit.Timer("test5(x)", "from __main__ import test5,x")

for list_size in range(10000, 50001, 10000):
    x = sample(range(1, list_size), list_size - 1)
    linear_list_speed = linear_search_time.timeit(number=100)

    x = sample(range(1, list_size), list_size - 1)
    nlogn_search_speed = nlogn_search_time.timeit(number=100)
    print("List size %d: %10.5f %15.5f" % (list_size, linear_list_speed, nlogn_search_speed))


# ================================================== Test 6 ========================================================


print("\nPopping the first element is O(n). Popping the last element is O(1).\n%27s %16s" % ('pop(0)', 'pop()'))
pop_last_time = timeit.Timer("x.pop()", "from __main__ import x")
pop_first_time = timeit.Timer("x.pop(0)", "from __main__ import x")
pop_first_list = []
pop_last_list = []

for list_size in range(10000, 50001, 10000):
    x = list(range(list_size))
    pop_last_speed = pop_last_time.timeit(number=1000)
    pop_last_list.append(pop_last_speed)

    x = list(range(list_size))
    pop_first_speed = pop_first_time.timeit(number=1000)
    pop_first_list.append(pop_first_speed)
    print("List size %d: %10.5f  %15.5f" % (list_size, pop_first_speed, pop_last_speed))

# Visually chart the data from the two lists.
print('\nNote: The above data for the popping test was graphed into the project folder as timeit.list_pop.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of Popping First and Last 1000 Elements in a List"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Size of List"
bar_chart.y_title = "Speed of Pop"
bar_chart.add('Popping First', pop_first_list)
bar_chart.add('Popping Last', pop_last_list)
bar_chart.render_to_file('graphs/timeit.list_pop.svg')
