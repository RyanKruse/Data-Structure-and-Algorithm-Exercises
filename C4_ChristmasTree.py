class Pascal:
    def __init__(self, height):
        self.rows = 0
        self.height = height
        self.a_list = []
        self.b_list = []
        self.c_list = []
        self.d_list = []

    def run(self):
        print(self.space(self.a_list))
        self.rows += 1
        print(self.space(self.b_list))
        self.rows += 1
        print(self.space(self.c_list))
        self.rows += 1
        print(self.space(self.d_list))

    def space(self, temp_list):
        string = ''
        for char in temp_list:
            if char < 10:
                string += str(char) + '   '
            elif char >= 10:
                string += str(char) + '  '
        for _ in range(10 - self.rows):
            string = '  ' + string
        return string

    def recursion(self, height, row=1):
        if row == 1:
            self.a_list.append(1)
            if row != height:
                self.recursion(height, row+1)
        elif row == 2:
            self.b_list.append(1)
            self.b_list.append(1)
            if row != height:
                self.recursion(height, row+1)
        elif row == 3:
            self.c_list.append(1)
            self.c_list.append(self.b_list[0] + self.b_list[1])
            self.c_list.append(1)
            if row != height:
                self.recursion(height, row+1)
        elif row == 4:
            self.d_list.append(1)
            self.d_list.append(self.c_list[0] + self.c_list[1])
            self.d_list.append(self.c_list[1] + self.c_list[2])
            self.d_list.append(1)

    def online_solution(self, num):
        if num == 0:
            return []
        elif num == 1:
            return [[1]]
        else:
            new_row = [1]
            result = self.online_solution(num-1)
            last_row = result[-1]
            for i in range(len(last_row)-1):
                new_row.append(last_row[i] + last_row[i+1])
            new_row += [1]
            result.append(new_row)
        return result

    def print(self, ans):
        self.rows = 0
        for row in ans:
            print(self.space(row))
            self.rows += 1


# TODO: Edit Pascal Triangle and clean it up, along with including commentary about why our approach failed.
pascal = Pascal(3)
pascal.recursion(4)
pascal.run()
answer = pascal.online_solution(9)
pascal.print(answer)
