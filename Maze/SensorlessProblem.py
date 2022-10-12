# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : sensorlessProblem.py
# Class : COSC76
# Purpose : Model and Implementation of the maze problem where a single robot without any sensors needs to determine
#           its location in the quickest manner

from Maze import Maze
from time import sleep


# representation of the sensorless robot problem
class SensorlessProblem:

    # maze and all initial belief states are known
    def __init__(self, maze):
        self.maze = maze
        self.start_state = tuple(self.get_initial_belief_states())

    # simple heuristic based on the number of belief states (fewer belief states is better)
    def uncertainty_heuristic(self, states):
        return len(states)

    # get initial belief states, i.e all locations in the maze the robot can legally be
    def get_initial_belief_states(self):
        belief_states = set()
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if self.is_legal((x, y)):
                    belief_states.add((x, y))

        return belief_states

    # test if the goal ahs been reached, i.e the robot is sure of its location
    def test_goal(self, states):
        if len(states) == 1:
            return True
        return False

    # determine if a move is legal, i.e. within the maze, no wall in the way
    def is_legal(self, state):
        return self.maze.is_floor(state[0], state[1])

    # move the robot to reduce number of belief states
    def robot_movement(self, states, direction, axis):      # direction indicates forward or backward while axis indicates horizontal or vertical
        successors = set()

        for state in states:
            next_state = list(state)
            next_state[axis] += direction
            # add to successors if move is legal
            if self.is_legal(next_state):
                successors.add(tuple(next_state))
            # else add current state
            else:
                successors.add(state)

        return tuple(successors)

    # get all successors, i.e. moves into all direction
    def get_successors(self, states):
        successors = set()
        successors.add(self.robot_movement(set(states), 1, 1))      # north
        successors.add(self.robot_movement(set(states), 1, 0))      # east
        successors.add(self.robot_movement(set(states), -1, 1))     # south
        successors.add(self.robot_movement(set(states), -1, 0))     # west

        return successors

    def __str__(self):
        string = "Blind robot problem: "
        return string

    def animate_path(self, path):
        # reset the robot locations in the maze
        print(str(self))
        for states in path:
            print(f'Step {path.index(states)}')
            self.maze.robotloc = tuple(sum(states, ()))
            print(str(self.maze))
            sleep(1)


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
