import pygame
from setting import *

class Textviews:
    def __init__ (self, text = "", font = "", size = 14, color = BLACK, background = WHITE):
        self.text = text
        if (font == ""): 
            self.font = pygame.font.SysFont("Arial", size)
        self.view = self.font.render(text, True, color, background)

    def draw(self, surface):
        surface.blit(self.view, (0,0))