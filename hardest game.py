import pygame
import math


class jogo:
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
        p1 = retangulo(71, 353, 101, 195)
        p2 = retangulo(4, 70, 97, 124)
        p3 = retangulo(71, 35, 101, 89)
        p4 = retangulo(459, 4, 172, 85)
        p5 = retangulo(70, 353, 631, 89)
        p6 = retangulo(70, 35, 631, 513)
        p7 = retangulo(459, 4, 172, 548)

        e1 = self.movimentovertical(180, 97, 5, 89, 530, 7, 71)
        e2 = self.movimentohorizontal(180, 97, 5, 172, 613, 7, 71)

        f = retangulo(4, 71, 630, 442)

        paredes = [p1, p2, p3, p4, p5, p6, p7]
        inimigos = []
        for e in e1, e2:
            inimigos.append(e)
        c = []

        n1 = nivel(self.screen, c, pygame.image.load('level/level1.png'), 125, 147, paredes, self, inimigos, f)
        self.niveis.append(n1)

        p1 = retangulo(68, 32, 171, 351)
        p2 = retangulo(4, 68, 167, 283)
        p3 = retangulo(68, 32, 171, 251)
        p4 = retangulo(332, 4, 239, 247)
        p5 = retangulo(4, 68, 639, 283)
        p6 = retangulo(68, 32, 571, 351)
        p7 = retangulo(332, 4, 239, 383)
        p8 = retangulo(68, 32, 571, 251)

        e1 = self.movimentovertical(247, 259, 3, 251, 365, 5, 66)
        e2 = self.movimentovertical(278, 360, -3, 251, 365, 5, 67)

        c1 = coin(396, 308)

        paredes = [p1, p2, p3, p4, p5, p6, p7, p8]
        inimigos = []
        for e in e1, e2:
            inimigos.append(e)

        f = retangulo(4, 68, 571, 283)
        c=[c1]

        n2 = nivel(self.screen, c, pygame.image.load('level/level2.png'), 193, 306, paredes, self, inimigos, f)
        self.niveis.append(n2)

        p1 = retangulo(288, 128, 308, 383)
        p2 = retangulo(4, 256, 596, 127)
        p3 = retangulo(288, 128, 212, 127)
        p4 = retangulo(4, 260, 208, 255)
        p5 = retangulo(96, 4, 212, 511)
        p6 = retangulo(96, 4, 500, 123)

        e1 = self.movimentohorizontal(219, 390, 3, 212, 290, 1, 0)
        e2 = self.movimentohorizontal(571, 198, -3, 500, 578, 1, 0)
        e3 = self.movimentohorizontal(219, 262, 6, 212, 578, 2, 32)
        e4 = self.movimentohorizontal(571, 326, -6, 212, 578, 2, 32)

        c1 = coin(219, 262)
        c2 = coin(571, 358)

        paredes = [p1, p2, p3, p4, p5, p6]
        inimigos = []
        for e in e1, e2, e3, e4:
            inimigos.append(e)
        f = retangulo(96, 4, 500, 187)
        c = [c1, c2]

        n3 = nivel(self.screen, c, pygame.image.load('level/level3.png'), 248, 468, paredes, self,  inimigos, f)
        self.niveis.append(n3)

        p1 = retangulo(66, 66, 171, 216)
        p2 = retangulo(397, 4, 237, 212)
        p3 = retangulo(4, 198, 634, 216)
        p4 = retangulo(397, 4, 237, 414)
        p5 = retangulo(66, 66, 171, 348)
        p6 = retangulo(4, 66, 167, 282)

        e1 = self.movimentocircular(328, 306, 0, 3.6, 80, 1, 1, 11)
        e2 = self.movimentocircular(328, 306, 1.57, 3.6, 80, 1, 1, 11)
        e3 = self.movimentocircular(526, 306, 0, 3.6, 80, -1, 1, 11)
        e4 = self.movimentocircular(526, 306, 1.57, 3.6, 80, -1, 1, 11)

        c1 = coin(609, 389)
        c2 = coin(609, 223)
        c3 = coin(427, 223)
        c4 = coin(427, 389)
        c5 = coin(245, 223)
        c6 = coin(245, 389)

        paredes = [p1, p2, p3, p4, p5, p6]
        inimigos = []
        for i in e1, e2, e3, e4:
            inimigos.append(i)
        f = retangulo(4, 66, 233, 282)
        c = [c1, c2, c3, c4, c5, c6]

        n4 = nivel(self.screen, c, pygame.image.load('level/level4.png'), 191, 303, paredes, self, inimigos, f)
        self.niveis.append(n4)

        p1 = retangulo(4, 64, 134, 276)
        p2 = retangulo(64, 160, 138, 116)
        p3 = retangulo(224, 4, 202, 112)
        p4 = retangulo(96, 352, 426, 116)
        p5 = retangulo(128, 4, 522, 272)
        p6 = retangulo(4, 64, 650, 276)
        p7 = retangulo(64, 192, 586, 340)
        p8 = retangulo(224, 4, 362, 532)
        p9 = retangulo(96, 352, 266, 180)
        p10 = retangulo(128, 4, 138, 340)

        e1 = inimigovertical(209, 123, 3,  122, 316)
        e2 = inimigovertical(241, 316, -3, 123, 317)
        e3 = inimigo(275, 123, 0)
        e4 = inimigo(335, 155, 0)
        e5 = inimigo(369, 187, 0)
        e6 = inimigo(401, 251, 0)
        e7 = inimigo(369, 316, 0)
        e8 = inimigo(401, 379, 0)
        e9 = inimigo(369, 444, 0)
        e10 = inimigovertical(369, 123, 3, 122, 508)
        e11 = inimigovertical(401, 508, -3, 123, 509)
        e12 = inimigo(433, 475, 0)
        e13 = inimigo(496, 507, 0)
        e14 = inimigovertical(529, 283, 4, 282, 508)
        e15 = inimigovertical(561, 508, -4, 283, 509)


        paredes = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
        f = retangulo(4, 64, 586, 276)
        c = []

        n5= nivel(self.screen, c, pygame.image.load('level/level5.png'), 157, 297, paredes, self, inimigos, f)
        self.niveis.append(n5)

        p1 = retangulo(100, 231, 336, 249)
        p2 = retangulo(166, 267, 303, 480)
        p3 = retangulo(33, 67, 204, 480)
        p4 = retangulo(33, 67, 535, 480)
        p5 = retangulo(4, 364, 568, 116)
        p6 = retangulo(364, 4, 204, 112)
        p7 = retangulo(4, 364, 200, 116)
        p8 = retangulo(298, 4, 237, 547)

        e1 = inimigoretangulo(213, 125, 3, 124, 223, 212, 310, 1)
        e2 = inimigoretangulo(309, 221, -3, 124, 223, 212, 310, 1)
        e3 = inimigoretangulo(445, 125, 3, 124, 223, 444, 542, 1)
        e4 = inimigoretangulo(541, 221, -3, 124, 223, 444, 542, 1)
        e5 = inimigovertical(344, 123, 3, 122, 224)
        e6 = inimigovertical(411, 224, -3, 123, 225)
        e7 = inimigohorizontal(211, 257, 3, 210, 312)
        e8 = inimigohorizontal(444, 257, 3, 443, 545)

        c1 = coin(244, 157)
        c2 = coin(277, 157)
        c3 = coin(244, 192)
        c4 = coin(277, 192)
        c5 = coin(477, 157)
        c6 = coin(510, 157)
        c7 = coin(477, 192)
        c8 = coin(510, 192)

        paredes = [p1, p2, p3, p4, p5, p6, p7, p8]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8]
        f = retangulo(66, 4, 469, 480)
        c = [c1, c2, c3, c4, c5, c6, c7, c8]

        n6 = nivel(self.screen, c, pygame.image.load('level/level6.png'), 257, 501, paredes, self, inimigos, f)
        self.niveis.append(n6)

        p1 = retangulo(66, 99, 534, 367)
        p2 = retangulo(66, 99, 534, 201)
        p3 = retangulo(265, 4, 269, 197)
        p4 = retangulo(66, 99, 203, 201)
        p5 = retangulo(4, 67, 199, 300)
        p6 = retangulo(66, 99, 203, 367)
        p7 = retangulo(265, 4, 269, 466)

        e1 = inimigovertical(376, 209, 3, 208, 440)
        e2 = inimigovertical(409, 439, 3, 208, 440)
        e3 = self.movimentohorizontal(277, 209, 3, 276, 508, 4, 66)
        e4 = self.movimentohorizontal(507, 241, 3, 276, 508, 4, 66)

        paredes = [p1, p2, p3, p4, p5, p6, p7]
        inimigos = []
        for e in e1, e2, e3, e4:
            inimigos.append(e)
        c = []
        f = retangulo(4, 67, 534, 300)

        n7 = nivel(self.screen, c, pygame.image.load('level/level7.png'), 224, 322, paredes, self, inimigos, f)
        self.niveis.append(n7)

        p1 = retangulo(265, 4, 269, 197)
        p2 = retangulo(265, 4, 269, 466)
        p3 = retangulo(4, 265, 265, 193)
        p4 = retangulo(4, 265, 534, 201)

        e1 = inimigo(343, 275, 0)
        e2 = inimigo(310, 275, 0)
        e3 = inimigo(343, 241, 0)
        e4 = inimigo(343, 375, 0)
        e5 = inimigo(310, 375, 0)
        e6 = inimigo(343, 408, 0)
        e7 = inimigo(443, 375, 0)
        e8 = inimigo(443, 408, 0)
        e9 = inimigo(476, 375, 0)
        e10 = inimigo(476, 275, 0)
        e11 = inimigo(443, 275, 0)
        e12 = inimigo(443, 241, 0)
        e13 = inimigoretangulo(343, 275, 3, 274, 374, 342, 443, 1)
        e14 = inimigoretangulo(310, 241, 4, 240, 407, 309, 476, 1)
        e15 = inimigoretangulo(276, 208, 5, 207, 440, 275, 509, 1)

        c1 = coin(476, 407)
        c2 = coin(309, 407)
        c3 = coin(309, 241)
        c4 = coin(476, 241)

        paredes = [p1, p2, p3, p4]
        inimigos = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]
        f = retangulo(67, 67, 368, 300)
        c = [c1, c2, c3, c4]

        n8 = nivel(self.screen, c, pygame.image.load('level/level8.png'), 388, 321, paredes, self, inimigos, f)
        self.niveis.append(n8)

        self.texto = texto(self.screen)
        self.laço()

    def movimentocircular(self, x, y, angle, vel, dia, dir, s, qua):
        inimigos = []
        for e in range(qua):
            e = inimigocircular(x, y, angle, vel, dia * s, dir)
            inimigos.append(e)
            dia -= 16
        return inimigos

    def movimentovertical(self, x, y, vel, ymin, ymax, qua, s):
        inimigos = []
        for e in range(qua):
            e = inimigovertical(x, y, vel, ymin, ymax)
            inimigos.append(e)
            x += s
        return inimigos

    def movimentohorizontal(self, x, y, vel, xmin, xmax, qua, s):
        inimigos = []
        for e in range(qua):
            e = inimigohorizontal(x, y, vel, xmin, xmax)
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

