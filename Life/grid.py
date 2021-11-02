import random
import numpy as np
import pygame


class Grid:
    def __init__(self, width, height, resolution, margin):
        self.resolution = resolution
        self.margin = margin

        # rows and columns of the grid
        # make it scalable
        self.row = int(width/resolution)
        self.cols = int(height/resolution)
        self.size = (self.row, self.cols)

        # the grid itself
        self.grid_life = np.ndarray(shape=(self.size))

    def random2d(self):
        for i in range(self.row):
            for j in range(self.cols):
                self.grid_life[i][j] = random.randint(0,1)

    def getNeighbours(self, x, y):
        # loop from -1, 2 to check all the neighbours
        # then count the total
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # toroidal boundary conditions
                x_edge = (x+i+self.row)%self.row
                y_edge = (y+j+self.cols)%self.cols
                total += self.grid_life[x_edge][y_edge]
        
        total -= self.grid_life[x][y]
        return total

    def gameOfLife(self, aliveColor, deadColor, surface):
        for i in range(self.row):
            for j in range(self.cols):
                x_pos = i * self.resolution
                y_pos = j * self.resolution

                # draw the live and dead cells
                if self.grid_life[i][j] == 1:
                    pygame.draw.rect(surface, aliveColor, [x_pos, y_pos, (self.resolution-self.margin), 
                    (self.resolution-self.margin)])
                else:
                    pygame.draw.rect(surface, deadColor, [x_pos, y_pos, (self.resolution-self.margin),
                    (self.resolution-self.margin)])

        # generating the next generation
        nextGrid = np.ndarray(shape=(self.size))
        
        for i in range(self.row):
            for j in range(self.cols):
                state = self.grid_life[i][j]
                neighbours = self.getNeighbours(i,j)
        # check the rules
                if state == 0 and neighbours == 3:
                    nextGrid[i][j] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    nextGrid[i][j] = 0
                else:
                    nextGrid[i][j] = state
        self.grid_life = nextGrid