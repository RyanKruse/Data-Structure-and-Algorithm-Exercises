def hash_string_unweighted(astring, table_size):
    """Simple Hash Function for Strings."""
    temp = 0
    for pos in range(len(astring)):
        temp = temp + ord(astring[pos])
    print(f'The value of "{astring}" is {temp}. The table size is {table_size}. The hash value is {temp%table_size}.')
    return temp % table_size


def hash_string_weighted(astring, table_size):
    """Simple Weighted Hash Function for Strings. The letter index, starting at 1, is multiplied with ord."""
    temp = 0
    for counter, pos in enumerate(range(len(astring)), start=1):
        temp = temp + (ord(astring[pos])*counter)
    print(f'The value of "{astring}" is {temp}. The table size is {table_size}. The hash value is {temp%table_size}.')
    return temp % table_size


def hash_string_custom(astring, table_size):
    """Simple Custom Hash Function for Strings. Uses hash value of previous letter."""
    temp = 0
    for pos in range(len(astring)):
        temp = temp + (ord(astring[pos])*(ord(astring[pos-1]) % table_size))
    print(f'The value of "{astring}" is {temp}. The table size is {table_size}. The hash value is {temp%table_size}.')
    return temp % table_size


def hash_string_test():
    print(hash_string_unweighted('cat', 11))
    print(hash_string_weighted('cat', 11))
    print(hash_string_custom('cat', 11))
    items = ['Ryan', 'John', 'Chris', 'Rebbecca', 'Michael', 'Issac', 'Kevin', 'Andrew', 'Sally', 'Samantha']  # len 10
    hash_list = [None] * len(items)
    counter = 0
    for item in items:
        hash_value = hash_string_custom(item, len(items))
        if hash_value not in hash_list:
            hash_list[counter] = hash_value
            counter += 1
    collisions = 0
    for hash_value in hash_list:
        if hash_value is None:
            collisions += 1
    print(f'Our Hash List is: {hash_list} meaning there were {collisions} collisions.\n')

    # Perfect hash function attempt.
    items = ['a', 'aa', 'aaa', 'A', 'AA', 'AAA', 'AaA', 'aAa', 'Aaa', 'aAA']
    hash_list = []
    for item in items:
        hash_list.append(hash(item))
    print(hash_list)


hash_string_test()
