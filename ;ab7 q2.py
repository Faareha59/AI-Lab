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

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

print("DFS Traversal:")
dfs(visited, graph, "A")