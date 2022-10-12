# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : MazeworldProblem.py
# Class : COSC76
# Purpose : Model and Implementation of the maze problem where one or multiple robots need to find the best path to
#           a goal state within the maze

import math

from Maze import Maze
from time import sleep


# representation of the maze problem
class MazeworldProblem:

    # maze, goal, start state, and number of robots are known
    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = tuple([0] + self.maze.robotloc)
        self.num_robots = math.ceil(len(self.start_state) // 2)

    # simple heuristic based on the Manhattan distance of all robots to their target
    def manhattan_heuristic(self, state):
        distances = []
        for coord1, coord2 in zip(state[1:], self.goal_locations):
            distance = abs(coord1 - coord2)
            distances.append(distance)
        return sum(distances)

    # test if the goal state has been reached, i.e. all robots are at their speified goal
    def test_goal(self, state):
        if state[1:] == self.goal_locations:
            return True
        return False

    # determine if a move is legal, i.e. within the maze, no wall and no robot in the way
    def is_legal(self, state, coords):
        for i in range(0, len(state), 2):
            for j in range(i+2, len(state), 2):
                if state[i] == state[j] and state[i+1] == state[j+1]:
                    return False

        return self.maze.is_floor(coords[0], coords[1])

    # move the robot whose turn it is
    def robot_movement(self, robot, state, successors, direction, axis):    # direction indicates forward or backward while axis indicates horizontal or vertical
        successors.append(tuple(state))     # no movement is always an option

        next_state = state.copy()
        next_state[robot+axis] += direction
        # add to successors if move is legal
        if self.is_legal(next_state[1:], next_state[robot:robot+2]):
            successors.append(tuple(next_state))

        return successors

    # get all successors, i.e. moves into all direction
    def get_successors(self, state):
        state = list(state)
        successors = []

        if state[0] < (self.num_robots-1):
            state[0] += 1
        else:
            state[0] = 0

        successors = self.robot_movement(2 * state[0] + 1, state, successors, 1, 1)     # north
        successors = self.robot_movement(2 * state[0] + 1, state, successors, 1, 0)     # east
        successors = self.robot_movement(2 * state[0] + 1, state, successors, -1, 1)    # south
        successors = self.robot_movement(2 * state[0] + 1, state, successors, -1, 0)    # west

        return successors

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])
        print(str(self))
        for state in path:
            self.maze.robotloc = tuple(state[1:])

            sleep(1)
            print(str(self.maze))


# A bit of test code. You might want to add to it to verify that things
# work as expected.
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, [1, 4, 1, 3, 1, 2])

    print(test_mp.get_successors([0, 1, 0, 1, 2, 2, 1]))