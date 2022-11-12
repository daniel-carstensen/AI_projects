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
        self.domain = domain
        self.variable_dict, self.domain_dict, self.constraints = self.build_map(input_str, input_format, self.domain)
        self.variables = list(self.variable_dict.keys())
        self.var_domain = {k: list(self.domain_dict.get(k)) for k in self.variables}
        super().__init__(self.variables, self.var_domain, self.constraints, mrv, lcv, ac)

    def build_map(self, input_str, input_format, domain):
        def check_overlap(k_corners, l_corners):
            bl_k = k_corners[0]
            tr_k = k_corners[3]

            bl_l = l_corners[0]
            tr_l = l_corners[3]

            return (tr_k[0] <= bl_l[0] or bl_k[0] >= tr_l[0] or tr_k[1] <= bl_l[1] or bl_k[1] >= tr_l[1]) is False

        if input_format == 'dimensions':
            domain_dict = defaultdict(list)
            constraints = defaultdict(lambda: defaultdict(list))

            component_dim = input_str.split('\n')

            variable_dict = {k: tuple([int(i) for i in component_dim[k].split(',')]) for k in range(len(component_dim))}

            for k in variable_dict.keys():
                curr_comp = variable_dict.get(k)
                for length in range(domain[0]):
                    for height in range(domain[1]):
                        if curr_comp[0] + length <= domain[0] and curr_comp[1] + height <= domain[1]:
                            domain_dict[k].append((length, height))

            for k in variable_dict.keys():
                for l in variable_dict.keys():
                    if k != l:
                        k_dim = variable_dict.get(k)
                        l_dim = variable_dict.get(l)
                        for k_coords in domain_dict.get(k):
                            for l_coords in domain_dict.get(l):
                                k_corners = [k_coords, (k_dim[0]+k_coords[0], k_coords[1]),
                                             (k_coords[0], k_dim[1]+k_coords[1]), (k_dim[0]+k_coords[0], k_dim[1]+k_coords[1])]
                                l_corners = [l_coords, (l_dim[0] + l_coords[0], l_coords[1]),
                                             (l_coords[0], l_dim[1] + l_coords[1]),
                                             (l_dim[0] + l_coords[0], l_dim[1] + l_coords[1])]
                                overlap = False
                                if check_overlap(k_corners, l_corners):
                                    overlap = True
                                if check_overlap(l_corners, k_corners):
                                    overlap = True
                                if overlap is False:
                                    constraints[k][l].append((k_coords, l_coords))

        return variable_dict, domain_dict, constraints

    def translate_solution(self):
        solution = self.get_solution()

        if len(solution) == 0:
            return 'No solution was found.'

        output = 'Solution:\n'

        for i, v in enumerate(solution):
            output += str(self.variable_dict[i]) + ': ' + str(v) + '\n'

        return output

    def print_solution(self):
        solution = self.get_solution()
        solution_circuit = []
        for i in range(self.domain[1]):
            solution_row = ''
            for j in range(self.domain[0]):
                comp = False

                for k in range(len(solution)):
                    bl_x = solution[k][0]
                    bl_y = solution[k][1]
                    tr_x = self.variable_dict.get(k)[0] + solution[k][0]
                    tr_y = self.variable_dict.get(k)[1] + solution[k][1]
                    # print((i,j))
                    # print(((bl_x, bl_y), (tr_x, tr_y)))
                    if i < tr_y and i >= bl_y and  j < tr_x and j >= bl_x:
                        solution_row += str(k)
                        comp = True

                if comp is False:
                    solution_row += '.'

            solution_circuit.append(solution_row)

        solution_circuit.reverse()
        for row in solution_circuit:
            print(row)
