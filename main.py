import pygame

from classes import BaseSprite, MainCharacter, Monster
from process import process


pygame.init()
SCREENWIDTH, SCREENHEIGHT = (800, 500)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

background = pygame.image.load('images/background.png')
main_character = MainCharacter(0, SCREENHEIGHT - 128, 128, 128, 'images/sword.png')
monster1 = Monster(40, 100, 90, 50, 'images/monster.png')
monster2 = Monster(40, 200, 90, 50, 'images/monster.png')
monster3 = Monster(40, 300, 90, 50, 'images/monster.png')
monster4 = Monster(40, 400, 90, 50, 'images/monster.png')

while True:

    process(main_character)

    # <LOGIC>
    main_character.motion(SCREENWIDTH, SCREENHEIGHT)
    Monster.movement(SCREENWIDTH)

    # </LOGIC>

    # <DRAW>
    screen.blit(background, (0, 0))
    BaseSprite.allsprites.draw(screen)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
