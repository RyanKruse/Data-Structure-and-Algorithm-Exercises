from data_structures import InsertQueue, AppendQueue, StackQueue, UnorderedList, LinkedQueue, LinkedStack, Stack, \
    DoublyLinkedQueue
from collections import deque
import pygal
import timeit


# ================================================== Test 1 ========================================================


# Test of Enqueue Times
print("\nEnqueue Speeds in Deque (append) vs. AppendQueue (append) vs. "
      "InsertQueue (insert(0)) vs. StackQueue (push) vs. DoublyQueue (add)")
print('%23s%23s%17s%16s%17s' % ('Deque', 'AppendQueue', 'InsertQueue', 'StackQueue', 'DoublyQueue'))
enqueue_time = timeit.Timer("x.enqueue(0)", "from __main__ import x")
deque_enqueue_time = timeit.Timer("x.append(0)", "from __main__ import x")
queue_times1 = []
reverse_queue_times1 = []
queue_stack_times1 = []
deque_times1 = []
linked_queue_times1 = []

for size in range(1000, 5001, 1000):
    x = deque()
    deque_speed = deque_enqueue_time.timeit(number=size)
    deque_times1.append(deque_speed)

    x = AppendQueue()
    reverse_queue_speed = enqueue_time.timeit(number=size)
    reverse_queue_times1.append(reverse_queue_speed)

    x = InsertQueue()
    queue_speed = enqueue_time.timeit(number=size)
    queue_times1.append(queue_speed)

    x = StackQueue()
    queue_stack_speed = enqueue_time.timeit(number=size)
    queue_stack_times1.append(queue_stack_speed)

    x = DoublyLinkedQueue()
    linked_queue_speed = enqueue_time.timeit(number=size)
    linked_queue_times1.append(linked_queue_speed)

    print("Enqueued %d: %10.5f  %15.5f  %15.5f  %15.5f %15.5f"
          % (size, deque_speed, reverse_queue_speed, queue_speed, queue_stack_speed, linked_queue_speed))


# ================================================== Test 2 ========================================================


# Test of Dequeue Times
print("\nDequeue Speeds in Deque (popleft) vs. AppendQueue (pop(0)) vs. "
      "InsertQueue (pop) vs. StackQueue (stack.pop) vs. DoublyQueue (pop(-1))")
print('%23s%23s%17s%16s%17s' % ('Deque', 'AppendQueue', 'InsertQueue', 'StackQueue', 'DoublyQueue'))
dequeue_time = timeit.Timer("x.dequeue()", "from __main__ import x")
deque_dequeue_time = timeit.Timer("x.popleft()", "from __main__ import x")
queue_times2 = []
reverse_queue_times2 = []
queue_stack_times2 = []
deque_times2 = []
linked_queue_times2 = []

for size in range(1000, 5001, 1000):
    x = deque()
    for num in range(0, size + 1):
        x.append(num)
    deque_speed = deque_dequeue_time.timeit(number=size)
    deque_times2.append(deque_speed)

    x = AppendQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    reverse_queue_speed = dequeue_time.timeit(number=size)
    reverse_queue_times2.append(reverse_queue_speed)

    x = InsertQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    queue_speed = dequeue_time.timeit(number=size)
    queue_times2.append(queue_speed)

    x = StackQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    queue_stack_speed = dequeue_time.timeit(number=size)
    queue_stack_times2.append(queue_stack_speed)

    x = DoublyLinkedQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    linked_queue_speed = dequeue_time.timeit(number=size)
    linked_queue_times2.append(linked_queue_speed)

    print("Dequeued %d: %10.5f  %15.5f  %15.5f  %15.5f %15.5f"
          % (size, deque_speed, reverse_queue_speed, queue_speed, queue_stack_speed, linked_queue_speed))


def helper(total_t, enqueue_t, dequeue_t):
    for index in range(0, 5):
        total_t.append(enqueue_t[index] + dequeue_t[index])
    return total_t


