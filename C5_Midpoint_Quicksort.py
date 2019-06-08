from C5_Textbook_Sort import quick_sort as default_quick_sort


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
