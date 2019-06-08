from collections import deque
import random


# Settings.
HOURS = 10
PERSON_EVERY_MINUTE = 3
USE_STALL_PROBABILITY = .2
URINAL_TIME = 60
URINAL_MULTIPLIER = 2
MIN_STALL_TIME = 300
MAX_STALL_TIME = 450
NUM_URINALS = 3
NUM_STALLS = 7


class Restroom:
    def __init__(self, test_case=0):
        """Sets, or resets, prior data. Creates restroom facilities depending on settings."""
        # Structure.
        self.person_count = 0
        self.time_left = 3600*HOURS
        self.urinal_queue = deque()
        self.stall_queue = deque()

        # Groups & Results.
        self.facility_group = []
        self.urinal_group = []
        self.stall_group = []
        self.person_group = []
        self.test_case = test_case
        self.urinal_waits = []
        self.stall_waits = []

        # Creates Facilities.
        for identifier in range(0, NUM_URINALS):
            Urinal(self, identifier)
        for identifier in range(0, NUM_STALLS):
            Stall(self, identifier)

    def run(self, test_case):
        """This runs the entire restroom simulation."""
        self.__init__(test_case)
        while self.time_left > 0:
            self.allocate(self.get_available(self.stall_group), self.stall_queue)
            self.allocate(self.get_available(self.urinal_group), self.urinal_queue)
            self.allocate(self.get_available(self.stall_group), self.urinal_queue)
            self.tick()
        self.display_results()

    def allocate(self, available_facility, queue):
        """This function assigns the people in queue into an available facility."""
        while available_facility and queue:
            available_facility.pop().occupy(queue.popleft())

    def get_available(self, facilities):
        """This function returns a list of all available facilities of a particular group."""
        temp = []
        for facility in facilities:
            if not facility.occupied:
                temp.append(facility)
        return temp

    def tick(self):
        """Each tick we attempt to add a person to a queue. Additionally, we tick all facilities."""
        for facility in self.facility_group:
            facility.tick()
        if random.random() < float(PERSON_EVERY_MINUTE/60):
            Person(self)
        self.time_left -= 1

    def display_results(self):
        """This function prints the result of each test case."""
        average_urinal_wait = sum(self.urinal_waits)/len(self.urinal_waits)
        max_urinal_wait = max(self.urinal_waits)
        urinal_queue_size = len(self.urinal_queue)
        average_stall_wait = sum(self.stall_waits) / len(self.stall_waits)
        max_stall_wait = max(self.stall_waits)
        stall_queue_size = len(self.stall_queue)

        print('%5d%19d%27d%27d%25d%22d%25d%30d' % (self.test_case, average_urinal_wait, average_stall_wait,
                                                   max_urinal_wait, max_stall_wait, urinal_queue_size, stall_queue_size,
                                                   self.person_count))


class Facilities:
    def __init__(self, restroom, identifier):
        """Initializes variables."""
        self.restroom = restroom
        self.identifier = identifier
        self.occupied = False
        self.time_left = 0

        # Appends facility to parent and child class groups.
        self.restroom.facility_group.append(self)
        exec('self.restroom.' + str(self.__class__.__name__).lower() + '_group.append(self)')

    def occupy(self, person):
        """This function lets the facility know it is occupied with a person and to record/set times."""
        if not person.needs_stall and isinstance(self, Stall):
            person.time = URINAL_TIME*URINAL_MULTIPLIER
        person.record_time()
        self.time_left = person.time
        self.occupied = True

    def tick(self):
        """Ticks the time a person is left in the facility by 1. Checks to see if facility becomes unoccupied."""
        self.time_left -= 1
        if self.time_left <= 0:
            self.occupied = False


class Urinal(Facilities):
    """A child class of the Facilities parent class."""
    def __init__(self, restroom, identifier):
        super().__init__(restroom, identifier)


class Stall(Facilities):
    """A child class of the Facilities parent class."""
    def __init__(self, restroom, identifier):
        super().__init__(restroom, identifier)


class Person:
    def __init__(self, restroom):
        """Initializes variables."""
        # Structure.
        self.restroom = restroom
        self.identifier = restroom.person_count
        self.restroom.person_count += 1
        self.restroom.person_group.append(self)

        # Time Records.
        self.time = 0
        self.time_began_waiting = self.restroom.time_left
        self.total_time_waited = 0

        # Person Classification.
        self.needs_stall = random.random() < USE_STALL_PROBABILITY
        self.classify()

    def classify(self):
        """Determines whether a spawned person needs to use the urinal or the stall. Places in appropriate queue."""
        if self.needs_stall:
            self.time = random.randint(MIN_STALL_TIME, MAX_STALL_TIME)
            self.restroom.stall_queue.append(self)
        else:
            self.time = URINAL_TIME
            self.restroom.urinal_queue.append(self)

    def record_time(self):
        """When a person occupies a facility, records how long a person spent from entering queue to using facility."""
        self.total_time_waited = self.time_began_waiting - self.restroom.time_left
        if self.needs_stall:
            self.restroom.stall_waits.append(self.total_time_waited)
        else:
            self.restroom.urinal_waits.append(self.total_time_waited)


simulation = Restroom()
print('Below are the results of running the restroom simulation 13 times.')
print('%s%25s%25s%25s%25s%25s%25s%25s' % ('Test Case', 'Average Urinal Wait', 'Average Stall Wait', 'Max Urinal Wait',
                                          'Max Stall Wait', 'Current Urinal Queue', 'Current Stall Queue',
                                          'Total People'))
# Simulation runs 10 times.
for index in range(1, 11):
    simulation.run(index)
