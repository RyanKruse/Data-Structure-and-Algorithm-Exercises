from turtle import *
from random import randint


class Drawing:
    # TODO: My other other guess on how to solve this is by using turtle forward & rotation recursion triangle loops.
    def __init__(self):
        self.turtle = Turtle()
        self.window = self.turtle.getscreen()
        self.turtle.speed('fastest')

    def sierpinski(self, points, iterations):
        colors = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
        # Draws the actual triangle. This is very interesting.
        self.turtle.fillcolor(colors[iterations])

        self.turtle.up()  # Lifts tail
        self.turtle.goto(points[0])  # Goes to correct position.
        self.turtle.down()  # Drops tail

        self.turtle.goto(points[1])
        self.turtle.goto(points[2])
        self.turtle.goto(points[0])
        # Call recursion
        if iterations > 0:
            # Draws left-most triangles.
            self.sierpinski([points[0], self.mid(points[0], points[1]), self.mid(points[0], points[2])], iterations - 1)
            # Draws up-most triangles.
            self.sierpinski([points[1], self.mid(points[0], points[1]), self.mid(points[1], points[2])], iterations - 1)
            # Draws right-most triangles.
            self.sierpinski([points[2], self.mid(points[2], points[1]), self.mid(points[0], points[2])], iterations - 1)

    def mid(self, p1, p2):
        return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

    def mountain_boss(self, points, iterations):
        self.draw_triangle(points)
        if iterations > 0:
            new_points = self.shrink(points)
            new_triangle = self.flip(new_points)
            self.mountain_boss(new_triangle, iterations - 1)

    def shrink(self, points):
        point0x = (points[0][0] + points[2][0]) / 3
        point0y = (points[0][1] + points[2][1]) / 3
        point2x = ((points[0][0] + points[2][0]) / 3) * 2
        point2y = ((points[0][1] + points[2][1]) / 3) * 2
        point1x = (points[0][0] + points[1][0] + points[2][0]) / 3
        point1y = (points[0][1] + points[1][1] + points[2][1]) / 3

        point0 = (point0x, point0y)
        point1 = (point1x, point1y)
        point2 = (point2x, point2y)

        return [point0, point1, point2, points[3]]

    def flip(self, points):
        if not points[3]:
            points[3] = True
            point1x = points[1][0]
            point1y = points[1][1] - (points[1][1] * 2)
            point1 = (point1x, point1y)
            return [points[0], point1, points[2], points[3]]
        else:
            points[3] = False
            point1x = points[1][0]
            point1y = points[1][1] + (points[1][1] * 2)
            point1 = (point1x, point1y)
            return [points[0], point1, points[2], points[3]]

    def draw_triangle(self, points):
        self.turtle.up()
        self.turtle.goto(points[0])
        self.turtle.down()
        self.turtle.goto(points[1])
        self.turtle.goto(points[2])
        self.turtle.goto(points[0])

    def mountain_boss1(self, points, iterations):
        self.turtle.up()
        self.turtle.goto(points[0])
        self.turtle.down()

        self.turtle.goto(points[1])
        self.turtle.goto(points[2])
        self.turtle.goto(points[0])

        if iterations > 0:
            point_1 = self.goat1(points[0], points[1], 1)
            point_2 = self.goat1(points[0], points[1], 2)
            point_3 = self.goat1(point_1, point_2, 3)

            # Stopping here. I need to fix variable names to match triangle points. Point 3 is causing issues,
            # I do not know how point 3 row/height logic works, as the triangle rotates as it drills deeper.

            self.mountain_boss1([point_2, point_3, point_1], iterations - 1)

    def goat1(self, p1, p2, point):
        if point == 1:
            return (p1[0] + p2[0]) / 3, ((p1[1] + p2[1]) / 3) * 2
        elif point == 2:
            return ((p1[0] + p2[0]) / 3) * 2, (p1[1] + p2[1]) / 3
        else:
            return (p2[0] + (p2[0] - p1[0])), p1[1]

    def mountain_boss2(self, points, iterations):
        self.draw_triangle(points)

        if iterations > 0:
            point0 = self.goat2(points[0], points[1], points[2], 0)
            point1 = self.goat2(points[0], points[1], points[2], 1)
            point2 = self.goat2(point1, point0, points[2], 2)

            # Stopping here. I need to fix variable names to match triangle points. Point 3 is causing issues,
            # I do not know how point 3 row/height logic works, as the triangle rotates as it drills deeper.

            self.mountain_boss2([point0, point1, point2], iterations - 1)

    def goat2(self, p0, p1, p2, point):
        if point == 0:
            # Left
            x = (p0[0] + p1[0]) / 3
            y = (p0[1] + p1[1]) / 3
            return x, y

        elif point == 1:
            # Peak
            x = (p0[0] + p1[0]) / 2
            y = (p0[1] + p1[1]) / 2
            return x, y

        else:
            # Right
            x = ((p0[0] + p1[0]) * 2) / 3
            y = ((p0[1] + p1[1]) * 2) / 3
            return x, y


