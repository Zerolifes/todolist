import pygame
from setting import *
from widget import Widget
from textviews import Textviews
from buttons import Buttons

class CalendarManager:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.w = WINDOW_WIDTH - self.x*2 
        self.h = WINDOW_HEIGHT - self.y*2

        self.month = Textviews(self, [20,20], "August 2023", sizeText=20, background=SILVER)

        self.mode = Widget(self,[0,20], [100,20], align=1)
        weekButton = Buttons(self.mode, [0,0], [self.mode.w // 2, self.mode.h],background=SILVER)
        monthButton = Buttons(self.mode, [self.mode.w // 2 , 0], [self.mode.w // 2, self.mode.h])
        self.mode.buttons.append(weekButton)
        self.mode.buttons.append(monthButton)
        # self.tools = Widget()
        # self.days = Widget()
    
    def draw(self, surface):
        #draw background
        pygame.draw.rect(surface,SILVER,(self.x,self.y,self.w,self.h),border_radius=10)
        #draw month
        self.month.draw(surface)
        #draw mode
        self.mode.draw(surface)

    def mouseListener(self):
        pass

    def keyboardListener(self):
        pass