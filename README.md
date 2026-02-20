# Tic Tac Toe Game

## Description
This project is a command-line implementation of the classic Tic Tac Toe game written in Python.  
The game is designed using an object-oriented approach and includes both unit tests and integration tests to ensure correctness.

Players take turns entering their moves via the terminal. The game detects win and draw conditions and allows players to start a new game after one finishes.


## Project Structure
```
├── main.py               # Main game loop and control flow
├── player.py             # Player-related logic (input handling, turn switching)
├── board.py              # Game board creation and win/tie logic
├── test_board.py         # Unit tests for the Board class
├── test_player.py        # Unit tests for the Player class
├── test_integration.py   # Integration tests for full game scenarios
├── README.md
└── requirements.txt
```


## How to Run the Game
Make sure you have Python 3 installed.

From the project directory, run:
```bash
python main.py
```

The game will start in the terminal and prompt players for input.


## How to Run the Tests
All tests are written using Python’s built-in `unittest` framework.

To run all tests, execute:
```bash
python -m unittest
```

This will run:
- Unit tests for the `Board` class
- Unit tests for the `Player` class
- Integration tests simulating full game scenarios


## Game Rules
- The player using the **X** symbol always starts first.
- Players take turns selecting a row and column (values between 0 and 2).
- A player wins by placing three of their symbols in a row, column, or diagonal.
- If the board is full and no player has won, the game ends in a draw.
- After each game, players are asked whether they want to play again.


## Requirements
This project uses only Python’s standard library.

- Python 3.11.2 or later

No external dependencies are required.
# TicTacToe
This project is a command-line implementation of the classic Tic Tac Toe game written in Python.
