import pygame
from setting import *

class Textviews:
    def __init__ (self, parent, pos , text = "", font = "", sizeText = 14, color = BLACK, background = WHITE):
        # set text
        self.text = text
        if (font == ""): 
            self.font = pygame.font.SysFont("Arial", sizeText)
        self.view = self.font.render(text, True, color, background)
        #set parent
        self.parent = parent
        #set pos
        self.x = self.parent.x + pos[0]
        self.y = self.parent.y + pos[1]



    def draw(self, surface):
        surface.blit(self.view,(self.x,self.y))