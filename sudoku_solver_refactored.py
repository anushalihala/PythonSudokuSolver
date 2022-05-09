import math
from sudoku_solver_exceptions import SudokuSolverException


class SudokuContext:
    def __init__(self, sudoku_string, sudoku_size=None):
        if sudoku_size is None:
            self.board_area = len(sudoku_string)
        else:
            self.board_area = sudoku_size

        self.sudoku_string = sudoku_string
        self.board_length = int(math.sqrt(self.board_area))
        self.current_board = dict()       # actual values in Sudoku board
        self.current_domain = dict()      # possible value each cell in Sudoku board can take
        self.neighbours = dict()  # CONSTRAINT; all neighbours must be different

        if len(sudoku_string) != self.board_area:
            raise SudokuSolverException(f"input Sudoku string length not equal to {self.board_area}")
        elif self.board_length**2 != self.board_area:
            raise SudokuSolverException("input Sudoku string length does not form a square")

    def _get_sudoku_indices(self, input_int):
        # converts linear indices [0-80] to 2d indices [r][c] with domain [0-8][0-8] of type string
        row = input_int // self.board_length
        col = input_int % self.board_length
        return str(row) + str(col)

    def _sudoku_string_to_context(self, sudoku_string):
        for i in range(self.board_area):
            sudoku_indices = self._get_sudoku_indices(i)
            cell_value = int(self.sudoku_string[i])
            self.board[sudoku_indices] = cell_value

            if cell_value == 0:
                # initial domain -> if cell empty, can take any value from 1 to 9
                self.domain[sudoku_indices] = set(range(1, 10))
            else:
                # initial domain -> if cell filled, can take only that value
                self.domain[sudoku_indices] = set([cell_value])

            self.neighbours[sudoku_indices] = self.compute_neighbours(sudoku_indices)

    def _get_linear_neighbours(self, const_index, const_row_or_col):
        const_list = [const_index] * self.board_length
        changing_list = range(0, self.board_length)
        changing_list = map(lambda x: str(x), changing_list)
        changing_list = filter(lambda x: x != const_index, changing_list)

        if const_row_or_col == "row":
            neighbours_list = zip(const_list, changing_list)
        elif const_row_or_col == "col":
            neighbours_list = zip(changing_list, const_list)
        else:
            raise SudokuSolverException("second argument of _get_linear_neighbours not one of ['row', 'col']")

        neighbours_list = map(lambda x: "".join(x), neighbours_list)
        neighbours_list = list(neighbours_list)
        return neighbours_list

    def _get_column_neighbours(self, sudoku_indices):
        # get neighbours from same column
        column_index = sudoku_indices[1]
        return self._get_linear_neighbours(column_index, 'col')

    def _get_row_neighbours(self, sudoku_indices):
        # get neighbours from same row
        row_index = sudoku_indices[0]
        return self._get_linear_neighbours(row_index, 'row')

    def _get_box_neighbours(self, sudoku_indices, box_length=3):
        row_index = sudoku_indices[0]
        column_index = sudoku_indices[1]

        number_of_boxes = self.board_length / box_length
        # check if whole number
        if number_of_boxes - int(number_of_boxes) != 0:
            raise SudokuSolverException("self.board_length not divisible by box_length argument value")
        horizontal_box_number = int(column_index) // number_of_boxes
        horizontal_box_number = int(horizontal_box_number)
        vertical_box_number = int(row_index) // number_of_boxes
        vertical_box_number = int(vertical_box_number)

        neighbours_list = []
        for row_index in range(box_length * vertical_box_number, box_length * vertical_box_number + box_length):
            for col_index in range(box_length * horizontal_box_number, box_length * horizontal_box_number + box_length):
                neighbours_list.append(str(row_index)+str(col_index))

        neighbours_list = list(filter(lambda x: x!=sudoku_indices, neighbours_list))
        return neighbours_list

    def _get_neighbours(self, sudoku_indices, box_length=3):
        return self._get_row_neighbours(sudoku_indices) + \
               self._get_column_neighbours(sudoku_indices) + \
               self._get_box_neighbours(sudoku_indices, box_length)


if __name__=="__main__":
    print("hello main refactored!")
    input_test = "010020300004005060070000008006900070000100002030048000500006040000800106008000000"
    # sc = SudokuContext(input_test)

    sc = SudokuContext("0"*81)