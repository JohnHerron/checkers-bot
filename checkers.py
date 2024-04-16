from game import Game
from board import Board

class Checkers(Game):
    '''Standard Checkers game where pawns jump over each other
    to claim pieces. Once a pawn reaches the opposite end of
    the board it will be promoted to a king which can move in both
    directions.
    Intances of this class represent nodes in a state space tree.'''
    def __init__(self, screen, n_squares) -> None:
        self.board = Board(screen, n_squares)
        self.state = [[0] * n_squares for _ in range(n_squares)] # nxn 2d array filled with 0's
        print(self.state)
        for row in self.board.pawns:
            for pawn in row:
                self.state[pawn.y][pawn.x] = -1 if pawn.color == 'darkgreen' else 1
        print(self.state)
        self.moves = []
        for pawn in self.board.pawns:
            # surrounding spaces
            pass

    def actions(self, node):
        '''Return list of valid moves from node'''
        return self.moves

    def result(self, node, move):
        '''Return the resulting node after making a move from current node'''
        if move not in self.moves: # don't allow illegal moves
            return node
        

    def terminal_test(self, node):
        '''Returns true if given node has no children (valid moves)'''
        return not self.moves
    