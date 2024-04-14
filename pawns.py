import pygame as pg

class Pawn:
    '''Pawns exist on an mxn board where their location is denoted by
    an (y, x) or (h, w) pair where (0,0) is the top left of the board'''
    def __init__(self, board, square, color, y, x) -> None:
        self.board = board
        self.king = False
        self.square = square
        self.color = color
        self.x = x
        self.y = y
        # TODO:
        # self.moves = self.generate_moves()

    def draw(self):
        pg.draw.circle(self.board.board, self.color, self.square.center, (self.square.height/2 * .7), 0)

    def move_to(self, h, w):
        '''Moves pawn to (h,w) on mxn board'''
        self.square = self.board.squares[h][w]
        self.y = h
        self.x = w