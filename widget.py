import pygame
from setting import *

class Widget:
    def __init__ (self, parent, pos, size, align = 0):
        #set parent
        self.parent = parent
        #set pos
        self.w = size[0]
        self.h = size[1]
        match align:
            case 0:
                self.x = self.parent.x + pos[0]
                self.y = self.parent.y + pos[1]
            case 1:
                self.x = self.parent.x + (self.parent.w - self.w) // 2
                self.y = self.parent.y + pos[1] 
        # setrestore
        self.buttons = []
        self.textviews = []

    def draw(self, surface):
        #draw background
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.w, self.h))
        #draw subview
        for button in self.buttons:
            button.draw(surface)
        for textview in self.textviews:
            textview.draw(surface)
