# import mapping as map
import heapq

data = {
            # x, y, g, f, h
    "heu": [],
    # "g": [[], []],
    # "f": [[], []],
    # "h": [[], []],
    "path": [[], []]
}


def calculate_heuristic(current, goal):
    # Manhattan heuristic
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def getNeighbors(cell, maze):
    # Get the valid neighboring cells for a given cell in the maze
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for direction in directions:
        row, col = cell[0] + direction[0], cell[1] + direction[1]
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1:
            neighbors.append((row, col))

    return neighbors

def getPath(lastPos, goal):
    # Reconstruct and print the shortest path from start to goal
    current = goal
    path = [current]

    while current in lastPos:
        current = lastPos[current]
        path.append(current)

    path.reverse()
    return path

def printPath(path):
    for cell in path:
        print(cell)

def a_star(maze):
    rows, cols = len(maze), len(maze[0])
    start, goal = None, None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goal = (i, j)

    open_set = []
    heapq.heappush(open_set, (0, start))
    g_scores = [[float('inf')] * cols for _ in range(rows)]
    g_scores[start[0]][start[1]] = 0
    f_scores = [[float('inf')] * cols for _ in range(rows)]
    f_scores[start[0]][start[1]] = calculate_heuristic(start, goal)
    h_scores = [[calculate_heuristic((i, j), goal) for j in range(cols)] for i in range(rows)]
    came_from = {}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            path = getPath(came_from, goal)
            # printPath(path)
         
            #append here
            data["path"].append(path)
 
            for i in range(len(g_scores)):
                heur = [[],[],[],[],[]]
                for j in range(len(g_scores[0])):
                    g = g_scores[i][j]
                    h = h_scores[i][j]
                    f = f_scores[i][j]
                
                    heur = [i, j, g, h, f]
            
                    # print(heur)
                    data["heu"].append(heur)

            break

        neighbors = getNeighbors(current, maze)

        for neighbor in neighbors:
            tentative_g_score = g_scores[current[0]][current[1]] + 1

            if tentative_g_score < g_scores[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current
                g_scores[neighbor[0]][neighbor[1]] = tentative_g_score
                f_scores[neighbor[0]][neighbor[1]] = tentative_g_score + h_scores[neighbor[0]][neighbor[1]]
                heapq.heappush(open_set, (f_scores[neighbor[0]][neighbor[1]], neighbor))


    return data

    