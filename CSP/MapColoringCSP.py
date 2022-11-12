# Author : Daniel Carstensen
# Date : 11/12/2022
# File name : MapColoringCSP.py
# Class : COSC76
# Purpose : Extension of general CSP class to solve map coloring problem

from collections import defaultdict
from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


# MapColoringCSP solver class (uses ConstraintSatisfactionProblem class as parent class)
class MapColoringCSP(ConstraintSatisfactionProblem):

    # domain_dict: dictionary that assigns each value a number
    # domain: variable domain, in this case same for every variable (numbers for colors)
    # create variable_dict and constraints with build_map method
    # variable_dict: dictionary that assigns each variable a number
    # constraints: binary constraints for each pair of variables
    # var_domain: domain (possible values) of each variable
    # mrv, lcv, ac: toggle minimum remaining values and least constraining value heuristics, and arc consistency
    def __init__(self, input_str, input_format, domain, mrv, lcv, ac):
        self.domain_dict = {k: domain[k] for k in range(len(domain))}
        self.domain = list(self.domain_dict.keys())

        self.variable_dict, self.constraints = self.build_map(input_str, input_format)
        self.variables = list(self.variable_dict.keys())

        self.var_domain = {k: list(self.domain) for k in self.variables}

        super().__init__(self.variables, self.var_domain, self.constraints, mrv, lcv, ac)   # init of parent class

    # input_str: input as text
    # input_format: format of input
    # build variable dictionary and constraints
    def build_map(self, input_str, input_format):
        constraints = defaultdict(lambda: defaultdict(list))

        if input_format == 'node_edge_list':
            # all nodes in first line, then undirected edges in following lines
            node_list, edge_list = input_str.split('\n')[0].split(' '), input_str.split('\n')[1:]
            variable_dict = {k: node_list[k] for k in range(len(node_list))}
            reverse_dict = {node_list[k]: k for k in range(len(node_list))}
            for edge in edge_list:
                start, end = edge.split(' ')
                for i in range(len(self.domain)):
                    for m in range(len(self.domain)):
                        if i != m:
                            # constrain values such that no two neighbors have the same value
                            constraints[reverse_dict[start]][reverse_dict[end]].append((i, m))
                            constraints[reverse_dict[end]][reverse_dict[start]].append((i, m))

        if input_format == 'adj_list':
            # each line begins with node and all neighbors of node
            node_list = []
            adj_list = input_str.split('\n')
            for l in adj_list:
                start = l.split(',')[0]
                node_list.append(start)
            variable_dict = {k: node_list[k] for k in range(len(node_list))}
            reverse_dict = {node_list[k]: k for k in range(len(node_list))}
            for l in adj_list:
                start = l.split(',')[0]
                for end in l.split(',')[1:]:
                    for i in range(len(self.domain)):
                        for m in range(len(self.domain)):
                            if i != m:
                                # constrain values such that no two neighbors have the same value
                                constraints[reverse_dict[start]][reverse_dict[end]].append((i, m))

        return variable_dict, constraints

    # get solution and retranslate assignment to original variables and inputs
    def translate_solution(self):
        solution = self.get_solution()

        if len(solution) == 0:
            return 'No solution was found.'

        output = 'Solution:\n'

        for i, v in enumerate(solution):
            output += self.variable_dict[i] + ': ' + self.domain_dict[v] + '\n'

        return output
