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
    size = 10

    pygame.init()
    display = pygame.display.set_mode((width, height))
    display.fill("white")

    for row in range(0, width, size):
        for cols in range(0, height, size):
            if grid[row][cols] == 1:
                pygame.draw.rect(display, "black", row * width)
            else:
                pygame.draw.rect(display, "black", cols * height, 1)

def main():
    grid = makeGrid()
    drawGrid(grid)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main()