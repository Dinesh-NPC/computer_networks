def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # Initialize distances
    distances[start] = 0  # Distance to the start node is 0
    visited = set()  # Keep track of visited nodes

    while len(visited) < len(graph):
        # Find the unvisited node with the smallest distance
        current_node = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node],
            default=None
        )
        if current_node is None:
            break  # All reachable nodes are visited

        visited.add(current_node)

        # Update distances for neighbors
        for neighbor, cost in graph[current_node].items():
            new_distance = distances[current_node] + cost
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances


# Example graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

# Run the algorithm
start_node = 'A'
distances = dijkstra(graph, start_node)

# Print results
print(f"Shortest distances from node {start_node}:")
for node, distance in distances.items():
    print(f"To {node}: {distance}")
