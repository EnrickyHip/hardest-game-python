import pygame
from Classes.Game.Rectangle import Rectangle
from Classes.Game.Background import Background
from Classes.Objects.Player import Player


class Level:
    def __init__(self, screen, coins, background, spawnx, spawny, walls, game, enemies, final):
        self.screen = screen
        self.backgorund = background
        self.game = game
        self.spawnx = spawnx
        self.spawny = spawny
        self.final = final
        self.active_sprite_list = pygame.sprite.Group()

        self.info = Rectangle(800, 36, 0, 0)
        self.active_sprite_list.add(self.info)

        self.background = Background(self.backgorund, self.screen)
        self.player = Player(self, spawnx, spawny)
        self.active_sprite_list.add(self.player)

        self.walls = pygame.sprite.Group()
        self.rectangles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.total_coins = len(coins)
        self.gotten_coins = self.total_coins

        for wall in walls:
            self.walls.add(wall)

        for enemy in enemies:
            self.enemies.add(enemy)
            self.active_sprite_list.add(enemy)

        for coin in coins:
            self.coins.add(coin)
            self.active_sprite_list.add(coin)

    def draw(self):
        self.background.draw()
        self.player.movement(self)
        self.active_sprite_list.draw(self.screen)

        for enemy in self.enemies:
            enemy.movement()

        if not self.player.get_alive():
            self.die()

    def test_collision(self, x, y):
        if self.player.get_alive():
            self.player.set_rect_x(self.player.get_rect_x() + x)
            self.player.set_rect_y(self.player.get_rect_y() + y)
        self.player.get_image().set_alpha(self.player.get_alpha())

        wall_list = pygame.sprite.spritecollide(self.player, self.walls, False) # colisão de paredes
        for wall in wall_list:
            if x > 0:
                self.player.get_rect().right = wall.rect.left
            elif x < 0:
                self.player.get_rect().left = wall.rect.right
            elif y < 0:
                self.player.get_rect().top = wall.rect.bottom
            elif y > 0:
                self.player.get_rect().bottom = wall.rect.top

        enemy_list = pygame.sprite.spritecollide(self.player, self.enemies, False) # colisão de inimigos
        if enemy_list:
            self.player.set_alive(False)

        if self.player.get_rect().colliderect(self.final.rect) and self.gotten_coins == 0:
            self.game.actual_level += 1
            self.game.active_sprite_list = pygame.sprite.Group()

        coin_list = pygame.sprite.spritecollide(self.player, self.coins, False) # colisao de moedas
        for coin in coin_list:
            if coin in self.active_sprite_list:
                self.active_sprite_list.remove(coin)
                self.gotten_coins -= 1

    def die(self):
        if self.player.get_alpha() > 0:
            self.player.set_alpha(self.player.get_alpha() - 7)
        else:
            self.player.set_alpha(255)
            self.player.set_alive(True)
            self.player.set_rect_x(self.spawnx)
            self.player.set_rect_y(self.spawny)
            self.game.deaths += 1

            for coin in self.coins:
                self.active_sprite_list.add(coin)
                self.gotten_coins = self.total_coins