class retangulo(pygame.sprite.Sprite):
    def __init__(self, l, a, x, y,):
        super().__init__()
        self.image = pygame.Surface([l, a])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((0, 0, 0))


class fundo:

    def __init__(self, f, s):
        self.iFundo = f
        self.screen = s

    def desenha(self):
        self.screen.blit(self.iFundo, (0, 0))

class nivel:
    def __init__(self, s, c, b, xq, yq, p, j, e, f):
        self.screen = s
        self.backgorund = b
        self.jogo = j
        self.spawnx = xq
        self.spawny = yq
        self.final = f
        self.active_sprite_list = pygame.sprite.Group()

        self.info = retangulo(800, 36, 0, 0)
        self.active_sprite_list.add(self.info)

        self.fundo = fundo(self.backgorund, self.screen)
        self.quad = quad(self, xq, yq)
        self.active_sprite_list.add(self.quad)

        self.paredes = pygame.sprite.Group()
        self.retangulos = pygame.sprite.Group()
        self.inimigos = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.tcoins = len(c)
        self.ncoins = self.tcoins

        for i in p:
            self.paredes.add(i)

        for i in e:
            self.inimigos.add(i)
            self.active_sprite_list.add(i)
        for i in c:
            self.coins.add(i)
            self.active_sprite_list.add(i)

    def desenha(self):
        self.fundo.desenha()
        self.quad.movimenta(self)
        self.active_sprite_list.draw(self.screen)


        for i in self.inimigos:
            i.movimenta()

        if not self.jogo.vivo:
            self.morte()


    def testacolisao(self, x, y):
        if self.jogo.vivo:
            self.quad.rect.x += x
            self.quad.rect.y += y
        self.quad.image.set_alpha(self.quad.alpha)

        lista_paredes = pygame.sprite.spritecollide(self.quad, self.paredes, False) # colisão de paredes
        for parede in lista_paredes:
            if x > 0:
                self.quad.rect.right = parede.rect.left
            elif x < 0:
                self.quad.rect.left = parede.rect.right
            elif y < 0:
                self.quad.rect.top = parede.rect.bottom
            elif y > 0:
                self.quad.rect.bottom = parede.rect.top

        lista_inimigos = pygame.sprite.spritecollide(self.quad, self.inimigos, False) # colisão de inimigos
        if lista_inimigos:
            self.jogo.vivo = False


        if self.quad.rect.colliderect(self.final.rect) and self.ncoins == 0:
            self.jogo.natual += 1
            self.jogo.active_sprite_list = pygame.sprite.Group()

        lista_coins = pygame.sprite.spritecollide(self.quad, self.coins, False) # colisao de moedas
        for c in lista_coins:
            if c in self.active_sprite_list:
                self.active_sprite_list.remove(c)
                self.ncoins -= 1

    def morte(self):
        if self.quad.alpha > 0:
            self.quad.alpha -= 7
        else:
            self.quad.alpha = 255
            self.jogo.vivo = True
            self.quad.rect.x = self.spawnx
            self.quad.rect.y = self.spawny
            self.jogo.mortes += 1
            for c in self.coins:
                self.active_sprite_list.add(c)
                self.ncoins = self.tcoins


