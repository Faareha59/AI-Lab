from collections import deque
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
def get_next_states(state):
    state = [list(row) for row in state]
    next_states = []
    i, j = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row.copy() for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            next_states.append(tuple(map(tuple, new_state)))
    return next_states
def bfs_8puzzle(start, goal):
    start_tuple = tuple(map(tuple, start))
    goal_tuple = tuple(map(tuple, goal))
    visited = set()
    queue = deque([(start_tuple, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_tuple:
            return path + [current_state]
        if current_state in visited:
            continue
        visited.add(current_state)
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))
    return None
start = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solution = bfs_8puzzle(start, goal)
print(f"Solution steps (states): {len(solution)}")
for idx, state in enumerate(solution):
    print(f"Step {idx}:")
    for row in state:
        print(row)
    print()