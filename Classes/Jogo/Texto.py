import pygame

class Texto:
    def __init__(self,s):
        self.placar_fonte = pygame.font.SysFont('verdana', 28)
        self.screen = s

    def mostra_mortes(self, mortes):
        txt_placar = self.placar_fonte.render('Mortes: ' + str(mortes), True, (255, 255, 255))
        self.screen.blit(txt_placar, (10,-2))