#player class

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game,  x, y):
        super().__init__()
        self.image = pygame.image.load('img/player.png')
        self.game = game
        self.alive = True
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def test_keys(self, level):
        level.test_collision(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.movement(0, -2)
            level.test_collision(0, -2)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.movement(0, 2)
            level.test_collision(0, 2)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.movement(-2, 0)
            level.test_collision(-2, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.movement(2, 0)
            level.test_collision(2, 0)

    def movement(self, x, y):
        if self.alive:
            self.rect.x += x
            self.rect.y += y

    # GETTERS

    @property
    def alive(self):
        return self.__alive

    @property
    def alpha(self):
        return self.__alpha

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    #SETTERS

    @alive.setter
    def alive(self, value):
        self.__alive = value

    @alpha.setter
    def alpha(self, value):
        self.__alpha = value

    @image.setter
    def image(self, value):
        self.__image = value

    @rect.setter
    def rect(self, value):
        self.__rect = value







