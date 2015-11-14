import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
clock = pygame.time.Clock()
FPS = 24

color1 = (22, 122, 11)
color2 = (0, 44, 166)
color3 = (234, 55, 45)

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
    screen.fill((90, 200, 90))
    x1, y1 = (0, 0)
    x2, y2 = (640, 360)
    pygame.draw.line(screen, color2, (x1, y1), (x2, y2), 5)
    pygame.draw.rect(screen, color3, (40, 40, 300, 45))
    pygame.draw.circle(screen, color1, (350, 200), 80, 40)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
