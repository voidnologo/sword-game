import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640, 360), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
