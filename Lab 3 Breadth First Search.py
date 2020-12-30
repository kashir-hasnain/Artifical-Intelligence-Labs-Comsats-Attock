
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.State = state
        self.Parent = parent
        self.Action = action
        self.Path_cost = path_cost

    def __eq__(self, other):
        return isinstance(other, Node) and self.State == other.State

    def __lt__(self, other):
        return  isinstance(other, Node) and self.Path_cost<other.Path_cost

    def __repr__(self):
        return "Node {} Cost {}".format(self.State, self.Path_cost)

    # Node class ends here


class Problem:
    def __init__(self, start, goal):
        self.Initial_state = start
        self.Goal_state = goal
        self.State_space = dict()
        self.Step_cost = dict()

        # self.State_space['Arad'] = {'a': 'Zeind', 'b': 'Sibiu', 'c': 'Timisor'}
        # self.Step_cost['Arad'] = {'a': 75, 'b': 140, 'c': 118}

        self.State_space['Arad'] = {'a': 'Zerind', 'b': 'Sibui', 'c': 'Timisoara'}
        self.Step_cost['Arad'] = {'a': 75, 'b': 140, 'c': 118}

        self.State_space['Zerind'] = {'a': 'Arad', 'b': 'Oradea'}
        self.Step_cost['zerid'] = {'a': 75, 'b': 71}

        self.State_space['Oradea'] = {'a': 'Sibiu', 'b': 'Zerind'}
        self.Step_cost['Oradea'] = {'a': 151, 'b': 71}

        self.State_space['Sibiu'] = {'a': 'Arad', 'b': 'Oradea', 'c': 'Rimnicu Vilcea', 'd': 'Fagaras'}
        self.Step_cost['Sibiu'] = {'a': 140, 'b': 151, 'c': 80, 'd': 99}

        self.State_space['Timisoara'] = {'a': 'Arad', 'b': 'Lugoj'}
        self.Step_cost['Timisoara'] = {'a': 118, 'b': 111}

        self.State_space['Lugoj'] = {'a': 'Timisoara', 'b': 'Mehadia'}
        self.Step_cost['Lugoj'] = {'a': 111, 'b': 70}

        self.State_space['Mehadia'] = {'a': 'Lugoj', 'b': 'Drobeta'}
        self.Step_cost['Mehadia'] = {'a': 70, 'b': 75}

        self.State_space['Drobeta'] = {'a': 'Mehadia', 'b': 'Craiova'}
        self.Step_cost['Drobeta'] = {'a': 75, 'b': 120}

        self.State_space['Craiova'] = {'a': 'Drobeta', 'b': 'Rimnicu Vilcea', 'c': 'Pitesti'}
        self.Step_cost['Craiova'] = {'a': 120, 'b': 146, 'c': 138}

        self.State_space['Rimnicu Vilcea'] = {'a': 'Sibiu', 'b': 'Craiova', 'c': 'Pitesti'}
        self.Step_cost['Rimnicu Vilcea'] = {'a': 80, 'b': 146, 'c': 97}

        self.State_space['Pitesti'] = {'a': 'Rimnicu Vilcea', 'b': 'Craiova', 'c': 'Bucharest'}
        self.Step_cost['Pitesti'] = {'a': 97, 'b': 138, 'c': 101}

        self.State_space['Fagaras'] = {'a': 'Sibiu', 'b': 'Bucharest'}
        self.Step_cost['Fagaras'] = {'a': 99, 'b': 211}

        self.State_space['Bucharest'] = {'a': 'Fagaras', 'b': 'Giurgiu', 'c': 'Pitesti', 'd': 'Urziceni'}
        self.Step_cost['Bucharest'] = {'a': 211, 'b': 90, 'c': 101, 'd': 85}

        self.State_space['Giurgiu'] = {'a': 'Bucharest'}
        self.Step_cost['Giurgiu'] = {'a': 90}

        self.State_space['Urziceni'] = {'a': 'Bucharest', 'b': 'Hirsova', 'c': 'Vaslui'}
        self.Step_cost['Urziceni'] = {'a': 85, 'b': 98, 'c': 142}

        self.State_space['Hirsova'] = {'a': 'Urziceni', 'b': 'Eforie'}
        self.Step_cost['Hirsova'] = {'a': 98, 'b': 86}

        self.State_space['Eforie'] = {'a': 'Hirsova'}
        self.Step_cost['Eforie'] = {'a': 86}

        self.State_space['Vaslui'] = {'a': 'Iasi', 'b': 'Urziceni'}
        self.Step_cost['Vaslui'] = {'a': 92, 'b': 142}

        self.State_space['Iasi'] = {'a': 'Vaslui', 'b': 'Neamt'}
        self.Step_cost['Iasi'] = {'a': 92, 'b': 87}

        self.State_space['Neamt'] = {'a': 'Iasi'}
        self.Step_cost['Neamt'] = {'a': 87}

    def goal_test(self, state):
        return self.Goal_state == state

    def actions(self, state):
        return self.State_space[state].keys()

    def result(self, state, action):
        # at given state and action what will be next state
        return self.State_space[state][action]

    def path_cost(self, state, action):
        return self.Step_cost[state][action]

# Problem class ends here


def child_node(problem, parent, action):
    next_state = problem.result(parent.state, action)
    step_cost = problem.path_cost(parent.state, action)
    return Node(next_state, parent, action, parent.Path_cost + int(step_cost))


def solution(node):
    path_back = list()
    while node:
        path_back.append(node)
        node = node.Parent

    # for node in path_back.reverse():
    for node in reversed(path_back):
        print(node)

def main():
    node1 = Node('Arad')
    node2 = Node('Zerand', node1, 'a', 75)
    node3 = Node('Zerand', node1, 'a', 75)
    print(node2)
    print(node1 < node2)

    problem = Problem('Arad', 'Bucharest')
    print(problem.result('Arad', 'a'))
    print(problem.actions('Arad'), problem.actions('Sibiu'))
    print(problem.path_cost('Arad', 'a'))



if __name__ == "__main__":
    main()
