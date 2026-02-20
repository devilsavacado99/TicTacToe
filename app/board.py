EMPTY_SYMBOL = "*"
BOARD_SIZE = 3

class Board():
    """
    Manages the Tic Tac Toe game board and game state logic.

    Responsible for creating and displaying the board, placing symbols,
    and checking win or tie conditions during the game.
    """

    def __init__(self):
        self.board = self.creating_board()
    
    def creating_board(self):
        """Creates the Tic Tac Toe board.

        Returns:
            list: Newly created game board.
        """

        game_board = []

        for _ in range(BOARD_SIZE):
            row = []
        
            for __ in range(BOARD_SIZE):
                row.append(EMPTY_SYMBOL)
        
            game_board.append(row)

        return game_board
    
    def display_board(self):
        """Prints the current state of the Tic Tac Toe board.
        """

        for row in self.board:
            print(row)


    def symbol_placement(self,row:int,column:int,symbol:str):
        """Places the player's symbol on selected position of game board.

        Args:
            row (int): The row (0 to 2) where the symbol will be placed.
            column (int): The column (0 to 2) where the symbol will be placed.
            symbol (str): The player's symbol ('X' or 'O').

        """
        self.board[row][column] = symbol


    def winner_check_horizontal(self):
        """
        Checks if there is a winner horizontally on the game board.

        Returns:
            bool: True if a winner is found, False otherwise.
        """
        for row in self.board:
            if row[0] != EMPTY_SYMBOL and row.count(row[0]) == len(row):
    
                return True
        return False


    def winner_check_vertical(self):
        """
        Checks if there is a winner vertically on the game board.

        Returns:
            bool: True if a winner is found, False otherwise.
        """
        for col in zip(*self.board):
            if col[0] != EMPTY_SYMBOL and col.count(col[0]) == len(col):
    
                return True
        return False


    def winner_check_diagonal(self):
        """
        Checks if there is a winner diagonally on the game board.

        Returns:
            bool: True if a winner is found, False otherwise.
        """

        diag_one = []
        diag_two = []

        for i in range(len(self.board)):
            diag_one.append(self.board[i][i])

        for i in range(len(self.board)):
            diag_two.append(self.board[i][len(self.board) - i - 1])
    
        if diag_one[0] != EMPTY_SYMBOL and diag_one.count(diag_one[0]) == len(diag_one):
    
            return True

        elif diag_two[0] != EMPTY_SYMBOL and diag_two.count(diag_two[0]) == len(diag_two):
           
            return True   

        return False

    def tie_check(self):
        """
        Checks if the game has ended in a draw.

        Returns:
            bool: True if the board is full and no winner is found, False otherwise.
        """
        for row in self.board:
            if EMPTY_SYMBOL in row:   
                return False
            
        return True
    
    def check_winner(self):
        """
        Checks whether there is a winner on the game board.

        This method evaluates the board by checking horizontal,
        vertical, and diagonal winning conditions. If any of these
        checks return True, the method returns True.

        Returns:
            bool: True if a winning condition is met, otherwise False.
        """

        winner = (
        self.winner_check_horizontal() or 
        self.winner_check_vertical() or 
        self.winner_check_diagonal()
        )

        return winner