import pygame
from setting import *
from widget import Widget
from textviews import Textviews

class CalendarManager:
    def __init__(self):
        textviews = Textviews("August 2023")



        self.month = Widget()
        self.mode = Widget()
        self.tools = Widget()
        self.days = Widget()
    
    def draw(self, surface):
        pass

    def mouseListener(self):
        pass

    def keyboardListener(self):
        pass