import pygame
from setting import *
from calendarManager import CalendarManager
from textviews import Textviews


# init pygame & appliction
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(CAPTION)


#declare objects
calendarManager = CalendarManager()

running = True

while running:
    # get user contact
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False

    screen.fill(WHITE)

    # application 
    calendarManager.draw(screen)

    pygame.display.flip()

pygame.quit()


