class HashTableLinear:
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
        """Needs resolution for full chain."""
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


hash_table = HashTableLinear(10)
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
"""
print(hash_table.__getitem__(1))
print(hash_table.__getitem__(24))
print(hash_table.__getitem__(33))
hash_table.__setitem__(72, 72)
print(hash_table)
"""