import pygame
import os
import numpy as np
os.environ['SDL_VIDEO_CENTERED'] = '1'

def zerosGrid(width, height):
    arr = [[0]*width]*height

    return arr

# Initialize Pygame
pygame.init()

WHITE = (255, 255, 255)
sandWidth = 10
width, height = 800, 800
rows = int(width/sandWidth)
cols = int(height/sandWidth)
window = pygame.display.set_mode((width, height))
grid = np.zeros((rows, cols))

running = True
while running:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            grid[int(x/sandWidth)][int(y/sandWidth)] = 1
    
    for i in range(rows):
        for j in range(cols):
            pygame.draw.rect(window, WHITE,(i*sandWidth, j*sandWidth, sandWidth , sandWidth), 1)

            if(grid[i][j] == 1):
                pygame.draw.rect(window, WHITE, (i*sandWidth, j*sandWidth, 10 , 10))

    # (grid[i][j]*255,grid[i][j]*255,grid[i][j]*255)
    # auxGrid = zerosGrid(width, height)
    # for i in range(rows):
    #     for j in range(cols):
    #         if (grid[i][j] == 1):
    #             if (grid[i][j+1] == 0):
    #                 auxGrid[i][j] = 0
    #                 auxGrid[i][j+1] = 1


    # grid = auxGrid

    pygame.display.update()

pygame.quit()

