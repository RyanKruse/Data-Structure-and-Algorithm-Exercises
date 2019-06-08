import time


class SudokuSolver:
    def __init__(self, sudoku_input):
        """We assume that the sudoku puzzle is solvable and that our inputs have no typos."""
        self.puzzle_raw = sudoku_input
        self.puzzle_final = [[], [], [], [], [], [], [], [], []]
        self.puzzle_final_backup = None
        self.puzzle_preserved = [[], [], [], [], [], [], [], [], []]

        self.answer_dictionary = {}
        self.brute_solutions = {}
        self.block_dict = {0: [[0, 1, 2], [0, 1, 2]],
                           1: [[0, 1, 2], [3, 4, 5]],
                           2: [[0, 1, 2], [6, 7, 8]],
                           3: [[3, 4, 5], [0, 1, 2]],
                           4: [[3, 4, 5], [3, 4, 5]],
                           5: [[3, 4, 5], [6, 7, 8]],
                           6: [[6, 7, 8], [0, 1, 2]],
                           7: [[6, 7, 8], [3, 4, 5]],
                           8: [[6, 7, 8], [6, 7, 8]]}
        self.binary_dict = {1: 0, 0: 1}
        self.row_counter = 0
        self.col_counter = 0
        self.empty_cells = 0
        self.start_time = 0
        self.end_time = 0
        self.solvable = True

    def solution(self):
        """
        The entire sudoku solver runs here:
            1) We format the raw puzzle input.
            2) We drill out guaranteed solutions.
            3) We fail solutions for binary cells and recursively call self.
        """
        self.format_puzzle()
        self.drill_cells()
        self.brute_force()

    def format_puzzle(self):
        """
        This splits the raw puzzle input into nested lists so it becomes easier to identify rows and columns.
        The end result is a list that contains 9 lists (mimicking 9 rows), which contain 9 elements each.

               self.puzzle_raw                                self.puzzle_final
        [4, 7, 1, 0, 3, 5, 0, 0, 0,         -->        [[4, 7, 1, 0, 3, 5, 0, 0, 0],
         9, 0, 0, 0, 0, 8, 0, 6, 3,         -->         [9, 0, 0, 0, 0, 8, 0, 6, 3],
         6, 3, 0, 1, 0, 0, 0, 5, 4,         -->         [6, 3, 0, 1, 0, 0, 0, 5, 4],
         7, 0, 6, 0, 0, 0, 0, 2, 0,         -->         [7, 0, 6, 0, 0, 0, 0, 2, 0],
         0, 9, 0, 5, 0, 0, 4, 1, 8,         -->         [0, 9, 0, 5, 0, 0, 4, 1, 8],
         0, 0, 0, 9, 2, 3, 5, 0, 0,         -->         [0, 0, 0, 9, 2, 3, 5, 0, 0],
         8, 4, 9, 0, 0, 7, 0, 0, 0,         -->         [8, 4, 9, 0, 0, 7, 0, 0, 0],
         0, 1, 0, 3, 0, 4, 9, 0, 0,         -->         [0, 1, 0, 3, 0, 4, 9, 0, 0],
         0, 0, 7, 0, 1, 0, 2, 0, 5]         -->         [0, 0, 7, 0, 1, 0, 2, 0, 5]]
        """
        # Starts our puzzle timer.
        self.start_time = time.time()
        # Records how many empty cells we have in our sudoku.
        for cell in self.puzzle_raw:
            if cell == 0:
                self.empty_cells += 1
        # Prints puzzle statistics.
        print('There are ' + str(self.empty_cells) + ' empty cells and ' + str(81 - self.empty_cells) + ' filled cells')
        print('Complete: 0%\n')
        # Formats our puzzle.
        counter = 0
        for index, cell in enumerate(self.puzzle_raw):
            if index % 9 == 0 and index:
                counter += 1
            self.puzzle_final[counter].append(cell)
            self.puzzle_preserved[counter].append(cell)

    def drill_cells(self):
        """
        This drills out guaranteed cell solutions by process of elimination until there are no more solutions found.

        For example: Assume there can only be one possible number in cell (3, 5). Plug that number in, we then identify
        there can only be one possible number for cell (8, 5). Plug that in, we then identify there can only be one
        possible number for cell (5, 3) and (5, 5), etc. Repeat this process in a while loop.

        When we call this function from the brute force methods, there will often be instances where there are
        absolutely zero possible numbers that can fit into a cell. In this case, we identify that the current puzzle
        is unsolvable.

        There are 3 possible scenarios we're in after the drill_cells() while loop ends:
            1) We solved the entire puzzle.
            2) We have an impossible puzzle due to a bad guess.
            3) We solved only a partial part of the puzzle.
        """
        # Sets variables and backs up puzzle.
        run_loop = True
        self.solvable = True
        self.puzzle_final_backup = [x[:] for x in self.puzzle_final]

        while run_loop:
            run_loop = False
            # Gets a dictionary of all possible numbers that fit into all empty cells.
            self.answer_dictionary = self.get_solutions()
            for key, value in self.answer_dictionary.items():
                # Audit all dictionary values.
                if not value:
                    # If a dictionary value has an empty list, puzzle is unsolvable and one of our guesses were bad.
                    run_loop = False
                    self.solvable = False
                    break
                elif len(value) == 1:
                    # If a dictionary value has a list with only 1 element, plug that into the final puzzle.
                    # Repeat loop to see if we can drill more answers with new value plugged in.
                    run_loop = True
                    self.puzzle_final[key[0]][key[1]] = value[0]

        if self.solvable:
            # States while loop ended.
            print("\tCan't drill further.\n")
        if not self.answer_dictionary:
            # If answer dictionary is empty, puzzle is solved.
            self.print_answer()
            exit()

    def get_solutions(self):
        """
        This function does the following:
            1) Loop through all cells in the puzzle.
            2) Identify all possible numbers that can fit into each individual empty cell.
            3) Store this data into a dictionary called solutions. The key is cell coordinates, value is number list.
            4) Return this dictionary when loop finishes.
        """
        solutions = {}
        # Loop through every single cell.
        for row_index, row in enumerate(self.puzzle_final):
            for col_index, cell in enumerate(row):
                # Processes only blank cells.
                if cell == 0:
                    # Gets a list of all numbers that can fit into the cell and adds data to solutions dictionary.
                    solutions[(row_index, col_index)] = self.get_valid(row_index, col_index)
        return solutions

    def get_valid(self, row_index, col_index):
        """
        Returns a list of all possible numbers that fit into an empty cell.

        The numbers that fit into an empty cell must pass through the following basic mathematical conditions:
            1) Checks to see if the number is not in the cell row.
            2) Checks to see if the number is not in the cell column.
            3) Checks to see if the number is not in the cell block.

        After identifying all possible numbers that can fit into the cell, print and return the valid numbers list.

        If there are no possible numbers, return an empty list. This means a previous guess was bad for the puzzle
        and this will get picked up in the next dictionary audit.
        """
        valid = []
        self.row_counter = row_index
        self.col_counter = col_index
        master_key = self.block_dict.get(self.get_block(row_index, col_index))

        for num in list(range(1, 10)):
            failed = False
            if num in self.puzzle_final[self.row_counter]:
                failed = True
            for row in self.puzzle_final:
                if num == row[self.col_counter]:
                    failed = True
            for row_key_index in master_key[0]:
                for col_key_index in master_key[1]:
                    if num == self.puzzle_final[row_key_index][col_key_index]:
                        failed = True
            if not failed:
                valid.append(num)

        if len(valid) == 1:
            print('\tRow: ' + str(self.row_counter) + ' Column: ' + str(self.col_counter) + ' is ' + str(valid))
        elif not valid:
            print('\tRow: ' + str(self.row_counter) + ' Column: ' + str(self.col_counter) + ' is impossible.')
        return valid

    def get_block(self, row, col):
        """
        Identifies which 3x3 block the cell is located in. This is used to pull dictionary values in get_valid.
        Below is a matrix of what block key is identified for each cell:

        0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2
        0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2
        0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 2
        ---------------------------------
        3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5
        3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5
        3 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5
        ---------------------------------
        6 | 6 | 6 | 7 | 7 | 7 | 8 | 8 | 8
        6 | 6 | 6 | 7 | 7 | 7 | 8 | 8 | 8
        6 | 6 | 6 | 7 | 7 | 7 | 8 | 8 | 8
        """
        if row <= 2:
            if col <= 2:
                return 0
            elif col <= 5:
                return 1
            else:
                return 2
        elif row <= 5:
            if col <= 2:
                return 3
            elif col <= 5:
                return 4
            else:
                return 5
        else:
            if col <= 2:
                return 6
            elif col <= 5:
                return 7
            else:
                return 8

    def brute_force(self):
        """
        This function cycles through empty cells that have only two solution values, i.e. (0, 2) = [2, 9]
        These are called binary cells; if one solution fails the other must succeed.
        Thus, the objective of this function is to fail solutions.

        The function follows these directions:
           1) Plug the first value into the binary cell and call drill_cells().
           2) If puzzle becomes unsolvable --> reset puzzle and accept second value as solution.
           3) Call drill_cells() to make progress, then recursively call self.
           4) ...If first value did not fail --> reset puzzle then repeat steps 1-3 with the second value.
           5) ...If both values did not fail --> reset puzzle and continue to next cell.

        There is a possibility that after trying all binary cells we still don't make any progress.
        This function requires dynamic recursive programming for such scenario and is mentioned in the TODO.
        """
        self.print_progress()
        self.brute_solutions = self.answer_dictionary.copy()

        for key, value in self.brute_solutions.items():
            if len(value) == 2:
                # There is a recursive call to self if one of the solutions succeed.
                self.test_solution(key, value, 0)
                self.restore_puzzle()
                self.test_solution(key, value, 1)
                self.restore_puzzle()

                print('We do not know the solution. Skip.')
                self.puzzle_final[key[0]][key[1]] = 0

    def test_solution(self, key, value, index):
        """Follows steps 1-4 in the brute force function. Test both binary cell solutions."""
        print("Row: %s Column %s is either [%d] or [%d]\nLet's plug [%d] into the cell\n"
              % (key[0], key[1], value[0], value[1], value[index]))
        self.puzzle_final[key[0]][key[1]] = value[index]
        self.drill_cells()

        if not self.solvable:
            print("\nThe value we plugged in made this solution impossible. Row %s Column %s must therefore be [%d]\n"
                  % (key[0], key[1], value[self.binary_dict.get(index)]))
            self.restore_puzzle()
            self.puzzle_final[key[0]][key[1]] = value[self.binary_dict.get(index)]
            self.drill_cells()
            self.brute_force()

    def print_progress(self):
        """Displays how much of the Sudoku puzzle is solved."""
        cells_remaining = 0
        for row in self.puzzle_final:
            for col in row:
                if col == 0:
                    cells_remaining += 1
        print('Complete: ' + str(round((1-(cells_remaining/self.empty_cells)) * 100)) + '%')

    def print_answer(self):
        """Once the puzzle is solved, we print our results."""
        self.end_time = time.time()
        print('%48s\n%16s%45s\n' % ('The puzzle is 100% solved', 'Input', 'Output'))
        for int in range(0, len(self.puzzle_final)):
            print(str(self.puzzle_preserved[int]) + '       -->       ' + str(self.puzzle_final[int]))
        print('\n\t\t\t\t   Total time to solve: %.3f seconds' % (self.end_time - self.start_time))

    def restore_puzzle(self):
        """Reset the puzzle state prior to the drill_cells() function running."""
        self.puzzle_final = [x[:] for x in self.puzzle_final_backup]


