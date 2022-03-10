import pygame
from Classes.Jogo.Retangulo import Retangulo
from Classes.Jogo.Fundo import Fundo
from Classes.Objetos.Player import Player


class Nivel:
    def __init__(self, s, c, b, xq, yq, p, j, e, f):
        self.screen = s
        self.backgorund = b
        self.jogo = j
        self.spawnx = xq
        self.spawny = yq
        self.final = f
        self.active_sprite_list = pygame.sprite.Group()

        self.info = Retangulo(800, 36, 0, 0)
        self.active_sprite_list.add(self.info)

        self.fundo = Fundo(self.backgorund, self.screen)
        self.quad = Player(self, xq, yq)
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

