import unittest
from app.board import Board
from unittest.mock import patch
from parameterized import parameterized

class TestBoard(unittest.TestCase):

    def setUp(self):
        
        self.print_patcher = patch("builtins.print")        # a "device that can silence the print"
        self.mock_print = self.print_patcher.start()        # The patch is activated and the called print() is silenced.
        self.board = Board()                                # recreating Board() for each test

    def test_creating_board(self):

        game_board = self.board.creating_board()
        expected_board = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]] 
        self.assertEqual(game_board,expected_board)       

    def test_board_type(self):
        
        game_board = self.board.creating_board()
        self.assertIsInstance(game_board,list)

        for row in game_board:
            self.assertIsInstance(row,list)

    def test_len_board(self):

        board = self.board.creating_board()

        self.assertEqual(len(board),3)

    def test_empty_board(self):

        board = self.board.creating_board()

        for row in board:
            for cell in row:
                self.assertEqual(cell,"*")

    def test_cell_number(self):

        board = self.board.creating_board()

        for row in board:
            self.assertEqual(len(row),3)

    def test_rows_are_distinct_objects(self): 
        board = self.board.creating_board()

        self.assertIsNot(board[0], board[1])        # asks if these are the same OBJECT in memory; they shouldn't be the same object.
        self.assertIsNot(board[1], board[2]) 
        self.assertIsNot(board[0], board[2])

    def test_display_board(self):
        
        board = self.board.creating_board()
        self.board.display_board(board)

        self.assertEqual(self.mock_print.call_count, 3)
        self.mock_print.assert_any_call(["*", "*", "*"])

    def test_symbol_placement(self):
        
        board = self.board.creating_board()
        self.board.symbol_placement(board,1,1,"X")

        self.assertEqual(board[1][1],"X")   

    def test_horizontal_winner_exists(self):

        board = [
            ["X", "O", "X"],
            ["O", "O", "O"],
            ["*", "*", "*"]
        ]

        result = self.board.winner_check_horizontal(board=board)

        self.assertTrue(result)

    def test_horizontal_winner_not_exists(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["*", "*", "*"]
        ]

        result = self.board.winner_check_horizontal(board=board)

        self.assertFalse(result)

    
    def test_horizontal_winner_all_star(self):

        board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]

        result = self.board.winner_check_horizontal(board=board)

        self.assertFalse(result)

    def test_vertical_winner_exists(self):

        board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["X", "*", "*"]
        ]

        result = self.board.winner_check_vertical(board=board)

        self.assertTrue(result)

    def test_vertical_winner_not_exists(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["*", "O", "*"]
        ]

        result = self.board.winner_check_vertical(board=board)

        self.assertFalse(result)

    def test_vertical_winner_all_star(self):

        board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]

        result = self.board.winner_check_vertical(board=board)

        self.assertFalse(result)

    def test_diognal_winner_exists(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "*", "X"]
        ]

        result = self.board.winner_check_diagonal(board=board)

        self.assertTrue(result)

    def test_diognal_second_winner_exists(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "*", "O"]
        ]

        result = self.board.winner_check_diagonal(board=board)

        self.assertTrue(result)


    def test_no_diognal_winner(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["*", "*", "O"]
        ]

        result = self.board.winner_check_diagonal(board=board)

        self.assertFalse(result)


    def test_tie(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]

        result = self.board.tie_check(board=board)
        
        self.assertTrue(result)

    
    def test_no_tie(self):

        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "*"]
        ]

        result = self.board.tie_check(board=board)
        
        self.assertFalse(result)

    def test_check_winner_returns_false(self):

        board = [["irrelevant"]]

        with patch.object(self.board, "winner_check_horizontal", return_value=False), \
            patch.object(self.board, "winner_check_vertical", return_value=False), \
            patch.object(self.board, "winner_check_diagonal", return_value=False):
        
            self.assertFalse(self.board.check_winner(board))

    def test_check_winner_horizontal_returns_true(self):

        board = [["irrelevant"]]

        with patch.object(self.board, "winner_check_horizontal", return_value=True), \
            patch.object(self.board, "winner_check_vertical", return_value=False), \
            patch.object(self.board, "winner_check_diagonal", return_value=False):
        
            self.assertTrue(self.board.check_winner(board))

    def test_check_winner_vertical_returns_true(self):

        board = [["irrelevant"]]

        with patch.object(self.board, "winner_check_horizontal", return_value=False), \
            patch.object(self.board, "winner_check_vertical", return_value=True), \
            patch.object(self.board, "winner_check_diagonal", return_value=False):
        
            self.assertTrue(self.board.check_winner(board))

    def test_check_winner_diagonal_returns_true(self):

        board = [["irrelevant"]]

        with patch.object(self.board, "winner_check_horizontal", return_value=False), \
            patch.object(self.board, "winner_check_vertical", return_value=False), \
            patch.object(self.board, "winner_check_diagonal", return_value=True):
        
            self.assertTrue(self.board.check_winner(board))


    def tearDown(self):
        self.print_patcher.stop()           # To prevent the mocked print from affecting other tests, 
                                            # we stop the patch and restore the original implementation.
