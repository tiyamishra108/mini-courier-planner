def merge_sort_parcels(parcels):
    """
    Sort parcels based on priority and delivery deadline.

    Lower priority number means higher priority.
    Earlier deadline gets preference when priorities match.
    """

    if len(parcels) <= 1:
        return parcels.copy()

    mid = len(parcels) // 2

    left = merge_sort_parcels(parcels[:mid])
    right = merge_sort_parcels(parcels[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted parcel lists into one sorted list.
    """

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        key_left = (
            left[i]["priority"],
            left[i]["deadline"]
        )

        key_right = (
            right[j]["priority"],
            right[j]["deadline"]
        )

        if key_left <= key_right:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    import json
    import time

    with open("data/parcels.json", "r") as file:
        parcels = json.load(file)

    start_time = time.perf_counter()

    sorted_parcels = merge_sort_parcels(parcels)

    end_time = time.perf_counter()

    print("\n========== PARCEL PRIORITIZATION ==========\n")

    for parcel in sorted_parcels:
        print(
            f"Parcel: {parcel['parcel_id']} | "
            f"Priority: {parcel['priority']} | "
            f"Deadline: {parcel['deadline']}"
        )

    print("\nExecution Time:",
          round((end_time - start_time) * 1000, 6), "ms")

    print("\nSorting completed successfully!")