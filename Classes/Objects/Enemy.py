import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, vel):
        super().__init__()
        self.image = pygame.image.load('img/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = vel

    def movement(self):
        self.rect = self.rect
