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
            self.assertEqual(sudoku_context_object.get_sudoku_indices(index), sudoku_indices[index])

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

    def test_initialization(self):
        sc = SudokuContext(self.sudoku_boards[0])

        current_board_answer = {'00': 0, '01': 1, '02': 0, '03': 0, '04': 2, '05': 0, '06': 3, '07': 0, '08': 0, '10': 0, '11': 0, '12': 4, '13': 0, '14': 0, '15': 5, '16': 0, '17': 6, '18': 0, '20': 0, '21': 7, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 8, '30': 0, '31': 0, '32': 6, '33': 9, '34': 0, '35': 0, '36': 0, '37': 7, '38': 0, '40': 0, '41': 0, '42': 0, '43': 1, '44': 0, '45': 0, '46': 0, '47': 0, '48': 2, '50': 0, '51': 3, '52': 0, '53': 0, '54': 4, '55': 8, '56': 0, '57': 0, '58': 0, '60': 5, '61': 0, '62': 0, '63': 0, '64': 0, '65': 6, '66': 0, '67': 4, '68': 0, '70': 0, '71': 0, '72': 0, '73': 8, '74': 0, '75': 0, '76': 1, '77': 0, '78': 6, '80': 0, '81': 0, '82': 8, '83': 0, '84': 0, '85': 0, '86': 0, '87': 0, '88': 0}
        self.assertEqual(sc.current_board, current_board_answer)
        current_domain_answer = {'00': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '01': {1}, '02': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '03': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '04': {2}, '05': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '06': {3},
         '07': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '08': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '10': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '11': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '12': {4}, '13': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '14': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '15': {5}, '16': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '17': {6},
         '18': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '20': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '21': {7},
         '22': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '23': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '24': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '25': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '26': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '27': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '28': {8}, '30': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '31': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '32': {6}, '33': {9},
         '34': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '35': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '36': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '37': {7}, '38': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '40': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '41': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '42': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '43': {1},
         '44': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '45': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '46': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '47': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '48': {2}, '50': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '51': {3},
         '52': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '53': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '54': {4}, '55': {8},
         '56': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '57': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '58': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '60': {5}, '61': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '62': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '63': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '64': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '65': {6},
         '66': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '67': {4}, '68': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '70': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '71': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '72': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '73': {8}, '74': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '75': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '76': {1},
         '77': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '78': {6}, '80': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '81': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '82': {8}, '83': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '84': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '85': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '86': {1, 2, 3, 4, 5, 6, 7, 8, 9},
         '87': {1, 2, 3, 4, 5, 6, 7, 8, 9}, '88': {1, 2, 3, 4, 5, 6, 7, 8, 9}}
        self.assertEqual(sc.current_domain, current_domain_answer)
        current_neighbours_answer = {'00': {'06', '30', '50', '05', '40', '07', '80', '12', '22', '10', '11', '08', '02', '01', '04', '03', '20',
                '60', '70', '21'},
         '01': {'06', '31', '05', '07', '12', '22', '81', '10', '41', '11', '08', '02', '51', '71', '61', '04', '03',
                '20', '01', '00', '21'},
         '02': {'06', '05', '07', '12', '22', '10', '32', '00', '72', '11', '62', '08', '42', '02', '52', '04', '03',
                '20', '01', '82', '21'},
         '03': {'06', '13', '24', '63', '05', '83', '07', '43', '53', '23', '14', '73', '08', '02', '04', '03', '25',
                '15', '01'},
         '04': {'34', '06', '24', '13', '84', '05', '07', '74', '23', '14', '08', '02', '04', '03', '25', '15', '54',
                '01', '64'},
         '05': {'75', '06', '13', '24', '85', '05', '07', '45', '23', '14', '35', '65', '08', '02', '04', '03', '25',
                '15', '01'},
         '06': {'06', '27', '46', '05', '07', '16', '36', '76', '18', '08', '02', '17', '26', '56', '04', '03', '01',
                '86', '28'},
         '07': {'06', '27', '05', '07', '16', '57', '67', '18', '08', '02', '26', '47', '04', '03', '37', '01', '17',
                '87', '28'},
         '08': {'48', '06', '27', '78', '05', '07', '16', '58', '68', '18', '08', '38', '02', '26', '04', '03', '01',
                '17', '28'},
         '10': {'13', '30', '50', '40', '16', '80', '12', '22', '14', '10', '18', '11', '02', '01', '21', '15', '20',
                '70', '17', '00', '60'},
         '11': {'13', '31', '16', '12', '22', '14', '81', '10', '41', '18', '02', '51', '71', '61', '15', '20', '01',
                '17', '00', '21'},
         '12': {'13', '16', '12', '22', '14', '10', '32', '00', '18', '72', '11', '62', '42', '02', '52', '15', '20',
                '01', '17', '82', '21'},
         '13': {'24', '13', '63', '83', '05', '16', '12', '43', '53', '23', '14', '10', '18', '73', '04', '03', '25',
                '15', '17'},
         '14': {'34', '24', '13', '84', '05', '16', '12', '74', '23', '14', '10', '18', '04', '03', '25', '15', '54',
                '17', '64'},
         '15': {'75', '24', '13', '85', '05', '16', '12', '45', '23', '14', '10', '35', '18', '65', '04', '25', '03',
                '15', '17'},
         '16': {'06', '13', '27', '46', '07', '16', '36', '12', '76', '14', '10', '18', '08', '17', '26', '56', '15',
                '86', '28'},
         '17': {'06', '13', '27', '07', '16', '12', '14', '57', '67', '10', '18', '08', '26', '47', '15', '37', '17',
                '87', '28'},
         '18': {'48', '06', '13', '27', '78', '07', '16', '12', '58', '14', '68', '10', '18', '08', '38', '26', '15',
                '17', '28'},
         '20': {'24', '27', '30', '50', '40', '80', '12', '22', '23', '10', '11', '02', '70', '28', '26', '21', '25',
                '20', '01', '00', '60'},
         '21': {'24', '27', '31', '12', '22', '23', '81', '10', '41', '11', '02', '51', '28', '26', '71', '61', '25',
                '20', '01', '00', '21'},
         '22': {'24', '27', '12', '23', '10', '32', '72', '11', '62', '42', '02', '52', '82', '28', '26', '25', '20',
                '01', '00', '21'},
         '23': {'24', '13', '27', '63', '83', '05', '43', '53', '23', '14', '73', '26', '04', '25', '03', '15', '20',
                '28', '21'},
         '24': {'34', '24', '13', '27', '84', '05', '74', '23', '14', '26', '04', '25', '03', '15', '20', '54', '28',
                '21', '64'},
         '25': {'75', '24', '13', '27', '85', '05', '23', '45', '14', '35', '65', '26', '04', '25', '03', '15', '20',
                '28', '21'},
         '26': {'24', '06', '27', '46', '07', '16', '36', '23', '76', '18', '08', '17', '26', '56', '25', '20', '86',
                '28', '21'},
         '27': {'24', '06', '27', '16', '07', '23', '57', '67', '18', '08', '26', '47', '25', '37', '20', '17', '87',
                '28', '21'},
         '28': {'48', '24', '06', '27', '78', '16', '07', '23', '58', '68', '18', '08', '38', '26', '25', '20', '17',
                '28', '21'},
         '30': {'34', '31', '30', '50', '40', '36', '80', '10', '32', '41', '35', '38', '42', '52', '51', '37', '20',
                '70', '60'},
         '31': {'34', '31', '30', '50', '40', '36', '81', '32', '41', '35', '38', '42', '52', '51', '71', '61', '37',
                '01', '21'},
         '32': {'34', '31', '30', '50', '40', '36', '12', '32', '41', '35', '72', '62', '38', '42', '02', '52', '51',
                '37', '82'},
         '33': {'44', '34', '13', '55', '31', '30', '63', '83', '36', '43', '53', '23', '45', '32', '35', '73', '38',
                '03', '37', '54'},
         '34': {'44', '34', '24', '55', '31', '30', '84', '33', '36', '43', '53', '74', '45', '14', '32', '35', '38',
                '04', '37', '54', '64'},
         '35': {'75', '44', '34', '55', '31', '30', '85', '05', '33', '36', '43', '53', '45', '32', '35', '65', '38',
                '25', '37', '15', '54'},
         '36': {'48', '34', '06', '31', '30', '46', '16', '36', '58', '76', '57', '32', '35', '38', '26', '47', '56',
                '37', '86'},
         '37': {'48', '34', '27', '31', '30', '46', '07', '36', '58', '57', '67', '32', '35', '38', '47', '56', '37',
                '17', '87'},
         '38': {'48', '34', '31', '30', '78', '46', '36', '58', '68', '57', '32', '35', '18', '38', '08', '47', '56',
                '37', '28'},
         '40': {'48', '31', '30', '50', '46', '40', '80', '43', '45', '10', '32', '41', '42', '52', '51', '47', '20',
                '70', '60'},
         '41': {'48', '31', '30', '50', '46', '40', '43', '45', '81', '32', '41', '42', '52', '51', '71', '47', '61',
                '01', '21'},
         '42': {'48', '31', '30', '50', '46', '40', '12', '43', '45', '32', '41', '72', '62', '42', '02', '52', '51',
                '47', '82'},
         '43': {'48', '44', '34', '13', '55', '63', '46', '83', '40', '33', '43', '53', '45', '23', '41', '35', '73',
                '42', '47', '03', '54'},
         '44': {'48', '34', '24', '55', '84', '46', '40', '33', '43', '53', '74', '45', '14', '41', '35', '42', '47',
                '04', '54', '64'},
         '45': {'48', '75', '44', '34', '55', '46', '85', '05', '40', '33', '43', '53', '45', '41', '35', '65', '42',
                '47', '25', '15', '54'},
         '46': {'48', '06', '46', '40', '16', '36', '43', '45', '58', '76', '57', '41', '42', '38', '26', '47', '56',
                '37', '86'},
         '47': {'48', '27', '46', '40', '07', '36', '43', '45', '58', '57', '67', '41', '42', '38', '47', '56', '37',
                '17', '87'},
         '48': {'48', '46', '78', '40', '36', '43', '45', '58', '68', '57', '41', '18', '42', '08', '38', '47', '56',
                '37', '28'},
         '50': {'31', '30', '50', '40', '80', '53', '58', '57', '10', '32', '41', '42', '52', '51', '56', '54', '20',
                '70', '60'},
         '51': {'31', '30', '50', '40', '53', '58', '57', '81', '32', '41', '42', '52', '51', '71', '61', '56', '54',
                '01', '21'},
         '52': {'31', '30', '50', '40', '12', '53', '58', '57', '32', '41', '72', '62', '42', '02', '52', '51', '56',
                '54', '82'},
         '53': {'44', '34', '13', '55', '63', '50', '83', '33', '43', '53', '58', '23', '45', '57', '35', '73', '52',
                '51', '56', '03', '54'},
         '54': {'44', '34', '24', '55', '84', '50', '33', '43', '53', '74', '58', '45', '14', '57', '35', '52', '51',
                '56', '04', '54', '64'},
         '55': {'75', '44', '34', '50', '85', '05', '33', '43', '53', '58', '45', '57', '35', '65', '52', '51', '56',
                '25', '15', '54'},
         '56': {'48', '06', '50', '46', '16', '36', '53', '58', '76', '57', '38', '52', '51', '26', '47', '56', '37',
                '54', '86'},
         '57': {'48', '27', '50', '46', '07', '36', '53', '58', '57', '67', '38', '52', '51', '47', '56', '37', '54',
                '17', '87'},
         '58': {'48', '50', '78', '46', '36', '53', '58', '68', '57', '18', '08', '38', '52', '51', '47', '56', '37',
                '54', '28'},
         '60': {'63', '30', '50', '40', '80', '68', '67', '10', '81', '72', '65', '62', '71', '61', '20', '70', '82',
                '60', '64'},
         '61': {'63', '31', '80', '68', '67', '81', '41', '72', '65', '62', '01', '51', '71', '61', '60', '70', '82',
                '21', '64'},
         '62': {'63', '80', '12', '68', '67', '81', '32', '72', '65', '62', '42', '02', '52', '71', '61', '70', '82',
                '60', '64'},
         '63': {'75', '13', '63', '84', '85', '83', '43', '53', '74', '23', '68', '67', '65', '73', '62', '61', '03',
                '60', '64'},
         '64': {'75', '34', '24', '63', '84', '85', '83', '74', '14', '68', '67', '65', '73', '62', '61', '04', '54',
                '60', '64'},
         '65': {'75', '63', '84', '85', '05', '83', '74', '45', '68', '67', '35', '65', '73', '62', '61', '25', '15',
                '60', '64'},
         '66': {'06', '63', '46', '78', '77', '16', '36', '88', '76', '68', '67', '65', '62', '26', '61', '56', '86',
                '87', '60', '64'},
         '67': {'27', '63', '78', '77', '07', '88', '76', '68', '57', '67', '65', '62', '86', '47', '61', '37', '17',
                '87', '60', '64', '66'},
         '68': {'48', '63', '78', '77', '88', '58', '76', '68', '67', '18', '65', '62', '08', '38', '61', '86', '87',
                '28', '60', '64', '66'},
         '70': {'75', '30', '50', '78', '40', '80', '74', '76', '81', '10', '72', '73', '62', '71', '61', '20', '70',
                '82', '60'},
         '71': {'75', '31', '78', '80', '74', '76', '81', '41', '72', '73', '62', '70', '51', '21', '71', '61', '01',
                '82', '60'},
         '72': {'75', '78', '80', '12', '74', '76', '81', '32', '72', '73', '62', '42', '02', '52', '71', '61', '70',
                '82', '60'},
         '73': {'75', '13', '63', '84', '78', '85', '83', '43', '53', '74', '23', '76', '72', '65', '73', '71', '03',
                '70', '64'},
         '74': {'75', '34', '24', '63', '84', '78', '85', '83', '74', '76', '14', '72', '65', '73', '71', '04', '54',
                '70', '64'},
         '75': {'75', '63', '84', '78', '85', '05', '83', '74', '45', '76', '35', '72', '65', '73', '71', '25', '15',
                '70', '64'},
         '76': {'75', '06', '78', '46', '77', '16', '36', '88', '74', '76', '68', '67', '72', '73', '26', '71', '56',
                '70', '86', '87', '66'},
         '77': {'75', '27', '78', '07', '88', '74', '76', '68', '57', '67', '72', '73', '17', '71', '47', '37', '70',
                '86', '87', '66'},
         '78': {'48', '75', '78', '77', '88', '74', '58', '76', '68', '67', '18', '72', '73', '08', '38', '71', '70',
                '86', '87', '28', '66'},
         '80': {'30', '84', '50', '85', '83', '40', '80', '81', '10', '72', '62', '71', '61', '20', '70', '86', '87',
                '82', '60'},
         '81': {'31', '84', '85', '83', '80', '81', '41', '72', '62', '01', '51', '21', '71', '61', '70', '86', '87',
                '82', '60'},
         '82': {'84', '85', '83', '80', '12', '81', '32', '72', '62', '42', '02', '52', '71', '61', '70', '86', '87',
                '82', '60'},
         '83': {'75', '13', '63', '84', '85', '83', '80', '43', '53', '74', '23', '81', '65', '73', '03', '86', '87',
                '82', '64'},
         '84': {'75', '34', '24', '63', '84', '85', '83', '80', '74', '14', '81', '65', '73', '04', '54', '86', '87',
                '82', '64'},
         '85': {'75', '63', '84', '85', '83', '05', '80', '74', '45', '81', '35', '65', '73', '25', '15', '86', '87',
                '82', '64'},
         '86': {'06', '84', '85', '46', '78', '77', '83', '16', '36', '80', '88', '76', '68', '81', '67', '26', '56',
                '86', '87', '82', '66'},
         '87': {'27', '84', '85', '78', '77', '83', '07', '80', '88', '76', '68', '57', '81', '67', '17', '47', '37',
                '86', '87', '82', '66'},
         '88': {'48', '84', '85', '78', '77', '83', '80', '58', '76', '68', '81', '67', '18', '08', '38', '82', '86',
                '87', '28', '66'}}
        self.assertEqual(sc.neighbours, current_neighbours_answer)


class TestSudokuCSP(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sudoku_boards = [
            "010020300004005060070000008006900070000100002030048000500006040000800106008000000"
        ]
        self.solved_sudoku_boards = [
            "815627394924385761673491528186952473457163982239748615591236847342879156768514239"
        ]

    def test_get_binary_constraints(self):
        # TODO
        pass