import pygame as pg
from pawns import Pawn
from square import Square

class Board:
    '''Board class represents an nxn game board used for display'''
    def __init__(self, window_surface, n_squares) -> None:
        self.window_surface = window_surface
        self.window_dims = window_surface.get_size()
        self.n_squares = n_squares
        self.pawns = []

        self.scaler = .9
        # scale square board to 90% window height
        self.board_height = self.window_dims[1]*self.scaler
        self.board = pg.Surface((self.board_height, self.board_height))

        # initialize Rect objs for squares on board
        self.generate_squares()
        # self.update_squares()
        # initialize pawns on board with their locations
        self.create_pawns()

    def draw(self):
        self.board.fill("pink")
        # draw square Rects to board
        [[square.draw() for square in row] for row in self.squares]
        
        # draw pawns on board
        [[pawn.draw() for pawn in row] for row in self.pawns]

        board_center = (
            (self.window_dims[0]-self.board.get_width())/2,
            (self.window_dims[1]-self.board.get_height())/2
        )
        # center board on center of window                
        self.window_surface.blit(self.board, board_center)

    def generate_squares(self):
        square_size = self.board.get_height()/self.n_squares
        self.squares = [[Square(self, ('white' if (x+y)%2 == 0 else 'black'), x, y, square_size) 
                         for x in range(self.n_squares)] for y in range(self.n_squares)]
        
    def create_pawns(self):
        num_rows = (self.n_squares//2) - 1
        # generate player 1's pawns
        self.pawns = [[Pawn(self, square[item], 'darkgreen', item, idx )
                        for item in range(self.n_squares) if square[item].color == 'black']
                           for idx, square in enumerate(self.squares[:num_rows])]
        # generate player 2's pawns
        self.pawns += [[Pawn(self, square[item], 'red', item, (idx + num_rows + 2))
                         for item in range(self.n_squares) if square[item].color == 'black']
                           for idx, square in enumerate(self.squares[-num_rows:])]
        
    # def update_squares(self):
    #     # update square locations
    #     for row in self.squares:
    #         for square in row:
    #             print(square)
    #     # [[print(f'{x}, {y}') for x in range(self.n_squares)] for y in range (self.n_squares)]
    
    def get_square(self, x, y):
        return self.squares[y][x]
