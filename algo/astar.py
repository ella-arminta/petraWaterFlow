import heapq

def calculate_heuristic(current, goal):
    # Calculate the Manhattan distance heuristic between two cells
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def get_neighbors(cell, maze):
    # Get the valid neighboring cells for a given cell in the maze
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for direction in directions:
        row, col = cell[0] + direction[0], cell[1] + direction[1]
        if 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1:
            neighbors.append((row, col))

    return neighbors

def print_path(came_from, goal):
    # Reconstruct and print the shortest path from start to goal
    current = goal
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
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
            print_path(came_from, goal)
            print('g : ',g_scores) # jarak dr skrg ke start
            print('h: ',h_scores) # h itu jarak estimasi dr sekarang ke goal
            print('f: ',f_scores)
            break

        neighbors = get_neighbors(current, maze)

        for neighbor in neighbors:
            tentative_g_score = g_scores[current[0]][current[1]] + 1

            if tentative_g_score < g_scores[neighbor[0]][neighbor[1]]:
                came_from[neighbor] = current
                g_scores[neighbor[0]][neighbor[1]] = tentative_g_score
                f_scores[neighbor[0]][neighbor[1]] = tentative_g_score + h_scores[neighbor[0]][neighbor[1]]
                heapq.heappush(open_set, (f_scores[neighbor[0]][neighbor[1]], neighbor))

maze = [
    [2, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 3]
]

a_star(maze)