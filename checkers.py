class Checkers:
    '''Standard Checkers game where pawns jump over each other
    to claim pieces. Once a pawn reaches the opposite end of
    the board it will be promoted to a king which can move in both
    directions.'''
    def __init__(self) -> None:
        # self.moves = TODO: GENERATE MOVES
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
    