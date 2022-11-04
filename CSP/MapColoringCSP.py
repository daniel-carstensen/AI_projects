# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : MapColoringCSP.py
# Class : COSC76
# Purpose :

from collections import defaultdict
from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


class MapColoringCSP(ConstraintSatisfactionProblem):

    def __init__(self, input_str, input_format, domain):
        self.domain_dict = {k: domain[k] for k in range(len(domain))}
        self.domain = list(self.domain_dict.keys())

        self.variable_dict, self.constraints = self.build_map(input_str, input_format)
        self.variables = list(self.variable_dict.keys())

        self.var_domain = {k: list(self.domain) for k in self.variables}

        super().__init__(self.variables, self.var_domain, self.constraints)

    def build_map(self, input_str, input_format):
        constraints = defaultdict(lambda: defaultdict(list))

        if input_format == 'node_edge_list':
            node_list, edge_list = input_str.split('\n')[0].split(' '), input_str.split('\n')[1:]
            variable_dict = {k: node_list[k] for k in range(len(node_list))}
            reverse_dict = {node_list[k]: k for k in range(len(node_list))}
            for edge in edge_list:
                start, end = edge.split(' ')
                for i in range(len(self.domain)):
                    for m in range(len(self.domain)):
                        if i != m:
                            constraints[reverse_dict[start]][reverse_dict[end]].append((i, m))
                            constraints[reverse_dict[end]][reverse_dict[start]].append((i, m))

        if input_format == 'adj_list':
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
                                constraints[reverse_dict[start]][reverse_dict[end]].append((i, m))

        return variable_dict, constraints

    def translate_solution(self):
        solution = self.get_solution()

        if len(solution) == 0:
            return 'No solution was found.'

        output = 'Solution:\n'

        for i, v in enumerate(solution):
            output += self.variable_dict[i] + ': ' + self.domain_dict[v] + '\n'

        return output