import pygame
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = "1"

width, height = 400, 400
size = (width, height)
black = (0,0,0)
white = (255, 255, 255)

pygame.init()
display = pygame.display.set_mode(size)
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
fps =  30
resolution = 20
margin = 1
running = True

def main():
    Grid = grid.Grid(width, height, resolution, margin) 
    Grid.random2d()
    running = True

    while running:
        clock.tick(fps)
        display.fill(black) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        Grid.gameOfLife(black, white, display)  

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()