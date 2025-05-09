import heapq

# Goal state
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Get position of zero (empty space)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Heuristic: number of misplaced tiles
def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Get all valid neighbors (moves)
def get_neighbors(state):
    neighbors = []
    i, j = find_zero(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [list(row) for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

# A* algorithm
def a_star(start_state):
    open_list = []
    heapq.heappush(open_list, (misplaced_tiles(start_state), 0, start_state, []))
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_path = path + [state]
                heapq.heappush(open_list, (g + 1 + misplaced_tiles(neighbor), g + 1, neighbor, new_path))

    return None

# Pretty print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(x) for x in row))
    print()

# Sample start state
start = ((1, 2, 3), (4, 0, 6), (7, 5, 8))

# Run the algorithm
solution = a_star(start)

# Show steps
if solution:
    print("Steps to reach goal:")
    for step in solution:
        print_state(step)
else:
    print("No solution found.")