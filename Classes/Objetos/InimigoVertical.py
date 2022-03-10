from Classes.Objetos.Inimigo import Inimigo

class InimigoVertical(Inimigo):
    def __init__(self, x, y, v, min, max):
        super().__init__(x, y, v)
        self.max = max
        self.min = min

    def movimenta(self):
        if self.rect.y >= self.max or self.rect.y <= self.min:
            self.vel *= -1
        self.rect.y += self.vel