#Sean McCarthy
from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):


    def __init__(self, initial={'F', 'G', 'C', 'W'}, goal=set()):
        """ Define goal state and initialize a problem """
        super().__init__(frozenset(initial) , goal)

    def goal_test(self, state):
        
        return state == self.goal

    def find_direction(self, state):
        """Return the index of the blank square in a given state"""
        for x in state:
            if x == 'F':
                return "RIGHT"
            else:
                return "LEFT"
    
    def result(self, state, action):
        new_state = list(state)
        if (self.find_direction(state) == "RIGHT"):
            for x in action:
                new_state.pop(new_state.index(x))
        else:
            for x in action:
                new_state.append(x)
        return_set = frozenset(new_state) 
        return return_set

    def actions(self, state):
        characters = {'F', 'G', 'C', 'W'}
        left = set()
        valid_actions = []
        for x in characters:
            for x in state:
                left.add(x)

        if(self.find_direction(state) == "RIGHT"):
            if(left == {'F', 'G', 'C', 'W'}):
               valid_actions.append({'F','G'})
            elif(left == {'F', 'W', 'C'}):
                valid_actions.append({'F','W'})
                valid_actions.append({'F','C'})
                valid_actions.append({'F'})
            elif(left == {'F', 'G', 'C'}):
                valid_actions.append({'F','C'})
                valid_actions.append({'F','G'})
            elif(left == {'F', 'W', 'G'}):
                valid_actions.append({'F', 'W'})
                valid_actions.append({'F','G'})
            elif(left == {'F','G'}):
                valid_actions.append({'F','G'})
                valid_actions.append({'F'})
        else:
            if(left == {'W', 'C'}):
                valid_actions.append({'F'})
                valid_actions.append({'F','G'})
            elif(left == {'C'}):
                valid_actions.append({'F','W'})
                valid_actions.append({'F','G'})
            elif(left == {'W'}):
                valid_actions.append({'F','C'})
                valid_actions.append({'F','G'})
            elif(left == {'G'}):
                valid_actions.append({'F','W'})
                valid_actions.append({'F','C'})
                valid_actions.append({'F'})
        return valid_actions



if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
    
#    print(wgc.goal_test({"W"}))
#    print(wgc.goal_test(frozenset()))
#    print(wgc.find_direction({"F"}))
#    print(wgc.find_direction({"W"}))
#    print(wgc.result({"F","G"}, {"F","G"}))
#    print(wgc.result(set(),{"F","W"}))
#    print(wgc.actions({"G"}))
    