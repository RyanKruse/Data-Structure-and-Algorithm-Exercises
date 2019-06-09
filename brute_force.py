from string import *


def calculations(str1, str2):
    cost = 0
    moves = 0
    str1 = str1.lower()
    str2 = str2.lower()
    alphabet = [chr(i) for i in range(97, 123)]
    str1_alphabet = [0 for i in range(0, 26)]
    str1_list = list(str1)
    str2_alphabet = [0 for i in range(0, 26)]
    str2_list = list(str2)

    for index, letter in enumerate(alphabet, start=0):
        for token in str1_list:
            if letter == token:
                str1_alphabet[index] += 1
        for token in str2_list:
            if letter == token:
                str2_alphabet[index] += 1

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet])

    """
    REMOVE FARTHEST LETTERS.
    """
    for index, token in enumerate(str1_alphabet, start=0):
        while token > str2_alphabet[index]:  # We are removing letters.
            str1_alphabet[index] -= 1  # Lower letter count by 1.
            token -= 1
            cost += 20  # Increase cost by 1.
            moves += 1

            if str1_alphabet[index] == 0:
                # Remove the letter if it is guaranteed 100% not in the other string.
                str1_list.remove(alphabet[index])
            else:
                # We need to remove the letter in a position, but the letter we remove should be the farthest away.
                # i.e. again --> aloud. We want to remove the 2nd 'a' from 'again', not the first since it is correct.
                master_index1 = []
                for index2, token2 in enumerate(str1_list, start=0):
                    if token2 == alphabet[index]:
                        master_index1.append(index2)
                master_index2 = []
                for index2, token2 in enumerate(str2_list, start=0):
                    if token2 == alphabet[index]:
                        master_index2.append(index2)
                print(f'Letter: {alphabet[index].upper()}. Master str2: {master_index2}, Master str1: {master_index1}')

                # Find max distances of index.
                max_distance = 0
                remove_index = 0
                for token_index1 in master_index1:
                    for token_index2 in master_index2:
                        if abs(token_index1 - token_index2) > max_distance:
                            max_distance = abs(token_index1 - token_index2)
                            remove_index = token_index1

                # Remove farthest index letter. Least likely to fall into place
                print(f'Max distance is {max_distance} and remove index is {remove_index}')
                del str1_list[remove_index]

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet, cost])
    """
    ADD LETTERS EXACT POSITION.
    """
    while len(str1_list) < len(str2_list):
        str1_list.append('~')

    for index, token in enumerate(str1_alphabet, start=0):
        while token < str2_alphabet[index]:  # We are removing letters.
            str1_alphabet[index] += 1  # Lower letter count by 1.
            token += 1
            cost += 20  # Increase cost by 1.
            moves += 1

            master_index2 = []
            for index2, token2 in enumerate(str2_list, start=0):
                if token2 == alphabet[index]:
                    master_index2.append(index2)

            # Insert letter.
            master_index1 = []
            for index2, token2 in enumerate(str1_list, start=0):
                if token2 == alphabet[index]:
                    master_index1.append(index2)

            print(f'Alphabet: {alphabet[index]} has master index in str2_list = {master_index2}\n'
                  f'master index in str1_list = {master_index1} Inserting letter in str_list at {master_index2[0]}')
            for index2, token_index2 in enumerate(master_index2, start=0):
                try:
                    if master_index2[index2] == master_index1[index2]:
                        continue  # The letters are already perfectly placed.
                    else:
                        str1_list.insert(token_index2, alphabet[index])
                        str1_list.remove('~')
                        break
                except IndexError:
                    str1_list.insert(token_index2, alphabet[index])
                    str1_list.remove('~')
                    break

    remaining_moves = len(str2) - moves
    cost += remaining_moves * 5
    """
    ALL LETTER PERFECTLY MATCH EACH OTHER IN STR_1 AND STR_2.
    SWAP LETTERS UNTIL STR_1 == STR_2
    """

    result_check([alphabet, str1, str2, str1_list, str2_list, str1_alphabet, str2_alphabet, cost])
    return cost


def result_check(print_input):
    print('\n')
    for items in print_input:
        print(f'{items.__class__.__name__} = {items}')
    print('\n')


# TODO: Figure out how on earth this is solved using a levenshtein algorithm.
# TODO: Consider expanding this problem by having a list of words from dictionary and finding top 5 closest matching.
# TODO: This algorithm can be expanded to include swapping costs and sparing word-to-word fixed transfer cost.
# The fact that again and against has a cost of 60, rather than 40, seems odd as 4 letters are correctly positioned.
# The textbook problem states that transferring letters is like the river problem, each letter transfer costs 5.

# Case in-sensitive
str_1 = 'algorithm'
str_2 = 'alligator'
min_cost = calculations(str_1, str_2)
print(f'The minimum cost of transforming "Algorithm" to "Alligator" is {min_cost}')


