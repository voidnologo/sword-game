import math
import pygame
from random import randint


class BaseSprite(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):

        # pygame.sprite.Sprite.__init__(self)
        super(BaseSprite, self).__init__()
        BaseSprite.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

    def destroy(self, class_name):
        class_name.List.remove(self)
        BaseSprite.allsprites.remove(self)
        del self


class MainCharacter(BaseSprite):

    List = pygame.sprite.Group()
    direction = ''

    def __init__(self, x, y, width, height, image_string):
        super(MainCharacter, self).__init__(x, y, width, height, image_string)
        MainCharacter.List.add(self)
        self.velx = 0
        self.vely = 8
        self.jumping = False
        self.go_down = False

    def motion(self, SCREENWIDTH, SCREENHEIGHT):

        location_x = self.rect.x + self.velx
        if location_x < 0 or location_x + self.width > SCREENWIDTH:
            self.velx = 0
        self.rect.x += self.velx

        self.__jump(SCREENHEIGHT)

    def __jump(self, SCREENHEIGHT):
        max_jump = 75

        if self.jumping:
            if self.rect.y < max_jump:
                self.go_down = True

            if self.go_down:
                self.rect.y += self.vely
                location_y = self.rect.y + self.vely
                if location_y + self.height > SCREENHEIGHT:
                    self.jumping = False
                    self.go_down = False
            else:
                self.rect.y -= self.vely


class Monster(BaseSprite):

    List = pygame.sprite.Group()
    START_HEALTH = 50
    HALF_HEALTH = START_HEALTH / 2.0

    def __init__(self, x, y, width, height, image_string):
        super(Monster, self).__init__(x, y, width, height, image_string)
        Monster.List.add(self)
        self.velx = randint(1, 4)
        self.amplitude = randint(30, 180)
        self.period = randint(3, 7) / 100.0
        self.health = self.START_HEALTH

    def motion(self, SCREENWIDTH):
        if self.rect.x + self.width > SCREENWIDTH or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx

        self.rect.x += self.velx
        self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 180

    def hit(self):
        self.health -= self.HALF_HEALTH

    @staticmethod
    def update_all(SCREENWIDTH):
        for monster in Monster.List:
            if monster.health <= 0:
                monster.destroy(Monster)

            monster.motion(SCREENWIDTH)

    # @staticmethod
    # def movement(SCREENWIDTH):
    #     for monster in Monster.List:
    #         monster.motion(SCREENWIDTH)


class Projectile(pygame.sprite.Sprite):

    List = pygame.sprite.Group()
    projectiles = []

    def __init__(self, x, y, width, height, image_string):
        super(Projectile, self).__init__()
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

        try:
            last_element = Projectile.projectiles[-1]
            difference = abs(self.rect.x - last_element.rect.x)
            if difference < self.width:
                return
        except Exception:
            pass

        Projectile.List.add(self)
        Projectile.projectiles.append(self)
        self.velx = None

    @staticmethod
    def movement():
        for projectile in Projectile.List:
            projectile.rect.x += projectile.velx
