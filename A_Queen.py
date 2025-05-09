import heapq

# Heuristic: count conflicts (same column or diagonal)
def count_conflicts(state):
    conflicts = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return conflicts

# A* for N-Queens
def solve_n_queens(n):
    # Priority queue: (f(n), g(n), state)
    heap = []
    heapq.heappush(heap, (0, 0, []))

    while heap:
        f, g, state = heapq.heappop(heap)

        if g == n:
            return state  # Goal reached

        for col in range(n):
            new_state = state + [col]
            h = count_conflicts(new_state)
            heapq.heappush(heap, (g + 1 + h, g + 1, new_state))

    return None  # No solution

# Display solution
def print_board(state):
    n = len(state)
    for row in range(n):
        line = ''
        for col in range(n):
            if state[row] == col:
                line += 'Q '
            else:
                line += '. '
        print(line)
    print()

# Run the program
if __name__ == "__main__":
    n = int(input("Enter value of N for N-Queens: "))
    solution = solve_n_queens(n)
    if solution:
        print("\nSolution Found:")
        print_board(solution)
    else:
        print("No solution exists.")
