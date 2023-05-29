from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
        self.priority = cost + heuristic

    def __lt__(self, other):
        return self.priority < other.priority

def vacuum_world_a_star():
    actions = ['Left', 'Right', 'Clean']
    goal_state = ['Clean', 'Clean']

    def h(state):
        # Heuristic function - number of dirty tiles
        return sum(1 for tile in state if tile == 'Dirty')

    def get_successors(state):
        successors = []
        successors.append(('Left', [state[0], state[1]]))
        successors.append(('Right', [state[0], state[1]]))
        successors.append(('Clean', [state[0], state[1]]))
        return successors

    def print_state(state):
        print("Current State:")
        print("Tile 1:", state[0])
        print("Tile 2:", state[1])
        print()

    def get_user_action():
        while True:
            action = input("Enter action (Left, Right, Clean): ")
            if action in actions:
                return action
            else:
                print("Invalid action. Please try again.")

    start_state = []
    start_state.append(input("Enter state for Tile 1 (Dirty or Clean): "))
    start_state.append(input("Enter state for Tile 2 (Dirty or Clean): "))
    print()

    start_node = Node(start_state)
    frontier = PriorityQueue()
    frontier.put(start_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()

        if current_node.state == goal_state:
            # Goal state found, construct the path
            path = []
            while current_node.parent:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path

        explored.add(tuple(current_node.state))

        print_state(current_node.state)

        successors = get_successors(current_node.state)
        for action, successor_state in successors:
            successor_node = Node(successor_state, current_node, action, current_node.cost + 1, h(successor_state))
            if tuple(successor_node.state) not in explored:
                frontier.put(successor_node)

        action = get_user_action()
        print()

        successor_state = [current_node.state[0], current_node.state[1]]
        if action == 'Left':
            successor_state[0] = 'Clean'
        elif action == 'Right':
            successor_state[1] = 'Clean'
        elif action == 'Clean':
            successor_state[0] = 'Clean'
            successor_state[1] = 'Clean'

        successor_node = Node(successor_state, current_node, action, current_node.cost + 1, h(successor_state))
        frontier.put(successor_node)

    return None

# Example usage
path = vacuum_world_a_star()
if path is None:
    print("Goal state not reachable!")
else:
    print("Path to goal state:")
    for action, state in path:
        print(f"Action: {action}, State: {state}")
