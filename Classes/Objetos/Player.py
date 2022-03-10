import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, j,  x, y):
        super().__init__()
        self.image = pygame.image.load('img/quad.png')
        self.jogo = j
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def movimenta(self, niv):
        niv.testacolisao(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            niv.testacolisao(0, -2)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            niv.testacolisao(0, 2)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            niv.testacolisao(-2, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            niv.testacolisao(2, 0)