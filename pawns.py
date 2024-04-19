import pygame as pg

class Pawn:
    '''Pawns exist on an mxn board where their location is denoted by
    an (y,x) or (h,w) pair where (0,0) is the top left of the board'''
    def __init__(self, board, square, color, x, y) -> None:
        self.board = board
        self.king = False
        self.square = square
        self.color = color
        self.highlight_color = 'yellow'
        self.highlighted = False
        self.x = x
        self.y = y
        square.set_pawn(self)

    def draw(self):
        pg.draw.circle(self.board.board, self.color, self.square.rect.center, (self.square.rect.height/2 * .7), 0)
        if self.highlighted:
            pg.draw.circle(self.board.board, self.highlight_color, self.square.rect.center, (self.square.rect.height/2 * .7), 3)

    def move_to(self, square):
        '''Move pawn to square on board, reassign associated pawns in square objects'''
        # remove pawn from previous square
        self.square.set_pawn(None)
        self.square = square
        # assign pawn to new square
        self.square.set_pawn(self)
        self.y = square.y
        self.x = square.x

    def get_location(self):
        return (self.x, self.y)
    
    def toggle_highlight(self):
        self.highlighted = not self.highlighted

    def kill_pawn(self):
        self.square.set_pawn(None)
        for row in self.board.pawns:
            try:
                row.remove(self)
            except:
                pass