class Treasury:
    def __init__(self, items, carry_limit):
        self.items = items
        self.raw_carry_limit = carry_limit
        self.carry_limit = carry_limit
        self.weight_count = [0] * (carry_limit + 1)
        self.max_value = [0] * (carry_limit + 1)
        self.nells_bag = []

    def plot(self):
        for weight in range(self.raw_carry_limit + 1):
            weight_count = weight
            new_item = [1, 2]
            for item in [c for c in self.items if c[0] <= weight]:
                b1 = self.max_value[weight - item[0]] + 1
                b2 = weight_count
                if b1 < b2:
                    weight_count = b1
                    new_item = item
            self.max_value[weight] = weight_count
            self.weight_count[weight] = new_item

    def print_answer(self):
        print(self.nells_bag)
        print(self.weight_count)
        print(self.max_value)
        self.print_items()

    def print_items(self):
        weight = self.raw_carry_limit
        items_used = []
        while weight > 0:
            try:
                this_item = self.weight_count[weight]
            except IndexError:
                break
            if this_item in items_used:
                try:
                    weight += 1
                except IndexError:
                    weight -= 1
            else:
                items_used.append(this_item)
                weight = weight - this_item[0]

        total_weight = 0
        for item in items_used:
            total_weight += item[0]
        if total_weight > self.raw_carry_limit:
            smallest = [99, 99]
            for item in items_used:
                if item[0] < smallest[0]:
                    smallest = item
            if total_weight - smallest[0] <= self.raw_carry_limit:
                items_used.remove(smallest)
            else:
                smallest2 = [99, 99]
                for item in items_used:
                    if item[0] < smallest2[0] and item != smallest:
                        smallest2 = item
                if total_weight - smallest2[0] <= self.raw_carry_limit:
                    items_used.remove(smallest2)
        value_counter = 0
        weight_counter = 0
        for item in items_used:
            print(item)
            value_counter += item[1]
            weight_counter += item[0]
        print(f'Final Weight: {weight_counter} and Final Value: {value_counter}')


items = [[2, 3], [3, 4], [4, 8], [5, 8], [9, 10]]
treasury = Treasury(items, 20)
treasury.plot()
treasury.print_answer()


def quick_sort(alist):
    print('\nLIST INPUT: \t\t\t\t\t\t\t%s\n' % alist)
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    """Helper function for quick sort."""
    # print(alist, "First:", first, "Last:", last)
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last):
    """Helper function for quick sort."""
    # mid_value = alist[len(alist[first:last])//2]
    # print(f"First Value: {first}, Last Value: {last}, Mid Value: {mid_value}")
    pivot_value_index = (len(alist[first:last])//2) + first
    pivot_value = alist[pivot_value_index]
    if pivot_value_index == first:
        first += 1
    print(f'Pivot Value: {pivot_value}, Pivot Value Index {pivot_value_index} first: {first}, last: {last} list: {alist}')
    left_mark = first
    right_mark = last
    done = False

    while not done:
        print(f"Running While Loop. Left: {left_mark}. Right: {right_mark}. Pivot: {pivot_value}. List: {alist}.")
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            print(f"alist[left_mark] = {alist[left_mark]} which is less than pivot value {pivot_value}...")
            left_mark = left_mark + 1
            print(f"Left Mark + 1 = {left_mark}")
        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            print(f"alist[right_mark] = {alist[right_mark]} which is greater than pivot value {pivot_value}...")
            right_mark = right_mark - 1
            print(f"Right Mark - 1 = {right_mark}")
        if right_mark < left_mark:
            done = True
            print("Loop Completed")
            # Catch if both are on left
            if left_mark < pivot_value_index:
                right_mark += 1
        else:
            print("Exchanged left and right marks.")
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[pivot_value_index]
    alist[pivot_value_index] = alist[right_mark]
    alist[right_mark] = temp
    print(f'We swapped {temp} with {alist[pivot_value_index]}')
    print(f"COMPLETE. List --> {alist}\n")
    return right_mark


list_input2 = [4, 9, 6, 10, 7, 5, 1, 3, 8, 2]  # Completely Random List
list_input3 = [3, 1, 4, 2, 5, 7, 8, 6, 10, 9]  # Partially Sorted List
list_input4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Completely Sorted List
list_input5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Completely Reverse Sorted List
list_input6 = [12, 73, 344, 12, -74, 23]
list_input7 = [0, -1, -5, -7, 4]
list_input8 = [0, 62, 0, 0, 2, 5, 0, 2, -2, 4, -2.5, -7.787, 62, 19999, -523, 0, -535, 235, 6.91114]
sorted_lists = []

for list_a in [list_input2, list_input3, list_input4, list_input5, list_input6, list_input7, list_input8]:
    list_b = list_a[:]
    print(f"{list_b} --> {quick_sort(list_b)} --> {list_b}")
    sorted_lists.append(list_b)
    if list_b != sorted(list_a):
        print('There seems to be a problem.')
        break
print('\n\n\n')
for index, list_c in enumerate([list_input2, list_input3, list_input4, list_input5, list_input6, list_input7, list_input8]):
    print(f'{list_c} --> {sorted_lists[index]}')

