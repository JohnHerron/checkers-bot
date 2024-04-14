import pygame as pg
from pawns import Pawn

class Board:
    '''Board class represents an nxn game board used for display'''
    def __init__(self, pg, window_surface, n_squares) -> None:
        self.window_surface = window_surface
        self.window_dims = window_surface.get_size()
        self.n_squares = n_squares
        self.pawns = []

        # scale square board to 90% window height
        self.board_height = self.window_dims[1]*.9
        self.board = pg.Surface((self.board_height, self.board_height))

        # initialize Rect objs for squares on board
        self.generate_squares()
        # initialize pawns on board with their locations
        self.create_pawns()

    def draw(self):
        self.board.fill("pink")
        # draw square Rects to board
        [[pg.draw.rect(self.board, self.squares[x][y][0], self.squares[x][y][1])
           for x in range(self.n_squares)] for y in range(self.n_squares)]
        
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
        self.squares = [[('white' if (x+y)%2 == 0 else 'black',pg.Rect(square_size * x, square_size * y, square_size, square_size)) 
                         for x in range(self.n_squares)] for y in range(self.n_squares)]
        
    def create_pawns(self):
        num_rows = (self.n_squares//2) - 1
        self.pawns = [[Pawn(self, square[item][1], 'darkgreen', idx, item ) for item in range(self.n_squares) if square[item][0] == 'black'] for idx, square in enumerate(self.squares[:num_rows])]
        self.pawns += [[Pawn(self, square[item][1], 'red', ((idx + num_rows) + 2), item) for item in range(self.n_squares) if square[item][0] == 'black'] for idx, square in enumerate(self.squares[-num_rows:])]
