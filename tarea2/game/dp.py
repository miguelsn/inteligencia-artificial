from search import SearchAlgorithm

class DynamicProgramming(SearchAlgorithm):
    def __init__(self, problem):
        super().__init__(problem)
        self.backrefs = {}
        self.futureCost = {}
        self.futureFrontier = [problem.endState()]
        self.currentState = problem.startState()
        self.startState = problem.startState()
        self.finished = False

    def futureCosts(self):
        if len(self.futureFrontier) == 0:
            return None
        
        state = self.futureFrontier.pop(0)

        if self.problem.isEnd(state):
            self.futureCost[state] = 0
            for _, previousState, _ in self.problem.successorsAndCosts(state):
                self.futureFrontier.append(previousState)
        elif state not in self.futureCost:
            visited = []
            for _, nextState, nextCost in self.problem.successorsAndCosts(state):
                if nextState in self.futureCost:
                    visited.append((nextState, nextCost))
                else:
                    self.futureFrontier.append(nextState)
            self.futureCost[state] = min(nextCost + self.futureCost[nextState] for nextState, nextCost in visited)
        
        return self.futureCost[state]
    
    def stateCost(self, state):
        return self.futureCost.get(state, None)
    
    def path(self, state):
        path = []
        while state != self.problem.startState():
            _, prevState = self.backrefs[state]
            path.append(state)
            state = prevState
        path.reverse()
        return path
    
    def step(self):
        if self.finished == True:
            return self.path(self.currentState)
        
        problem = self.problem
        backrefs = self.backrefs
        state = self.currentState

        path = self.path(state)

        if problem.isEnd(state):
            self.finished = True
            return path

        if state not in self.futureCost:
            for _ in range(len(self.futureFrontier)):
                self.futureCosts()
            return path
        
        nextState = state
        best = None

        for action, next, _ in problem.successorsAndCosts(state):
            if self.futureCost[next] < self.futureCost[nextState]:
                nextState = next
                best = action
            
        backrefs[nextState] = (best, state)
        self.currentState = nextState
        return path