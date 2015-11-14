import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
clock = pygame.time.Clock()
FPS = 60

r = 0
g = 0
b = 0
rc = False
gc = False
bc = False
radius = 5
x = random.randint(1, 639)
y = random.randint(1, 359)

while True:

    # <PROCESS>
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # </PROCESS>

    # <LOGIC>
    if not rc and not gc and not bc:
        r += 1
        if r > 255:
            r = 0
            rc = True

    if rc and not gc and not bc:
        g += 1

        if g > 255:
            g = 0
            gc = True

    if rc and gc and not bc:
        b += 1

        if b > 255:
            b = 0
            bc = True

    if rc and gc and bc:
        rc = False
        gc = False
        bc = False

    if (x - radius) < 0 or (x + radius) > 640 or (y - radius) < 0 or (y + radius) > 360:
        x = random.randint(1, 639)
        y = random.randint(1, 359)
        radius = 5

    radius += 1
    # </LOGIC>

    # <DRAW>
    screen.fill((r, g, b))

    pygame.draw.circle(screen, (b, r, g), (x, y), radius, 5)

    pygame.display.flip()
    # </DRAW>

    clock.tick(FPS)