NYT_puzzle_easy1 = [4, 7, 1, 0, 3, 5, 0, 0, 0,
                    9, 0, 0, 0, 0, 8, 0, 6, 3,
                    6, 3, 0, 1, 0, 0, 0, 5, 4,
                    7, 0, 6, 0, 0, 0, 0, 2, 0,
                    0, 9, 0, 5, 0, 0, 4, 1, 8,
                    0, 0, 0, 9, 2, 3, 5, 0, 0,
                    8, 4, 9, 0, 0, 7, 0, 0, 0,
                    0, 1, 0, 3, 0, 4, 9, 0, 0,
                    0, 0, 7, 0, 1, 0, 2, 0, 5]

NYT_puzzle_medi1 = [0, 0, 0, 5, 0, 0, 0, 0, 0,
                    2, 1, 6, 8, 0, 0, 0, 3, 0,
                    0, 0, 0, 0, 0, 0, 8, 0, 0,
                    4, 0, 2, 0, 7, 0, 0, 0, 0,
                    0, 0, 3, 0, 0, 1, 0, 0, 7,
                    5, 0, 0, 6, 4, 0, 9, 0, 0,
                    0, 0, 0, 0, 2, 0, 7, 5, 0,
                    3, 9, 7, 0, 0, 0, 0, 2, 0,
                    0, 0, 0, 0, 0, 0, 4, 0, 0]

