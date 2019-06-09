# Implementation of the full logic gate ADT, child logic gate inheritances, and gate pin connections.


class LogicGate:
    def __init__(self, name=''):
        self.id = name
        self.output = None
        self.a = None
        append_group(self)

    def __str__(self):
        """Returns a word representation of self."""
        return self.id + ' (' + str(self.__class__.__name__) + ')'

    def get_output(self):
        """
         Returns the calculated output for this gate, after pin inputs and logic is calculated.
         If this gate is connected to another gate as a FromLogicGate, our output will become the pin input for the
         ToLogicGate; this occurs in the get_input() function for the ToLogicGate object.
         """
        self.output = self.logic()
        return self.output

    def get_input(self, alphabet):
        """
        This function gets an alphabet and transforms that alphabet into self.a, self.b, or self.c (denoted as pin_x)
        Then we check if pin_x is empty. If it is, we run a while loop to accept a valid user input and return it.

        Otherwise, we check if pin_x is a connector. If it is, we do several things:
            1) We call the FromLogicGate answer function and store the output into a variable (fr_answer).
            2) We check if fr_answer is a list. If it is, we determine which element we return from the list by
               checking the connector switch.
            3) If fr_answer is not a list, that means it does not have 2 outputs, thus we return fr_answer.

        Lastly, there are error functions on the bottom catch any bad switch, user, or gate inputs.
        """
        pin_x = eval('self.' + alphabet)
        if pin_x is None:
            # If our pin is empty, get a valid pin state from user.
            while True:
                # Only accepts an input of 0 or 1.
                pin_x = input('Enter Pin ' + alphabet.upper() + ' for ' + str(self) + ' --> ')
                if pin_x == '0' or pin_x == '1':
                    return int(pin_x)

        if isinstance(pin_x, Connector):
            # If our pin is a connector, get FromLogicGate answer and Connector switch.
            fr_answer = pin_x.fr.get_output()
            if isinstance(fr_answer, list):
                # If the answer is a list, we consult the connector switch to determine which output we are returning.
                if pin_x.switch == 'sum':
                    return fr_answer[0]
                elif pin_x.switch == 'carry':
                    return fr_answer[1]
                # Error to catch invalid switch statements.
                self.switch_error()
            else:
                # If the answer is not a list, return FromLogicGate answer.
                return fr_answer
        # Error to catch pins not empty and not a connector.
        self.pin_error()

    def connect(self, connector):
        """Links Connector to the next get_available ToLogicGate Pin as it meets class conditions."""
        if not self.a and isinstance(self, (UnaryGate, BinaryGate, TrinaryGate)):
            self.a = connector
        elif not self.b and isinstance(self, (BinaryGate, TrinaryGate)):
            self.b = connector
        elif not self.c and isinstance(self, TrinaryGate):
            self.c = connector
        else:
            # Error when connector is assigned a logic gate with no available inputs.
            self.pin_error()

    def pin_error(self):
        raise RuntimeError('Error: No empty input pins get_available for connector, or pin has an invalid input.')

    def switch_error(self):
        raise RuntimeError('Error: We have 2 possible inputs but there is no valid switch to choose between them.')

    def logic(self):
        """The grandchild classes replace this function."""
        pass


class Connector:
    """A Connector works to bridge the answer of one gate to the input of another. Also holds switch statement."""
    def __init__(self, fr, to, switch=None):
        self.fr = fr
        self.to = to
        self.switch = switch
        to.connect(self)


class TrinaryGate(LogicGate):
    """"Has three pins."""
    def __init__(self, name=''):
        super().__init__(name)
        self.b = None
        self.c = None


class BinaryGate(LogicGate):
    """Has two pins."""
    def __init__(self, name=''):
        super().__init__(name)
        self.b = None


class UnaryGate(LogicGate):
    """Has one pin."""
    def __init__(self, name=''):
        super().__init__(name)


class FullAdderGate(TrinaryGate):
    """
    Gets three input values. Returns a [sum, carry] list.

    A | B | C | s | c
    ------------------
    0 | 0 | 0 | 0 | 0
    1 | 0 | 0 | 1 | 0
    0 | 1 | 0 | 1 | 0
    0 | 0 | 1 | 1 | 0
    1 | 1 | 0 | 0 | 1
    0 | 1 | 1 | 0 | 1
    1 | 0 | 1 | 0 | 1
    1 | 1 | 1 | 1 | 1
    """
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        self.c = self.get_input('c')
        if self.a == 1 and self.b == 1 and self.c == 1:
            return [1, 1]
        elif self.a == 0 and self.b == 0 and self.c == 0:
            return [0, 0]
        elif (self.a == 1 and self.b == 1) or (self.b == 1 and self.c == 1) or (self.c == 1 and self.a == 1):
            return [0, 1]
        else:
            return [1, 0]


