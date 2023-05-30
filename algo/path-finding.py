import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

class AStarSearch:
    def __init__(self, start_node, goal_node_name):
        self.start_node = start_node
        self.goal_node_name = goal_node_name

    def calculate_heuristic(self, node):
        # Calculate the heuristic (estimated cost) from the current node to the goal node
        # Replace this with your specific heuristic calculation logic
        return 0

    def search(self):
        open_list = []
        heapq.heappush(open_list, (0, self.start_node))

        # Cost from start node to each explored node
        g_score = {self.start_node: 0}

        # Estimated total cost from start node to goal node via each explored node
        f_score = {self.start_node: self.calculate_heuristic(self.start_node)}

        while open_list:
            current_node = heapq.heappop(open_list)[1]

            if current_node.name == self.goal_node_name:
                # Goal node reached
                return current_node

            for neighbor, cost in current_node.neighbors.items():
                # Calculate the tentative g_score for the neighbor node
                tentative_g_score = g_score[current_node] + cost

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Update g_score and f_score for the neighbor node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.calculate_heuristic(neighbor)

                    # Add the neighbor node to the open list with the updated f_score
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        # Goal node not found
        return None


# Create nodes and define their neighbors and costs
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")

nodeA.add_neighbor(nodeB, 5)
nodeA.add_neighbor(nodeC, 3)
nodeB.add_neighbor(nodeD, 2)
nodeC.add_neighbor(nodeD, 8)
nodeC.add_neighbor(nodeE, 4)
nodeD.add_neighbor(nodeE, 6)

# Create an instance of AStarSearch with the start node and goal node name
search = AStarSearch(nodeA, "E")

# Perform the A* search
result = search.search()

if result:
    print("Goal node found:", result.name)
else:
    print("Goal node not found")