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
            print(enemy)
            enemy.movement()

        if not self.player.alive:
            self.die()

    def test_collision(self, x, y):
        if self.player.alive:
            self.player.rect.x += x
            self.player.rect.y += y
        self.player.image.set_alpha(self.player.alpha)

        wall_list = pygame.sprite.spritecollide(self.player, self.walls, False) # colisão de paredes
        for wall in wall_list:
            if x > 0:
                self.player.rect.right = wall.rect.left
            elif x < 0:
                self.player.rect.left = wall.rect.right
            elif y < 0:
                self.player.rect.top = wall.rect.bottom
            elif y > 0:
                self.player.rect.bottom = wall.rect.top

        enemy_list = pygame.sprite.spritecollide(self.player, self.enemies, False) # colisão de inimigos
        if enemy_list:
            self.player.alive = False

        if self.player.rect.colliderect(self.final.rect) and self.gotten_coins == 0:
            self.game.actual_level += 1
            self.game.active_sprite_list = pygame.sprite.Group()

        coin_list = pygame.sprite.spritecollide(self.player, self.coins, False) # colisao de moedas
        for coin in coin_list:
            if coin in self.active_sprite_list:
                self.active_sprite_list.remove(coin)
                self.gotten_coins -= 1

    def die(self):
        if self.player.alpha > 0:
            self.player.alpha -= 7
        else:
            self.player.alpha = 255
            self.player.alive = True
            self.player.rect.x = self.spawnx
            self.player.rect.y = self.spawny
            self.game.deaths += 1

            for coin in self.coins:
                self.active_sprite_list.add(coin)
                self.gotten_coins = self.total_coins

