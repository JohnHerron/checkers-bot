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
        self.selected_pawn = None
        self.state = [[0] * n_squares for _ in range(n_squares)] # nxn 2d array filled with 0's
        for row in self.board.pawns:
            for pawn in row:
                self.state[pawn.y][pawn.x] = 1 if pawn.color == 'red' else -1
        self.moves = {} # dict of possible moves on board
        for row_num, row in enumerate(self.state):
            for col, tile_val in enumerate(row):
                if tile_val:
                    self.moves.update({f'{row_num},{col}': self.calculate_moves(row_num, col, tile_val)})
        print(self.moves)
                    

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
    
    def calculate_moves(self, row, col, val, jumped = False):
        '''Returns list of possible locations a piece on a give tile can move to.
        If there is no pawn on tile, returns empty list.
        Move format: [(y,x),(y,x)...]'''
        valid_moves = []
        if not val:
            return []
        front = row - val
        left = col - val
        right = col + val
        # must check if diagonals are within bounds of board
        if front >= 0 and front < self.board.n_squares:
            if left >= 0 and left < self.board.n_squares:
                if self.state[front][left] == 0:
                    valid_moves.append((front, left))
                elif self.state[front][left] != val:
                    valid_moves.append(self.calculate_moves(front, left, val, True))
            if right >= 0 and right < self.board.n_squares:
                if self.state[front][right] == 0:
                    valid_moves.append((front, right))
                elif self.state[front][right] != val:
                    valid_moves.append(self.calculate_moves(front, right, val, True))

        return valid_moves
    
    def select_pawn(self, pawn):
        '''Only allows one pawn to be selected at a time'''
        # check if pawn is being deselected
        if self.selected_pawn == pawn:
            self.selected_pawn.toggle_highlight()
            self.selected_pawn = None
        else:
            if self.selected_pawn: # remove highlight from previously selected pawn
                self.selected_pawn.toggle_highlight()
            self.selected_pawn = pawn
            self.selected_pawn.toggle_highlight()