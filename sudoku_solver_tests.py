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
        self.assertEquals(sudoku_context_object.board_area, len(self.sudoku_boards[0]))
        sudoku_context_object_mini = SudokuContext("1234", 2)
        self.assertEquals(sudoku_context_object_mini.board_area, 4)

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

    def test_get_neighbours_4(self):
        input_sudoku_string = "0"*16
        sc = SudokuContext(input_sudoku_string, 2)

        # test _get_column_neighbours
        self.assertEqual(sc._get_column_neighbours("00"), ["10", "20", "30"])
        self.assertEqual(sc._get_column_neighbours("33"), ["03", "13", "23"])

        # test _get_row_neighbours
        self.assertEqual(sc._get_row_neighbours("00"), ["01", "02", "03"])
        self.assertEqual(sc._get_row_neighbours("33"), ["30", "31", "32"])

        # test _get_box_neighbours
        self.assertEqual(sc._get_box_neighbours("00"), ['01', '10', '11'])
        self.assertEqual(sc._get_box_neighbours("33"), ['22', '23', '32'])

        # test _get_neighbours
        self.assertEqual(sc._get_neighbours("00"), set(["01", "02", "03"] + ["10", "20", "30"] + ['01', '10', '11']))

    def test_get_neighbours_81(self):
        input_sudoku_string = "0"*81
        sc = SudokuContext(input_sudoku_string)

        # test _get_column_neighbours
        self.assertEqual(sc._get_column_neighbours("00"), ["10", "20", "30", "40", "50", "60", "70", '80'])
        self.assertEqual(sc._get_column_neighbours("44"), ["04", "14", "24", "34", "54", "64", "74", '84'])
        self.assertEqual(sc._get_column_neighbours("88"), ["08", "18", "28", "38", "48", "58", "68", "78"])

        # test _get_row_neighbours
        self.assertEqual(sc._get_row_neighbours("00"), ["01", "02", "03", "04", "05", "06", "07", "08"])
        self.assertEqual(sc._get_row_neighbours("44"), ["40", "41", "42", "43", "45", "46", "47", "48"])
        self.assertEqual(sc._get_row_neighbours("88"), ["80", "81", "82", "83", "84", "85", "86", "87"])

        # test _get_box_neighbours
        self.assertEqual(sc._get_box_neighbours("00"), ['01', '02', '10', '11', '12', '20', '21', '22'])
        self.assertEqual(sc._get_box_neighbours("44"), ['33', '34', '35', '43', '45', '53', '54', '55'])
        self.assertEqual(sc._get_box_neighbours("88"), ['66', '67', '68', '76', '77', '78', '86', '87'])
        self.assertEqual(sc._get_box_neighbours("07"), ['06', '08', '16', '17', '18', '26', '27', '28'])
        self.assertEqual(sc._get_box_neighbours("70"), ['60', '61', '62', '71', '72', '80', '81', '82'])

        # test _get_neighbours
        self.assertEqual(sc._get_neighbours("00"), set(["01", "02", "03", "04", "05", "06", "07", "08"] + ["10", "20", "30", "40", "50", "60", "70", '80'] + ['01', '02', '10', '11', '12', '20', '21', '22']))