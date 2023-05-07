# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    node = {"state": problem.getStartState(), "pathcost": 0}
    if problem.isGoalState(node["state"]):
        return node[""]

    # Stack is LIFO
    stack = util.Stack()
    stack.push(node)

    visited = []

    while True:
        if stack.isEmpty():
            raise ValueError("Queue is empty.")
        node = stack.pop()
        visited.append(node["state"])
        #    print("###############")
        #    print(problem.getStartState())
        #    print(problem.getStartState)
        #   print("###############")
        #      for each action in problem.ACTIONS(node.STATE) do
        for successor in problem.getSuccessors(node["state"]):
            child = {
                "state": successor[0],
                "direction": successor[1],
                "pathcost": successor[2],
                "parent": node,
            }
            if child["state"] not in visited:
                # LOOP SOLUTIONS
                if problem.isGoalState(child["state"]):
                    directions = []
                    node = child
                    while "parent" in node:
                        directions.append(node["direction"])
                        node = node["parent"]
                    directions.reverse()
                    return directions

                # RECURSIVE SOLUTIONS
                if problem.isGoalState(child["state"]):
                    directions = []
                    node = child
                    if "parent" in node:
                        recursivePathFinder(node, directions)
                    directions.reverse()
                    return directions

                stack.push(child)


