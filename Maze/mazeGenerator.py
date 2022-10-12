# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : mazeGenerator.py
# Class : COSC76
# Purpose : Create random mazes with specified width and height

import random


# automatically generated mazes
class mazeGenerator:

    # width and height need to be specified
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.symbols = ['.', '#']

    # method to generate the maze
    def generate_maze(self):
        f = open(f'maze{self.height}x{self.width}.maz', 'w')    # create a .maz file and write the randomly generated maze
        maze = ''

        for i in range(self.height):
            for j in range(self.width):
                maze += random.choices(self.symbols, weights=[0.65, 0.35])[0]
            maze += '\n'

        f.write(maze)
        f.close()


mazeGen = mazeGenerator(8, 8)
mazeGen.generate_maze()