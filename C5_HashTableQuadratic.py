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
                    position = self.rehash(position)  # TODO
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
            position = self.rehash(position)  # TODO
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
            position = self.rehash(position)  # TODO
            if position == start:
                # If starting position found, stop.
                break
        # Data is either an element or None.
        return data

    def put(self, key, data):
        self.rehash_counter = 1
        hash_value = self.hash_function(key)
        while self.fill_data(key, data, hash_value):
            hash_value = self.rehash(hash_value)  # TODO
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

"""
hash_table.__delitem__(81)
hash_table.__delitem__(13)
print(hash_table)
"""
