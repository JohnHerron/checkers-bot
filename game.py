import pygame as pg
from board import Board

pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Checkers")
clock = pg.time.Clock()
running = True
board = Board(pg, screen, 8)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((138, 221, 237))

    # RENDER GAME HERE
    board.draw()

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()