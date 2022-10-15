import pygame
import time
import sys

grid_size = (300, 300)
cell_size = 2
calc_per_frame = 100  
fps = 60

class Ant:
    def __init__(self):
        # setting the starting position of the ant
        self.x = int(grid_size[0]/2) 
        self.y = int(grid_size[1]/2)       
        # 0 = up, 1 = right, 2 = down, 3 = left
        self.direction = 0

    def turnRight(self):
        self.direction += 1
        # how many turns can it make before going back to the starting position
        self.direction = self.direction % 4

    def turnLeft(self):
        self.direction -= 1
        self.direction = self.direction % 4
    
    def moveForward(self):
        if self.direction == 0:
            self.x -= 1
        elif self.direction == 1:
            self.y += 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y -= 1
        # using modulo for the toroidal boundary conditions
        self.x = self.x % grid_size[0] 
        self.y = self.y % grid_size[1]
        
def initialize():
    pygame.init()
    display = pygame.display.set_mode((grid_size[0]*cell_size, grid_size[1]*cell_size))
    display.fill(pygame.Color("black"))
    clock = pygame.time.Clock()
    cells = [[0 for j in range(grid_size[1])] for i in range(grid_size[0])] 
    ant = Ant()
    return display, clock, cells, ant

def generateNext(cells, ant, display): 
    if cells[ant.x][ant.y] == 1:
        ant.turnRight()
        cells[ant.x][ant.y] = 0
        pygame.draw.rect(display, "black", (ant.x*cell_size, ant.y*cell_size, cell_size, cell_size), 0)
    elif cells[ant.x][ant.y] == 0 :
        ant.turnLeft()
        cells[ant.x][ant.y] = 1
        pygame.draw.rect(display, "white", (ant.x*cell_size, ant.y*cell_size, cell_size, cell_size), 0)
    ant.moveForward() 


def langtonsAnt(display, clock, cells, ant):
    time.sleep(0.1) 
    generation = 0
    while True:
        for i in range(calc_per_frame):
            generation += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            generateNext(cells, ant, display)        
        pygame.display.update()
        clock.tick(fps)

def main():
    display, clock, cells, ant = initialize()
    langtonsAnt(display, clock, cells, ant)

if __name__ == "__main__":
    main()