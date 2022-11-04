# Author : Daniel Carstensen
# Date : 11/xx/2022
# File name : ConstraintSatisfactionProblem.py
# Class : COSC76
# Purpose :

import copy


class ConstraintSatisfactionProblem:

    def __init__(self, variables, var_domain, constraints):

        self.variables = variables
        self.var_domain = var_domain
        self.constraints = constraints
        self.assignment = [-1]*len(self.variables)

    def is_consistent(self, var, val):
        for neighbor in self.constraints[var].keys():
            if self.assignment[neighbor] != -1:
                if (val, self.assignment[neighbor]) not in self.constraints[var][neighbor]:
                    return False

        return True

    def get_next_var(self):
        for i, var in enumerate(self.assignment):
            if var == -1:
                return i

    def get_domain(self, var):
        return self.var_domain[var]

    def get_solution(self):
        return self.backtrack()

    def backtrack(self):
        if -1 not in self.assignment:
            return self.assignment

        var = self.get_next_var()
        vals = self.get_domain(var)

        for val in vals:
            if self.is_consistent(var, val):
                self.assignment[var] = val
                result = self.backtrack()
                if len(result) != 0:
                    return result
                self.assignment[var] = -1

        return []








