class River:
    def __init__(self):
        self.sets = []
        self.filtered = []
        self.position = []
        self.final = []
        self.formatted = []

    def recursion(self, person):
        self.position.append(person)
        if len(self.position) >= 7:
            print(f'{self.position[1:]} was added to set.')
            self.sets.append(self.position[1:])
        else:
            self.recursion(0)
            self.position.pop()
            self.recursion(1)
            self.position.pop()

    def process(self):
        for t in self.sets:
            temp = 0
            for num in t:
                temp += num
            if temp == 3:
                self.filtered.append(t)
        for t in self.filtered:
            boat1 = t[0] + t[1]
            boat2 = t[2] + t[3]
            boat3 = t[4] + t[5]
            if boat1 + boat2 != 3 and boat2 + boat3 != 3:
                self.final.append(t)
        for t in self.final:
            self.formatted.append([[t[0], t[1]], [t[2], t[3]], [t[4], t[5]]])

    def answer(self):
        print('\nThe answer to the boat problem (0 = Missionary; 1 = Cannibal):')
        for t in self.formatted:
            print(f'\t{t}')


# Missionaries are 0, Carnivores are 1
river = River()
river.recursion(0)
river.process()
river.answer()
