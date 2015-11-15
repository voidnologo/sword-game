import pygame
import sys


pygame.init()
WIDTH, HEIGHT = (640, 360)
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

img_sword = pygame.image.load('sword.png')

while True:

    # <PROCESS>
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # </PROCESS>

    # <LOGIC>
    # </LOGIC>

    # <DRAW>
    x = 200
    y = 200

    screen.blit(img_sword, (x, y))

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
