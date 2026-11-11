import csv
import matplotlib.pyplot as plt


def load_results():

    data = []

    with open("results/performance_results.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data


def generate_charts():

    results = load_results()

    sizes = [int(row["Dataset Size"]) for row in results]

    merge_sort = [
        float(row["Merge Sort (ms)"]) for row in results
    ]

    builtin_sort = [
        float(row["Built-in Sort (ms)"]) for row in results
    ]

    knapsack = [
        float(row["Knapsack DP (ms)"]) for row in results
    ]

    dijkstra = [
        float(row["Dijkstra (ms)"]) for row in results
    ]

    nearest_neighbor = [
        float(row["Nearest Neighbor (ms)"]) for row in results
    ]

    # Chart 1: Sorting Comparison

    plt.figure(figsize=(8, 5))

    plt.plot(sizes, merge_sort, marker="o", label="Merge Sort")
    plt.plot(sizes, builtin_sort, marker="s", label="Built-in Sort")

    plt.title("Sorting Algorithm Performance")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/sorting_comparison.png")
    plt.close()

    # Chart 2: Knapsack Performance

    plt.figure(figsize=(8, 5))

    plt.plot(sizes, knapsack, marker="o")

    plt.title("Knapsack DP Performance")
    plt.xlabel("Dataset Size")
    plt.ylabel("Execution Time (ms)")
    plt.grid(True)

    plt.savefig("results/knapsack_performance.png")
    plt.close()

    # Chart 3: Graph Algorithm Performance

    plt.figure(figsize=(8, 5))

    plt.plot(sizes, dijkstra, marker="o", label="Dijkstra")
    plt.plot(
        sizes,
        nearest_neighbor,
        marker="s",
        label="Nearest Neighbor"
    )

    plt.title("Graph Algorithm Performance")
    plt.xlabel("Parcel Dataset Size")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/graph_performance.png")
    plt.close()

    print("\nAll performance charts generated successfully!")

    print("1. results/sorting_comparison.png")
    print("2. results/knapsack_performance.png")
    print("3. results/graph_performance.png")


if __name__ == "__main__":
    generate_charts()