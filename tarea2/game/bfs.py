from search import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):
    def __init__(self,problem):
        super().__init__(problem)
        self.stack = [(0, [self.startState])]
        self.pastCosts[self.startState] = 0
        self.path = []
    def stateCost(self, state):
        return self.pastCosts.get(state, None)

    def step(self):
        problem = self.problem
        stack = self.stack
        if stack == []:
            return self.path
        pathCost, path= stack.pop(0)
        print(stack)
        lastState = path[-1]
        print(lastState)
        self.numStatesExplored += 1
        if problem.isEnd(lastState):
            self.stack = []
            self.path = path
            return path
        for action, newState, cost in problem.successorsAndCosts(lastState):
            if newState not in path:
                temppath = path.copy()
                temppath.append(newState)
                self.stack.append((pathCost+cost, temppath))
                print(self.stack)
                self.pastCosts[newState] = self.pastCosts[lastState]+cost
        #print(self.stack)
        return path
        
