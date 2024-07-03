import pygame
import os
import numpy as np
os.environ['SDL_VIDEO_CENTERED'] = '1'

def zerosGrid(width, height):
    arr = [[0]*width]*height

    return arr

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (120, 120, 120)
GREEN = (0, 255, 0)
sandWidth = 10
width, height = 800,800
rows = int(width/sandWidth)
cols = int(height/sandWidth)
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Falling Sand - David Kessler")
grid = np.zeros((rows, cols))

running = True
cont = 0
while running:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            grid[int(x/sandWidth)][int(y/sandWidth)] = 1

    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(window, (grid[i][j]*255, grid[i][j]*255, grid[i][j]*255), (i*sandWidth, j*sandWidth, sandWidth, sandWidth))
            pygame.draw.rect(window, GREY,(i*sandWidth, j*sandWidth, sandWidth , sandWidth), 1)

            
    auxGrid = np.zeros((rows, cols))
    for i in range(cols):
        for j in range(rows):
            if (grid[i][j] == 1):
                if (grid[i][j+1] == 0  and j < rows - 2):
                    auxGrid[i][j+1] = 1
                else:
                    auxGrid[i][j] = 1
            elif (j== rows-1):
                pygame.draw.rect(window, GREEN, (i*sandWidth, j*sandWidth, sandWidth, sandWidth))
                pygame.draw.rect(window, GREY,(i*sandWidth, j*sandWidth, sandWidth , sandWidth), 1)

            
            
    grid = auxGrid

    clock.tick(30)
    pygame.display.update()

pygame.quit()

