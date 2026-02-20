PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_SYMBOL = "*"

class Player():
    """
    Represents a player in the Tic Tac Toe game.

    Handles user interactions such as selecting a board position,
    switching turns between players, and deciding whether to play again.
    """
    def position_selection(self, board:list):
        """
        Prompts the user to select a position (1 to 9) on the board to place their symbol.

        Args:
            board (list): A list representing the current game board.

        Returns:
            tuple[int, int]: A tuple containing the selected row and column indices.
        """
        
        while True:
            try:
                row = int(input("Which row (0-2) do you want to put your symbol on?: "))
                col = int(input("Which column (0-2) do you want to put your symbol on?: "))

                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == EMPTY_SYMBOL:
                        return row, col
                
                    else:
                        print("This cell is already occupied. Choose another one.")
                else:
                    print("Row and column must be between 0 and 2.")

            except ValueError:
                print("Please enter valid numbers for row and column.")


    def taking_turns(self, players_symbol:str):
        """
        Switches the turn between players.

        Args:
            players_symbol (str): The player's symbol, either 'X' or 'O'.

        Returns:
            str: The symbol of the next player ('X' or 'O').
        """

        if players_symbol == PLAYER_X:
            players_symbol = PLAYER_O

        else:
            players_symbol = PLAYER_O
        return players_symbol
    
    

    def play_again(self):
        """
        Asks the user whether they want to play again.

        Returns:
            bool: True if the user chooses to play again ('Y'), 
            False if they choose to exit ('N').
        """ 

        while True:

            user_answer = input("Do you want to play the game again? If yes then type Y or if no then type N: ")

            if user_answer.upper() == "Y":
                return True

            elif user_answer.upper() == "N": 
                return False
            
            else:
                print("Invalid input. Please enter Y or N.")

