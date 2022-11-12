# Author : Daniel Carstensen
# Date : 11/12/2022
# File name : CircuitCSP.py
# Class : COSC76
# Purpose : Extension of general CSP class to solve circuit layout problem

from collections import defaultdict
from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


class CircuitCSP(ConstraintSatisfactionProblem):

    # domain: size of the circuit board (general domain)
    # create variable_dict, domain_dict, and constraints with build_map method
    # variable_dict: dictionary that assigns each variable a number
    # domain_dict: dictionary that assigns each variable a list of possible values
    # constraints: binary constraints for each pair of variables
    # mrv, lcv, ac: toggle minimum remaining values and least constraining value heuristics, and arc consistency
    def __init__(self, input_str, input_format, domain, mrv, lcv, ac):
        self.domain = domain
        self.variable_dict, self.domain_dict, self.constraints = self.build_map(input_str, input_format)
        self.variables = list(self.variable_dict.keys())
        super().__init__(self.variables, self.domain_dict, self.constraints, mrv, lcv, ac)  # init of parent class

    # input_str: input as text
    # input_format: format of input
    # build variable dictionary and constraints
    def build_map(self, input_str, input_format):

        # helper method to check if two components overlap
        # bl_: bottom lower corner
        # tr_: top right corner
        def check_overlap(k_corners, l_corners):
            bl_k = k_corners[0]
            tr_k = k_corners[1]

            bl_l = l_corners[0]
            tr_l = l_corners[1]

            return (tr_k[0] <= bl_l[0] or bl_k[0] >= tr_l[0] or tr_k[1] <= bl_l[1] or bl_k[1] >= tr_l[1]) is False

        if input_format == 'dimensions':
            domain_dict = defaultdict(list)
            constraints = defaultdict(lambda: defaultdict(list))

            # each line contains dimensions of one components
            component_dim = input_str.split('\n')

            # create dictionary assigning each component dimensions as tuple (length, height) to a number
            variable_dict = {k: tuple([int(i) for i in component_dim[k].split(',')]) for k in range(len(component_dim))}

            # create domain for each component by check if specific location of bottom left corner contains entire
            # component within the board domain
            for k in variable_dict.keys():
                curr_comp = variable_dict.get(k)
                for length in range(self.domain[0]):
                    for height in range(self.domain[1]):
                        if curr_comp[0] + length <= self.domain[0] and curr_comp[1] + height <= self.domain[1]:
                            domain_dict[k].append((length, height))

            # create binary constraints by checking for each pair of components and all possible locations of each
            # component if components overlap
            for k in variable_dict.keys():
                for l in variable_dict.keys():
                    if k != l:
                        k_dim = variable_dict.get(k)
                        l_dim = variable_dict.get(l)
                        for k_coords in domain_dict.get(k):
                            for l_coords in domain_dict.get(l):
                                # bottom left and top right corner coordinates
                                k_corners = [k_coords, (k_dim[0]+k_coords[0], k_dim[1]+k_coords[1])]
                                l_corners = [l_coords, (l_dim[0] + l_coords[0], l_dim[1] + l_coords[1])]
                                overlap = False
                                if check_overlap(k_corners, l_corners):
                                    overlap = True
                                if check_overlap(l_corners, k_corners):
                                    overlap = True
                                if overlap is False:
                                    constraints[k][l].append((k_coords, l_coords))

        return variable_dict, domain_dict, constraints

    # get solution and retranslate assignment to original variables and inputs
    def translate_solution(self):
        solution = self.get_solution()

        if len(solution) == 0:
            return 'No solution was found.'

        output = 'Solution:\n'

        for i, v in enumerate(solution):
            output += str(self.variable_dict[i]) + ': ' + str(v) + '\n'

        return output

    # get solution and print the location of each component in solution in the board
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
                    if i < tr_y and i >= bl_y and  j < tr_x and j >= bl_x:
                        solution_row += str(k)
                        comp = True

                if comp is False:
                    solution_row += '.'

            solution_circuit.append(solution_row)

        solution_circuit.reverse()
        for row in solution_circuit:
            print(row)
