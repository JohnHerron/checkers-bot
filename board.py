import pygame as pg

class Board:
    def __init__(self, pg, window_surface) -> None:
        self.window_surface = window_surface
        self.window_dims = window_surface.get_size()
        # scale board to 90% window size
        self.board = pg.Surface((self.window_dims[0]*.9,self.window_dims[1]*.9))

    def draw(self):
        self.board.fill("white")
        board_center = (
            (self.window_dims[0]-self.board.get_width())/2,
            (self.window_dims[1]-self.board.get_height())/2
        )
        # blit center of board to center of window                
        self.window_surface.blit(self.board, board_center)