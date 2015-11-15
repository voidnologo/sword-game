import pygame

from classes import BaseSprite, MainCharacter
from process import process


pygame.init()
SCREENWIDTH, SCREENHEIGHT = (800, 500)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

main_character = MainCharacter(0, SCREENHEIGHT - 128, 128, 128, 'images/sword_right.png')

while True:

    process(main_character)

    # <LOGIC>
    main_character.motion(SCREENWIDTH, SCREENHEIGHT)
    # </LOGIC>

    # <DRAW>
    screen.fill((30, 30, 30))
    BaseSprite.allsprites.draw(screen)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
