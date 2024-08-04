import heapq
from data.lesmis_graph import graph
from helpers.draw import draw_graph

def dijkstra(g, start):
    distances = {node: float('infinity') for node in g}
    distances[start] = 0

    heap = [(0, start)]

    paths = {node: [] for node in g}

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, attr in g[current_vertex].items():
            weight = attr['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

                paths[neighbor] = paths[current_vertex] + [current_vertex]

    return distances, paths


if __name__ == "__main__":
    draw_graph(graph)

    start_vertex = 'Valjean'

    shortest_distances, shortest_paths = dijkstra(graph, start_vertex)

    for vertex, distance in sorted(shortest_distances.items(), key=lambda x: x[1]):
        path = shortest_paths[vertex] + [vertex]
        print(f"Shortest path from {start_vertex} to {vertex}: {distance:.2f}, Path: {path}")
