import unittest
from main import main
from unittest.mock import patch,call
from parameterized import parameterized


class TestIntegration(unittest.TestCase):
    """Integration tests covering full Tic Tac Toe game flows."""

    def setUp(self):
        
        self.print_patcher = patch("builtins.print")        # a "device that can silence the print"
        self.mock_print = self.print_patcher.start()        # The patch is activated and the called print() is silenced.

    @parameterized.expand([
    ("x_wins",
        [
            "0", "0",       # X
            "2", "2",       # O
            "0", "1",       # X
            "2", "1",       # O
            "0", "2",       # X
            "N"             # play again? - No
        ],
        ["We have a winner! X has won!"],
    ),
    ("o_wins",
        [
            "0", "0",       # X
            "2", "2",       # O
            "1", "0",       # X
            "2", "1",       # O
            "0", "2",       # X
            "2", "0",       # O
            "N"             # play again? - No
        ],
        ["We have a winner! O has won!"],
    ),
    ("there_is_a_tie",
        [
            "0", "0",       # X
            "0", "1",       # O
            "0", "2",       # X
            "1", "1",       # O
            "1", "0",       # X
            "1", "2",       # O
            "2", "1",       # X
            "2", "0",       # O
            "2", "2",       # X
            "N"             # play again? - No
        ],
        ["Opsie! The board is full, the game is a draw!"],
    ),
    ("position_input_str",
        [
            "b",            # must be int
            "0", "0",       # X
            "2", "2",       # O
            "1", "0",       # X
            "2", "1",       # O
            "0", "2",       # X
            "2", "0",       # O
            "N"             # play again? - No
        ],
        [
            "Please enter valid numbers for row and column.",
            "We have a winner! O has won!",
        ],
    ),
    ("position_input_out_of_range",
        [
            "4", "1",       # must be in range
            "0", "0",       # X
            "2", "2",       # O
            "1", "0",       # X
            "2", "1",       # O
            "0", "2",       # X
            "2", "0",       # O
            "N"             # play again? - No
        ],
        [
            "Row and column must be between 0 and 2.",
            "We have a winner! O has won!",
        ],
    ),
    ("position_input_already_occupied",
        [
            "0", "0",       # X
            "2", "2",       # O
            "0", "0",       # X is already placed there
            "1", "0",       # X
            "2", "1",       # O
            "0", "2",       # X
            "2", "0",       # O
            "N"             # play again? - No
        ],
        [
            "This cell is already occupied. Choose another one.",
            "We have a winner! O has won!",
        ],
    ),
    ("playing_again",
        [
            "0", "0",       # X
            "2", "2",       # O
            "0", "1",       # X
            "2", "1",       # O
            "0", "2",       # X wins
            "y",            # play again? - Y

            "0", "0",       # X
            "2", "2",       # O
            "1", "0",       # X
            "2", "1",       # O
            "0", "2",       # X
            "2", "0",       # O wins
            "N"
        ],
        [
            "We have a winner! X has won!",
            "We have a winner! O has won!",
        ],
    ),
])
    @patch("builtins.input")
    def test_main_flow(self, name, side_effect_values, expected_messages,mock_input):
        
        mock_input.side_effect = side_effect_values

        main()  

        for message in expected_messages:
            self.mock_print.assert_any_call(message)            # BURAYA MSG nasıl eklenir
    
            

    def tearDown(self):
        self.print_patcher.stop()           # To prevent the mocked print from affecting other tests, 
                                            # we stop the patch and restore the original implementation.
