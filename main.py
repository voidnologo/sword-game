import pygame
import sys

from classes import *


pygame.init()
WIDTH, HEIGHT = (640, 360)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0, 100, 128, 128, 'images/sword.png')
# img_sword = pygame.image.load('sword.png')

while True:

    # <PROCESS>
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # </PROCESS>

    # <LOGIC>
    bug.motion()
    # </LOGIC>

    # <DRAW>
    screen.fill((0, 0, 0))
    BaseClass.allsprites.draw(screen)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
