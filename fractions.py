class Fraction:
    def __init__(self, numerator, denominator):
        """Initializes fraction class. Only accepts integers."""
        self.common = None
        self.numerator = None
        self.denominator = None
        self.recalc(numerator, denominator)

    def recalc(self, numerator, denominator):
        """
        First checks both inputs are integers.
        Then checks if denominator is negative. If so, flip the value of numerator and make denominator positive.
        Lastly, finds the largest common denominator of numerator and denominator then divides both values by it.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise RuntimeError('Error: Numerator or denominator is not an integer.')

        if denominator < 0:
            denominator = -denominator
            numerator = -numerator

        self.common = self.gcd(numerator, denominator)
        self.numerator = numerator//self.common
        self.denominator = denominator//self.common

    def get_numerator(self):
        """Returns the numerator."""
        return str(self.numerator)

    def get_denominator(self):
        """Returns the denominator."""
        return str(self.denominator)

    def print(self):
        """Prints self in console."""
        print(self)

    def __str__(self):
        """Returns a word representation of the Fraction numerator and denominator."""
        return str(self.numerator) + '/' + str(self.denominator)

    def __repr__(self):
        """Returns a word representation of this object's instance of the Fraction ADT."""
        return 'Fraction(%s, %s)' % (self.numerator, self.denominator)

    def __radd__(self, other):
        """
        Returns a new fraction object with sum of the numerator and denominator,
        This function fires if the object being added to is not of the fraction class.
        print(2 + Fraction(2/1)) will print 4
        print(Fraction(2/1) + 4) will print 6
        """
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __iadd__(self, other):
        """
        Increments self numerator and denominator with other self numerator and denominator.
        We are not returning a new fraction object, but instead returning a modified version of self.
        Because numerator and denominator values may change, we recalc self variables.
        """
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.numerator = self.numerator * other.denominator + self.denominator * other.numerator
        self.denominator = self.denominator * other.denominator

        self.recalc(self.numerator, self.denominator)

        return self

    def __add__(self, other):
        """Returns a new fraction object with sum of the numerator and denominator."""
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        """Returns a new fraction object with subtraction of the numerator and denominator."""
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        """Returns a new fraction object with multiplication of the numerator and denominator."""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        """Returns a new fraction object with division of the numerator and denominator."""
        return Fraction(self.numerator // other.numerator, self.denominator // other.denominator)

    def __eq__(self, other):
        """Puts two fractions in common terms and then checks if equal."""
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other):
        """Puts two fractions in common terms and then checks if not equal."""
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __gt__(self, other):
        """Checks if value of one fraction is greater than value of other."""
        return self.numerator/self.denominator > other.numerator/other.denominator

    def __ge__(self, other):
        """Checks if value of one fraction is greater or equal to value of other."""
        return self.numerator/self.denominator >= other.numerator/other.denominator

    def __lt__(self, other):
        """Checks if value of one fraction is less than value of other."""
        return self.numerator/self.denominator < other.numerator/other.denominator

    def __le__(self, other):
        """Checks if value of one fraction is less than or equal to value of other."""
        return self.numerator/self.denominator <= other.numerator/other.denominator

    def gcd(self, m, n):
        """Returns the greatest common denominator of two integers."""
        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n
        return n


def test_case_1():
    """Contains sample code to test the functions of the fraction class. All works correctly."""
    # __init__()
    quarter = Fraction(1, 4)
    half = Fraction(2, 4)
    whole = 1

    # print()
    quarter.print()  # 3/4

    # __repr__()
    print(repr(quarter))  # Fraction(1, 4)

    # get_numerator()
    print(quarter.get_numerator())  # 1

    # get_denominator()
    print(quarter.get_denominator())  # 4

    # __radd__(other)
    print(quarter + 1)  # 5/4
    whole += quarter
    print(whole)  # 5/4
    whole -= quarter
    print(whole)  # 1/1

    # __iadd__(other)
    quarter += half
    print(quarter)  # 3/4
    quarter -= half
    print(quarter)  # 1/4

    # __add__(other)
    print(quarter + half)  # 3/4

    # __sub__(other)
    print(quarter - half)  # -1/4

    # __mul__(other)
    print(quarter * half)  # 1/8

    # __truediv__(other)
    print(quarter / half)  # 1/2

    # __eq__(other)
    print(quarter == half)  # False

    # __ne__(other)
    print(quarter != half)  # True

    # __gt__(other)
    print(quarter > half)  # False

    # __ge__(other)
    print(quarter >= half)  # False

    # __lt__(other)
    print(quarter < half)  # True

    # __le__(other)
    print(quarter <= half)  # True

    # gcd(m, n)
    print(quarter.gcd(12, 16))  # 4
    print(quarter.gcd(14, 63))  # 7


test_case_1()
