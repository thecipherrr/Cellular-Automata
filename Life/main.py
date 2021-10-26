import pygame
import sys
import random 

width = 400
height = 400
size = 20

def makeGrid():
    grid = []
    for row in range(width):
        grid.append([])
        for cols in range(height):
            grid[row].append(random.randint(0, 1))
    return grid

def drawGrid(grid):
    size = 20

    pygame.init()
    display = pygame.display.set_mode((width, height))
    display.fill("white")

    for row in range(0, width, size):
        for cols in range(0, height, size):
            color = "white"
            if grid[row][cols] == 1:
                color = "black"
            rect = pygame.Rect(row, cols, size, size)
            pygame.draw.rect(display, color, rect)
            pygame.display.update()

def main():
    grid = makeGrid()
    drawGrid(grid)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()