def depthFirstSearchRecursive(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    node = {"state": problem.getStartState(), "pathcost": 0}
    if problem.isGoalState(node["state"]):
        return node[""]

    # Stack is LIFO
    stack = util.Stack()
    stack.push(node)

    # Visited array
    visited = []

    while True:
        if stack.isEmpty():
            raise ValueError("Queue is empty.")
        node = stack.pop()
        visited.append(node["state"])
        #    print("###############")
        #    print(problem.getStartState())
        #    print(problem.getStartState)
        #   print("###############")
        #      for each action in problem.ACTIONS(node.STATE) do
        for successor in problem.getSuccessors(node["state"]):
            child = {
                "state": successor[0],
                "direction": successor[1],
                "pathcost": successor[2],
                "parent": node,
            }
            if child["state"] not in visited:
                # RECURSIVE SOLUTIONS
                if problem.isGoalState(child["state"]):
                    directions = []
                    node = child
                    if "parent" in node:
                        recursivePathFinder(node, directions)
                    directions.reverse()
                    return directions
                stack.push(child)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
    #    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    node = {"state": problem.getStartState(), "pathcost": 0}
    #    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if problem.isGoalState(node["state"]):
        # will be back
        return []
    #    frontier ← a FIFO queue with node as the only element
    queue = util.Queue()
    queue.push(node)
    #    explored ← an empty set
    visited = []
    #    loop do
    while True:
        #      if EMPTY?(frontier) then return failure
        if queue.isEmpty():
            raise ValueError("Queue is empty.")
        #      node ← POP(frontier) /* chooses the shallowest node in frontier */
        node = queue.pop()
        #      add node.STATE to explored
        visited.append(node["state"])
        #    print("###############")
        #    print(problem.getStartState())
        #    print(problem.getStartState)
        #   print("###############")
        #      for each action in problem.ACTIONS(node.STATE) do
        for successor in problem.getSuccessors(node["state"]):
            #         child ← CHILD-NODE(problem,node,action)
            #        print(successor)
            #        print(node)
            child = {
                "state": successor[0],
                "direction": successor[1],
                "pathcost": successor[2],
                "parent": node,
            }
            #         if child.STATE is not in explored or frontier then
            if child["state"] not in visited:
                #            if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                # LOOP SOLUTIONS
                if problem.isGoalState(child["state"]):
                    directions = []
                    node = child
                    while "parent" in node:
                        directions.append(node["direction"])
                        node = node["parent"]
                    directions.reverse()
                    return directions
                # frontier ← INSERT(child,frontier)
                queue.push(child)


def breadthFirstSearchRecursive(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
    #    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    node = {"state": problem.getStartState(), "pathcost": 0}
    #    if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if problem.isGoalState(node["state"]):
        # will be back
        return node[""]
    #    frontier ← a FIFO queue with node as the only element
    queue = util.Queue()
    queue.push(node)
    #    explored ← an empty set
    visited = []
    #    loop do
    while True:
        #      if EMPTY?(frontier) then return failure
        if queue.isEmpty():
            raise ValueError("Queue is empty.")
        #      node ← POP(frontier) /* chooses the shallowest node in frontier */
        node = queue.pop()
        #      add node.STATE to explored
        visited.append(node["state"])
        #    print("###############")
        #    print(problem.getStartState())
        #    print(problem.getStartState)
        #   print("###############")
        #      for each action in problem.ACTIONS(node.STATE) do
        for successor in problem.getSuccessors(node["state"]):
            #         child ← CHILD-NODE(problem,node,action)
            #        print(successor)
            #        print(node)
            child = {
                "state": successor[0],
                "direction": successor[1],
                "pathcost": successor[2],
                "parent": node,
            }
            #         if child.STATE is not in explored or frontier then
            if child["state"] not in visited:
                #            if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)

                # RECURSIVE SOLUTIONS
                if problem.isGoalState(child["state"]):
                    directions = []
                    node = child
                    if "parent" in node:
                        recursivePathFinder(node, directions)
                    directions.reverse()
                    return directions
                #            frontier ← INSERT(child,frontier)
                queue.push(child)


# RECURSIVE SOLUTIONS FUNCTION
def recursivePathFinder(node, directions):
    if "direction" in node:
        directions.append(node["direction"])
    if "parent" in node:
        recursivePathFinder(node["parent"], directions)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    """
    function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
         node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
         frontier ← a priority queue ordered by PATH-COST, with node as the only element
         explored ← an empty set
         loop do
           if EMPTY?(frontier) then return failure
           node ← POP(frontier) /* chooses the lowest-cost node in frontier */
           if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
           add node.STATE to explored
           for each action in problem.ACTIONS(node.STATE) do
              child ← CHILD-NODE(problem,node,action)
              if child.STATE is not in explored or frontier then
                 frontier ← INSERT(child,frontier)
              else if child.STATE is in frontier with higher PATH-COST then
                 replace that frontier node with child
    """

    node = {"state": problem.getStartState(),"directions": [] ,"pathcost": 0}

    if problem.isGoalState(node["state"]):
        return node[""]

    priorityqueue = util.PriorityQueue()
    priorityqueue.push(node,node["pathcost"])

    visited = []

    while True:
        if priorityqueue.isEmpty():
            raise ValueError("Priority queue is empty.")
        node = priorityqueue.pop()

        if node["state"] not in visited:
            visited.append(node["state"])
            if problem.isGoalState(node["state"]):
                return node["directions"]
        #    print("###############")
        #    print(problem.getStartState())
        #    print(problem.getStartState)
        #   print("###############")
            print(node["state"])
            for successor in problem.getSuccessors(node["state"]):
                
                newDirections = node["directions"] + [successor[1]]
                newCost = problem.getCostOfActions(newDirections) 

                child = {
                    "state": successor[0],
                    "directions": newDirections,
                    "pathcost": newCost,
                    "parent": node,
                }

                priorityqueue.push(child,newCost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem=None):
    """
    Heuristic calculation by using Manhattan Calculation.
    """
    return util.manhattanDistance( state, problem.getStartState())

def aStarSearch(problem, heuristic=manhattanHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    node = {"state": problem.getStartState(),"directions": [] ,"pathcost":  heuristic(problem.getStartState(), problem)}

    # ilk state bizim istediğimiz state mi kontrolü
    if problem.isGoalState(node["state"]):
        return []

    # priority queue kullanılıyor (arkada queue prioritysine göre sıralamasını heapsort yapıyor. Sıralama ikinci verilen argüman olan pathcosta göre yapılır.)
    # heapsort küçükten büyüğe sıralar bu yüzden her zaman en kısa yol queue tepesindedir ve poplandığında en kısa yol alınır
    priorityqueue = util.PriorityQueue()
    priorityqueue.push(node,node["pathcost"])# (arg1 sıralancak şey, arg2 priority == cost ne kadar düşük olduğu)

    # visited
    visited = []

    while True:
        # queue boş kontrol
        if priorityqueue.isEmpty():
            raise ValueError("Priority queue is empty.")
        # queue başındaki elemanın alınması
        node = priorityqueue.pop()

        # elemanın gidilip gidilmediğinin kontrolü
        if node["state"] not in visited:
            # elemana gittim arrayi
            visited.append(node["state"])
            # bu eleman benim aradığım eleman mı ?
            # bütün yollar directionsta gönder yolu
            if problem.isGoalState(node["state"]):
                return node["directions"]
            
            # olduğum konumdan nerelere gideceğim 
            for successor in problem.getSuccessors(node["state"]):

                newDirections = node["directions"] + [successor[1]]
                newCost = problem.getCostOfActions(newDirections) + heuristic(successor[0], problem)
                print(newCost)
                child = {
                    "state": successor[0],
                    "directions": newDirections,
                    "pathcost": newCost,
                    "parent": node,
                }

                priorityqueue.push(child,newCost)


# Abbreviations
bfs = breadthFirstSearch
bfsr = breadthFirstSearchRecursive
dfs = depthFirstSearch
dfsr = depthFirstSearchRecursive
astar = aStarSearch
ucs = uniformCostSearch
