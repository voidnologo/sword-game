import pygame

from classes import BaseSprite, MainCharacter, Monster, Projectile
from process import process


pygame.init()
SCREENWIDTH, SCREENHEIGHT = (800, 500)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

background = pygame.image.load('images/background.png')
main_character = MainCharacter(0, SCREENHEIGHT - 128, 128, 128, 'images/sword.png')
total_frames = 0

while True:

    process(main_character, FPS, total_frames)

    # <LOGIC>
    main_character.motion(SCREENWIDTH, SCREENHEIGHT)
    Monster.update_all(SCREENWIDTH)
    Projectile.movement()
    # BaseSprite.allsprites.update()  # calls the 'update' method on each sprite
    total_frames += 1

    # </LOGIC>

    # <DRAW>
    screen.blit(background, (0, 0))
    BaseSprite.allsprites.draw(screen)
    Projectile.List.draw(screen)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
