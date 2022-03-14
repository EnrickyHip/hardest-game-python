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

    def movement(self, level):
        level.test_collision(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            level.test_collision(0, -2)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            level.test_collision(0, 2)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            level.test_collision(-2, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            level.test_collision(2, 0)

    # GETTERS

    def get_alive(self):
        return self.alive

    def get_alpha(self):
        return self.alpha

    def get_rect(self):
        return self.rect

    def get_rect_x(self):
        return self.rect.x

    def get_rect_y(self):
        return self.rect.y

    def get_image(self):
        return self.image

    #SETTERS

    def set_rect_x(self, value):
        self.rect.x = value

    def set_rect_y(self, value):
        self.rect.y = value

    def set_alive(self, value):
        self.alive = value

    def set_alpha(self, value):
        self.alpha = value






