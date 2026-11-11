import time

from algorithms.dijkstra import build_graph, dijkstra, reconstruct_path


def nearest_neighbor_tsp(graph, start, destinations):
    """
    Generate an approximate delivery route using
    the Nearest Neighbor TSP algorithm.

    Dijkstra is used to calculate shortest distances
    between delivery locations.
    """

    # Remove duplicate destinations and starting location
    unvisited = list(dict.fromkeys(
        location for location in destinations
        if location != start
    ))

    current = start

    route = [start]
    total_distance = 0

    # Cache shortest paths between locations
    shortest_paths = {}

    def get_shortest_path(source, destination):

        key = (source, destination)

        if key not in shortest_paths:

            distances, parents = dijkstra(graph, source)

            shortest_paths[key] = (
                distances[destination],
                reconstruct_path(
                    parents,
                    source,
                    destination
                )
            )

        return shortest_paths[key]

    # Visit nearest unvisited destination
    while unvisited:

        nearest_location = None
        minimum_distance = float("inf")

        for destination in unvisited:

            distance, path = get_shortest_path(
                current,
                destination
            )

            if distance < minimum_distance:

                minimum_distance = distance
                nearest_location = destination

        if nearest_location is None or minimum_distance == float("inf"):
            raise ValueError(
                "Some delivery locations are unreachable."
            )

        distance, path = get_shortest_path(
            current,
            nearest_location
        )

        # Add actual road path without duplicating current location
        route.extend(path[1:])

        total_distance += distance

        current = nearest_location

        unvisited.remove(nearest_location)

    # Return to warehouse
    if current != start:

        return_distance, return_path = get_shortest_path(
            current,
            start
        )

        if return_distance == float("inf"):
            raise ValueError(
                "Warehouse cannot be reached from final location."
            )

        route.extend(return_path[1:])

        total_distance += return_distance

    return route, total_distance


if __name__ == "__main__":

    import json

    # Load location dataset
    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    # Build graph
    graph = build_graph(location_data)

    warehouse = location_data["warehouse"]

    destinations = [
        location
        for location in location_data["locations"]
        if location != warehouse
    ]

    # Measure execution time
    start_time = time.perf_counter()

    route, total_distance = nearest_neighbor_tsp(
        graph,
        warehouse,
        destinations
    )

    end_time = time.perf_counter()

    # Display results
    print("\n========== COURIER DELIVERY ROUTE ==========\n")

    print("Starting Location:", warehouse)

    print("\nDelivery Route:")

    print(" -> ".join(route))

    print("\nTotal Locations Visited:",
          len(destinations))

    print("Total Distance:",
          total_distance, "km")

    print("\nRoute Summary:")

    print("Start:", warehouse)
    print("End:", warehouse)

    print("\nExecution Time:",
          round((end_time - start_time) * 1000, 6), "ms")

    print("\nNearest Neighbor TSP completed successfully!")