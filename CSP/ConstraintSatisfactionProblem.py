# Author : Daniel Carstensen
# Date : 11/12/2022
# File name : ConstraintSatisfactionProblem.py
# Class : COSC76
# Purpose : General Purpose Search Algorithm to solve constraint satisfaction problems

import math


# ConstraintSatisfactionProblem solver class
class ConstraintSatisfactionProblem:

    # variables: variables in the CSP
    # var_domain: domain (possible values) of each variable
    # constraints: binary constraints for each pair of variables
    # mrv, lcv, ac: toggle minimum remaining values and least constraining value heuristics, and arc consistency
    # assignment: list where index is variable and entry is assigned value
    def __init__(self, variables, var_domain, constraints, mrv, lcv, ac):

        self.variables = variables
        self.var_domain = var_domain
        self.constraints = constraints
        self.mrv = mrv
        self.lcv = lcv
        self.ac = ac
        self.assignment = [-1]*len(self.variables)

    # check if specific assignment is consistent with all constraints
    def is_consistent(self, var, val):
        for neighbor in self.constraints[var].keys():   # check for all 'neighbors' of variable
            if self.assignment[neighbor] != -1:
                if (val, self.assignment[neighbor]) not in self.constraints[var][neighbor]:
                    return False

        return True

    # get domain of specific variable
    def get_domain(self, var):
        return self.var_domain[var]

    # get next variable to assign
    def get_next_var(self):
        # if mrv then use mrv heuristic
        if self.mrv:
            return self.get_next_mrv_var()

        # else return first unassigned variable in assignment list
        for i, var in enumerate(self.assignment):
            if var == -1:
                return i

    # get next variable using mrv heuristic
    # return variable with the least amount of possible variables left
    # use degree heuristic (most neighbors) as tie-breaker
    def get_next_mrv_var(self):
        mrv = math.inf
        mrv_var = -1
        # for each unassigned variable, count number of possible values
        for i, var in enumerate(self.assignment):
            if var == -1:
                if mrv_var == -1:
                    mrv_var = i
                vals = self.get_domain(i)
                num_vals = 0
                for val in vals:
                    if self.is_consistent(i, val):
                        num_vals += 1
                if num_vals < mrv:
                    mrv_var = i
                    mrv = num_vals
                # if tied, choose variable with the most neighbors
                elif num_vals == mrv and len(self.constraints[var].keys()) > len(self.constraints[mrv_var].keys()):
                    mrv_var = i
                    mrv = num_vals

        return mrv_var

    # get optimal order of values to try out
    # count number of possible values for each unassigned neighbor of variable given a specific value
    # return sorted values list
    def get_lcv_order(self, var, vals):
        lcv_vals = []
        for val in vals:
            num_possibilities = 0
            # for each unassigned neighbor, count possible values
            for neighbor in self.constraints[var].keys():
                if self.assignment[neighbor] == -1:
                    neighbor_vals = self.get_domain(neighbor)
                    for n_val in neighbor_vals:
                        if n_val != val:
                            num_possibilities += 1
            lcv_vals.append((num_possibilities, val))

        lcv_vals.sort(reverse=True, key=lambda x: x[0])
        ordered_vals = [lcv_vals[i][1] for i in range(len(lcv_vals))]

        return ordered_vals

    # check for arc consistency
    # for all binary pairs of variables
    # remove impossible values with variable domains
    # check if assignment leaves each variable with at least one possible value
    def ac_3(self):
        arc_queue = []
        # queue all binary pairs of variables
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
                        if len(left_domain) == 0:   # return false if no possible values remain
                            return False
                        changed = True

                # if domain changed, update domain and recheck ac with all neighbors of variable
                if changed:
                    self.var_domain[curr_arc[0]] = left_domain
                    for neighbor in self.constraints[curr_arc[0]].keys():
                        arc_queue.append((neighbor, curr_arc[0]))

        return True

    # recursively search through possible assignments
    # return complete assignment or empty list, if no solution exists
    def backtrack(self):
        if -1 not in self.assignment:
            return self.assignment

        var = self.get_next_var()
        vals = self.get_domain(var)

        # order values list if lcv toggled on
        if self.lcv:
            vals = self.get_lcv_order(var, vals)

        for val in vals:
            if self.is_consistent(var, val):
                self.assignment[var] = val
                arc_consistent = True
                if self.ac:
                    arc_consistent = self.ac_3()
                if arc_consistent:
                    result = self.backtrack()
                    if len(result) != 0:
                        return result
                self.assignment[var] = -1

        return []

    # start backtracking search
    def get_solution(self):
        return self.backtrack()
