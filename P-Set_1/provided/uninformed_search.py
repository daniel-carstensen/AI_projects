# Author : Daniel Carstensen
# Date : 09/29/2022
# File name : uninformed_search
# Class : COSC76
# Purpose : Design BFS, depth-limited DFS, and iterative DFS to traverse a problem and find a solution path

from collections import deque
from SearchSolution import SearchSolution


# SearchNode class to wrap state objects, keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.curr_depth = 0


# BFS function to traverse a search problem
def bfs_search(search_problem):
    solution = SearchSolution(search_problem, 'BFS')
    visited = set()     # memoizing to prevent visiting the same node twice

    if search_problem.start_state == (0, 0, 0):
        solution.path.append(search_problem.start_state)

    next_nodes = deque()    # use FIFO queue
    curr_node = SearchNode(search_problem.start_state)
    next_nodes.append(curr_node)

    # search while there are successors and the goal has not been found
    while (len(next_nodes) > 0) and (not search_problem.test_goal(curr_node.state)):
        curr_node = next_nodes.popleft()
        solution.nodes_visited += 1
        successors = search_problem.get_successors(curr_node.state)

        for s in successors:
            if s not in visited:
                visited.add(s)
                next_nodes.append(SearchNode(s, curr_node))

    # use backchaining to reconstruct solution path
    if search_problem.test_goal(curr_node.state):
        while curr_node is not None:
            solution.path.insert(0, curr_node.state)
            curr_node = curr_node.parent

    return solution


# recursive and path checking DFS function to traverse a search problem
# no use of memoizing to be memory efficient
# We pass the solution along to each new recursive call to dfs_search
# so that statistics like number of nodes visited or recursion depth
# might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state

    if node is None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, 'DFS')
        solution.path.append(node.state)    # add state to solution path
        solution.nodes_visited += 1
        successors = search_problem.get_successors(node.state)

        for s in successors:
            path = dfs_search(search_problem=search_problem, depth_limit=depth_limit-1, node=SearchNode(s), solution=solution)
            if path is not None:
                return path

        solution.path.remove(node.state)    # remove state from solution path if the goal was not found
        return solution

    # check if the current state is the goal state
    elif search_problem.test_goal(node.state):
        solution.path.append(node.state)
        return solution

    # run while there are successors and the depth limit has not been reached
    elif len(search_problem.get_successors(node.state)) > 0 and depth_limit > 0:
        solution.path.append(node.state)        # add state to solution path
        solution.nodes_visited += 1
        successors = search_problem.get_successors(node.state)

        for s in successors:
            if s not in solution.path:  # path checking, only explore nodes that have not been visited yet on this path
                path = dfs_search(search_problem=search_problem, depth_limit=depth_limit-1, node=SearchNode(s), solution=solution)
                if path is not None:
                    return path

    if node.state in solution.path:
        solution.path.remove(node.state)


# modified DFS function to only search at specific, increasing depths
def ids_search(search_problem, depth_limit=100):
    # run a simple loop to increase the depth until the goals is found or max. depth is reached

    for i in range(depth_limit+1):
        solution = dfs_search(search_problem, depth_limit=i)
        if len(solution.path) > 0:
            return solution

    return solution