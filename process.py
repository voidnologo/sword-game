import pygame
import sys


def process(main_character):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        main_character.image = pygame.image.load('images/sword_right.png')
        main_character.velx = 5
    elif keys[pygame.K_a]:
        main_character.image = pygame.image.load('images/sword_left.png')
        main_character.velx = -5
    else:
        main_character.velx = 0

    if keys[pygame.K_w]:
        main_character.jumping = True
