import json
import heapq
import time


def build_graph(location_data):
    """
    Create an undirected weighted graph using road connections.
    """

    graph = {
        location: []
        for location in location_data["locations"]
    }

    for road in location_data["roads"]:

        source = road["from"]
        destination = road["to"]
        distance = road["distance"]

        graph[source].append((destination, distance))
        graph[destination].append((source, distance))

    return graph


def dijkstra(graph, start):
    """
    Find shortest distances from the starting location
    to all other locations using Dijkstra's algorithm.
    """

    distances = {
        location: float("inf")
        for location in graph
    }

    parents = {
        location: None
        for location in graph
    }

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_location = heapq.heappop(
            priority_queue
        )

        # Ignore outdated queue entries
        if current_distance > distances[current_location]:
            continue

        for neighbor, weight in graph[current_location]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                parents[neighbor] = current_location

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    return distances, parents


def reconstruct_path(parents, start, destination):
    """
    Reconstruct the shortest path using parent information.
    """

    if destination not in parents:
        return []

    if destination != start and parents[destination] is None:
        return []

    path = []
    current = destination

    while current is not None:

        path.append(current)

        if current == start:
            break

        current = parents[current]

    if path[-1] != start:
        return []

    path.reverse()

    return path


if __name__ == "__main__":

    # Load location dataset
    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    # Build graph
    graph = build_graph(location_data)

    warehouse = location_data["warehouse"]

    # Measure execution time
    start_time = time.perf_counter()

    distances, parents = dijkstra(graph, warehouse)

    end_time = time.perf_counter()

    # Display results
    print("\n========== DIJKSTRA SHORTEST PATH ==========\n")

    print("Starting Location:", warehouse)

    print("\nShortest Routes:\n")

    for destination in graph:

        path = reconstruct_path(
            parents,
            warehouse,
            destination
        )

        if path:

            print(
                f"{warehouse} -> {destination} | "
                f"Path: {' -> '.join(path)} | "
                f"Distance: {distances[destination]} km"
            )

        else:

            print(
                f"{warehouse} -> {destination} | "
                "No route available"
            )

    print("\nExecution Time:",
          round((end_time - start_time) * 1000, 6), "ms")

    print("\nDijkstra algorithm completed successfully!")