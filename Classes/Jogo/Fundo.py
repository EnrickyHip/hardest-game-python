class Fundo:

    def __init__(self, f, s):
        self.iFundo = f
        self.screen = s

    def desenha(self):
        self.screen.blit(self.iFundo, (0, 0))