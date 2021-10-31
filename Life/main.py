import pygame
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

width, height = 1024, 768
size = (width, height)
black = (0,0,0)
white = (255, 255, 255)

pygame.init()
print(pygame.display.Info())
display = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
fps =  60
black = (0,0,0)
white = (255, 255, 255)


def makeGrid():
    grid = []
    for row in range(0, width):
        grid.append([])
        for cols in range(0, height):
            grid[row].append(random.randint(0, 1))
    
    return grid



def checkNeighbours(grid, i, j):
    total = 0
    for n in range(-1, 2):
        for m in range(-1, 2):
            x = (i+n+len(grid[0])) % len(grid[0])
            y = (j+n+len(grid[1])) % len(grid[1]) 
            total += grid[x][y]

    total -= grid[x][y] 
    return total


def main():   
    running = True
    grid = makeGrid()   
    while running:
        display.fill(white)
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for row in range(0, width, 20):
            for cols in range(0, height, 20):
                rect = pygame.Rect(row, cols, 20, 20)
                if grid[row][cols] == 1:
                    pygame.draw.rect(display, black, rect)
                else:
                    pygame.draw.rect(display, black, rect, 1)

        for i in range(len(grid[0])):
            for j in range(len(grid[1])):
                # rule checking
                if grid[i][j] == 1 and (checkNeighbours(grid, i, j) < 2 or checkNeighbours(grid, i, j) > 3):
                    grid[i][j] = 0
                elif grid[i][j] == 0 and checkNeighbours(grid, i, j) == 3:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i][j] 
        pygame.display.update()           
    pygame.quit()


if __name__ == "__main__":
    main()