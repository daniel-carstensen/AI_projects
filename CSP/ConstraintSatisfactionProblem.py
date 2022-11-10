# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : ConstraintSatisfactionProblem.py
# Class : COSC76
# Purpose :

import math


class ConstraintSatisfactionProblem:

    def __init__(self, variables, var_domain, constraints, mrv, lcv, ac):

        self.variables = variables
        self.var_domain = var_domain
        self.constraints = constraints
        self.mrv = mrv
        self.lcv = lcv
        self.ac = ac
        self.assignment = [-1]*len(self.variables)

    def is_consistent(self, var, val):
        for neighbor in self.constraints[var].keys():
            if self.assignment[neighbor] != -1:
                if (val, self.assignment[neighbor]) not in self.constraints[var][neighbor]:
                    return False

        return True

    def get_domain(self, var):
        return self.var_domain[var]

    def get_solution(self):
        return self.backtrack()

    def get_next_mrv_var(self):
        mrv = math.inf
        mrv_var = -1
        for i, var in enumerate(self.assignment):
            if var == -1:
                vals = self.get_domain(i)
                num_vals = 0
                for val in vals:
                    if self.is_consistent(var, val):
                        num_vals += 1
                if num_vals < mrv:
                    mrv_var = i
                    mrv = num_vals
                elif num_vals == mrv and len(self.constraints[var].keys()) > len(self.constraints[mrv_var].keys()):
                    mrv_var = i
                    mrv = num_vals

        return mrv_var

    def get_next_var(self):
        if self.mrv:
            return self.get_next_mrv_var()

        for i, var in enumerate(self.assignment):
            if var == -1:
                return i

    def get_lcv_order(self, var, vals):
        lcv_vals = []
        for val in vals:
            self.assignment[var] = val
            num_possibilities = 0
            for neighbor in self.constraints[var].keys():
                if self.assignment[neighbor] != -1:
                    neighbor_vals = self.get_domain(neighbor)
                    for n_val in neighbor_vals:
                        if self.is_consistent(neighbor, n_val):
                            num_possibilities += 1
            lcv_vals.append((num_possibilities, val))
            self.assignment[var] = -1

        lcv_vals.sort(reverse=True)
        ordered_vals = [lcv_vals[i][1] for i in range(len(lcv_vals))]

        return ordered_vals

    def ac_3(self):
        arc_queue = []
        for i in range(len(self.assignment)):
            for j in range(i+1, len(self.assignment)):
                if i != j:
                    arc_queue.append((i, j))
                    arc_queue.append((j, i))

        while len(arc_queue) != 0:
            curr_arc = arc_queue.pop(0)
            if curr_arc[1] in self.constraints[curr_arc[0]].keys():
                left_domain = [self.assignment[curr_arc[0]]]
                right_domain = [self.assignment[curr_arc[1]]]
                if left_domain[0] == -1:
                    left_domain = self.get_domain(curr_arc[0])
                if right_domain[0] == -1:
                    right_domain = self.get_domain(curr_arc[1])

                changed = False
                for left_val in left_domain:
                    available = False
                    for right_val in right_domain:
                        if left_val != right_val:
                            available = True
                    if available is False:
                        left_domain.remove(left_val)
                        if len(left_domain) == 0:
                            return False
                        changed = True

                if changed:
                    self.var_domain[curr_arc[0]] = left_domain
                    for neighbor in self.constraints[curr_arc[0]].keys():
                        arc_queue.append((neighbor, curr_arc[0]))

        return True

    def backtrack(self):
        if -1 not in self.assignment:
            return self.assignment

        var = self.get_next_var()
        vals = self.get_domain(var)

        if self.lcv:
            vals = self.get_lcv_order(var, vals)

        for val in vals:
            if self.is_consistent(var, val):
                self.assignment[var] = val
                if self.ac is False or self.ac_3():
                    result = self.backtrack()
                    if len(result) != 0:
                        return result
                self.assignment[var] = -1

        return []








