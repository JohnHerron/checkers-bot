import pygame as pg
from checkers import Checkers
from game import Game
from minimax import minimax
import time


pg.init()
screen = pg.display.set_mode((1280, 720))
pg.display.set_caption("Checkers")
clock = pg.time.Clock()
running = True
game = Game(Checkers(screen, 4), minimax)

pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 40)
    
while running:
    if game.game.turn == 'GREEN':
       time.sleep(0.5)
       game.move_bot()
       if game.getWinner():
            text_surface = my_font.render(f"{game.getWinner()} WINS!!!", True, (0,0,0))

    # poll for events
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            for row in game.game.board.squares:
              for square in row:
                if square.col_rect.collidepoint(event.pos):
                    game.handle_click(square)
                    if game.getWinner():
                       text_surface = my_font.render(f"{game.getWinner()} WINS!!!", True, (0,0,0), (245, 227, 88))
                       
        # pygame.QUIT event means the user clicked X to close the window
        if event.type == pg.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill((138, 221, 237))

    # RENDER GAME HERE
    game.game.board.draw()

    # display win screen
    if game.getWinner():
        screen.blit(text_surface, (10, 10))

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()