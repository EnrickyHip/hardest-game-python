#generic rectangle class
#its used for making walls, the level final, and also the game's on the head

import pygame

class Rectangle(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y,):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0, 0, 0))
