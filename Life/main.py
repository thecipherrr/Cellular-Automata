import pygame
import sys
import random

dimensions = (400, 400)
black = (0,0,0)
white = (255, 255, 255)

pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill("white")
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
fps = 60

black = (0,0,0)
white = (255, 255, 255)


def makeGrid():
    grid = []
    for row in range(0, dimensions[0]):
        grid.append([])
        for cols in range(0, dimensions[1]):
            grid[row].append(random.randint(0, 1))
    
    return grid

grid = makeGrid()

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    for row in range(0, dimensions[0], 20):
        for cols in range(0, dimensions[1], 20):
            rect = pygame.Rect(row, cols, 20, 20)
            if grid[row][cols] == 1:
                pygame.draw.rect(display, black, rect)
            else:
                pygame.draw.rect(display, black, rect, 1)
    pygame.display.flip()
