def sequential_search(alist, item):
    """
    Sequential Search: Starting at the first item in the list, we simply move from item to item, following
    the underlying sequential ordering until we either find what we are looking for or run out of items.
    """
    i = 0
    while i < len(alist):
        if alist[i] == item:  # Item found.
            return True
        i += 1
    return False


def ordered_sequential_search(alist, item):
    """
    Ordered Sequential Search: Advantage over Sequential Search as it can stop early. Stops on average after n/2 items.
    """
    i = 0
    while i < len(alist) and alist[i] <= item:
        if alist[i] == item:
            return True
        i += 1
    return False


def binary_search(alist, item):
    """
    Binary Search: Examines the middle item. If that item is the one we are searching for, we exit. If it is not the
    correct item, we use the ordered nature of the list to eliminate half of the remaining items. We then check to see
    if the item we are searching is greater or less than our middle item. Call self again focusing on correct half.
    """
    # Base cases
    if len(alist) == 0:
        return False
    mid_index = len(alist) // 2  # "//" converts operand to int, rounding down to nearest whole number.
    mid_item = alist[mid_index]
    if mid_item == item:
        return True

    # Recursive calls.
    if item < mid_item:
        return binary_search(alist[:mid_index], item)  # Search bottom half.
    else:
        return binary_search(alist[mid_index+1:], item)  # Search top half.


def search_test():
    sample = [25, 95, 45, 96, 56, 24, 0, 7, 83]
    print(sequential_search(sample, 25))
    print(sequential_search(sample, 26))
    sample.sort()
    print(ordered_sequential_search(sample, 83))
    print(ordered_sequential_search(sample, 82))
    print(binary_search(sample, 96))
    print(binary_search(sample, 99))


search_test()
