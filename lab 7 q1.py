from collections import deque
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    return new_path
            visited.add(node)
    return None
graph = {
    "A": ["B", "C", "H"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C", "E", "F"],
    "E": ["D", "G", "H"],
    "F": ["D", "G"],
    "G": ["E", "F"],
    "H": ["A", "E"]
}
start_node = "A"
goal_node = "G"
shortest_path = bfs_shortest_path(graph, start_node, goal_node)
print(f"Shortest path from {start_node} to {goal_node}: {shortest_path}")