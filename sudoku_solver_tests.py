import unittest
from sudoku_solver_refactored import SudokuContext

# def square(n):
#     return n * n
#
# def cube(n):
#     return n * n * n


class TestSudokuContext(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sudoku_boards = [
            "010020300004005060070000008006900070000100002030048000500006040000800106008000000"
        ]
        self.solved_sudoku_boards = [
            "815627394924385761673491528186952473457163982239748615591236847342879156768514239"
        ]
        self.sudoku_context_objects = None  # TODO

    def test_sudoku_size_validation(self):
        sudoku_context_object = SudokuContext(self.sudoku_boards[0])
        self.assertEquals(sudoku_context_object.board_size, len(self.sudoku_boards[0]))
        sudoku_context_object_mini = SudokuContext("1234")
        self.assertEquals(sudoku_context_object_mini.board_size, 4)
        sudoku_context_object_invalid = SudokuContext("1234", 5)
        self.assertEquals(sudoku_context_object_invalid.board_size, 5)

    # def test_sudoku_string_to_context(self):
    #     # generate answers
    #     sudoku_indices = []
    #     for i in range(9):
    #         for j in range(9):
    #             sudoku_indices.append(str(i)+str(j))

        # for index in range(len(sudoku_indices)):
        #     self.assertEqual(SudokuContext(self.sudoku_boards, index), sudoku_indices[index])

