import pygame
from Classes.Jogo.Retangulo import Retangulo
from Classes.Jogo.Nivel import Nivel
from Classes.Jogo.Texto import Texto
from Classes.Objetos.Coin import Coin
from Classes.Objetos.Inimigo import Inimigo
from Classes.Objetos.InimigoVertical import InimigoVertical
from Classes.Objetos.InimigoHorizontal import InimigoHorizontal
from Classes.Objetos.InimigoCircular import InimigoCircular
from Classes.Objetos.InimigoRetangulo import InimigoRetangulo

class Jogo:
    def __init__(self):
        self.jogando = True
        self.vivo = True
        self.mortes = 0
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("O Jogo Mais Difícil do Mundo")
        icon = pygame.image.load('img/quad.png')
        pygame.display.set_icon(icon)

        self.niveis = []
        self.natual = 0
        self.crianivel()

    def crianivel(self):
        p1 = Retangulo(71, 353, 101, 195)
        p2 = Retangulo(4, 70, 97, 124)
        p3 = Retangulo(71, 35, 101, 89)
        p4 = Retangulo(459, 4, 172, 85)
        p5 = Retangulo(70, 353, 631, 89)
        p6 = Retangulo(70, 35, 631, 513)
        p7 = Retangulo(459, 4, 172, 548)

        e1 = self.movimentovertical(180, 97, 5, 89, 530, 7, 71)
        e2 = self.movimentohorizontal(180, 97, 5, 172, 613, 7, 71)

        f = Retangulo(4, 71, 630, 442)

        paredes = [p1, p2, p3, p4, p5, p6, p7]
        inimigos = []
        for e in e1, e2:
            inimigos.append(e)
        c = []

        n1 = Nivel(self.screen, c, pygame.image.load('level/level1.png'), 125, 147, paredes, self, inimigos, f)
        self.niveis.append(n1)

        p1 = Retangulo(68, 32, 171, 351)
        p2 = Retangulo(4, 68, 167, 283)
        p3 = Retangulo(68, 32, 171, 251)
        p4 = Retangulo(332, 4, 239, 247)
        p5 = Retangulo(4, 68, 639, 283)
        p6 = Retangulo(68, 32, 571, 351)
        p7 = Retangulo(332, 4, 239, 383)
        p8 = Retangulo(68, 32, 571, 251)

        e1 = self.movimentovertical(247, 259, 3, 251, 365, 5, 66)
        e2 = self.movimentovertical(278, 360, -3, 251, 365, 5, 67)

        c1 = Coin(396, 308)

        paredes = [p1, p2, p3, p4, p5, p6, p7, p8]
        inimigos = []
        for e in e1, e2:
            inimigos.append(e)

        f = Retangulo(4, 68, 571, 283)
        c=[c1]

        n2 = Nivel(self.screen, c, pygame.image.load('level/level2.png'), 193, 306, paredes, self, inimigos, f)
        self.niveis.append(n2)

        p1 = Retangulo(288, 128, 308, 383)
        p2 = Retangulo(4, 256, 596, 127)
        p3 = Retangulo(288, 128, 212, 127)
        p4 = Retangulo(4, 260, 208, 255)
        p5 = Retangulo(96, 4, 212, 511)
        p6 = Retangulo(96, 4, 500, 123)

        e1 = self.movimentohorizontal(219, 390, 3, 212, 290, 1, 0)
        e2 = self.movimentohorizontal(571, 198, -3, 500, 578, 1, 0)
        e3 = self.movimentohorizontal(219, 262, 6, 212, 578, 2, 32)
        e4 = self.movimentohorizontal(571, 326, -6, 212, 578, 2, 32)

        c1 = Coin(219, 262)
        c2 = Coin(571, 358)

        paredes = [p1, p2, p3, p4, p5, p6]
        inimigos = []
        for e in e1, e2, e3, e4:
            inimigos.append(e)
        f = Retangulo(96, 4, 500, 187)
        c = [c1, c2]

        n3 = Nivel(self.screen, c, pygame.image.load('level/level3.png'), 248, 468, paredes, self,  inimigos, f)
        self.niveis.append(n3)

        p1 = Retangulo(66, 66, 171, 216)
        p2 = Retangulo(397, 4, 237, 212)
        p3 = Retangulo(4, 198, 634, 216)
        p4 = Retangulo(397, 4, 237, 414)
        p5 = Retangulo(66, 66, 171, 348)
        p6 = Retangulo(4, 66, 167, 282)

        e1 = self.movimentocircular(328, 306, 0, 3.6, 80, 1, 1, 11)
        e2 = self.movimentocircular(328, 306, 1.57, 3.6, 80, 1, 1, 11)
        e3 = self.movimentocircular(526, 306, 0, 3.6, 80, -1, 1, 11)
        e4 = self.movimentocircular(526, 306, 1.57, 3.6, 80, -1, 1, 11)

        c1 = Coin(609, 389)
        c2 = Coin(609, 223)
        c3 = Coin(427, 223)
        c4 = Coin(427, 389)
        c5 = Coin(245, 223)
        c6 = Coin(245, 389)

        paredes = [p1, p2, p3, p4, p5, p6]
        inimigos = []
        for i in e1, e2, e3, e4:
            inimigos.append(i)
        f = Retangulo(4, 66, 233, 282)
        c = [c1, c2, c3, c4, c5, c6]

        n4 = Nivel(self.screen, c, pygame.image.load('level/level4.png'), 191, 303, paredes, self, inimigos, f)
        self.niveis.append(n4)

        p1 = Retangulo(4, 64, 134, 276)
        p2 = Retangulo(64, 160, 138, 116)
        p3 = Retangulo(224, 4, 202, 112)
        p4 = Retangulo(96, 352, 426, 116)
        p5 = Retangulo(128, 4, 522, 272)
        p6 = Retangulo(4, 64, 650, 276)
        p7 = Retangulo(64, 192, 586, 340)
        p8 = Retangulo(224, 4, 362, 532)
        p9 = Retangulo(96, 352, 266, 180)
        p10 = Retangulo(128, 4, 138, 340)

        e1 = InimigoVertical(209, 123, 3,  122, 316)
        e2 = InimigoVertical(241, 316, -3, 123, 317)
        e3 = Inimigo(275, 123, 0)
        e4 = Inimigo(335, 155, 0)
        e5 = Inimigo(369, 187, 0)
        e6 = Inimigo(401, 251, 0)
        e7 = Inimigo(369, 316, 0)
        e8 = Inimigo(401, 379, 0)
        e9 = Inimigo(369, 444, 0)
        e10 = InimigoVertical(369, 123, 3, 122, 508)
        e11 = InimigoVertical(401, 508, -3, 123, 509)
        e12 = Inimigo(433, 475, 0)
        e13 = Inimigo(496, 507, 0)
        e14 = InimigoVertical(529, 283, 4, 282, 508)
        e15 = InimigoVertical(561, 508, -4, 283, 509)


        paredes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
        f = Retangulo(4, 64, 586, 276)
        c = []

        n5 = Nivel(self.screen, c, pygame.image.load('level/level5.png'), 157, 297, paredes, self, inimigos, f)
        self.niveis.append(n5)

        p1 = Retangulo(100, 231, 336, 249)
        p2 = Retangulo(166, 267, 303, 480)
        p3 = Retangulo(33, 67, 204, 480)
        p4 = Retangulo(33, 67, 535, 480)
        p5 = Retangulo(4, 364, 568, 116)
        p6 = Retangulo(364, 4, 204, 112)
        p7 = Retangulo(4, 364, 200, 116)
        p8 = Retangulo(298, 4, 237, 547)

        e1 = InimigoRetangulo(213, 125, 3, 124, 223, 212, 310, 1)
        e2 = InimigoRetangulo(309, 221, -3, 124, 223, 212, 310, 1)
        e3 = InimigoRetangulo(445, 125, 3, 124, 223, 444, 542, 1)
        e4 = InimigoRetangulo(541, 221, -3, 124, 223, 444, 542, 1)
        e5 = InimigoVertical(344, 123, 3, 122, 224)
        e6 = InimigoVertical(411, 224, -3, 123, 225)
        e7 = InimigoHorizontal(211, 257, 3, 210, 312)
        e8 = InimigoHorizontal(444, 257, 3, 443, 545)

        c1 = Coin(244, 157)
        c2 = Coin(277, 157)
        c3 = Coin(244, 192)
        c4 = Coin(277, 192)
        c5 = Coin(477, 157)
        c6 = Coin(510, 157)
        c7 = Coin(477, 192)
        c8 = Coin(510, 192)

        paredes = [p1, p2, p3, p4, p5, p6, p7, p8]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8]
        f = Retangulo(66, 4, 469, 480)
        c = [c1, c2, c3, c4, c5, c6, c7, c8]

        n6 = Nivel(self.screen, c, pygame.image.load('level/level6.png'), 257, 501, paredes, self, inimigos, f)
        self.niveis.append(n6)

        p1 = Retangulo(66, 99, 534, 367)
        p2 = Retangulo(66, 99, 534, 201)
        p3 = Retangulo(265, 4, 269, 197)
        p4 = Retangulo(66, 99, 203, 201)
        p5 = Retangulo(4, 67, 199, 300)
        p6 = Retangulo(66, 99, 203, 367)
        p7 = Retangulo(265, 4, 269, 466)

        e1 = InimigoVertical(376, 209, 3, 208, 440)
        e2 = InimigoVertical(409, 439, 3, 208, 440)
        e3 = self.movimentohorizontal(277, 209, 3, 276, 508, 4, 66)
        e4 = self.movimentohorizontal(507, 241, 3, 276, 508, 4, 66)

        paredes = [p1, p2, p3, p4, p5, p6, p7]
        inimigos = []
        for e in e1, e2, e3, e4:
            inimigos.append(e)
        c = []
        f = Retangulo(4, 67, 534, 300)

        n7 = Nivel(self.screen, c, pygame.image.load('level/level7.png'), 224, 322, paredes, self, inimigos, f)
        self.niveis.append(n7)

        p1 = Retangulo(265, 4, 269, 197)
        p2 = Retangulo(265, 4, 269, 466)
        p3 = Retangulo(4, 265, 265, 193)
        p4 = Retangulo(4, 265, 534, 201)

        e1 = Inimigo(343, 275, 0)
        e2 = Inimigo(310, 275, 0)
        e3 = Inimigo(343, 241, 0)
        e4 = Inimigo(343, 375, 0)
        e5 = Inimigo(310, 375, 0)
        e6 = Inimigo(343, 408, 0)
        e7 = Inimigo(443, 375, 0)
        e8 = Inimigo(443, 408, 0)
        e9 = Inimigo(476, 375, 0)
        e10 = Inimigo(476, 275, 0)
        e11 = Inimigo(443, 275, 0)
        e12 = Inimigo(443, 241, 0)
        e13 = InimigoRetangulo(343, 275, 3, 274, 374, 342, 443, 1)
        e14 = InimigoRetangulo(310, 241, 4, 240, 407, 309, 476, 1)
        e15 = InimigoRetangulo(276, 208, 5, 207, 440, 275, 509, 1)

        c1 = Coin(476, 407)
        c2 = Coin(309, 407)
        c3 = Coin(309, 241)
        c4 = Coin(476, 241)

        paredes = [p1, p2, p3, p4]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
        f = Retangulo(67, 67, 368, 300)
        c = [c1, c2, c3, c4]

        n8 = Nivel(self.screen, c, pygame.image.load('level/level8.png'), 388, 321, paredes, self, inimigos, f)
        self.niveis.append(n8)

        self.texto = Texto(self.screen)
        self.laço()

    def movimentocircular(self, x, y, angle, vel, dia, dir, s, qua):
        inimigos = []
        for e in range(qua):
            e = InimigoCircular(x, y, angle, vel, dia * s, dir)
            inimigos.append(e)
            dia -= 16
        return inimigos

    def movimentovertical(self, x, y, vel, ymin, ymax, qua, s):
        inimigos = []
        for e in range(qua):
            e = InimigoVertical(x, y, vel, ymin, ymax)
            inimigos.append(e)
            x += s
        return inimigos

    def movimentohorizontal(self, x, y, vel, xmin, xmax, qua, s):
        inimigos = []
        for e in range(qua):
            e = InimigoHorizontal(x, y, vel, xmin, xmax)
            inimigos.append(e)
            y += s
        return inimigos

    def laço(self):
        clock = pygame.time.Clock()
        janela = True

        while janela:
            clock.tick(60)

            niv = self.niveis[self.natual]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela = False

            if self.jogando:
                niv.desenha()

            self.texto.mostra_mortes(self.mortes)
            pygame.display.update()
        pygame.quit()