from Classes.Objects.Enemy import Enemy

class VerticalEnemy(Enemy):
    def __init__(self, x, y, vel, min, max):
        super().__init__(x, y)
        self.vel = vel
        self.max = max
        self.min = min

    def movement(self):
        if self.rect.y >= self.max or self.rect.y <= self.min:
            self.vel *= -1
        self.rect.y += self.vel
