#player class

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game, level,  x, y):
        super().__init__()
        self.image = pygame.image.load('img/player.png')
        self.level = level
        self.game = game
        self.alive = True
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def test_keys(self):
        self.test_collision(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.movement(0, -2)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.movement(0, 2)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.movement(-2, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.movement(2, 0)

    def movement(self, x, y):
        if self.alive:
            self.rect.x += x
            self.rect.y += y
        
        self.test_collision(x, y)

    def test_collision(self, x, y):
        self.image.set_alpha(self.alpha)

        self.wall_collision(x, y)
        self.enemy_collision()
        self.coin_collision()  

        if x == 0 and y == 0:
            self.final_collision()

    def wall_collision(self, x, y):
        wall_list = pygame.sprite.spritecollide(self, self.level.walls, False) # wall collisions

        for wall in wall_list:
            if x > 0:
                self.rect.right = wall.rect.left
            elif x < 0:
                self.rect.left = wall.rect.right
            elif y < 0:
                self.rect.top = wall.rect.bottom
            elif y > 0:
                self.rect.bottom = wall.rect.top

    def enemy_collision(self):
        enemy_list = pygame.sprite.spritecollide(self, self.level.enemies, False)  # enemy collisions

        if enemy_list:
            self.alive = False

    def coin_collision(self):
        coin_list = pygame.sprite.spritecollide(self, self.level.coins, False) # coin collsions

        for coin in coin_list:
            if coin in self.level.active_sprite_list:
                self.level.active_sprite_list.remove(coin)
                self.level.left_coins -= 1

    def final_collision(self):
        if self.rect.colliderect(self.level.final.rect) and self.level.left_coins == 0: # final collision
            self.game.actual_level += 1
            self.game.active_sprite_list = pygame.sprite.Group()

    def die(self):
        if self.decreaseAlpha():
            self.alive = True
            self.rect.x = self.level.spawnx
            self.rect.y = self.level.spawny

            self.game.deaths += 1

            for coin in self.level.coins:
                self.level.active_sprite_list.add(coin)
                self.level.left_coins = self.level.total_coins

    def decreaseAlpha(self):
        if self.alpha > 0:
            self.alpha = self.alpha - 7
        else:
            self.alpha = 255
            return True

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
