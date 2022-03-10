import pygame

class Retangulo(pygame.sprite.Sprite):
    def __init__(self, l, a, x, y,):
        super().__init__()
        self.image = pygame.Surface([l, a])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0, 0, 0))