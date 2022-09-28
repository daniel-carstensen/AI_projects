# Author : Daniel Carstensen
# Date : 09/29/2022
# File name : FoxProblem
# Class : COSC76
# Purpose : Create a state space representation of the Chicken and Fox Problem

class FoxProblem:
    # represent state in the problem as a triple indicating the number of chicken and foxes on the close shore,
    # as well as the location of the boat as a binary

    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.current_state = start_state
        self.goal_state = (0, 0, 0)  # the goal is to bring all chicken and foxes across the river

        # total number of chicken and foxes
        self.num_foxes = self.start_state[0]
        self.num_chicken = self.start_state[1]

    # method to evaluate if an action is legal, i.e. the foes don't outnumber the chicken
    def is_permitted(self, state):
        cs_foxes = state[1]
        cs_chicken = state[0]

        # close shore
        if cs_foxes > cs_chicken:
            if cs_chicken != 0:
                return False

        # far shore
        if (self.num_foxes - cs_foxes) > (self.num_chicken - cs_chicken):
            if (self.num_chicken - cs_chicken) != 0:
                return False

        return True

    # get successor states for the given state
    def get_successors(self, state):
        successor_states = []

        # close shore
        cs_foxes = state[1]
        cs_chicken = state[0]

        # far shore
        fs_foxes = self.num_foxes - cs_foxes
        fs_chicken = self.num_chicken - cs_chicken

        boat = state[2]

        # possible actions if the boat is on the far shore
        if boat == 0:
            if fs_foxes > 0:
                new_state = (cs_foxes + 1, cs_chicken, 1)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

                if fs_foxes > 1:
                    new_state = (cs_foxes + 2, cs_chicken, 1)
                    if self.is_permitted(new_state):
                        successor_states.append(new_state)

            if fs_chicken > 0:
                new_state = (cs_foxes, cs_chicken + 1, 1)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

                if fs_chicken > 1:
                    new_state = (cs_foxes, cs_chicken + 2, 1)
                    if self.is_permitted(new_state):
                        successor_states.append(new_state)

            if fs_foxes > 0 and fs_chicken > 0:
                new_state = (cs_foxes + 1, cs_chicken + 1, 1)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

        # possible actions if the boat is on the close shore
        else:
            if cs_foxes > 0:
                new_state = (cs_foxes - 1, cs_chicken, 0)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

                if cs_foxes > 1:
                    new_state = (cs_foxes - 2, cs_chicken, 0)
                    if self.is_permitted(new_state):
                        successor_states.append(new_state)

            if cs_chicken > 0:
                new_state = (cs_foxes, cs_chicken - 1, 0)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

                if cs_chicken > 1:
                    new_state = (cs_foxes, cs_chicken - 2, 0)
                    if self.is_permitted(new_state):
                        successor_states.append(new_state)

            if cs_foxes > 0 and cs_chicken > 0:
                new_state = (cs_foxes - 1, cs_chicken - 1, 0)
                if self.is_permitted(new_state):
                    successor_states.append(new_state)

        return successor_states

    # method to test of a given state is the goal state
    def test_goal(self, state):
        if state == self.goal_state:
            return True

        return False

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
