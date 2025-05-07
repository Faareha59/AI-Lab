romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}
def dfs_path(graph, start, goal, path=None, visited=None, total_distance=0):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path = path + [start]
    visited.add(start)

    if start == goal:
        return (path, total_distance)

    min_path = None
    min_distance = float('inf')

    for neighbor, distance in graph[start]:
        if neighbor not in visited:
            new_total = total_distance + distance
            result = dfs_path(graph, neighbor, goal, path, visited.copy(), new_total)
            if result is not None:
                result_path, result_distance = result
                if result_distance < min_distance:
                    min_distance = result_distance
                    min_path = result_path

    return (min_path, min_distance) if min_path else None
path, total_distance = dfs_path(romania_map, 'Arad', 'Bucharest')

print("DFS Path from Arad to Bucharest:")
print(" -> ".join(path))
print(f"Total Distance: {total_distance}")