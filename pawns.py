import pygame as pg

class Pawn:
    '''Pawns exist on an mxn board where their location is denoted by
    an (y,x) or (h,w) pair where (0,0) is the top left of the board'''
    def __init__(self, board, square, color, x, y) -> None:
        self.board = board
        self.king = False
        self.square = square
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        pg.draw.circle(self.board.board, self.color, self.square.center, (self.square.height/2 * .7), 0)

    def move_to(self, location):
        '''--> tuple moves pawn to (x,y) or (w,h) on mxn board'''
        self.square = self.board.squares[location[1]][location[0]][1]
        self.y = location[1]
        self.x = location[0]

    def get_location(self):
        return (self.x, self.y)