def bubble_sort(alist):
    print('\nLIST INPUT: \t\t %s' % alist)
    for pass_num in range(len(alist) - 1, 0, -1):
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        print('PASS %d: Bubble Sort: %s' % (pass_num, alist))


def short_bubble_sort(alist):
    """An extension of the bubble sort function, modified so that a bubble sort stops early if list is sorted."""
    exchanges = True
    pass_num = len(alist) - 1
    print('\nLIST INPUT: \t\t\t   %s' % alist)
    while pass_num > 0 and exchanges:
        exchanges = False  # Stops sort early
        for i in range(pass_num):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        pass_num = pass_num - 1
        print('PASS %d: Short Bubble Sort: %s' % (pass_num, alist))


def selection_sort(alist):
    print('\nLIST INPUT: \t\t\t%s' % alist)
    for fills_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fills_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location
        temp = alist[fills_slot]
        alist[fills_slot] = alist[position_of_max]
        alist[position_of_max] = temp
        print('PASS %d: Selection Sort: %s' % (fills_slot, alist))


def insertion_sort(alist):
    print('\nLIST INPUT: \t\t\t%s' % alist)
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position = position - 1
        alist[position] = current_value
        print('PASS %d: Insertion Sort: %s' % (index, alist))


def shell_sort(alist):
    print('\nLIST INPUT: \t\t\t\t\t\t\t   %s' % alist)
    start_increment = 2
    sublist_count = len(alist) // start_increment
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        print("After increments of size", sublist_count, "the list is now    ", alist)
        sublist_count = sublist_count // 2


def gap_insertion_sort(alist, start, gap):
    """Helper function for shell sort."""
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value
        print('\t\t\t\t\t   GAP INSERTION SORT END: %s' % alist)


def merge_sort(alist):
    print("Splitting ", alist)

    if len(alist) <= 1:
        # Base Case
        pass

    else:
        # Split
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        # Do Math
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1

    print("Merging ", alist)


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
    pivot_value = alist[first]
    print(f'Pivot Value: {pivot_value}, first: {first}, last: {last} list: {alist}')
    left_mark = first + 1
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
        else:
            print("Exchanged left and right marks.")
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp
    print(f"COMPLETE. List --> {alist}\n")
    return right_mark


def test_sort(alist):
    sort_names = ['Bubble Sort', 'Short Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Shell Sort',
                  'Merge Sort', 'Quick Sort']
    sort_functions = ['bubble_sort', 'short_bubble_sort', 'selection_sort', 'insertion_sort', 'shell_sort',
                      'merge_sort', 'quick_sort']
    for index, sort_type in enumerate(sort_names, start=0):
        unsorted_list = alist[:]
        execution_string = sort_functions[index] + '(unsorted_list)'
        print("%s: %s --> (Returns %s) --> %s" % (sort_names[index], alist, exec(execution_string), unsorted_list))


# TODO: Bubble sort is throwing errors.
list_input1 = [25, 95, 45, 96, 56, 24, 0, 7, 83]
list_input2 = [4, 9, 6, 10, 7, 5, 1, 3, 8, 2]  # Completely Random List
list_input3 = [3, 1, 4, 2, 5, 7, 8, 6, 10, 9]  # Partially Sorted List
list_input4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Completely Sorted List
list_input5 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Completely Reverse Sorted List
list_input6 = ['P', 'Y', 'T', 'H', 'O', 'N', '!']  # Character List
# test_sort(list_input6)
