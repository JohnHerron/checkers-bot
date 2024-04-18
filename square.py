import pygame as pg


class Square:
    '''Represents one square on a game board'''
    def __init__(self, board, color, x, y, size) -> None:
        self.board = board
        self.color = color
        self.pawn = None
        self.x = x
        self.y = y
        self.highlighted = False
        self.highlight_color = 'yellow'
        self.highlight_scaler = 0.3
        self.rect = pg.Rect(x * size, y * size, size, size)
        # collision rect is for collision detection, which requires a different
        # location than what is needed to blit the square to the game board
        self.col_rect = self.calculate_collision_rect(x, y)

    def draw(self):
        pg.draw.rect(self.board.board, self.color, self.rect)
        if self.highlighted:
            pg.draw.circle(self.board.board, self.highlight_color, self.rect.center, ((self.rect.height/2) * self.highlight_scaler), 0)

    def calculate_collision_rect(self, idx_x, idx_y):
        size = self.board.board_height / self.board.n_squares
        left_edge = (self.board.window_dims[0]/2) - (self.board.board_height/2)
        top_edge = (self.board.window_dims[1] - self.board.board_height)/2
        return pg.Rect(left_edge + (size * idx_x), top_edge + (size * idx_y), size, size)
    
    def toggle_highlight(self):
        self.highlighted = not self.highlighted

    def get_pawn(self):
        return self.pawn
    
    def set_pawn(self, pawn):
        self.pawn = pawn