drawing = Drawing()
drawing.mountain_boss([(0, 0), (60, 90), (120, 0), False], 2)
drawing.mountain_boss1([(0, 0), (60, 90), (120, 0)], 3)
drawing.mountain_boss2([(0, 0), (60, 90), (120, 0)], 3)

# Credit goes to "Billywob" from codegolf.stackexchange.com
hilbert_seq = "ab"
turtle = Turtle()
turtle.speed('fastest')
window = turtle.getscreen()

for _ in range(3):
    new_seq = ""
    for char in hilbert_seq:
        if char == "a":
            new_seq += "-bF+aFa+Fb-"
        elif char == "b":
            new_seq += "+aF-bFb-Fa+"
        else:
            new_seq += char
    hilbert_seq = new_seq

# Oh my god this is ingenious.
for char in hilbert_seq:
    if char == "F":
        turtle.forward(9)
    elif char == "+":
        turtle.right(90)
    elif char == "-":
        turtle.left(90)

turtle.up()
window.exitonclick()


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]


c1 = [1, 5, 8, 10, 25]
make_change = list(range(1, 34))
coinCount = [0]*64
coinsUsed = [0]*64
for num in make_change:
    print(f'{num} = {dpMakeChange(c1, num, coinCount, coinsUsed)}')


# This code is heavily outdated and poorly formatted compared to Backward Logic Gate classes.
# I am saving this code as it was a textbook problem to experiment with forward logic gate outputs.


class ForwardLogicGate:
    """Experimental Logic Gate utilizing forward return statements."""
    def __init__(self, name=''):
        self.name = name
        self.output = None
        self.a = None
        self.connector = None

    def push_output(self):
        return self.do_logic()

    def do_logic(self):
        pass


class ForwardUnaryGate(ForwardLogicGate):
    """Experimental Logic Gate utilizing forward return statements."""
    def __init__(self, name=''):
        super().__init__(name)

    def set_connector(self, connector):
        self.connector = connector

    def receive_input(self, input):
        self.a = input


class ForwardNotGate(ForwardUnaryGate):
    """Experimental Logic Gate utilizing forward return statements."""
    def __init__(self, name=''):
        super().__init__(name)

    def do_logic(self):
        if self.a == None:
            self.a = int(input('Enter pin A for ' + self.name + ' --> '))
        if self.a == 1:
            self.output = 0
        else:
            self.output = 1
        return self.pass_output()

    def pass_output(self):
        if self.connector:
            self.connector.get_to_gate().receive_input(self.output)
            return self.connector.get_to_gate().push_output()
        else:
            return self.output


class ForwardConnector:
    """Experimental Connector utilizing forward return statements."""
    def __init__(self, from_gate, to_gate, output=None):
        self.from_gate = from_gate
        self.to_gate = to_gate
        self.output = output
        from_gate.set_connector(self)

    def get_from_gate(self):
        return self.from_gate

    def get_to_gate(self):
        return self.to_gate


def test_case_4():
    """This forward logic gate implementation only contains a sample of the forward circuitry (ForwardNotGate)."""
    g1 = ForwardNotGate('G1')
    g2 = ForwardNotGate('G2')
    c1 = ForwardConnector(g1, g2)
    print(g1.push_output())


test_case_4()


class River:
    def __init__(self, missionaries, cannibals):
        self.side_1 = []
        self.side_2 = []
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.population = missionaries + cannibals
        self.steps = []
        self.sets = []

    def run(self):
        self.prep()
        self.recursion()

    def prep(self):
        for missionary in range(self.missionaries):
            self.side_1.append('M')
        for cannibal in range(self.cannibals):
            self.side_1.append('C')

    def recursion(self):
        if self.side_1:
            self.side_2.append(self.side_1.pop())
            self.side_2.append(self.side_1.pop())
            valid = self.check_both()
            if valid:
                self.recursion()
            else:
                print('they did not make it')
        else:
            print('they made it')

    def check_both(self):
        m_counter = 0
        c_counter = 0
        for char in self.side_1:
            if char == 'M':
                m_counter += 1
            elif char == 'C':
                c_counter += 1
        if c_counter > m_counter > 0:
            return False
        m_counter = 0
        c_counter = 0
        for char in self.side_2:
            if char == 'M':
                m_counter += 1
            elif char == 'C':
                c_counter += 1
        if c_counter > m_counter > 0:
            return False
        return True


river = River(2, 2)
river.run()


class Treasury2:
    def __init__(self, items):
        self.items = items
        self.possibilities = []

    def plot(self):
        for key, value in self.items.items():
            self.possibilities.append([key])
        temp = []
        for num in self.possibilities:
            for key, value in self.items.items():
                if not num[0] == key:
                    temp.append([num[0], key])
        self.possibilities = self.possibilities + temp


