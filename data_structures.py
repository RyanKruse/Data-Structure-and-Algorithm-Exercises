class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class InsertQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class AppendQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class StackQueue:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def __str__(self):
        return '[' + str(self.input) + ', ' + str(self.output) + ']'

    def isempty(self):
        return self.input.isempty() and self.output.isempty()

    def enqueue(self, item):
        self.input.push(item)

    def dequeue(self):
        if self.output.isempty():
            while not self.input.isempty():
                self.output.push(self.input.pop())
        return self.output.pop()

    def size(self):
        return self.input.size() + self.output.size()


class Deque:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items == []

    def append(self, item):
        self.items.append(item)

    def add(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def popleft(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class LinkedStack:
    def __init__(self):
        self.items = UnorderedList()

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items.isempty()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items.head.data

    def size(self):
        return self.items.length()


class LinkedQueue:
    def __init__(self):
        self.items = UnorderedList()

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items.isempty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop(self.size() - 1)

    def size(self):
        return self.items.length()


class LinkedDeque:
    def __init__(self):
        self.items = UnorderedList()

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items.isempty()

    def append(self, item):
        self.items.insert(self.size(), item)

    def add(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(self.size() - 1)

    def popleft(self):
        return self.items.pop()

    def size(self):
        return self.items.length()


class DoublyLinkedQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def __str__(self):
        return str(self.items)

    def isempty(self):
        return self.items.isempty()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop(-1)

    def size(self):
        return self.items.length()


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        """Gets a printable string of the list."""
        if self.head is None:
            return '[]'
        a_string = '['
        current = self.head
        while current is not None:
            if isinstance(current.data, str):
                a_string += "'" + current.data + "', "
            else:
                a_string += str(current.data) + ', '
            current = current.next
        return a_string[:-2] + ']'

    def add(self, item):
        """Adds an item to the start of the list."""
        node = Node(item)
        node.next = self.head
        self.head = node

    def remove(self, item):
        """Removes the first occurrence of an item in a list."""
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                break
            previous = current
            current = current.next

    def search(self, item):
        """Checks to see if an item is in the list. Returns a bool."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def isempty(self):
        """Checks to see if list is empty."""
        return self.head is None

    def length(self):
        """Traverses the entire list and returns list length."""
        current = self.head
        index = 0
        while current is not None:
            index += 1
            current = current.next
        return index

    def index(self, item):
        """Takes an item and finds the index of the item in the list."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1

    def get(self, position):
        """Takes an index and returns the item in that list index."""
        index = 0
        current = self.head
        while current is not None:
            if index == position:
                return current
            current = current.next
            index += 1

    def pop(self, position=0):
        """Pops an item from the list. If no position is provided, pop's head."""
        current = self.head
        previous = None
        index = 0
        if not isinstance(position, int) or position < 0:
            raise TypeError('Error: Inputs can only be of a positive integer data type.')
        elif position == 0 and current is not None:
            temp = self.head.data
            self.head = self.head.next
            return temp

        while current is not None:
            if position == index:
                break
            previous = current
            current = current.next
            index += 1

        if current is None and index <= position:
            raise IndexError(f'Error: Index out of range for popping item.')
        temp = current.data
        previous.next = current.next
        return temp

    def slice(self, start, stop):
        """Takes 2 integer inputs and returns an unordered linked list with nodes between those inputs."""
        current = self.head
        sliced_list = UnorderedList()
        index = 0
        if (not isinstance(start, int) or not isinstance(stop, int)) or (start < 0 or stop < 0):
            raise TypeError('Error: Inputs can only be of a positive integer data type.')
        elif start >= stop or self.head is None:
            return sliced_list

        while current is not None:
            if stop == index:
                break
            elif start <= index:
                sliced_list.add(current.data)
            current = current.next
            index += 1

        if stop != index:
            raise IndexError('Error: Slice index is out of range.')
        sliced_list.reverse()
        return sliced_list

    def reverse(self):
        """Reverses the linked list."""
        previous = None
        current = self.head
        nex = current.next

        while current is not None:
            current.next = previous
            previous = current
            current = nex
            if nex is not None:
                nex = nex.next

        self.head = previous


class UnorderedList(LinkedList):
    def __init__(self):
        super().__init__()

    def append(self, item):
        """Adds an item to the end of the list."""
        current = self.head
        if self.head is None:
            self.head = Node(item)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(item)

    def insert(self, position, item):
        """Takes an item and a position and inserts that item as a node in the list."""
        node = Node(item)
        current = self.head
        previous = None
        index = 0
        if not isinstance(position, int) or position < 0:
            raise TypeError('Error: Position of insert can only be of a positive integer data type.')
        elif self.head is None or position == 0:
            return self.add(item)

        while current is not None:
            if index == position:
                break
            previous = current
            current = current.next
            index += 1

        if current is None and index != position:
            raise IndexError(f'Error: Index out of range for position of insert.')
        node.next = previous.next
        previous.next = node


class OrderedList(LinkedList):
    def __init__(self):
        super().__init__()

    def add(self, item):
        """Adds an item in the ordered position in the list. Can stop early."""
        current = self.head
        previous = None
        node = Node(item)

        while current is not None:
            if current.data > item:
                break
            previous = current
            current = current.next

        if previous is None:
            node.next = self.head
            self.head = node
            return
        node.next = current
        previous.next = node

    def remove(self, item):
        """Removes the first occurrence of an item in a list. Can stop early."""
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                break
            elif current.data > item:
                break
            previous = current
            current = current.next

    def search(self, item):
        """Checks to see if an item is in the list. Returns a bool. Can stop early."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            elif current.data > item:
                break
            current = current.next
        return False

    def index(self, item):
        """Takes an item and finds the index of the item in the list. Can stop early."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            elif current.data > item:
                return
            current = current.next
            index += 1


class DoublyNode:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.back = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """Gets a printable string of the list."""
        if self.head is None:
            return '[]'
        a_string = '['
        current = self.head
        while current is not None:
            if isinstance(current.data, str):
                a_string += "'" + current.data + "', "
            else:
                a_string += str(current.data) + ', '
            current = current.next
        return a_string[:-2] + ']'

    def add(self, item):
        """Adds an item to the start of the list."""
        node = DoublyNode(item)
        if self.head is not None:
            self.head.back = node
        else:  # Means empty list
            self.tail = node
        node.next = self.head
        self.head = node

    def remove(self, item):
        """Removes the first occurrence of an item in a list."""
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                if previous is None:  # Removing first item
                    self.head = current.next
                    if self.head is not None:
                        self.head.back = None
                    else:
                        self.tail = None
                else:  # Removing n item
                    previous.next = current.next
                    if current.next is not None:
                        current.next.back = previous
                    else:
                        self.tail = previous
                break
            previous = current
            current = current.next

    def search(self, item):
        """Checks to see if an item is in the list. Returns a bool."""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def isempty(self):
        """Checks to see if list is empty."""
        return self.head is None

    def length(self):
        """Traverses the entire list and returns list length."""
        current = self.head
        index = 0
        while current is not None:
            index += 1
            current = current.next
        return index

    def index(self, item):
        """Takes an item and finds the index of the item in the list."""
        current = self.head
        index = 0
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1

    def get(self, position):
        """Takes an index and returns the item in that list index."""
        index = 0
        if position < 0:
            current = self.tail
            while current is not None:
                index -= 1
                if index == position:
                    return current
                current = current.back
        else:
            current = self.head
            while current is not None:
                if index == position:
                    return current
                current = current.next
                index += 1

    def pop(self, position=0):
        """Pops an item from the list. If no position is provided, pop's head."""
        current = self.head
        index = 0
        if not isinstance(position, int):
            raise TypeError('Error: Inputs can only be of an integer data type.')
        elif position == 0 and current is not None:
            temp = self.head.data
            self.head = self.head.next
            self.head.back = None
            return temp
        if position < 0:
            current = self.tail
            while current is not None:
                index -= 1
                if index == position:
                    break
                current = current.back
        else:
            current = self.head
            while current is not None:
                if index == position:
                    break
                current = current.next
                index += 1
        if current is None:
            raise IndexError(f'Error: Index out of range for popping item.')
        temp = current.data
        if current.next is not None:
            current.next.back = current.back
        else:
            self.tail = current.back
        if current.back is not None:
            current.back.next = current.next
        else:
            self.head = current.next
        return temp

    def slice(self, start, stop):
        """Takes 2 integer inputs and returns an unordered linked list with nodes between those inputs."""
        # TODO: It is possible to accept negative values. It is possible to have start >= stop.
        current = self.head
        sliced_list = DoublyLinkedList()
        index = 0
        if (not isinstance(start, int) or not isinstance(stop, int)) or (start < 0 or stop < 0):
            raise TypeError('Error: Inputs can only be of a positive integer data type.')
        elif start >= stop or self.head is None:
            return sliced_list

        while current is not None:
            if stop == index:
                break
            elif start <= index:
                sliced_list.add(current.data)
            current = current.next
            index += 1

        if stop != index:
            raise IndexError('Error: Slice index is out of range.')
        sliced_list.reverse()
        return sliced_list

    def reverse(self):
        """Reverses the linked list."""
        previous = None
        current = self.head
        self.tail = current
        temp = current.next
        while current is not None:
            current.next = previous
            current.back = temp
            previous = current
            current = temp
            if temp is not None:
                temp = temp.next
        self.head = previous

    def append(self, item):
        """Similar to the add function, except backwards."""
        current = self.tail
        node = DoublyNode(item)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        current.next = node
        node.back = current
        self.tail = node

    def insert(self, position, item):
        """Takes an item and a position and inserts that item as a node in the list."""
        node = DoublyNode(item)
        current = self.head
        previous = None
        index = 0
        if not isinstance(position, int) or position < 0:
            raise TypeError('Error: Position of insert can only be of a positive integer data type.')
        elif self.head is None or position == 0:
            return self.add(item)

        while current is not None:
            if index == position:
                break
            previous = current
            current = current.next
            index += 1

        if current is None and index != position:
            raise IndexError(f'Error: Index out of range for position of insert.')

        node.next = previous.next
        if node.next is not None:
            node.next.back = node
        else:
            self.tail = node
        previous.next = node
        node.back = previous


def test_1():
    """Add and Remove functions work correctly."""
    temp = DoublyLinkedList()
    temp.add(10)
    temp.add(20)
    temp.add(30)
    temp.add(40)
    temp.add(50)
    print(f'temp = {temp}')
    print(f'temp.head = {temp.head}')
    print(f'temp.head.next = {temp.head.next}')
    print(f'temp.head.back = {temp.head.back}')
    print(f'temp.tail = {temp.tail}')
    print(f'temp.tail.next = {temp.tail.next}')
    print(f'temp.tail.back = {temp.tail.back}')

    temp.remove(10)
    temp.remove(50)
    temp.remove(30)
    print(f'\ntemp = {temp}')
    print(f'temp.head = {temp.head}')
    print(f'temp.head.next = {temp.head.next}')
    print(f'temp.head.back = {temp.head.back}')
    print(f'temp.tail = {temp.tail}')
    print(f'temp.tail.next = {temp.tail.next}')
    print(f'temp.tail.back = {temp.tail.back}')


def test_2():
    """Index and Get functions work correctly."""
    temp = DoublyLinkedList()
    temp.add(10)
    temp.add(20)
    temp.add(30)
    temp.add(40)
    temp.add(50)
    print(f'temp = {temp}')
    print(f'temp.index(50) = {temp.index(50)}')
    print(f'temp.index(40) = {temp.index(40)}')
    print(f'temp.index(30) = {temp.index(30)}')
    print(f'temp.index(20) = {temp.index(20)}')
    print(f'temp.index(10) = {temp.index(10)}')
    print(f'temp.get(0) = {temp.get(0)}')
    print(f'temp.get(1) = {temp.get(1)}')
    print(f'temp.get(2) = {temp.get(2)}')
    print(f'temp.get(3) = {temp.get(3)}')
    print(f'temp.get(4) = {temp.get(4)}')
    print(f'temp.get(5) = {temp.get(5)}')
    print(f'temp.get(-1) = {temp.get(-1)}')
    print(f'temp.get(-2) = {temp.get(-2)}')
    print(f'temp.get(-3) = {temp.get(-3)}')
    print(f'temp.get(-4) = {temp.get(-4)}')
    print(f'temp.get(-5) = {temp.get(-5)}')
    print(f'temp.get(-6) = {temp.get(-6)}')


def test_3():
    """Pop() and Pop(index) functions work correctly."""
    temp = DoublyLinkedList()
    temp.add(10)
    temp.add(20)
    temp.add(30)
    temp.add(40)
    temp.add(50)
    temp.add(60)
    temp.add(70)
    print(f'temp = {temp}')
    print(f'temp.pop() = {temp.pop()}')
    print(f'temp.pop(-2) = {temp.pop(-2)}')
    print(f'temp.pop(0) = {temp.pop(0)}')
    print(f'temp.pop(3) = {temp.pop(3)}')
    print(f'\ntemp = {temp}')
    print(f'temp.head = {temp.head}')
    print(f'temp.head.next = {temp.head.next}')
    print(f'temp.head.back = {temp.head.back}')
    print(f'temp.tail = {temp.tail}')
    print(f'temp.tail.next = {temp.tail.next}')
    print(f'temp.tail.back = {temp.tail.back}')


def test_4():
    """Slice and Reverse functions work correctly."""
    temp = DoublyLinkedList()
    temp.add(10)
    temp.add(20)
    temp.add(30)
    temp.add(40)
    temp.add(50)
    sliced = temp.slice(1, 4)
    print(f'temp = {sliced}')
    print(f'temp.reverse = {sliced.reverse()}')
    print(f'temp = {sliced}')
    print(f'temp.head = {sliced.head}')
    print(f'temp.head.next = {sliced.head.next}')
    print(f'temp.head.back = {sliced.head.back}')
    print(f'temp.tail = {sliced.tail}')
    print(f'temp.tail.next = {sliced.tail.next}')
    print(f'temp.tail.back = {sliced.tail.back}')


def test_5():
    """Append and Insert functions work correctly."""
    temp = DoublyLinkedList()
    temp.append(20)
    temp.insert(1, 30)
    temp.insert(0, 10)
    temp.append(40)
    temp.add(0)
    temp.insert(0, -10)
    temp.insert(6, 50)
    print(f'temp = {temp}')
    print(f'temp.head = {temp.head}')
    print(f'temp.head.next = {temp.head.next}')
    print(f'temp.head.back = {temp.head.back}')
    print(f'temp.tail = {temp.tail}')
    print(f'temp.tail.next = {temp.tail.next}')
    print(f'temp.tail.back = {temp.tail.back}')


run_test = False
if run_test:
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
