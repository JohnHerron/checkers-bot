import pygame as pg
from checkers import Checkers
from game import Game
from minimax import Minimax


pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Checkers")
clock = pg.time.Clock()
running = True
minimax = Minimax()
game = Game(Checkers(screen, 8), minimax)
    
while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            for row in game.game.board.squares:
              for square in row:
                if square.col_rect.collidepoint(event.pos):
                    game.handle_click(square)
        # pygame.QUIT event means the user clicked X to close the window
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((138, 221, 237))

    # RENDER GAME HERE
    game.game.board.draw()

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()