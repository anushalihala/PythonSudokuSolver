import math


class SudokuContext:
    def __init__(self, sudoku_string, sudoku_size=None):
        if sudoku_size is None:
            self.board_size = len(sudoku_string)
        else:
            self.board_size = sudoku_size
        self.current_board = dict()       # actual values in Sudoku board
        self.current_domain = dict()      # possible value each cell in Sudoku board can take
        self.neighbours = dict()  # CONSTRAINT; all neighbours must be different

        if len(sudoku_string) != self.board_size:
            raise Exception(f"input Sudoku string length not equal to {self.board_size}")

    def __get_sudoku_indices(self, input_int):
        # converts linear indices [0-80] to 2d indices [0-8][0-8]
        divisor = int(math.sqrt(self.board_size))
        row = input_int / divisor
        col = input_int % divisor
        return str(row) + str(col)

    def __sudoku_string_to_context(self, sudoku_string):
        for i in range(self.board_size):
            # storing values from linear string Sudoku board into custom data structure (dictionary with rowcol as index)
            idx = get_indx(i)  # idx is a two character string with first value=row and second value=column
            val = int(sb_list[i])
            self.board[idx] = val

            if val == 0:
                self.domain[idx] = set(range(1, 10))  # initial domain -> if cell empty, can take any value from 1 to 9
            else:
                self.domain[idx] = set([val])  # initial domain -> if cell filled, can take only that value

            self.neighbours[idx] = self.compute_neighbours(idx)

if __name__=="__main__":
    print("hello main refactored!")
    # input_test = "010020300004005060070000008006900070000100002030048000500006040000800106008000000"
    # sc = SudokuContext(input_test)

    sudoku_indices = []
    for i in range(9):
        for j in range(9):
            sudoku_indices.append(str(i) + str(j))
    print(sudoku_indices)