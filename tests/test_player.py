import unittest
from app.player import Player
from unittest.mock import patch
from parameterized import parameterized


class TestPlayer(unittest.TestCase):

    def setUp(self):
        
        self.print_patcher = patch("builtins.print")        # a "device that can silence the print"
        self.mock_print = self.print_patcher.start()        # The patch is activated and the called print() is silenced.
        self.player = Player()                              # recreating Player() for each test


    @parameterized.expand([
        ("pos_0_0", ["0", "0"], (0, 0)),
        ("pos_0_1", ["0", "1"], (0, 1)),
        ("pos_0_2", ["0", "2"], (0, 2)),
        ("pos_1_0", ["1", "0"], (1, 0)),
        ("pos_1_1", ["1", "1"], (1, 1)),
        ("pos_1_2", ["1", "2"], (1, 2)),
        ("pos_2_0", ["2", "0"], (2, 0)),
        ("pos_2_1", ["2", "1"], (2, 1)),
        ("pos_2_2", ["2", "2"], (2, 2))
    ])
    @patch("builtins.input")  
    def test_position_correct(self,name, side_effect_values,  expected_result, mock_input):
        
        mock_input.side_effect = side_effect_values

        board = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]
        
        result = self.player.position_selection(board=board)
        self.assertEqual(result,expected_result, msg=(
        f"Position selection failed for input {side_effect_values}. "
        f"Expected {expected_result}, but got {result}."
        )) 

    @parameterized.expand([
        ("pos_str", ["a","2","1"],(2,1)),
        ("pos_special_char", ["!","2","2"],(2,2)),
        ("pos_float", ["1.1","2","1"],(2,1)),
        ("pos_empty", ["", "2", "0"], (2, 0)),
        ("pos_space", [" ", "1", "2"], (1, 2)),
        ("pos_none", ["None", "2", "1"], (2, 1)),
    ])
    @patch("builtins.input")
    def test_position_not_number(self,name,side_effect_values, expected_result, mock_input):

        mock_input.side_effect = side_effect_values     #if an incorrect input is entered, two more inputs are requested

        board = [
            ["X", "O", "X"],
            ["O", "X", "*"],
            ["*", "*", "*"]
        ]

        result = self.player.position_selection(board=board)

        self.assertEqual(result,expected_result,msg=(
        f"Position selection failed for input {side_effect_values}. "
        f"Expected {expected_result}, but got {result}."
        )) 

        self.mock_print.assert_any_call("Please enter valid numbers for row and column.")

    @parameterized.expand([
        ("row_out_of_range", ["1","5","2","1"],(2,1)),
        ("col_out_of_range", ["7","2","2","2"],(2,2)),
        ("both_out_of_range", ["9","4","1","2"],(1,2)),
        ("negative_index", ["-2", "2", "2","1"], (2, 1)),
    ])
    @patch("builtins.input")
    def test_position_not_in_range(self,name, side_effect_values, expected_result, mock_input):

        mock_input.side_effect = side_effect_values     #if an incorrect input is entered, two more inputs are requested
        
        board = [
            ["X", "O", "X"],
            ["O", "X", "*"],
            ["*", "*", "*"]
        ]

        result = self.player.position_selection(board=board)
        self.assertEqual(result,expected_result,msg=(
        f"Position selection failed for input {side_effect_values}. "
        f"Expected {expected_result}, but got {result}."
        )) 

        self.mock_print.assert_any_call("Row and column must be between 0 and 2.")
        

    @parameterized.expand([
    ("cell_occupied_center",["1", "1", "2", "1"],(2, 1)),
    ("cell_occupied_top_left",["0", "0", "2", "0"],(2, 0)),
    ("cell_occupied_top_middle",["0", "1", "2", "1"],(2, 1)),
    ("cell_occupied_bottom_right",["2", "2", "2", "0"],(2, 0)),
    ])
    @patch("builtins.input")
    def test_position_not_empty(self,name, side_effect_values, expected_result, mock_input):

        mock_input.side_effect = side_effect_values     #if an incorrect input is entered, two more inputs are requested
        board = [
            ["X", "O", "X"],
            ["O", "X", "*"],
            ["*", "*", "O"]
        ]

        result = self.player.position_selection(board=board)
        self.assertEqual(result,expected_result,msg=(
        f"Position selection failed for input {side_effect_values}. "
        f"Expected {expected_result}, but got {result}."
        ))

        self.mock_print.assert_any_call("This cell is already occupied. Choose another one.")
        
    
    @parameterized.expand([
    ("player_x","X","O"),
    ("player_o","O","X"),
    ])
    def test_taking_turns(self,name,current_symbol, expected_next_symbol):

        self.assertEqual(self.player.taking_turns(current_symbol),expected_next_symbol,msg=(
        f"Turn switching failed for current symbol '{current_symbol}'. "
        f"Expected '{expected_next_symbol}'."
        ))

    @patch("builtins.input")
    def test_play_again(self,mock_input):

        mock_input.return_value = "y"

        result = self.player.play_again()

        self.assertTrue(result, msg="play_again should return True when user inputs 'y'.")

    
    @patch("builtins.input")
    def test_no_play_again(self,mock_input):

        mock_input.return_value = "n"

        result = self.player.play_again()

        self.assertFalse(result, msg="play_again should return False when user inputs 'n'.")

    @parameterized.expand([
    ("yes_space", [" Y ","y"], True),
    ("no_space", [" n ","n"], False),
    ("invalid_word_then_y_or_n", ["yes","y"], True),
    ("invalid_special", ["?","y"], True),
    ("invalid_space", [" ","n"], False),
    ("invalid_number", ["1","y"], True),
    ("invalid_float", ["2.1","n"], False),
])
    @patch("builtins.input")
    def test_play_again_wrong_input(self, name, side_effect_values, expected_result, mock_input):

        mock_input.side_effect = side_effect_values       # if an incorrect input is entered, another valid input are requested 

        result = self.player.play_again()

        self.assertEqual(result,expected_result,     msg=(
        f"play_again() returned unexpected result."
        f"Input sequence : {side_effect_values}"
        f"Expected return: {expected_result}"
        f"Actual return  : {result}"))

        self.mock_print.assert_any_call("Invalid input. Please enter Y or N.")

    def tearDown(self):
        self.print_patcher.stop()                       # To prevent the mocked print from affecting other tests, 
                                                        # we stop the patch and restore the original implementation.
