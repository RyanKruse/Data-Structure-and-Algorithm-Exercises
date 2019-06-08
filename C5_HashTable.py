class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __len__(self):
        return int(self.size)

    def __contains__(self, item):
        if self.__getitem__(item) is None:
            return False
        return True

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self):
        return "Slots:" + str(self.slots) + " \nData:" + str(self.data)

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        # Resize
        load_factor = len([a for a in self.data if a is not None])/len(self)
        print(f'Load factor is: {load_factor}')
        if load_factor >= .7:
            print(f'\nOld Slots: {self.slots}')
            print(f'Old Data: {self.data}')
            print('\tDouble Hash Table Size. Load Factor above .7')
            temp_slots = [None] * self.size
            temp_data = [None] * self.size
            self.size *= 2
            self.slots = self.slots + temp_slots
            self.data = self.data + temp_data
            print(f'New Slots: {self.slots}')
            print(f'New Data: {self.data}')

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __delitem__(self, key):
        data = None
        self.put(key, data)
        for index, element in enumerate(self.slots):
            if element == key:
                self.slots[index] = None


    def hash_function(self, key, size):
        """Simple: Returns remainder of division with hash table size."""
        return key % size

    def rehash(self, old_hash, size):
        """Simple: Increases hash slot by 1."""
        return (old_hash + 1) % size


hash_table = HashTable(10)
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
hash_table.__delitem__(92)
hash_table.__delitem__(50)
hash_table.__delitem__(140)
print('We deleted 92, 50, and 140 from the hash table.')
for number in range(1, 300):
    if number in hash_table:
        print(f'{number} is in the hash table.')

print(hash_table)
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

"""
for number in range(1, 300):
    if number in hash_table:
        print(f'{number} is in the hash table.')
"""
