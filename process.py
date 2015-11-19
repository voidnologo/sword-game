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
        classes.MainCharacter.direction = 'right'
    elif keys[pygame.K_a]:
        main_character.image = pygame.image.load('images/sword_left.png')
        main_character.velx = -5
        classes.MainCharacter.direction = 'left'
    else:
        main_character.velx = 0

    if keys[pygame.K_w]:
        main_character.jumping = True

    if keys[pygame.K_SPACE]:
        x = main_character.rect.x + 85 if classes.MainCharacter.direction == 'right' else main_character.rect.x
        p = classes.Projectile(x, main_character.rect.y, 48, 48, 'images/projectiles/fire_48.png')
        p.velx = 8 if classes.MainCharacter.direction == 'right' else -8
        if p.velx < 0:
            pygame.transform.flip(p.image, True, False)

    spawn(FPS, total_frames)
    collisions()


def spawn(FPS, total_frames):
    four_seconds = FPS * 4
    if total_frames % four_seconds == 0:
        x = 1 if random.choice([True, False]) else 710  # left = 1, right = SCREENWIDTH - image.width
        classes.Monster(x, 130, 90, 50, 'images/monster.png')


def collisions():
    for monster in classes.Monster.List:
        monster_hit = pygame.sprite.spritecollide(monster, classes.Projectile.List, True)
        if len(monster_hit) > 0:
            for hit in monster_hit:
                monster.health -= monster.half_health
