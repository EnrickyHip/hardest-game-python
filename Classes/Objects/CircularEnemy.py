from Classes.Objects.Enemy import Enemy
import math

class CircularEnemy(Enemy):
    def __init__(self, x, y, angle, vel, diameter, direction):
        super().__init__(x, y, vel)
        self.direction = direction
        self.angle = angle
        self.diameter = diameter
        self.x = x
        self. y = y

    def movement(self):
        self.rect.x = int(math.cos(self.angle) * self.diameter + self.x)
        self.rect.y = int(math.sin(self.angle) * self.diameter + self.y)
        self.angle += self.vel * self.direction / 100
