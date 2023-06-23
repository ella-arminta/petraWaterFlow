import heapq

class Peta:
    def __init__(self):
        self.peta = {}

    def add_edge(self, source, destination, weight):
        if source not in self.peta:
            self.peta[source] = []
        if destination not in self.peta:
            self.peta[destination] = []
        self.peta[source].append((destination, weight))
        self.peta[destination].append((source, weight))

    def find_path(self, start, end):
        distances = {vertex: float('inf') for vertex in self.peta}
        distances[start] = 0
        previous = {}
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            if current_vertex == end:
                break

            for neighbor, edge_weight in self.peta[current_vertex]:
                distance = current_distance + edge_weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        current_vertex = end
        while current_vertex != start:
            path.append(current_vertex)
            current_vertex = previous[current_vertex]

        path.append(start)
        path.reverse()

        return path

    def get_cost(self, start, end):
        path = self.find_path(start, end)
        cost = 0
        for i in range(len(path) - 1):
            current_vertex = path[i]
            next_vertex = path[i + 1]
            neighbors = self.peta[current_vertex]
            for neighbor, weight in neighbors:
                if neighbor == next_vertex:
                    cost += weight
                    break

        return cost


# Example usage:
# peta = Peta()
# peta.add_edge('plantai1','plantai2',5)
# peta.add_edge('wlantai1','plantai1',10)
# path = peta.find_path('plantai2', 'wlantai1')
# print(path)  # Output: ['A', 'C', 'D']

# cost = peta.get_cost('plantai2', 'wlantai1')
# print(cost)  # Output: 7
