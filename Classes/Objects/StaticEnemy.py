#static enemy, inherited ftom Enemy class

from Classes.Objects.Enemy import Enemy


class StaticEnemy(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)

    def movement(self):
        self.rect = self.rect
