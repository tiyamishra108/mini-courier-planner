import json
import time

from algorithms.sorting import merge_sort_parcels
from algorithms.knapsack import knapsack
from algorithms.dijkstra import build_graph
from algorithms.nearest_neighbor import nearest_neighbor_tsp


def load_data():
    """Load parcel and location datasets."""

    with open("data/parcels.json", "r") as file:
        parcels = json.load(file)

    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    return parcels, location_data


def main():

    start_time = time.perf_counter()

    # Load datasets
    parcels, location_data = load_data()

    capacity = location_data["box_capacity"]
    warehouse = location_data["warehouse"]

    # 1. Sort parcels by priority and deadline
    sorted_parcels = merge_sort_parcels(parcels)

    # 2. Optimize parcel selection using Knapsack
    selected_parcels, total_weight, total_value, dp_table = knapsack(
        sorted_parcels, capacity
    )

    # 3. Identify unique delivery destinations
    destinations = list(
        dict.fromkeys(
            parcel["destination"]
            for parcel in selected_parcels
            if parcel["destination"] != warehouse
        )
    )

    # 4. Build delivery graph
    graph = build_graph(location_data)

    # 5. Generate optimized delivery route
    route, total_distance = nearest_neighbor_tsp(
        graph, warehouse, destinations
    )

    end_time = time.perf_counter()

    # Display final report
    print("\n" + "=" * 55)
    print("              MINI-COURIER PLANNER")
    print("=" * 55)

    print("\n1. PARCEL PRIORITIZATION")
    print("-" * 55)

    for parcel in sorted_parcels:
        print(
            f"{parcel['parcel_id']} | "
            f"Priority: {parcel['priority']} | "
            f"Deadline: {parcel['deadline']}"
        )

    print("\n2. OPTIMAL PACKING PLAN")
    print("-" * 55)

    print("Box Capacity:", capacity, "kg")

    for parcel in selected_parcels:
        print(
            f"{parcel['parcel_id']} | "
            f"Destination: {parcel['destination']} | "
            f"Weight: {parcel['weight']} kg | "
            f"Value: {parcel['value']}"
        )

    print("\nTotal Selected Parcels:", len(selected_parcels))
    print("Total Weight:", total_weight, "kg")
    print("Total Value:", total_value)
    print("Remaining Capacity:", capacity - total_weight, "kg")

    print("\n3. DELIVERY ROUTE")
    print("-" * 55)

    print("Warehouse:", warehouse)
    print("Delivery Destinations:", destinations)
    print("Route:", " -> ".join(route))
    print("Total Distance:", total_distance, "km")

    print("\n4. PERFORMANCE")
    print("-" * 55)

    print(
        "Total Execution Time:",
        round((end_time - start_time) * 1000, 6),
        "ms"
    )

    print("\n" + "=" * 55)
    print("       COURIER PLANNING COMPLETED SUCCESSFULLY")
    print("=" * 55)


if __name__ == "__main__":
    main()