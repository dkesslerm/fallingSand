import pygame
import os
import numpy as np
import random 

os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

GREY = (120, 120, 120)

sandWidth = 10
width, height = 800,800
rows = int(width/sandWidth)
cols = int(height/sandWidth)
window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Falling Sand - David Kessler")
grid = np.zeros((rows, cols))

running = True
beingDragged = False
while running:
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            beingDragged = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            beingDragged = False

    if (beingDragged):
        x, y = pygame.mouse.get_pos()
        mouseCol = int(x/sandWidth)
        mouseRow = int(y/sandWidth)
        
        extent = [-1, 0, 1]

        for i in extent:
            for j in extent:
                if (random.random() < 0.5):
                    col = mouseCol + i
                    row = mouseRow + j
                    if (col >= 0 and col <= cols-1 and row >= 0 and row <= rows-1):
                        grid[col][row] = 1       
    
    for i in range(cols):
        for j in range(rows):
            pygame.draw.rect(window, (grid[i][j]*255, grid[i][j]*255, grid[i][j]*255), (i*sandWidth, j*sandWidth, sandWidth, sandWidth))
            pygame.draw.rect(window, GREY,(i*sandWidth, j*sandWidth, sandWidth , sandWidth), 1)

            
    auxGrid = np.zeros((rows, cols))
    for i in range(cols):
        for j in range(rows):
            if (grid[i][j] > 0):
                if (j < rows - 1):
                    below = grid[i][j+1]
                    dir = random.choice([-1, 1])
                    belowL = grid[i][j+1]
                    belowR = grid[i][j+1]
                    if (i-dir >= 0 and i-dir < cols-1):
                        belowL = grid[i-dir][j+1]
                    if (i+dir >= 0 and i+dir < cols-1):
                        belowR = grid[i+dir][j+1]

                    if (below == 0):
                        auxGrid[i][j+1] = 1
                    elif (belowL == 0):
                        auxGrid[i-dir][j] = 1
                    elif (belowR == 0):
                        auxGrid[i+dir][j] = 1
                    else:
                        auxGrid[i][j] = 1
                elif (j == rows - 1):
                    auxGrid[i][j] = 1

    grid = auxGrid

    clock.tick(45)
    pygame.display.update()

pygame.quit()