# Get overall speed score for each queue type.
queue_times3 = []
reverse_queue_times3 = []
queue_stack_times3 = []
deque_times3 = []
linked_queue_times3 = []

queue_times3 = helper(queue_times3, queue_times1, queue_times2)
reverse_queue_times3 = helper(reverse_queue_times3, reverse_queue_times1, reverse_queue_times2)
queue_stack_times3 = helper(queue_stack_times3, queue_stack_times1, queue_stack_times2)
deque_times3 = helper(deque_times3, deque_times1, deque_times2)
linked_queue_times3 = helper(linked_queue_times3, linked_queue_times1, linked_queue_times2)

# Visually chart the data.
print('\nThe data for enqueue and dequeue was combined and graphed into the project folder as timeit.queues.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of a Deque vs. AppendQueue vs. InsertQueue vs. StackQueue vs. DoublyQueue"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Items Enqueued then Dequeued"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('Deque', deque_times3)
bar_chart.add('AppendQueue', reverse_queue_times3)
bar_chart.add('InsertQueue', queue_times3)
bar_chart.add('StackQueue', queue_stack_times3)
bar_chart.add('DoublyQueue', linked_queue_times3)
bar_chart.render_to_file('graphs/timeit.queues.svg')


# ================================================== Test 3 ========================================================


# Test performance of a python list vs. linked list. Append.
print("\nAdding elements in linked (add) vs. linked (append) vs. list (append) vs. list (insert(0)).")
print('%28s%25s%20s%25s' % ('linked.add', 'linked.append', 'list.append', 'list.insert(0)'))
linked_head_time = timeit.Timer("x.add(0)", "from __main__ import x")
linked_tail_time = timeit.Timer("x.append(0)", "from __main__ import x")
list_head_time = timeit.Timer("x.append(0)", "from __main__ import x")
list_tail_time = timeit.Timer("x.insert(0, 0)", "from __main__ import x")
linked_head_times = []
linked_tail_times = []
list_head_times = []
list_tail_times = []

for size in range(1000, 5001, 1000):
    x = UnorderedList()
    linked_head_speed = linked_head_time.timeit(number=size)
    linked_head_times.append(linked_head_speed)

    x = UnorderedList()
    linked_tail_speed = linked_tail_time.timeit(number=int(size / 10))
    linked_tail_times.append(linked_tail_speed)

    x = []
    list_head_speed = list_head_time.timeit(number=size)
    list_head_times.append(list_head_speed)

    x = []
    list_tail_speed = list_tail_time.timeit(number=size)
    list_tail_times.append(list_tail_speed)
    print("Added %d: %13.5f  %20.5f  %20.5f  %20.5f"
          % (size, linked_head_speed, linked_tail_speed, list_head_speed, list_tail_speed))

# Visually chart the data.
print('\nThe above data for the linked and list test was graphed into the project folder as timeit.add_items.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of Adding Elements using linked.add vs. linked.append (10%) vs. list.append vs. list.insert(0)"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Number of Elements Added"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('linked.add', linked_head_times)
bar_chart.add('linked.append', linked_tail_times)
bar_chart.add('list.append', list_head_times)
bar_chart.add('list.insert(0)', list_tail_times)
bar_chart.render_to_file('graphs/timeit.add_items.svg')


# ================================================== Test 4 ========================================================


# Test performance of a python list vs. linked list. Pop.
print("\nPopping tail elements in linked vs. list.")
print('%30s%19s' % ('linked.pop(-1)', 'list.pop(0)'))
linked_pop_time = timeit.Timer("x.pop(x.length()-1)", "from __main__ import x")
list_pop_time = timeit.Timer("x.pop(0)", "from __main__ import x")
linked_pop_times = []
list_pop_times = []

for size in range(1000, 5001, 1000):
    x = UnorderedList()
    for num in range(0, size + 1):
        x.add(num)
    linked_pop_speed = linked_pop_time.timeit(number=int(1000 / 1000))
    linked_pop_times.append(linked_pop_speed)

    x = []
    for num in range(0, size + 1):
        x.append(num)
    list_pop_speed = list_pop_time.timeit(number=1000)
    list_pop_times.append(list_pop_speed)

    print("Popped %d: %10.5f  %20.5f "
          % (size, linked_pop_speed, list_pop_speed))

# Visually chart the data.
print('\nThe above data for the linked and list test was graphed into the project folder as timeit.pop_items.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of Popping 1 Tail with linked.pop(-1) vs. 1000 Tails with list.pop(0)"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Size"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('linked.pop', linked_pop_times)
bar_chart.add('list.pop', list_pop_times)
bar_chart.render_to_file('graphs/timeit.pop_items.svg')


# ================================================== Test 5 ========================================================


# Test performance of a python list vs. linked list. Slice.
print("\nSlicing all elements in linked vs. list.")
print('%28s%17s' % ('linked.slice', 'list[:]'))
linked_slice_time = timeit.Timer("x.slice(0, x.length())", "from __main__ import x")
list_slice_time = timeit.Timer("x[:]", "from __main__ import x")
linked_slice_times = []
list_slice_times = []

for size in range(1000, 5001, 1000):
    x = UnorderedList()
    for num in range(0, size + 1):
        x.add(num)
    linked_slice_speed = linked_slice_time.timeit(number=1)
    linked_slice_times.append(linked_slice_speed)

    x = []
    for num in range(0, size + 1):
        x.append(num)
    list_slice_speed = list_slice_time.timeit(number=1000)
    list_slice_times.append(list_slice_speed)

    print("Sliced %d: %10.5f  %20.5f "
          % (size, linked_slice_speed, list_slice_speed))

print('\nThe above data for the linked and list test was graphed into the project folder as timeit.slice_items.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of 1 Slice with linked.slice vs. 1,000 Slices with list[:]"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Size"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('linked.slice', linked_slice_times)
bar_chart.add('list[:]', list_slice_times)
bar_chart.render_to_file('graphs/timeit.slice_items.svg')


# ================================================== Test 6 ========================================================


# Test performance of a Deque vs. Stack vs. LinkedStack.
print("\nPushing and Popping items in Deque vs. Stack vs. LinkedStack")
print('%30s%20s%28s%15s%22s%28s' % (
'Deque.append', 'Stack.push', 'LinkedStack.push', 'Deque.pop', 'Stack.pop', 'LinkedStack.pop'))
append_time = timeit.Timer("x.append(0)", "from __main__ import x")
push_time = timeit.Timer("x.push(0)", "from __main__ import x")
pop_time = timeit.Timer("x.pop()", "from __main__ import x")
deque_append_times = []
stack_push_times = []
linked_stack_push_times = []
deque_pop_times = []
stack_pop_times = []
linked_stack_pop_times = []

for size in range(1000, 5001, 1000):
    x = deque()
    deque_append_speed = append_time.timeit(number=size)
    deque_append_times.append(deque_append_speed)
    dequeue_pop_speed = pop_time.timeit(number=size)
    deque_pop_times.append(dequeue_pop_speed)

    x = Stack()
    stack_push_speed = push_time.timeit(number=size)
    stack_push_times.append(stack_push_speed)
    stack_pop_speed = pop_time.timeit(number=size)
    stack_pop_times.append(stack_pop_speed)

    x = LinkedStack()
    linked_stack_push_speed = push_time.timeit(number=size)
    linked_stack_push_times.append(linked_stack_push_speed)
    linked_stack_pop_speed = pop_time.timeit(number=size)
    linked_stack_pop_times.append(linked_stack_pop_speed)
    print("Added %d: %13.5f  %20.5f  %20.5f  %20.5f  %20.5f  %20.5f"
          % (size, deque_append_speed, dequeue_pop_speed, stack_push_speed, stack_pop_speed, linked_stack_push_speed,
             linked_stack_pop_speed))

deque_times = []
stack_times = []
linked_stack_times = []
deque_times = helper(deque_times, deque_append_times, deque_pop_times)
stack_times = helper(stack_times, stack_push_times, stack_pop_times)
linked_stack_times = helper(linked_stack_times, linked_stack_push_times, linked_stack_pop_times)

# Visually chart the data.
print('\nThe above data for the stacks test was graphed into the project folder as timeit.stacks.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of Pushing and Popping Items in a Deque vs. Stack vs. LinkedStack"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Items Pushed then Popped"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('Deque', deque_times)
bar_chart.add('Stack', stack_times)
bar_chart.add('LinkedStack', linked_stack_times)
bar_chart.render_to_file('graphs/timeit.stacks.svg')


# ================================================== Test 7 ========================================================


# Test of LinkedListQueue Enqueue and Dequeue Times.

# Test of LinkedListQueue Enqueue Times.
print("\nEnqueue Speeds in SinglyLinkedQueue vs. DoublyLinkedQueue")
print('%45s%27s' % ('SinglyLinkedQueue', 'DoublyLinkedQueue'))
enqueue_time = timeit.Timer("x.enqueue(0)", "from __main__ import x")
singly_queue_times1 = []
doubly_queue_times1 = []

for size in range(1000, 5001, 1000):
    x = LinkedQueue()
    singly_queue_speed = enqueue_time.timeit(number=size)
    singly_queue_times1.append(singly_queue_speed)

    x = DoublyLinkedQueue()
    doubly_queue_speed = enqueue_time.timeit(number=size)
    doubly_queue_times1.append(doubly_queue_speed)

    print("Enqueued %d: %20.5f  %25.5f" % (size, singly_queue_speed, doubly_queue_speed))


# Test of LinkedListQueue Dequeue Times.
print("\nDequeue Speeds in SinglyLinkedQueue vs. DoublyLinkedQueue")
print('%45s%27s' % ('SinglyLinkedQueue', 'DoublyLinkedQueue'))
dequeue_time = timeit.Timer("x.dequeue()", "from __main__ import x")
singly_queue_times2 = []
doubly_queue_times2 = []

for size in range(1000, 5001, 1000):
    x = LinkedQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    singly_queue_speed = dequeue_time.timeit(number=size)
    singly_queue_times2.append(singly_queue_speed)

    x = DoublyLinkedQueue()
    for num in range(0, size + 1):
        x.enqueue(num)
    doubly_queue_speed = dequeue_time.timeit(number=size)
    doubly_queue_times2.append(doubly_queue_speed)

    print("Dequeued %d: %20.5f  %25.5f"
          % (size, singly_queue_speed, doubly_queue_speed))


def helper(total_t, enqueue_t, dequeue_t):
    for index in range(0, 5):
        total_t.append(enqueue_t[index] + dequeue_t[index])
    return total_t


# Get overall speed score for each LinkedListQueue type.
singly_queue_times3 = []
doubly_queue_times3 = []

singly_queue_times3 = helper(singly_queue_times3, singly_queue_times1, singly_queue_times2)
doubly_queue_times3 = helper(doubly_queue_times3, doubly_queue_times1, doubly_queue_times2)

# Visually chart the data.
print('\nThe data for enqueue and dequeue was combined and graphed into the project folder as timeit.linked_queues.svg')
bar_chart = pygal.Bar()
bar_chart.title = "Speed of a SinglyLinkedQueue vs. DoublyLinkedQueue"
bar_chart.x_labels = ['1000', '2000', '3000', '4000', '5000']
bar_chart.x_title = "Items Enqueued then Dequeued"
bar_chart.y_title = "Speed (Seconds)"
bar_chart.add('SinglyLinkedQueue', singly_queue_times3)
bar_chart.add('DoublyLinkedQueue', doubly_queue_times3)
bar_chart.render_to_file('graphs/timeit.linked_queues.svg')

# TODO: Fix variable names.
# TODO: Figure out how reverse function works.
# TODO: Some tests only run 10 or .1% of the time. Note them in the print statements.
# TODO: Combine Enqueue and Dequeue Timer for-loops.
# TODO: Make the lists appear clean and tidy and consistent.
