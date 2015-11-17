import pygame
import sys
import classes
import random


def process(main_character, FPS, total_frames):

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

    spawn(FPS, total_frames)


def spawn(FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        x = 1 if random.choice([True, False]) else 710  # left = 1, right = SCREENWIDTH - image.width
        classes.Monster(x, 130, 90, 50, 'images/monster.png')
