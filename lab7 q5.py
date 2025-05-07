import heapq
def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start))

    came_from = {}
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0

    while open_set:
        current_f, current_g, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], current_g

        for neighbor, weight in graph[current_node]:
            tentative_g = current_g + weight
            if tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None, float('inf')
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 2)],
    'C': [('A', 3), ('D', 4)],
    'D': [('B', 2), ('C', 4), ('E', 5)],
    'E': []
}
heuristic = {
    'A': 8,
    'B': 7,
    'C': 5,
    'D': 5,
    'E': 0
}

start = 'A'
goal = 'E'

path, total_cost = a_star(graph, start, goal, heuristic)

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", total_cost)