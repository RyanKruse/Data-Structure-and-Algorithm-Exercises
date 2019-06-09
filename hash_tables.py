
# ================================================== Hash Functions =================================================


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


# ================================================ Hash Table Linear ===============================================


class HashTableLinear:
    """This is the hash table class"""
    def __init__(self, size):
        """Initialize hash table variables."""
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __len__(self):
        """Return hash table size. O(1)."""
        return int(self.size)

    def __contains__(self, key):
        """Determines if key is in hash table. O(1)."""
        if self.__getitem__(key) is None:
            return False
        return True

    def __getitem__(self, key):
        """Get data from hash table. O(1)."""
        return self.get(key)

    def __setitem__(self, key, data):
        """Put data in hash table. O(1)."""
        self.put(key, data)

    def __str__(self):
        """Returns a string of all occupied slots and data from the hash table. O(N)."""
        return "Slot List " + str(self.slots) + " \nData List " + str(self.data)

    def put(self, key, data):
        """Stores key and data into hash table. If load factor exceeds 70%, resize hash table. O(1)."""
        # Get hash value of key.
        hash_value = self.hash_function(key, len(self.slots))
        hash_value_start = hash_value

        # Allowed hash table to dynamically adjust size as load increases.
        load_factor = len([a for a in self.data if a is not None]) / len(self)
        if load_factor >= .7:
            temp_slots = [None] * self.size
            temp_data = [None] * self.size
            self.size *= 2
            self.slots = self.slots + temp_slots
            self.data = self.data + temp_data

        # If slot corresponding to hash value is empty, set slot and data.
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # If slot corresponding to hash value is equal to key, replace data.
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                # If slot corresponding to hash value is not equal to key and is not empty, rehash hash value.
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                # Set slot and data.
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        """Returns the data corresponding to key from hash table. If slot for key is not found, return None. O(1)."""
        # Gets hash value of key.
        start_slot = self.hash_function(key, len(self.slots))
        position = start_slot

        # Search slots for key.
        while self.slots[position] is not None:
            # If key is found, return data.
            if self.slots[position] == key:
                return self.data[position]
            # If key is not found, rehash new position.
            position = self.rehash(position, len(self.slots))
            if position == start_slot:
                return None

    def hash_function(self, key, size):
        """Returns remainder of being divided by hash table size. O(1)."""
        return key % size

    def rehash(self, old_hash, size):
        """Increases hash slot by 1 if previous hash value had collision. O(1)."""
        return (old_hash + 1) % size


def test_1():
    hash_table.put(193, 193)
    hash_table.put(241, 241)
    hash_table.put(92, 92)
    hash_table.put(50, 50)
    hash_table.put(51, 51)
    hash_table.put(140, 140)
    print(hash_table.get(193))
    if len(hash_table) > 10:
        print('Hash size is greater than 10.')
    for number in range(1, 300):
        if number in hash_table:
            print(f'{number} is in the hash table.')
    print(hash_table)


def test_2():
    hash_table.put(50, 50)
    hash_table.put(1, 1)
    hash_table.put(2, 2)
    hash_table.put(3, 3)
    hash_table.put(4, 4)
    hash_table.put(5, 5)
    hash_table.put(6, 6)
    print(hash_table)
    if 50 in hash_table:
        print(f'50 is in the hash table.')
    hash_table.put(55, 55)
    print(hash_table)


hash_table = HashTableLinear(10)
test_1()
test_2()


# ================================================ Hash Table Quadratic ===============================================


class HashTableQuadratic:
    def __init__(self, size):
        self.table_size = int(size)
        self.slot_list = [None] * self.table_size
        self.data_list = [None] * self.table_size
        self.max_load_factor = .7
        self.rehash_counter = 1

    def __len__(self):
        return self.table_size

    def __str__(self):
        return "Slot List " + str(self.slot_list) + " \nData List " + str(self.data_list)

    def __contains__(self, key):
        if self.get(key) is not None:
            return True
        return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        start = self.hash_function(key)
        position = start
        self.rehash_counter = 1
        while self.slot_list[position] is not None:
            if self.slot_list[position] == key:
                # If key is found, set to None and reset all positions that appear after it until None is hit.
                # This is because all collided values will need to be readjusted.
                print(f'Deleted {self.slot_list[position]}')
                self.slot_list[position] = None
                self.data_list[position] = None
                self.rehash_counter = 1
                while True:
                    position = self.rehash(position)
                    if self.slot_list[position] is None:
                        break
                    temp_rehash_counter = self.rehash_counter
                    temp_key = self.slot_list[position]
                    temp_data = self.data_list[position]
                    self.slot_list[position] = None
                    self.data_list[position] = None
                    self.__setitem__(temp_key, temp_data)
                    self.rehash_counter = temp_rehash_counter
                break
            position = self.rehash(position)
            if position == start:
                # Otherwise, if starting position found, stop.
                break

    def get(self, key):
        start = self.hash_function(key)
        position = start
        data = None
        self.rehash_counter = 1
        while self.slot_list[position] is not None:
            if self.slot_list[position] == key:
                # If key is found, set data and stop.
                data = self.data_list[position]
                break
            position = self.rehash(position)
            if position == start:
                # If starting position found, stop.
                break
        # Data is either an element or None.
        return data

    def put(self, key, data):
        self.rehash_counter = 1
        hash_value = self.hash_function(key)
        while self.fill_data(key, data, hash_value):
            hash_value = self.rehash(hash_value)
        self.calc_load()

    def calc_load(self):
        filled = 0
        for key in self.slot_list:
            if key is not None:
                filled += 1
        if filled / self.table_size >= self.max_load_factor:
            print('Load Limit Reached. Resizing Table.')
            new_hash_table = HashTableQuadratic(self.table_size * 2)
            for index, element in enumerate(self.slot_list):
                temp_key = self.slot_list[index]
                temp_item = self.data_list[index]
                if temp_key is not None:
                    new_hash_table.__setitem__(temp_key, temp_item)
            self.slot_list = new_hash_table.slot_list
            self.data_list = new_hash_table.data_list
            self.table_size = new_hash_table.table_size

    def fill_data(self, key, data, hash_value):
        if self.slot_list[hash_value] is None or self.slot_list[hash_value] == 'DUMMY':
            # If slot is None, we input key and data.
            self.slot_list[hash_value] = key
            self.data_list[hash_value] = data
            return False
        elif self.slot_list[hash_value] == key:
            # If slot is equal to key, we replace data.
            self.data_list[hash_value] = data
            return False
        # If we can't do either, do open addressing.
        return True

    def hash_function(self, key):
        """This recalculates the hash value so it fits in a list slot."""
        return key % self.table_size

    def rehash(self, hash_value):
        """In collision event, changes hash value by +1"""
        rehash_value = hash_value + (self.rehash_counter**2)
        self.rehash_counter += 1
        return rehash_value % self.table_size


