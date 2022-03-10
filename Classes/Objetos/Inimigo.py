import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, v):
        super().__init__()
        self.image = pygame.image.load('img/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = v

    def movimenta(self):
        self.rect = self.rect