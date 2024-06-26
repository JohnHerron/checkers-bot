# checkers-bot
Checkers game with AI opponent and move hints.

-TO RUN: run `main.py` file with pygame installed

https://github.com/JohnHerron/checkers-bot/assets/50757583/d5611599-7991-4c67-8682-795ad875a173

Components of the Code:

-`main.py` contains the game loop and event catching.

-`game.py` contains the game's container class that handles the interaction between the game loop and the board game.

-`checkers.py` dictates the game and its rules. All game logic takes place here.

-`board.py` generates a pygame surface with a board of NxN squares.

-`square.py` represents each square on a board, each containing information about the pawn it is associated with.

-`pawn.py` generator class for interacting with the pawns physically on the game board, stores information about itself like its color and whether it is a king. Also draws itself to its associated square.

-`minimax.py` contains the minimax algorithm, specialized for use in the checkers game.
