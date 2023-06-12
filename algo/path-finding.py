import heapq, math

class Node:
    def __init__(self, name, x, y, heuristic_cost):
        self.name = name
        self.x = x
        self.y = y
        self.heuristic_cost = heuristic_cost
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append((neighbor))

    def calculate_distance(nodeA, nodeB):
        return math.sqrt(pow((nodeA.x - nodeB.x),2) + pow((nodeA.y - nodeB.start_y),2))
    
def a_star_search(start_node, goal_name):
    open_list = [(start_node.heuristic_cost, 0, start_node)]  # Priority queue of nodes
    visited = set()  # Set to keep track of visited nodes

    while open_list:
        _, total_cost, current_node = heapq.heappop(open_list)
        visited.add(current_node)

        if current_node.name == goal_name:
            return current_node

        for neighbor, distance in current_node.neighbors:
            if neighbor not in visited:
                neighbor_cost = total_cost + distance
                heuristic_cost = neighbor_cost + neighbor.heuristic_cost
                heapq.heappush(open_list, (heuristic_cost, neighbor_cost, neighbor))

        print(f"Current node: {current_node.name}, Total cost: {total_cost}")

    return None  # Goal not found

# Example usage
# Create the graph/map
A = Node('A', 5, 10)
B = Node('B', 3, 5)
C = Node('C', 1, 2)
D = Node('D', 8,9)
E = Node('E', 0,7)

# Define the connections
A.add_neighbor(B)
A.add_neighbor(C)
B.add_neighbor(D)
C.add_neighbor(D)
C.add_neighbor(E)
D.add_neighbor(E)

# Perform A* search
goal_name = 'E'
start_node = A
goal_node = a_star_search(start_node, goal_name)

if goal_node:
    print(f"Goal node '{goal_name}' found!")
else:
    print(f"Goal node '{goal_name}' not found.")
