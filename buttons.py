import pygame
from setting import *

class Buttons:
    def __init__ (self, parent, pos, size, text = "", font = "", sizeText = 14, color = BLACK, background = WHITE):
        #set view
        self.background = background
        self.default = background
        # set parent
        self.parent = parent
        # set pos
        self.x = self.parent.x + pos[0] 
        self.y = self.parent.y + pos[1]
        self.w = size[0]
        self.h = size[1]
    
    def draw(self, surface):
        #listen user
        self.mouseListener()
        #draw background
        pygame.draw.rect(surface, self.background , (self.x ,self.y, self.w, self.h))

    def mouseListener(self):
        [x,y] = pygame.mouse.get_pos()
        if (self.x <= x and x <= self.x + self.w and self.y <= y and y<= self.y + self.h):
            self.background = BLACK
        else: self.background = self.default 