import pygame
import sys


def process(bug):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        bug.image = pygame.image.load('images/sword_right.png')
        bug.velx = 5
    elif keys[pygame.K_a]:
        bug.image = pygame.image.load('images/sword_left.png')
        bug.velx = -5
    else:
        bug.velx = 0
