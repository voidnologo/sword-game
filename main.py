import pygame

from classes import BaseClass, Bug
from process import process


pygame.init()
SCREENWIDTH, SCREENHEIGHT = (640, 360)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0, SCREENHEIGHT - 128, 128, 128, 'images/sword_right.png')

while True:

    process(bug)

    # <LOGIC>
    bug.motion()
    # </LOGIC>

    # <DRAW>
    screen.fill((0, 0, 0))
    BaseClass.allsprites.draw(screen)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
