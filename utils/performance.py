import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import csv
import time
import random

from algorithms.sorting import merge_sort_parcels
from algorithms.knapsack import knapsack
from algorithms.dijkstra import build_graph, dijkstra
from algorithms.nearest_neighbor import nearest_neighbor_tsp


def generate_parcels(size):

    parcels = []

    for i in range(size):

        parcels.append({
            "parcel_id": f"P{i + 1}",
            "destination": random.choice(["A", "B", "C", "D", "E"]),
            "weight": random.randint(1, 10),
            "value": random.randint(50, 500),
            "priority": random.randint(1, 3),
            "deadline": "12:00"
        })

    return parcels


def measure_time(function, *args, **kwargs):

    repetitions = 100
    total_time = 0

    for _ in range(repetitions):

        start = time.perf_counter()

        function(*args, **kwargs)

        end = time.perf_counter()

        total_time += (end - start)

    average_time = (total_time / repetitions) * 1000

    return average_time

def run_performance_tests():

    dataset_sizes = [10, 50, 100, 200]

    results = []

    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    graph = build_graph(location_data)

    warehouse = location_data["warehouse"]

    destinations = [
        location for location in location_data["locations"]
        if location != warehouse
    ]

    print("\n========== PERFORMANCE TESTING ==========\n")

    for size in dataset_sizes:

        parcels = generate_parcels(size)

        # Merge Sort
        merge_time = measure_time(
            merge_sort_parcels, parcels
        )

        # Built-in Sorting
        builtin_time = measure_time(
            sorted,
            parcels,
            key=lambda p: (p["priority"], p["deadline"])
        )

        # Knapsack DP
        knapsack_time = measure_time(
            knapsack, parcels, 20
        )

        # Dijkstra
        dijkstra_time = measure_time(
            dijkstra, graph, warehouse
        )

        # Nearest Neighbor TSP
        tsp_time = measure_time(
            nearest_neighbor_tsp,
            graph,
            warehouse,
            destinations
        )

        results.append({
            "Dataset Size": size,
            "Merge Sort (ms)": merge_time,
            "Built-in Sort (ms)": builtin_time,
            "Knapsack DP (ms)": knapsack_time,
            "Dijkstra (ms)": dijkstra_time,
            "Nearest Neighbor (ms)": tsp_time
        })

        print("Dataset Size:", size)
        print("Merge Sort:", round(merge_time, 6), "ms")
        print("Built-in Sort:", round(builtin_time, 6), "ms")
        print("Knapsack DP:", round(knapsack_time, 6), "ms")
        print("Dijkstra:", round(dijkstra_time, 6), "ms")
        print("Nearest Neighbor:", round(tsp_time, 6), "ms")
        print("-" * 45)

    # Save results to CSV

    with open("results/performance_results.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nPerformance results saved successfully!")
    print("File: results/performance_results.csv")


if __name__ == "__main__":
    run_performance_tests()