"""
if value[0] > self.raw_carry_limit:
    # We skip values that are flat out too large.
    continue

if value[0] > self.carry_limit:
    # We skip items that are larger than our carry limit... unless it is worth more.
    for key2, value2 in self.nells_bag.items():
        if value[0] > value2[0]:
            del self.nells_bag[key2]
            self.nells_bag[key] = value
        else:
            continue

else:
    # Put item in Nell's Bag.
    self.nells_bag[key] = value
    self.carry_limit = self.carry_limit - value[0]
"""

"""
        total_weight = 0
        for item in items_used:
            total_weight += item[0]
        if total_weight > self.raw_carry_limit:
            smallest = [99, 99]
            for item in items_used:
                if item[0] < smallest[0]:
                    smallest = item
            items_used.remove(smallest)
        for item in items_used:
            print(item)
"""

"""
for token_index2 in master_index2:
    if stop:
        break
    for token_index1 in master_index1:
        if token_index1 != token_index2:
            str1_list.insert(master_index2[token_index2], alphabet[index])
            str1_list.remove('~')
            stop = True
            break
"""


def bin_dec(a):
    return sum([int(a[-i])*2**(i-1) for i in range(1, len(list(a))+1)])


"""
print(bin_dec(1111001))
alist =[1111001, 1100101]
temp = ""
for k in alist:
    temp += chr(bin_dec(k))
print(temp)
"""


def delete(self, key):
    """Accidentally rebuilt the put function in the hash table linear probing delete method."""
    start = self.hash_function(key)
    position = start
    while self.slot_list[position] is not None:
        if self.slot_list[position] == key:
            # If key is found, set to None and reset collided positions.
            self.slot_list[position] = None
            self.data_list[position] = None
            counter = 1
            while True:
                if self.slot_list[position + counter] is None:
                    break
                next_key = self.slot_list[position + counter]
                if self.hash_function(next_key) <= start:
                    self.slot_list[position] = self.slot_list[position + counter]
                    self.data_list[position] = self.data_list[position + counter]
                    self.slot_list[position + counter] = None
                    self.data_list[position + counter] = None
                    position = position + counter
                    counter = 0
                counter += 1
            break
        position = self.rehash(position)
        if position == start:
            # If starting position found, stop.
            break


# The following code appears in the Emerald Key Project. Graveyard has been pushed here.
"""
for index, element in enumerate(self.temp):
    if '\n' in element:
        # we want to clean out the \n in our data.
        print_simulation(repr(element))
        if element[0] == "\n":
            print_simulation('CATCH ME')
        else:
            # These need to be split.
            pass
"""

"""
    def dijkstra_shortest_path(self):
        # Put all vertices in an unvisited queue.
        for vertex in self.graph.adjacency_list:
            self.deque.append(vertex)

        # start_vertex has a distance of 0 from itself
        start_vertex = self.graph.first_vertex
        start_vertex.distance = 0

        # One vertex is removed with each iteration; repeat until the list is empty.
        while len(self.deque) > 0:
            # Visit vertex with minimum distance from start_vertex
            smallest_index = 0
            for queue_index in range(1, len(self.deque)):
                if self.deque[queue_index].distance < self.deque[smallest_index].distance:
                    smallest_index = queue_index
            current_vertex = self.deque.popleft()

            # Check potential path lengths from the current vertex to all neighbors.
            for adj_vertex in g.adjacency_list[current_vertex]:
                edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight

                # If shorter path from start_vertex to adj_vertex is found,
                # update adj_vertex's distance and predecessor
                if alternative_path_distance < adj_vertex.distance:
                    adj_vertex.distance = alternative_path_distance
                    adj_vertex.pred_vertex = current_vertex

"""

"""
# Build current city mask (i.e. if current city = 2, then build [0, 0, 1, 0]
current_city_mask = [0] * LOAD_COUNT
current_city_mask[position] = 1

print_simulation("Our Current City Mask: " + str(current_city_mask))
"""

"""

    def fill_graph(self):
        # This function may not be necessary as can do the traveling salesman problem using a 2-D array, which we
        # have already built using a nested list in Python.
        # Load unique_count first.
        counter = 0
        for address in self.address_list:
            a_string = "vertex_" + str(counter) + " = Vertex('" + address + "')"
            exec(a_string)
            a_string = "self.graph.add_vertex(vertex_" + str(counter) + ")"
            exec(a_string)
            counter = counter + 1

        # Load weights second.
        for row_index, row in enumerate(self.distance_matrix):
            for col_index, col in enumerate(row):
                a_string = "self.graph.add_undirected_edge(vertex_" + str(row_index) + ", vertex_" + str(col_index) + \
                           ", " + str(col) + ")"
                exec(a_string)
"""


