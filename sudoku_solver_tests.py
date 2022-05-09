import unittest

from sudoku_solver_refactored import SudokuContext
import sudoku_solver_exceptions


class TestSudokuContext(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sudoku_boards = [
            "010020300004005060070000008006900070000100002030048000500006040000800106008000000"
        ]
        self.solved_sudoku_boards = [
            "815627394924385761673491528186952473457163982239748615591236847342879156768514239"
        ]

    def test_sudoku_size_validation(self):
        sudoku_context_object = SudokuContext(self.sudoku_boards[0])
        self.assertEquals(sudoku_context_object.board_size, len(self.sudoku_boards[0]))
        sudoku_context_object_mini = SudokuContext("1234")
        self.assertEquals(sudoku_context_object_mini.board_size, 4)

        self.assertRaises(sudoku_solver_exceptions.SudokuSolverException, SudokuContext, "1234", 5)

    def test_sudoku_string_to_context(self):
        sudoku_context_object = SudokuContext(self.sudoku_boards[0])
        # generate answers
        sudoku_indices = []
        for i in range(9):
            for j in range(9):
                sudoku_indices.append(str(i)+str(j))

        for index in range(len(sudoku_indices)):
            self.assertEqual(sudoku_context_object._get_sudoku_indices(index), sudoku_indices[index])

