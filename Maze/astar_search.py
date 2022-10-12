# Author : Daniel Carstensen
# Date : 10/11/2022
# File name : astar_search.py
# Class : COSC76
# Purpose : Implementation of the A* algorithm for solving search problems

from SearchSolution import SearchSolution
from heapq import heappush, heappop


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        return self.transition_cost + self.heuristic(self.state)

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
# as far as possible. Grab the states from the nodes,
# and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


# implementation of A* search
def astar_search(search_problem, heuristic_fn):     # takes the search problem and a specified heuristic
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))    # start with starting point
    pqueue = []
    heappush(pqueue, start_node)    # push onto heap sorted by evaluation function

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)      # instantiate solution

    visited_cost = {}   # instantiate visited dict with transition costs
    visited_cost[start_node.state] = 0

    while len(pqueue) > 0:  # run while not all nodes have been explored
        curr_node = heappop(pqueue)     # pop the node with the highest priority
        solution.nodes_visited += 1

        # return solution if the goal stat has been reached
        if search_problem.test_goal(curr_node.state):
            solution.cost = curr_node.transition_cost
            solution.path = backchain(curr_node)
            break

        successors = search_problem.get_successors(curr_node.state)     # get successors from problem

        # for each successor if the state has not been visited or the cost to the state for the current node is lower
        # than the cost for the previous node: push the successor into the queue
        for s in successors:
            s = AstarNode(s, heuristic_fn, curr_node, curr_node.transition_cost)
            if s.state[1:] != curr_node.state[1:]:
                s.transition_cost += 1

            if visited_cost.get(s.state) is None:
                visited_cost[s.state] = s.transition_cost
                heappush(pqueue, s)

            elif visited_cost.get(s.state) > s.transition_cost:
                visited_cost[s.state] = s.transition_cost
                heappush(pqueue, s)

    return solution