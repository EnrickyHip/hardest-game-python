import pygame

class Text:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('verdana', 28)
        self.screen = screen

    def show_deaths(self, deaths):
        text = self.font.render('Deaths: ' + str(deaths), True, (255, 255, 255))
        self.screen.blit(text, (10,-2))