class HalfAdderGate(BinaryGate):
    """
    Gets two input values. Returns a [sum, carry] list.

    A | B | s | c
    --------------
    0 | 0 | 0 | 0
    0 | 1 | 1 | 0
    1 | 0 | 1 | 0
    1 | 1 | 0 | 1
    """
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a != self.b:
            return [1, 0]
        elif self.a == 1 and self.b == 1:
            return [0, 1]
        else:
            return [0, 0]


class AndGate(BinaryGate):
    """Gets two input values. Returns 1 if both values are 1."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a == 1 and self.b == 1:
            return 1
        else:
            return 0


class NandGate(BinaryGate):
    """Gets two input values. Returns 0 if both values are 1."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a == 1 and self.b == 1:
            return 0
        else:
            return 1


class OrGate(BinaryGate):
    """Gets two input values. Returns 1 if at least one values is 1."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a == 1 or self.b == 1:
            return 1
        else:
            return 0


class NorGate(BinaryGate):
    """Gets two input values. Returns 0 if at least one value is 1."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a == 1 or self.b == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    """Gets two input values. Returns 1 if one value, but not both, is 1."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        self.b = self.get_input('b')
        if self.a != self.b:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """Gets one input value. Returns the opposite value."""
    def __init__(self, name=''):
        super().__init__(name)

    def logic(self):
        self.a = self.get_input('a')
        if self.a == 0:
            return 1
        else:
            return 0


def append_group(gate):
    """Contains all created logic gates."""
    group.append(gate)


def test_1(group):
    """Test Case 1: A 4-Bit Adder. Input 2 binary numbers in backward order to see the sum."""
    gate_list = []
    answer_string = ''
    g1 = FullAdderGate('G1')
    g2 = FullAdderGate('G2')
    g3 = FullAdderGate('G3')
    g4 = FullAdderGate('G4')
    c1 = Connector(g1, g2, 'carry')
    c2 = Connector(g2, g3, 'carry')
    c3 = Connector(g3, g4, 'carry')

    # This gets the sum of every single FullAdderGate.
    group[-1].get_output()
    for gate in group:
        gate_list.append(gate.output[0])
    gate_list.append(group[-1].output[1])

    # Then it formats it into an answer which is then printed.
    gate_list.reverse()
    for num in gate_list:
        answer_string += str(num)
    print('The sum is %s.' % answer_string)


def test_2():
    """
    Test Case 2.1: A fuller adder circuit. Input the gates and compare the results with the matrix table.
    Test Case 2.2: A half adder circuit. Input the gates and compare the results with the matrix table.
    """

    # A | B | C | s | c
    # ------------------
    # 0 | 0 | 0 | 0 | 0
    # 1 | 0 | 0 | 1 | 0
    # 0 | 1 | 0 | 1 | 0
    # 0 | 0 | 1 | 1 | 0
    # 1 | 1 | 0 | 0 | 1
    # 0 | 1 | 1 | 0 | 1
    # 1 | 0 | 1 | 0 | 1
    # 1 | 1 | 1 | 1 | 1

    g1 = FullAdderGate('G1')
    print(g1.get_output())

    # A | B | s | c
    # --------------
    # 0 | 0 | 0 | 0
    # 0 | 1 | 1 | 0
    # 1 | 0 | 1 | 0
    # 1 | 1 | 0 | 1

    g1 = HalfAdderGate('G1')
    print(g1.get_output())


def test_3():
    """Test Case 3: Expected G8 output is 1 only if all inputs from G1 to G8 are 0."""
    # Block 1
    g1 = AndGate('G1')
    g2 = OrGate('G2')
    g3 = NotGate('G3')
    c1 = Connector(g1, g2)
    c2 = Connector(g2, g3)

    # Block 2
    g4 = NandGate('G4')
    g5 = XorGate('G5')
    c3 = Connector(g4, g5)
    c4 = Connector(g3, g5)

    # Block 3
    g6 = NotGate('G6')
    g7 = NorGate('G7')
    g8 = AndGate('G8')
    c5 = Connector(g5, g6)
    c6 = Connector(g7, g8)
    c7 = Connector(g6, g8)
    print(g8.get_output())


group = []
test_1(group)
test_2()
test_3()

