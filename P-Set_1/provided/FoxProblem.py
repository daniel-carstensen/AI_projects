class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.current_state = start_state
        self.goal_state = (0, 0, 0)

        self.num_foxes = self.start_state[0]
        self.num_chicken = self.start_state[1]

    def is_permitted(self, state):
        cs_foxes = state[1]
        cs_chicken = state[0]
        if cs_foxes > cs_chicken:
            if cs_chicken != 0:
                return False

        if (self.num_foxes - cs_foxes) > (self.num_chicken - cs_chicken):
            if (self.num_chicken - cs_chicken) != 0:
                return False

        return True

    # get successor states for the given state
    def get_successors(self, state):
        successor_states = []
        cs_foxes = state[1]
        cs_chicken = state[0]

        fs_foxes = self.num_foxes - cs_foxes
        fs_chicken = self.num_chicken - cs_chicken

        boat = state[2]

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

    def test_goal(self, state):
        if state == self.goal_state:
            return True

        return False

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