NYT_puzzle_medi2 = [0, 0, 0, 0, 0, 5, 1, 0, 0,
                    0, 0, 0, 6, 0, 0, 9, 0, 7,
                    8, 2, 0, 0, 0, 0, 6, 0, 0,
                    0, 5, 0, 0, 8, 0, 4, 0, 0,
                    0, 0, 0, 0, 7, 0, 0, 0, 0,
                    0, 0, 4, 0, 0, 9, 2, 0, 8,
                    0, 0, 2, 3, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 5, 0, 0, 0, 1,
                    6, 3, 0, 2, 0, 4, 0, 0, 9]

NYT_puzzle_hard1 = [0, 0, 0, 5, 0, 0, 0, 0, 0,
                    0, 9, 0, 0, 0, 3, 0, 4, 0,
                    0, 0, 4, 9, 1, 0, 0, 8, 0,
                    0, 6, 9, 0, 0, 4, 8, 3, 0,
                    0, 0, 8, 1, 0, 0, 0, 0, 6,
                    4, 0, 0, 0, 0, 0, 5, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 7,
                    3, 0, 0, 0, 6, 0, 1, 0, 0,
                    6, 7, 0, 0, 2, 0, 0, 0, 0]

# TODO: After Castle 4, design a recursive solution to solve NYT_puzzle_med2.
sudoku_solver = SudokuSolver(NYT_puzzle_medi1)
sudoku_solver.solution()
