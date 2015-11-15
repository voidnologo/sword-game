import pygame


class BaseClass(pygame.sprite.Sprite):

    allsprites = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):

        # pygame.sprite.Sprite.__init__(self)
        super(BaseClass, self).__init__()
        BaseClass.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height


class Bug(BaseClass):

    List = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        super(Bug, self).__init__(x, y, width, height, image_string)
        Bug.List.add(self)
        self.velx = 0

    def motion(self):
        self.rect.x += self.velx
