#enemies with horizontal movement, inherit from the Enemy class

from Classes.Objects.Enemy import Enemy

class HorizontalEnemy(Enemy):
    def __init__(self, x, y, vel, min, max):
        super().__init__(x, y)
        self.max = max
        self.min = min
        self.vel = vel

    def movement(self):
        if self.rect.x >= self.max or self.rect.x <= self.min:
            self.vel *= -1
            
        self.rect.x += self.vel
