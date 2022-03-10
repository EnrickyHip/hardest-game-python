from Classes.Objetos.Inimigo import Inimigo
import math

class InimigoCircular(Inimigo):
    def __init__(self, x, y, a, v, dia, dir):
        super().__init__(x, y, v)
        self.d = dir
        self.angle = a
        self.diametro = dia
        self.x = x
        self. y = y

    def movimenta(self):
        self.rect.x = int(math.cos(self.angle) * self.diametro + self.x)
        self.rect.y = int(math.sin(self.angle) * self.diametro + self.y)
        self.angle += self.vel * self.d / 100