class texto:
    def __init__(self,s):
        self.placar_fonte = pygame.font.SysFont('verdana', 28)
        self.screen = s

    def mostra_mortes(self, mortes):
        txt_placar = self.placar_fonte.render('Mortes: ' + str(mortes), True, (255, 255, 255))
        self.screen.blit(txt_placar, (10,-2))



class quad(pygame.sprite.Sprite):
    def __init__(self, j,  x, y):
        super().__init__()
        self.image = pygame.image.load('img/quad.png')
        self.jogo = j
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alpha = 255

    def movimenta(self, niv):
        niv.testacolisao(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            niv.testacolisao(0, -2)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            niv.testacolisao(0, 2)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            niv.testacolisao(-2, 0)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            niv.testacolisao(2, 0)

class inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y, v):
        super().__init__()
        self.image = pygame.image.load('img/ball.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = v

    def movimenta(self):
        self.rect = self.rect


class inimigovertical(inimigo):
    def __init__(self, x, y, v, min, max):
        super().__init__(x, y, v)
        self.max = max
        self.min = min

    def movimenta(self):
        if self.rect.y >= self.max or self.rect.y <= self.min:
            self.vel *= -1
        self.rect.y += self.vel

class inimigohorizontal(inimigo):
    def __init__(self, x, y, v, min, max):
        super().__init__(x, y, v)
        self.max = max
        self.min = min

    def movimenta(self):
        if self.rect.x >= self.max or self.rect.x <= self.min:
            self.vel *= -1
        self.rect.x += self.vel

class inimigoretangulo(inimigo):
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

class inimigocircular(inimigo):
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


class coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/coin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




if __name__ == "__main__":
    j = jogo()