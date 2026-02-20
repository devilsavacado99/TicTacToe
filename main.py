from app.player import Player
from app.board import Board

"""
Main entry point for the Tic Tac Toe game.
"""
def displaying_rules():
    """Prints the rules of the Tic Tac Toe game."""

    print("The rules of the game are as follows: The player with the X symbol always starts first." \
    "Players take turns putting their marks in empty squares. " \
    "The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.")

def main():
    """
    Runs the main control loop for the Tic Tac Toe game.

    This function initializes the game, displays the rules and board,
    and manages the overall game flow. During each game round, it:
    - Prompts the current player to choose a position.
    - Places the player's symbol on the board.
    - Displays the updated board.
    - Checks for a winning or draw condition.
    - Switches turns between players.

    After each completed game, the players are asked whether they want
    to play again. The game continues until the players choose to exit.
    """

    player = Player()
    play_game = True

    while play_game:

        displaying_rules()

        board = Board()
        game_board = board.board

    
        print("Welcome to the Tic Tac Toe game! Here is the board:")
        board.display_board()

        current_player = "X"
        game_on = True

        while game_on:

            position = player.position_selection(game_board)        #position is a tuple
            row = position[0]                                       #tuple unpacking
            column = position[1]                                    #tuple unpacking

            board.symbol_placement(row,column,current_player)

            board.display_board()
        
            if board.check_winner():
            
                game_on = False
                print(f"We have a winner! {current_player} has won!")
                break

            elif board.tie_check():
                
                game_on = False
                print("Opsie! The board is full, the game is a draw!")
                break

            current_player = player.taking_turns(current_player)

        play_game = player.play_again()

if __name__ == "__main__":

    main()


