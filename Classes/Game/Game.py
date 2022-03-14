import pygame
from Classes.Game.Rectangle import Rectangle
from Classes.Game.Level import Level
from Classes.Game.Text import Text
from Classes.Objects.Coin import Coin
from Classes.Objects.StaticEnemy import StaticEnemy
from Classes.Objects.VerticalEnemy import VerticalEnemy
from Classes.Objects.HorizontalEnemy import HorizontalEnemy
from Classes.Objects.CircularEnemy import CircularEnemy
from Classes.Objects.RectangleEnemy import RectangleEnemy


class Game:
    def __init__(self):
        self.playing = True
        self.deaths = 0

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Hardest Game Ever In Python")
        icon = pygame.image.load('img/player.png')
        pygame.display.set_icon(icon)

        self.levels = []
        self.actual_level = 0
        self.create_levels()

        self.text = Text(self.screen)
        self.loop()

    @staticmethod
    def circular_movement_group(x, y, angle, vel, diameter, direction, spacing, quantity):
        enemies = []
        for enemy in range(quantity):
            enemy = CircularEnemy(x, y, angle, vel, diameter * spacing, direction)
            enemies.append(enemy)
            diameter -= 16
        return enemies

    @staticmethod
    def vertical_movement_group(x, y, vel, ymin, ymax, quantity, spacing):
        enemies = []
        for enemy in range(quantity):
            enemy = VerticalEnemy(x, y, vel, ymin, ymax)
            enemies.append(enemy)
            x += spacing
        return enemies

    @staticmethod
    def horizontal_movement_group(x, y, vel, xmin, xmax, quantity, spacing):
        enemies = []
        for enemy in range(quantity):
            enemy = HorizontalEnemy(x, y, vel, xmin, xmax)
            enemies.append(enemy)
            y += spacing
        return enemies

    def create_levels(self):
        wall1 = Rectangle(71, 353, 101, 195)
        wall2 = Rectangle(4, 70, 97, 124)
        wall3 = Rectangle(71, 35, 101, 89)
        wall4 = Rectangle(459, 4, 172, 85)
        wall5 = Rectangle(70, 353, 631, 89)
        wall6 = Rectangle(70, 35, 631, 513)
        wall7 = Rectangle(459, 4, 172, 548)

        enemy_group1 = self.vertical_movement_group(180, 97, 5, 89, 530, 7, 71)
        enemy_group2 = self.horizontal_movement_group(180, 97, 5, 172, 613, 7, 71)

        final = Rectangle(4, 71, 630, 442)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]
        enemies = []
        for enemy in enemy_group1, enemy_group2:
            enemies.append(enemy)
        coins = []

        level1 = Level(self.screen, coins, pygame.image.load('level/level1.png'), 125, 147, walls, self, enemies, final)
        self.levels.append(level1)

        wall1 = Rectangle(68, 32, 171, 351)
        wall2 = Rectangle(4, 68, 167, 283)
        wall3 = Rectangle(68, 32, 171, 251)
        wall4 = Rectangle(332, 4, 239, 247)
        wall5 = Rectangle(4, 68, 639, 283)
        wall6 = Rectangle(68, 32, 571, 351)
        wall7 = Rectangle(332, 4, 239, 383)
        wall8 = Rectangle(68, 32, 571, 251)

        enemy_group1 = self.vertical_movement_group(247, 259, 3, 251, 365, 5, 66)
        enemy_group2 = self.vertical_movement_group(278, 360, -3, 251, 365, 5, 67)

        coin1 = Coin(396, 308)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]
        enemies = []

        for enemy in enemy_group1, enemy_group2:
            enemies.append(enemy)

        final = Rectangle(4, 68, 571, 283)
        coins = [coin1]

        level2 = Level(self.screen, coins, pygame.image.load('level/level2.png'), 193, 306, walls, self, enemies, final)
        self.levels.append(level2)

        wall1 = Rectangle(288, 128, 308, 383)
        wall2 = Rectangle(4, 256, 596, 127)
        wall3 = Rectangle(288, 128, 212, 127)
        wall4 = Rectangle(4, 260, 208, 255)
        wall5 = Rectangle(96, 4, 212, 511)
        wall6 = Rectangle(96, 4, 500, 123)

        enemy1 = HorizontalEnemy(219, 390, 3, 212, 290)
        enemy2 = HorizontalEnemy(571, 198, -3, 500, 578)
        enemy_group1 = self.horizontal_movement_group(219, 262, 6, 212, 578, 2, 32)
        enemy_group2 = self.horizontal_movement_group(571, 326, -6, 212, 578, 2, 32)

        coin1 = Coin(219, 262)
        coin2 = Coin(571, 358)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6]
        enemies = [enemy1, enemy2]

        for enemy in enemy_group1, enemy_group2:
            enemies.append(enemy)

        final = Rectangle(96, 4, 500, 187)
        coins = [coin1, coin2]

        level3 = Level(self.screen, coins, pygame.image.load('level/level3.png'), 248, 468, walls, self, enemies, final)
        self.levels.append(level3)

        wall1 = Rectangle(66, 66, 171, 216)
        wall2 = Rectangle(397, 4, 237, 212)
        wall3 = Rectangle(4, 198, 634, 216)
        wall4 = Rectangle(397, 4, 237, 414)
        wall5 = Rectangle(66, 66, 171, 348)
        wall6 = Rectangle(4, 66, 167, 282)

        enemy_group1 = self.circular_movement_group(328, 306, 0, 3.6, 80, 1, 1, 11)
        enemy_group2 = self.circular_movement_group(328, 306, 1.57, 3.6, 80, 1, 1, 11)
        enemy_group3 = self.circular_movement_group(526, 306, 0, 3.6, 80, -1, 1, 11)
        enemy_group4 = self.circular_movement_group(526, 306, 1.57, 3.6, 80, -1, 1, 11)

        coin1 = Coin(609, 389)
        coin2 = Coin(609, 223)
        coin3 = Coin(427, 223)
        coin4 = Coin(427, 389)
        coin5 = Coin(245, 223)
        coin6 = Coin(245, 389)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6]
        enemies = []
        for enemy in enemy_group1, enemy_group2, enemy_group3, enemy_group4:
            enemies.append(enemy)
        final = Rectangle(4, 66, 233, 282)
        coins = [coin1, coin2, coin3, coin4, coin5, coin6]

        level4 = Level(self.screen, coins, pygame.image.load('level/level4.png'), 191, 303, walls, self, enemies, final)
        self.levels.append(level4)

        wall1 = Rectangle(4, 64, 134, 276)
        wall2 = Rectangle(64, 160, 138, 116)
        wall3 = Rectangle(224, 4, 202, 112)
        wall4 = Rectangle(96, 352, 426, 116)
        wall5 = Rectangle(128, 4, 522, 272)
        wall6 = Rectangle(4, 64, 650, 276)
        wall7 = Rectangle(64, 192, 586, 340)
        wall8 = Rectangle(224, 4, 362, 532)
        wall9 = Rectangle(96, 352, 266, 180)
        wall10 = Rectangle(128, 4, 138, 340)

        enemy1 = VerticalEnemy(209, 123, 3, 122, 316)
        enemy2 = VerticalEnemy(241, 316, -3, 123, 317)
        enemy3 = StaticEnemy(275, 123)
        enemy4 = StaticEnemy(335, 155)
        enemy5 = StaticEnemy(369, 187)
        enemy6 = StaticEnemy(401, 251)
        enemy7 = StaticEnemy(369, 316)
        enemy8 = StaticEnemy(401, 379)
        enemy9 = StaticEnemy(369, 444)
        enemy10 = VerticalEnemy(369, 123, 3, 122, 508)
        enemy11 = VerticalEnemy(401, 508, -3, 123, 509)
        enemy12 = StaticEnemy(433, 475)
        enemy13 = StaticEnemy(496, 507)
        enemy14 = VerticalEnemy(529, 283, 4, 282, 508)
        enemy15 = VerticalEnemy(561, 508, -4, 283, 509)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10]
        enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12,
                   enemy13, enemy14, enemy15]
        final = Rectangle(4, 64, 586, 276)
        coins = []

        level5 = Level(self.screen, coins, pygame.image.load('level/level5.png'), 157, 297, walls, self, enemies, final)
        self.levels.append(level5)

        wall1 = Rectangle(100, 231, 336, 249)
        wall2 = Rectangle(166, 267, 303, 480)
        wall3 = Rectangle(33, 67, 204, 480)
        wall4 = Rectangle(33, 67, 535, 480)
        wall5 = Rectangle(4, 364, 568, 116)
        wall6 = Rectangle(364, 4, 204, 112)
        wall7 = Rectangle(4, 364, 200, 116)
        wall8 = Rectangle(298, 4, 237, 547)

        enemy1 = RectangleEnemy(213, 125, 3, 124, 223, 212, 310, 1)
        enemy2 = RectangleEnemy(309, 221, -3, 124, 223, 212, 310, 1)
        enemy3 = RectangleEnemy(445, 125, 3, 124, 223, 444, 542, 1)
        enemy4 = RectangleEnemy(541, 221, -3, 124, 223, 444, 542, 1)
        enemy5 = VerticalEnemy(344, 123, 3, 122, 224)
        enemy6 = VerticalEnemy(411, 224, -3, 123, 225)
        enemy7 = HorizontalEnemy(211, 257, 3, 210, 312)
        enemy8 = HorizontalEnemy(444, 257, 3, 443, 545)

        coin1 = Coin(244, 157)
        coin2 = Coin(277, 157)
        coin3 = Coin(244, 192)
        coin4 = Coin(277, 192)
        coin5 = Coin(477, 157)
        coin6 = Coin(510, 157)
        coin7 = Coin(477, 192)
        coin8 = Coin(510, 192)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8]
        enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
        final = Rectangle(66, 4, 469, 480)
        coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8]

        level6 = Level(self.screen, coins, pygame.image.load('level/level6.png'), 257, 501, walls, self, enemies, final)
        self.levels.append(level6)

        wall1 = Rectangle(66, 99, 534, 367)
        wall2 = Rectangle(66, 99, 534, 201)
        wall3 = Rectangle(265, 4, 269, 197)
        wall4 = Rectangle(66, 99, 203, 201)
        wall5 = Rectangle(4, 67, 199, 300)
        wall6 = Rectangle(66, 99, 203, 367)
        wall7 = Rectangle(265, 4, 269, 466)

        enemy1 = VerticalEnemy(376, 209, 3, 208, 440)
        enemy2 = VerticalEnemy(409, 439, 3, 208, 440)
        enemy_group1 = self.horizontal_movement_group(277, 209, 3, 276, 508, 4, 66)
        enemy_group2 = self.horizontal_movement_group(507, 241, 3, 276, 508, 4, 66)

        walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]
        enemies = [enemy1, enemy2]
        for enemy in enemy_group1, enemy_group2:
            enemies.append(enemy)
        coins = []
        final = Rectangle(4, 67, 534, 300)

        level7 = Level(self.screen, coins, pygame.image.load('level/level7.png'), 224, 322, walls, self, enemies,
                       final)
        self.levels.append(level7)

        wall1 = Rectangle(265, 4, 269, 197)
        wall2 = Rectangle(265, 4, 269, 466)
        wall3 = Rectangle(4, 265, 265, 193)
        wall4 = Rectangle(4, 265, 534, 201)

        enemy1 = StaticEnemy(343, 275)
        enemy2 = StaticEnemy(310, 275)
        enemy3 = StaticEnemy(343, 241)
        enemy4 = StaticEnemy(343, 375)
        enemy5 = StaticEnemy(310, 375)
        enemy6 = StaticEnemy(343, 408)
        enemy7 = StaticEnemy(443, 375)
        enemy8 = StaticEnemy(443, 408)
        enemy9 = StaticEnemy(476, 375)
        enemy10 = StaticEnemy(476, 275)
        enemy11 = StaticEnemy(443, 275)
        enemy12 = StaticEnemy(443, 241)
        enemy13 = RectangleEnemy(343, 275, 3, 274, 374, 342, 443, 1)
        enemy14 = RectangleEnemy(310, 241, 4, 240, 407, 309, 476, 1)
        enemy15 = RectangleEnemy(276, 208, 5, 207, 440, 275, 509, 1)

        coin1 = Coin(476, 407)
        coin2 = Coin(309, 407)
        coin3 = Coin(309, 241)
        coin4 = Coin(476, 241)

        walls = [wall1, wall2, wall3, wall4]
        enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12,
                   enemy13, enemy14, enemy15]
        final = Rectangle(67, 67, 368, 300)
        coins = [coin1, coin2, coin3, coin4]

        level8 = Level(self.screen, coins, pygame.image.load('level/level8.png'), 388, 321, walls, self, enemies, final)
        self.levels.append(level8)

    def loop(self):
        clock = pygame.time.Clock()
        janela = True

        while janela:
            clock.tick(60)

            level = self.levels[self.actual_level]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela = False

            if self.playing:
                level.draw()

            self.text.show_deaths(self.deaths)
            pygame.display.update()
        pygame.quit()
