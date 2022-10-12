# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : test_mazeworld.py
# Class : COSC76
# Purpose : Test of A* Algorithm for solving the mazeworld problem

from MazeworldProblem import MazeworldProblem
from Maze import Maze
from astar_search import astar_search


# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# create the mazes
test_maze3 = Maze('maze3.maz')
test_maze4x15 = Maze('maze4x15.maz')
test_maze6x6 = Maze('maze6x6.maz')
test_maze6x8 = Maze('maze6x8.maz')
test_maze25x25 = Maze('maze25x25.maz')
test_maze40x40 = Maze('maze40x40.maz')

# create/open a text file and write solution for each maze
f = open('multirobot_test_results.txt', 'w')
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
result = astar_search(test_mp, null_heuristic)
f.write(str(result))

result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

test_mp = MazeworldProblem(test_maze4x15, (12, 3, 11, 3, 0, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

test_mp = MazeworldProblem(test_maze6x6, (0, 5, 1, 5, 2, 5))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

test_mp = MazeworldProblem(test_maze6x8, (6, 2, 11, 1, 3))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

test_mp = MazeworldProblem(test_maze25x25, (0, 24, 24, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

test_mp = MazeworldProblem(test_maze40x40, (1, 30))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
f.write(str(result))

f.close()