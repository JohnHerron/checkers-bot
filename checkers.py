from game import Game
from board import Board
from pawns import Pawn

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
        self.calculate_all_moves()
        self.winner = None
        self.turn = 'RED'

    def actions(self, node):
        '''Return list of valid moves from node
        Node is a string formatted: "y,x" (y,x) pair representing space on the game board.'''
        return self.moves[node]

    def result(self, node, move):
        '''Return the resulting node after making a move from current node'''
        if move not in self.moves: # don't allow illegal moves
            return node
        
    def terminal_test(self, node):
        '''Returns true if given node has no children (valid moves)'''
        return not self.moves
    
    def calculate_moves(self, row, col, pawn_val):
        '''Returns list of possible locations a piece on a give tile can move to.
        If there is no pawn on tile, returns empty list.
        Move format: [(y,x),(y,x)...]'''
        valid_moves = []
        if not pawn_val:
            return []
        king = False
        if abs(pawn_val) > 1:
            val = pawn_val // 2
            king = True
        else:
            val = pawn_val
        front = row - val
        back = row + val
        left = col - val
        right = col + val
        beyond_front = front - val
        beyond_back = back + val
        beyond_left = left - val
        beyond_right = right + val
        # forwards movement
        if self.index_within_board(front):
            if self.index_within_board(left):
                if self.state[front][left] == 0:
                    valid_moves.append((front, left))
                elif (self.index_within_board(beyond_front) and
                      self.index_within_board(beyond_left) and
                      self.state[front][left] != val and 
                      self.state[front][left] != pawn_val): # check if jump is possible
                    if self.state[beyond_front][beyond_left] == 0:
                        valid_moves.append((beyond_front, beyond_left))
            if self.index_within_board(right):
                if self.state[front][right] == 0:
                    valid_moves.append((front, right))
                elif (self.index_within_board(beyond_front) and
                      self.index_within_board(beyond_right) and
                      self.state[front][right] != val and 
                      self.state[front][right] != pawn_val): # check if jump is possible
                    if self.state[beyond_front][beyond_right] == 0:
                        valid_moves.append((beyond_front, beyond_right))
        # backwards movement
        if self.index_within_board(back) and king:
            if self.index_within_board(left):
                if self.state[back][left] == 0:
                    valid_moves.append((back, left))
                elif (self.index_within_board(beyond_back) and
                      self.index_within_board(beyond_left) and
                      self.state[back][left] != val and 
                      self.state[back][left] != pawn_val): # check if jump is possible
                    if self.state[beyond_back][beyond_left] == 0:
                        valid_moves.append((beyond_back, beyond_left))
            if self.index_within_board(right):
                if self.state[back][right] == 0:
                    valid_moves.append((back, right))
                elif (self.index_within_board(beyond_back) and
                      self.index_within_board(beyond_right) and
                      self.state[back][right] != val and 
                      self.state[back][right] != pawn_val): # check if jump is possible
                    if self.state[beyond_back][beyond_right] == 0:
                        valid_moves.append((beyond_back, beyond_right))

        return valid_moves
    
    def index_within_board(self, x) -> bool:
        return x >= 0 and x < self.board.n_squares

    def calculate_all_moves(self):
        '''Recalculates all possible moves on board for each square on the board'''
        self.moves.clear()
        for row_num, row in enumerate(self.state):
            for col, tile_val in enumerate(row):
                if tile_val:
                    self.moves.update({f'{row_num},{col}': self.calculate_moves(row_num, col, tile_val)})
    
    def toggle_select_pawn(self, pawn):
        '''Only allows one pawn to be selected at a time.
        Highlights outline of selected pawn, also highlights tiles pawn can move to.'''
        # check if pawn is being deselected
        if self.selected_pawn == pawn:
            pawn.toggle_highlight()
            self.toggle_highlight_squares()
            self.selected_pawn = None
        else: # new pawn selected
            if self.selected_pawn: 
                # remove previous highlights
                self.selected_pawn.toggle_highlight()
                self.toggle_highlight_squares()
            # highlight newly selected pawn and squares
            self.selected_pawn = pawn
            self.selected_pawn.toggle_highlight()
            self.toggle_highlight_squares()
            
    def move_pawn(self, pawn, square):
        # remove highlighting from before move is made
        self.toggle_select_pawn(pawn)
        # update state to remove pawn
        self.state[pawn.y][pawn.x] = 0

        # if pawn jumped, remove pawn that got jumped
        if abs(pawn.x - square.x) > 1 and abs(pawn.y - square.y) > 1:
            if square.x - pawn.x > 0: # moved right
                horizontal_movement = 1
            elif square.x - pawn.x < 0: # moved left
                horizontal_movement = -1
            if square.y - pawn.y < 0: # moved up
                vertical_movement = -1
            elif square.y - pawn.y > 0: # moved down
                vertical_movement = 1

            self.board.get_square(pawn.x + horizontal_movement, pawn.y + vertical_movement).get_pawn().kill_pawn()
            self.state[pawn.y + vertical_movement][pawn.x + horizontal_movement] = 0

        # move pawn
        pawn.move_to(square)

        # if pawn has made it to opposite side then promote
        if ((pawn.color == 'red' and pawn.y == 0) or
            (pawn.color == 'darkgreen' and pawn.y == (self.board.n_squares - 1))):
            pawn.promote()
        # update state to place pawn
        if pawn.king:
            self.state[pawn.y][pawn.x] = 2 if pawn.color == 'red' else -2
        else:
            self.state[pawn.y][pawn.x] = 1 if pawn.color == 'red' else -1
        # update moves
        self.calculate_all_moves()
        self.check_win()

    def toggle_highlight_squares(self):
        '''Toggles highlight of squares for currently selected pawn'''
        for square_coords in self.actions(f'{self.selected_pawn.y},{self.selected_pawn.x}'):
            self.board.get_square(square_coords[1], square_coords[0]).toggle_highlight()

    def check_win(self):
        if Pawn._red_count == 0:
            self.winner = 'GREEN'
        if Pawn._green_count == 0:
            self.winner = 'RED'

    def switch_turn(self):
        if self.turn == 'GREEN':
            self.turn = 'RED'
        else:
            self.turn = 'GREEN'

    def handle_click(self, square):
        '''Handles player interactions with board, skips if clicked on the bot player's pawn'''
        pawn = square.get_pawn()
        if pawn and pawn.color == 'red':
            print(f'clicked pawn at {pawn.y}, {pawn.x}')
            self.toggle_select_pawn(pawn)
        elif square.highlighted == True:
            pawn = self.selected_pawn
            self.move_pawn(pawn, square)
            self.switch_turn()
        