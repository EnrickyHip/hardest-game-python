#enemies who movement like a rectangle. inherit from the Enemy class
#ymin, ymax, xmin and xmax delimits the rectangle which the enenmy is gonna movement

from Classes.Objects.Enemy import Enemy

class RectangleEnemy(Enemy):
    def __init__(self, x, y, vel, ymin, ymax, xmin, xmax, direction):
        super().__init__(x, y)
        self.vel = vel
        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin
        self.direction = direction

    def movement(self):
        if self.rect.y >= self.ymax or self.rect.y <= self.ymin:
            self.rect.x += self.vel * self.direction
            if self.rect.x >= self.xmax or self.rect.x <= self.xmin:
                self.vel *= -1
                self.rect.y += self.vel
        else:
            self.rect.y += self.vel
