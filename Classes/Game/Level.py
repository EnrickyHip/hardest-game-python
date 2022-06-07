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
        self.background = Background(self.backgorund, self.screen)
        self.player = Player(self.game, self, spawnx, spawny)

        self.total_coins = len(coins)
        self.left_coins = self.total_coins

        #creating sprite groups
        self.walls = pygame.sprite.Group()
        self.rectangles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.addSprites(walls, enemies, coins)


    def addSprites(self, walls, enemies, coins): #add sprites to respective group
        self.active_sprite_list.add(self.info)
        self.active_sprite_list.add(self.player)

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
        self.player.test_keys()
        self.active_sprite_list.draw(self.screen)

        for enemy in self.enemies:
            enemy.movement()

        if not self.player.alive:
            self.player.die()


