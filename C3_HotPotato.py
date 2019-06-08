from collections import deque
import random


class HotPotatoSim:
    def __init__(self, names, max_passes, min_passes, randomized):
        """
        Initializes variables.
        If randomized = False, total passes will equal max_passes always.
        If randomized = True, total passes will equal random integers between min_passes and max_passes."""
        self.queue = deque()
        self.names = names
        self.randomized = randomized
        self.max_passes = max_passes
        self.min_passes = min_passes
        self.passes = self.max_passes
        self.prep_sim()

    def prep_sim(self):
        """Prepares the simulator by filling up the queue."""
        for name in self.names:
            self.queue.append(name)
        print('Here are our players: \n%s, %s has the potato.\n' % (self.names, self.names[0]))

    def run_sim(self):
        """Runs the simulator until there is only one person left."""
        while True:
            if len(self.queue) == 1:
                print('%s is the winner!' % self.queue.popleft())
                break
            if self.randomized:
                self.passes = random.randint(self.min_passes, self.max_passes)
            for _ in range(0, self.passes):
                self.queue.append(self.queue.popleft())
            print('Potato was passed %d times. %s is out.' % (self.passes, self.queue.popleft()))


hot_potato_sim = HotPotatoSim(['Bill', 'Brad', 'Kent', 'Jane', 'Susan', 'David', 'Henry'], 7, 1, True)
hot_potato_sim.run_sim()