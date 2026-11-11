def knapsack(parcels, capacity):
   
    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            # Exclude current parcel
            dp[i][w] = dp[i - 1][w]

            # Include current parcel if capacity allows
            if weight <= w:

                include_value = (
                    value + dp[i - 1][w - weight]
                )

                dp[i][w] = max(
                    dp[i][w],
                    include_value
                )

    # Backtrack to find selected parcels
    selected_parcels = []

    remaining_capacity = capacity

    for i in range(n, 0, -1):

        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:

            parcel = parcels[i - 1]

            selected_parcels.append(parcel)

            remaining_capacity -= parcel["weight"]

    selected_parcels.reverse()

    total_weight = sum(
        parcel["weight"] for parcel in selected_parcels
    )

    total_value = sum(
        parcel["value"] for parcel in selected_parcels
    )

    return selected_parcels, total_weight, total_value, dp


if __name__ == "__main__":

    import json
    import time

    # Load parcel dataset
    with open("data/parcels.json", "r") as file:
        parcels = json.load(file)

    # Load box capacity
    with open("data/locations.json", "r") as file:
        location_data = json.load(file)

    capacity = location_data["box_capacity"]

    # Measure execution time
    start_time = time.perf_counter()

    selected, total_weight, total_value, dp_table = knapsack(
        parcels, capacity
    )

    end_time = time.perf_counter()

    # Display results
    print("\n========== OPTIMAL PACKING PLAN ==========\n")

    print("Box Capacity:", capacity, "kg")

    print("\nSelected Parcels:")

    for parcel in selected:
        print(
            f"{parcel['parcel_id']} | "
            f"Weight: {parcel['weight']} kg | "
            f"Value: {parcel['value']}"
        )

    print("\nTotal Weight:", total_weight, "kg")
    print("Total Value:", total_value)

    print("\nRemaining Capacity:",
          capacity - total_weight, "kg")

    print("\n========== DP TABLE ==========\n")

    print("Maximum achievable value at each capacity:")

    print(dp_table[-1])

    print("\nExecution Time:",
          round((end_time - start_time) * 1000, 6), "ms")

    print("\nKnapsack optimization completed successfully!")