def fill_package_hashtable(self):
    """
    This is a hash table function that takes the package ID as the key and stores all information about the
    package as the value. Since we know all the keys and there are no collisions, this is a perfect hash table.
    Additionally, since we already grouped the data beforehand, there is no need to have 8+ parameter inputs into
    the hash table function. We only need the key and value of the key for this to work correctly. The value is
    the grouped data, with 8 elements each, in a python list.

    The elements of the hash table values are categorized below:
        Element 0: Package ID
        Element 1: Address
        Element 2: City
        Element 3: State
        Element 4: Zipcode
        Element 5: Delivery Deadline
        Element 6: Weight
        Element 7: Special Notes
        Element 8: Delivery Status
        Element 9: Vertex Address
        Element 10: Address Index
    """
    for element in self.packages:
        self.package_hashtable.put(int(element[0]), element)


"""
def start(self):
    self.build_proxy()
    self.print_data(self.proxy)
    mask = [False] * PROXY_COUNT
    mask[0] = True
    print("Okay... I'm about to find the fastest_route path for Truck 1... This takes about 7 seconds...")
    self.hamiltonian_cycle_slow(mask, 0, 0, [0])
    print(self.min_cost)
    print("Looks like the simulation looks good. let's run it! Above is our current data!")

# if cost * self.patience > self.fastest_route[0]:  # Ignore patience.
# return

"                  \n" + \
               "                    Location: " + str(self.simulation.index_addresses[self.location]) + \
                " || Next Stop: " + str(self.simulation.index_addresses[self.address_map[self.next_address]]) + "\n" + \


       "                   _______________________________________________________________________________\n" + \
       "             /    | Package IDs: " + str(self.truck_1.ids) + self.space(lim_1, len_1) + "\n" + \
       "            /---, | Address Route: " + str(self.truck_1.address_map) + self.space(lim_2, len_2) + "\n" + \
       "       -----# ==| | Route Weight: " + str(self.truck_1.weight_map) + " = " + str(
    self.truck_1.weight) + self.space(lim_3, len_3) + "\n" + \
       "       | :) # ==| | Miles: " + str(self.truck_1.miles) + " || Packages: " + str(self.truck_1.count) + \
       " || Location: " + str(self.index_addresses[self.truck_1.location]) + self.space(lim_4, len_4) + "\n" + \
       "  -----'----#   | |_______________________________________________________________________________|\n" + \
       "  |)___()  '#   |______====____   \_____________________________________________________|\n" + \
       ' [_/,-,\"--"------ //,-,  ,-,\\\   |/                               //,-,  ,-,  ,-,\\ __#\n' + \
       "   ( 0 )|===******||( 0 )( 0 )||-  o                                '( 0 )( 0 )( 0 )||\n" + \
       "----'-'--------------'-'--'-'-----------------------------------------'-'--'-'--'-'--------------\n" + \
       "                                     TRUCK " + str(self.truck_1.identifier) + " -" + str(self.time)
"""


"""

unique_indexes = duplicate_indexes[:]
unique_indexes = list(set_time(unique_indexes))  # Remove duplicate indexes

duplicate_count = len(duplicate_indexes) - len(set_time(duplicate_indexes))  # Counts duplicates.
unique_count = len(unique_indexes)  # Counts uniques.

# Since truck is only filled partially, attempts to load up remaining slots with duplicate address packages.
for package in self.warehouse:
    if package[-1] in unique_indexes and package[0] not in package_ids:
        duplicate_indexes.append(package[-1])
        package_ids.append(package[0])
        duplicate_count = duplicate_count + 1

total_count = duplicate_count + unique_count
"""

"""
print_simulation(simulation.package_hashtable)
for elements in simulation.package_table:
    print_simulation(str(elements))
print_simulation(simulation.package_hashtable)

# Print complete
for index, element in enumerate(self.temp):
    print_simulation(self.temp[index])
print_simulation(address_list)
"""


"""
    def build_proxy(self):
        # Before building our traveling salesman algorithm, lets create a graph using the subset of all the data.
        # This will make it easier to work with 4 unique_count rather than 27 unique_count for testing purposes.
        proxy = self.distances[:]
        for row in proxy:
            while len(row) > LOAD_COUNT:
                del row[-1]
        while len(proxy) > LOAD_COUNT:
            del proxy[-1]
        self.proxy = proxy
"""

"""
def seed_duplicates(self, bay, ids, indexes, hub, count):
    # Checks to see if there are any duplicate address packages we missed. Add that to bay.
    for package in hub:
        for pair in bay:
            if package[-1] == pair[-1]:
                bay, ids, indexes, hub, count = self.loading(package, bay, ids, indexes, hub, count)
    return bay, ids, indexes, hub, count
"""