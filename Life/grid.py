import random
import numpy as np
import pygame


class Grid:
    def __init__(self, width, height, resolution, size):
        self.width = width
        self.height = height
        self.resolution = resolution
        self.size = size

        # rows and columns of the grid
        # make it scalable
        self.row = width/resolution
        self.cols = height/resolution
        self.size = (self.row, self.cols)

        # the grid itself
        self.grid = np.ndarray(shape=self.size)

    def random2d(self):
        for i in range(self.width):
            for j in range(self.height):
                self.grid[i][j] = random.randint(0,1)

    def neighbours(self, x, y):
        # loop from -1, 2 to check all the neighbours
        # then count the total
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # implement toroid boundary conditions later
                pass 


    def gameOfLife(self, aliveColor, deadColor, surface):
        for i in range(self.width):
            for j in range(self.height):
                x_pos = i * self.resolution
                y_pos = j * self.resolution

            # draw the live and dead cells
            if self.grid[x_pos][y_pos] == 1:
                pygame.draw.rect(surface, aliveColor, [x_pos, y_pos, self.scale-self.size, self.scale-self.size])
            else:
                pygame.draw.rect(surface, deadColor, [x_pos, y_pos, self.scale-self.size, self.scale-self.size])

        # generating the next generation
        nextGrid = np.ndarray(shape=self.size)
        for i in range(self.row):
            for j in range(self.cols):
                # implement the rules
                break