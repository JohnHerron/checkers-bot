import pygame as pg

class Board:
    '''Board class represents an nxn game board used for display'''
    def __init__(self, pg, window_surface, n_squares) -> None:
        self.window_surface = window_surface
        self.window_dims = window_surface.get_size()
        self.n_squares = n_squares
        # scale square board to 90% window height
        self.board_height = self.window_dims[1]*.9
        self.board = pg.Surface((self.board_height, self.board_height))
        # initialize Rect objs for squares on board
        self.generate_squares()

    def draw(self):
        self.board.fill("pink")
        # draw square Rects to board
        [[pg.draw.rect(self.board, self.squares[x][y][0], self.squares[x][y][1])
           for x in range(self.n_squares)] for y in range(self.n_squares)]

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