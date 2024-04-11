import pygame as pg

class Board:
    def __init__(self, pg, window_surface) -> None:
        self.window_surface = window_surface
        self.window_dims = window_surface.get_size()
        # scale square board to 90% window height
        self.board_height = self.window_dims[1]*.9
        self.board = pg.Surface((self.board_height, self.board_height))
        # create Rect objs for squares on board
        self.generate_squares()

    def draw(self):
        self.board.fill("white")
        # draw square Rects to board
        [[pg.draw.rect(self.board, self.squares[x][y][0], self.squares[x][y][1]) for x in range(8)] for y in range(8)]

        board_center = (
            (self.window_dims[0]-self.board.get_width())/2,
            (self.window_dims[1]-self.board.get_height())/2
        )
        # blit center of board to center of window                
        self.window_surface.blit(self.board, board_center)

    def generate_squares(self):
        square_size = self.board.get_height()/8
        self.squares = [[('white' if (x+y)%2 == 0 else 'black',pg.Rect(square_size * x, square_size * y, square_size, square_size))
                         for x in range(8)] for y in range(8)]
        print(self.squares)