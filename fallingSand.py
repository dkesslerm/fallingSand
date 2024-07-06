import pygame
import os
import numpy as np
import random 

# some initial stuff
GREY = (120, 120, 120) # rgb value
SAND_WIDTH = 10 # the width of each "grain" of sand
WIDTH = 800
HEIGHT = 800 # these will be our window dimensions
MAX_FPS = 120
MIN_FPS = 30
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# window config
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand - David Kessler")

# some initial variables
clock = pygame.time.Clock()
rows = int(WIDTH/SAND_WIDTH)
cols = int(HEIGHT/SAND_WIDTH)
fps = 60 # default fps value
running = True
being_dragged = False
paused = False
grid = np.zeros((rows, cols)) # a matrix that is directly initialized to have all its values equal to 0

while running:

    # event loop
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                running = False # we can also quit by pressing the scape key, just a little optimization
                break
            elif (event.key == pygame.K_p):
                paused = True
            elif (event.key == pygame.K_r):
                paused = False
            elif (event.key == pygame.K_DOWN):
                fps = fps - 5
                if fps < MIN_FPS:
                    fps = MIN_FPS
            elif (event.key == pygame.K_UP):
                fps = fps + 5
                if fps > MAX_FPS:
                    fps = MAX_FPS
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            being_dragged = True
        elif (event.type == pygame.MOUSEBUTTONUP):
            being_dragged = False
    
    # we set the value of a square (and the ones around it) to one if we click on it with a 50% chance. this makes it a little more realistic
    if (being_dragged):
        x, y = pygame.mouse.get_pos()
        mouse_col = int(x/SAND_WIDTH)
        mouse_row = int(y/SAND_WIDTH)
        
        extent = [-1, 0, 1] 

        for i in extent:
            for j in extent:
                if (random.random() < 0.5):
                    col = mouse_col + i
                    row = mouse_row + j
                    if (col >= 0 and col <= cols-1 and row >= 0 and row <= rows-1): # we don't want weird stuff happening
                        grid[col][row] = 1       
    
    # here is where we draw the rectangles
    for i in range(cols):
        for j in range(rows):
            rect = pygame.Rect(i*SAND_WIDTH, j*SAND_WIDTH, SAND_WIDTH, SAND_WIDTH)
            
            # automatically draws in white or black depending on the value of the square
            pygame.draw.rect(window, (grid[i][j]*255, grid[i][j]*255, grid[i][j]*255), rect)
            pygame.draw.rect(window, GREY, rect, 1) # completely optional, just think it looks better with a grid
                                                    # on the background. if 
            
    aux_grid = np.zeros((rows, cols)) # auxiliar grid used to reflect the changes from one iteration to other

    # movement of the grains of sand
    if (not paused):
        for i in range(cols):
            for j in range(rows):
                if (grid[i][j] == 1):
                    if (j < rows - 1): # just checking it's not the last row 
                        below = grid[i][j+1]
                        dir = random.choice([-1, 1]) # some kind of randomness to falling left or right
                        below_l = -1
                        below_r = -1
                        if (i-dir >= 0 and i-dir <= cols-1):
                            below_l = grid[i-dir][j+1]
                        if (i+dir >= 0 and i+dir <= cols-1):
                            below_r = grid[i+dir][j+1]

                        if (below == 0):
                            aux_grid[i][j+1] = 1 # make them fall
                        elif (below_l == 0):
                            aux_grid[i-dir][j] = 1 # changeable for aux_grid[i-dir][j+1] = 1 to give it some sort of "slide" effect
                        elif (below_r == 0):
                            aux_grid[i+dir][j] = 1 # i prefer it like this though, it makes the grains of sand "bounce"
                        else:
                            aux_grid[i][j] = 1 # make them stack on each other
                    elif (j == rows - 1): # if it's the last row, no need to check below
                        aux_grid[i][j] = 1

        grid = aux_grid

    clock.tick(fps)
    pygame.display.update()

pygame.quit()

