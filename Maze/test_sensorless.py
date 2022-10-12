# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : test_sensorless.py
# Class : COSC76
# Purpose : Test of A* Algorithm for solving the sensorless problem

from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# create the mazes
test_maze3 = Maze('maze3.maz')
test_maze6x6 = Maze('maze6x6.maz')
test_maze6x8 = Maze('maze6x8.maz')
test_maze8x8 = Maze('maze8x8.maz')

# create/open a text file and write solution for each maze
f = open('sensorless_test_results.txt', 'w')
test_sp = SensorlessProblem(test_maze3)
result = astar_search(test_sp, test_sp.uncertainty_heuristic)
f.write(str(result))

test_sp = SensorlessProblem(test_maze6x6)
result = astar_search(test_sp, test_sp.uncertainty_heuristic)
f.write(str(result))

test_sp = SensorlessProblem(test_maze6x8)
result = astar_search(test_sp, test_sp.uncertainty_heuristic)
f.write(str(result))

test_sp = SensorlessProblem(test_maze8x8)
result = astar_search(test_sp, test_sp.uncertainty_heuristic)
f.write(str(result))

f.close()

# animate the solution to one maze
test_sp = SensorlessProblem(test_maze6x6)
result = astar_search(test_sp, test_sp.uncertainty_heuristic)
test_sp.animate_path(result.path)
