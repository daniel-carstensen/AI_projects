# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : CircuitCSP.py
# Class : COSC76
# Purpose :

from collections import defaultdict
from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


class CircuitCSP(ConstraintSatisfactionProblem):
    # shapes: index on bottom left corner
    # domain:
    # constraint: every corner, check if point is in other piece (for both pieces)
    def __init__(self, input_str, input_format, domain, mrv, lcv, ac):

        self.variable_dict, self.domain_dict, self.constraints = self.build_map(input_str, input_format, domain)
        self.domain = list(self.domain_dict.keys())
        self.variables = list(self.variable_dict.keys())

        self.var_domain = {k: list(self.domain) for k in self.variables}

        super().__init__(self.variables, self.var_domain, self.constraints, mrv, lcv, ac)

    def build_map(self, input_str, input_format, domain):
        def check_overlap(point, dim):
            if point[0] <= dim[0] or point[1] <= dim[1]:
                return False
            return True

        if input_format == 'dimensions':
            domain_dict = defaultdict(list)
            constraints = defaultdict(lambda: defaultdict(list))

            component_dim = input_str.split('\n')

            variable_dict = {k: tuple([int(i) for i in component_dim[k].split(',')]) for k in range(len(component_dim))}

            for k in variable_dict.keys():
                curr_comp = variable_dict.get(k)
                for row in range(domain[0]):
                    for col in range(domain[1]):
                        if curr_comp[0] + row <= domain[0] and curr_comp[1] + col <= domain[1]:
                            domain_dict[k].append((row, col))

            for k in variable_dict.keys():
                for l in variable_dict.keys():
                    if k != l:
                        k_dim = variable_dict.get(k)
                        l_dim = variable_dict.get(l)
                        for k_coords in domain_dict.get(k):
                            for l_coords in domain_dict.get(k):
                                k_corners = [k_coords, (k_dim[0]+k_coords[0], k_coords[1]),
                                             (k_coords[0], k_dim[1]+k_coords[1]), (k_dim[0]+k_coords[0], k_dim[1]+k_coords[1])]
                                l_corners = [l_coords, (l_dim[0] + l_coords[0], l_coords[1]),
                                             (l_coords[0], l_dim[1] + l_coords[1]),
                                             (l_dim[0] + l_coords[0], l_dim[1] + l_coords[1])]
                                overlap = False
                                for c in k_corners:
                                    if check_overlap(c, (l_dim[0] + l_coords[0], l_dim[1] + l_coords[1])):
                                        overlap = True
                                        break
                                for c in l_corners:
                                    if check_overlap(c, (k_dim[0] + k_coords[0], k_dim[1] + k_coords[1])):
                                        overlap = True
                                        break

                                if overlap is False:
                                    constraints[k][l].append((k_coords, l_coords))

                print(constraints[k])

        return variable_dict, domain_dict, constraints

    def translate_solution(self):
        solution = self.get_solution()

        if len(solution) == 0:
            return 'No solution was found.'

        output = 'Solution:\n'

        for i, v in enumerate(solution):
            output += self.variable_dict[i] + ': ' + self.domain_dict[v] + '\n'

        return output