def test_3():
    hash_table = HashTableQuadratic(11)
    hash_table.__setitem__(9, 9)
    hash_table.__setitem__(10, 10)
    hash_table.__setitem__(0, 0)
    hash_table.__setitem__(11, 11)
    hash_table.__setitem__(22, 22)
    hash_table.__setitem__(33, 33)
    print(hash_table)
    hash_table.__delitem__(0)
    print(hash_table)


test_3()


# ================================================ Hash Table Chaining ===============================================


class HashTableChaining:
    def __init__(self, size):
        self.table_size = int(size)
        self.slot_list = [None] * self.table_size
        self.data_list = [None] * self.table_size
        for index, element in enumerate(self.slot_list):
            self.slot_list[index] = [None]
            self.data_list[index] = [None]

    def __len__(self):
        return self.table_size

    def __str__(self):
        return "Slot List " + str(self.slot_list) + " \nData List " + str(self.data_list)

    def __contains__(self, key):
        if self.get(key) is not None:
            return True
        return False

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        hash_value = self.hash_function(key)
        for index, element in enumerate(self.slot_list[hash_value]):
            if self.slot_list[hash_value][index] == key:
                # If slot is equal to key, we pop the element. We do not set dummy variables for the following example:
                # Put (1, 1), Put (11, 11), Delete (1, 1), Put (11, 11).
                # The last put will not replace the previous key but insert a new key. There are now two 11 keys.
                self.slot_list[hash_value].pop(index)
                self.data_list[hash_value].pop(index)
                break

    def get(self, key):
        hash_value = self.hash_function(key)
        data = None
        for index, element in enumerate(self.slot_list[hash_value]):
            if self.slot_list[hash_value][index] == key:
                # If slot is equal to key, we set data.
                data = self.data_list[hash_value][index]
                break
        return data

    def put(self, key, data):
        hash_value = self.hash_function(key)
        placed = False
        for index, element in enumerate(self.slot_list[hash_value]):
            if self.slot_list[hash_value][index] is None or self.slot_list[hash_value][index] == 'DUMMY':
                # If slot is None or dummy, we input key and data.
                self.slot_list[hash_value][index] = key
                self.data_list[hash_value][index] = data
                placed = True
                break
            elif self.slot_list[hash_value][index] == key:
                # If slot is equal to key, we replace data.
                self.data_list[hash_value][index] = data
                placed = True
                break
        if not placed:
            # We append to end of chain if neither above condition was met.
            self.slot_list[hash_value].append(key)
            self.data_list[hash_value].append(data)

    def hash_function(self, key):
        """This recalculates the hash value so it fits in a list slot."""
        return key % self.table_size


def test_4():
    hash_table = HashTableChaining(10)
    hash_table.__setitem__(62, 62)
    hash_table.__setitem__(81, 81)
    hash_table.__setitem__(24, 24)
    hash_table.__setitem__(19, 19)
    hash_table.__setitem__(13, 13)
    hash_table.__setitem__(1, 1)
    hash_table.__setitem__(33, 33)
    hash_table.__setitem__(41, 41)
    hash_table.__setitem__(51, 51)
    print(hash_table)
    print(hash_table.__getitem__(1))
    print(hash_table.__getitem__(24))
    print(hash_table.__getitem__(33))
    print(hash_table.__getitem__(41))
    print(hash_table.__getitem__(51))
    hash_table.__setitem__(41, 51)
    print(hash_table.__getitem__(41))
    hash_table.__delitem__(24)
    hash_table.__delitem__(81)
    hash_table.__delitem__(51)
    hash_table.__setitem__(1, 1)
    hash_table.__delitem__(62)
    hash_table.__setitem__(62, 62)
    print(hash_table)


test_4()
