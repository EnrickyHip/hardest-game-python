from Classes.Objetos.Inimigo import Inimigo

class InimigoRetangulo(Inimigo):
    def __init__(self, x, y, v, ymin, ymax, xmin, xmax, dir):
        super().__init__(x, y, v)
        self.xmax = xmax
        self.xmin = xmin
        self.ymax = ymax
        self.ymin = ymin
        self.direcao = dir

    def movimenta(self):
        if self.rect.y >= self.ymax or self.rect.y <= self.ymin:
            self.rect.x += self.vel*self.direcao
            if self.rect.x >= self.xmax or self.rect.x <= self.xmin:
                self.vel *= -1
                self.rect.y += self.vel
        else:
            self.rect.y += self.vel