from Classes.Objetos.Inimigo import Inimigo

class InimigoHorizontal(Inimigo):
    def __init__(self, x, y, v, min, max):
        super().__init__(x, y, v)
        self.max = max
        self.min = min

    def movimenta(self):
        if self.rect.x >= self.max or self.rect.x <= self.min:
            self.vel *= -1
        self.rect.x += self.vel