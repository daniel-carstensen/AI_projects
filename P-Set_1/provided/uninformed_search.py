from collections import deque
from SearchSolution import SearchSolution


# you might find a SearchNode class useful to wrap state objects,
# keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.curr_depth = 0


# you might write other helper functions, too. For example,
# I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem):
    solution = SearchSolution(search_problem, 'BFS')
    visited = set()

    if search_problem.start_state == (0, 0, 0):
        solution.path.append(search_problem.start_state)

    next_nodes = deque()
    curr_node = SearchNode(search_problem.start_state)
    next_nodes.append(curr_node)

    while (len(next_nodes) > 0) and (not search_problem.test_goal(curr_node.state)):
        curr_node = next_nodes.popleft()
        solution.nodes_visited += 1
        successors = search_problem.get_successors(curr_node.state)

        for s in successors:
            if s not in visited:
                visited.add(s)
                next_nodes.append(SearchNode(s, curr_node))

    if search_problem.test_goal(curr_node.state):
        while curr_node is not None:
            solution.path.insert(0, curr_node.state)
            curr_node = curr_node.parent

    return solution


# Don't forget that your dfs function should be recursive and do path checking,
# rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
# so that statistics like number of nodes visited or recursion depth
# might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node is None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, 'DFS')
        solution.path.append(node.state)
        solution.nodes_visited += 1
        successors = search_problem.get_successors(node.state)

        for s in successors:
            path = dfs_search(search_problem=search_problem, depth_limit=depth_limit-1, node=SearchNode(s), solution=solution)
            if path is not None:
                return path

        solution.path.remove(node.state)
        return solution

    elif search_problem.test_goal(node.state):
        solution.path.append(node.state)
        return solution

    elif len(search_problem.get_successors(node.state)) > 0 and depth_limit > 0:
        solution.path.append(node.state)
        solution.nodes_visited += 1
        successors = search_problem.get_successors(node.state)

        for s in successors:
            if s not in solution.path:
                path = dfs_search(search_problem=search_problem, depth_limit=depth_limit-1, node=SearchNode(s), solution=solution)
                if path is not None:
                    return path

    if node.state in solution.path:
        solution.path.remove(node.state)


def ids_search(search_problem, depth_limit=100):
    for i in range(depth_limit+1):
        solution = dfs_search(search_problem, depth_limit=i)
        if len(solution.path) > 0:
            return solution
    return solution