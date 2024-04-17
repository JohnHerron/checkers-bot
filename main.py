import pygame as pg
from checkers import Checkers


pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Checkers")
clock = pg.time.Clock()
running = True
checker_game = Checkers(screen, 8)
    
while running:
    # poll for events
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            for row in checker_game.board.pawns:
              for pawn in row:
                if pawn.square.col_rect.collidepoint(event.pos):
                    checker_game.select_pawn(pawn)
        # pygame.QUIT event means the user clicked X to close the window
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((138, 221, 237))

    # RENDER GAME HERE
    checker_game.board.draw()

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()