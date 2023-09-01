from search import *

class WolfGoatCabbage(Problem):
    def __init__(self):
        self.initial = frozenset({'F', 'G', 'W', 'C'})
        self.goal = frozenset()
        
    def is_valid_state(self, state):
        # Check if the wolf is eating the goat
        if 'W' in state and 'G' in state and 'F' not in state:
            return False
        # Check if the goat is eating the cabbage
        if 'G' in state and 'C' in state and 'F' not in state:
            return False
        return True

    def actions(self, state):
        """
        Returns a list of possible actions that can be executed in the given state.
        There are four possible actions in any given state of the environment.
        """
        possible_actions = []
        new_state = list(state)

        # Check whether 'F' is on the left or right side of the river
        if 'F' in new_state:
            # 'F' is on the left side of the river
            new_state.remove('F')
            for item in new_state:
                temp_state = list(new_state)
                temp_state.remove(item)
                if self.is_valid_state(temp_state):
                    possible_actions.append({'F', item})
        else:
            # 'F' is on the right side of the river
            right_side = ['C', 'G', 'W']
            for item in new_state:
                right_side.remove(item)
            if self.is_valid_state(right_side):
                possible_actions.append({'F',})
            else:
                for item in right_side:
                    temp_state = list(right_side)
                    temp_state.remove(item)
                    if self.is_valid_state(temp_state):
                        possible_actions.append({'F', item})

        return possible_actions

    
    def result(self,state, action):
        """
        Given state and action, returns a new state that is the result of the action.
        Assumes that the action is valid in the state.
        """

        # If the action is not present in the state, add it to the state
        # If the action is present in the state, remove it from the state
        new_state = set(state)
        for item in action:
            if item in new_state:
                new_state.remove(item)
            else:
                new_state.add(item)
        
        return frozenset(new_state)

        
    def goal_test(self, state):
        return state == self.goal
    



if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)