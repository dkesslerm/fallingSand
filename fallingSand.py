import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def zerosMatrix(width, height):
    arr = [[0]*width]*height

    return arr

# Initialize Pygame
pygame.init()

width, height = 800, 800
window = pygame.display.set_mode((width, height))

running = True
while running:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()

pygame.quit()

