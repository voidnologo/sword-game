import pygame


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


class MainCharacter(BaseSprite):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        super(MainCharacter, self).__init__(x, y, width, height, image_string)
        MainCharacter.List.add(self)
        self.velx = 0
        self.vely = 5
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

    def __init__(self, x, y, width, height, image_string):
        super(Monster, self).__init__(x, y, width, height, image_string)
        Monster.List.add(self)
