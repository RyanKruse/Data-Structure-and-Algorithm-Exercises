import string
from Allies import Stack


class Calculator:
    def __init__(self, answer=0):
        self.final_infix = ''
        self.user_infix = None
        self.infix_split = []
        self.numbers = {}
        self.answer = answer
        self.previous_answer = None
        self.recalc = False

    def run(self):
        """This runs the entire calculator."""
        print("\nEnter an infix expression to calculate the result. Enter 'q' to quit.")
        while True:
            self.__init__(self.answer)
            self.get_input()
            self.get_digits()
            self.calculations()
            self.print_answer()

    def get_input(self):
        """
        Gets user input and strips all white space. Checks to see if we quit.

        The "elif self.user_infix[0] in '+-/*':" statement determines whether or not we are going to be adding
        the previous answer to the start of the self.infix_split list. A user input beginning with an operator
        forces this elif-statement to fire, otherwise there won't be an operand paired with the operator.
        In the event there is no previous answer, we default the previous answer as 0.

        Finally, construct self.infix_split, a char list of the infix expression, and check if valid.
        """
        self.user_infix = "".join(input('--> ').split())

        if self.user_infix == 'q':
            quit()
        elif self.user_infix[0] in '+-/*':
            # Working with previous answer.
            self.recalc = True
            self.previous_answer = self.answer
            self.infix_split = list(str(self.previous_answer) + self.user_infix) + ['~']
        else:
            # Not working with previous answer.
            self.infix_split = list(self.user_infix) + ['~']

        for char in self.infix_split:
            if char not in '0123456789.~+-/*()':
                raise TypeError('Error: This calculator can only accept the follow characters: 0123456789.+-/*()')

    def get_digits(self):
        """
        This pushes numbers in stack. Then it converts that stack into a dictionary value with an alphabetic key.

        The reason we do this is that the calculations function cannot handle multiple digits because it is
        processing each element by character. For example, 2 + 2 can be processed but 10 + 10 cannot because it would
        be expecting a + - * / operator between the 1 and the 0.

        It is easier to have proxy variables, such as A + B rather than 10 + 10, and use that to pull dictionary values.
        The result would look like self.numbers.get('A') + self.numbers.get('B') with the self.numbers dictionary
        looking like {'A': 10, 'B': 10}. The calculator would read this as 10 + 10 without issue.

        Thus, the purpose of this function is to build that self.numbers dictionary and build self.final_infix with
        alphabetical variables substituting multi-digit numbers. self.final_infix is a word that looks like 'A+B'.
        """
        operands = Stack()
        alphabet_num = 65

        for char in self.infix_split:
            if char in '0123456789.':
                operands.push(char)
            elif not operands.isempty():
                alphabet = chr(alphabet_num)
                alphabet_num += 1
                number = ''
                # Converts number into a dictionary item.
                while not operands.isempty():
                    number = operands.pop() + number
                self.numbers[alphabet] = number
                self.final_infix += alphabet + char
            else:
                self.final_infix += char

    def calculations(self):
        """
        This is where the calculator does its magic.

        To see how this function works, please reference the textbook material on Chapter 3 Stacks. This algorithm was
        built by making an algorithm that takes an infix expression and transforms it into a postfix expression
        (2+2 --> 22+). Then, by taking that postfix expression and processing the operators and operands it until there
        is only 1 element in the stack, we get the postfix answer, which is the same answer for the infix expression.
        (22+ --> 4)

        It is possible to build a calculator with simply those 2 algorithms linked up to each other. However, this
        function is a hybrid of the two where it is able to simultaneously work with operators and operands, such that
        when an infix expression is determined to be in postfix expression, we immediately calculate the answer.
        """
        precedent = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
        operator_stack = Stack()
        operand_stack = Stack()

        for item in self.final_infix:
            if item in string.ascii_letters:
                operand_stack.push(self.numbers.get(item))
            elif item == '(':
                operator_stack.push(item)
            elif item == ')':
                # Here be dragons.
                top_of_stack = operator_stack.pop()
                while top_of_stack != '(':
                    operand2 = float(operand_stack.pop())
                    operand1 = float(operand_stack.pop())
                    operand_stack.push(self.do_math(top_of_stack, operand1, operand2))
                    top_of_stack = operator_stack.pop()
            elif item in precedent:
                while (not operator_stack.isempty()) and precedent[operator_stack.peek()] >= precedent[item]:
                    operand2 = float(operand_stack.pop())
                    operand1 = float(operand_stack.pop())
                    operand_stack.push(self.do_math(operator_stack.pop(), operand1, operand2))
                operator_stack.push(item)
            elif item == '~':
                # This is a helper variable to signal the end of infix expression and empty all stacks.
                while not operator_stack.isempty():
                    operand2 = float(operand_stack.pop())
                    operand1 = float(operand_stack.pop())
                    operand_stack.push(self.do_math(operator_stack.pop(), operand1, operand2))
            else:
                raise TypeError('Error: Calculations blew up.')

        self.answer = operand_stack.pop()

    def print_answer(self):
        """Prints the calculated answer."""
        if self.recalc:
            print('%0.4f%s = %0.4f' % (float(self.previous_answer), self.user_infix, float(self.answer)))
        else:
            print('%s = %0.4f' % (self.user_infix, float(self.answer)))

    def do_math(self, operator, operand1, operand2):
        """This is where the core math of the calculator takes place."""
        if operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        elif operator == '+':
            return operand1 + operand2
        else:
            return operand1 - operand2


calculator = Calculator()
calculator.run()
