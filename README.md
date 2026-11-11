# Mini-Courier Planner

## 1. Project Overview

Mini-Courier Planner is a Python-based courier management system that helps plan parcel deliveries efficiently.

The system prioritizes parcels, selects the best combination of parcels according to the available box capacity, calculates shortest delivery paths, and generates an optimized delivery route.

The project demonstrates the practical application of sorting, dynamic programming, graph algorithms, and approximation techniques.

## 2. Objectives

- Prioritize parcels based on delivery priority and deadlines.
- Select parcels using the 0/1 Knapsack algorithm.
- Calculate shortest paths between delivery locations.
- Generate a delivery route using the Nearest Neighbor approximation algorithm.
- Measure algorithm execution time on different dataset sizes.
- Compare algorithm performance using charts.

## 3. Technologies Used

- Python
- JSON
- CSV
- Matplotlib
- Visual Studio Code

## 4. Project Structure

```text
daa capstone project/
│
├── algorithms/
│   ├── sorting.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── nearest_neighbor.py
│
├── data/
│   ├── parcels.json
│   └── locations.json
│
├── results/
│   ├── performance_results.csv
│   ├── sorting_comparison.png
│   ├── knapsack_performance.png
│   └── graph_performance.png
│
├── screenshots/
│
├── utils/
│   ├── performance.py
│   └── plot_results.py
│
├── main.py
└── README.md
```

## 5. Algorithms Implemented

### A. Merge Sort

Used to prioritize parcels based on priority and delivery deadline.

- Time Complexity: O(n log n)
- Space Complexity: O(n)

### B. 0/1 Knapsack using Dynamic Programming

Selects the most valuable combination of parcels without exceeding the box capacity.

- Time Complexity: O(nW)
- Space Complexity: O(nW)

Here, n represents the number of parcels and W represents the box capacity.

### C. Dijkstra's Shortest Path Algorithm

Calculates the shortest distances between the warehouse and delivery locations.

- Time Complexity: O((V + E) log V)
- Space Complexity: O(V + E)

### D. Nearest Neighbor Approximation

Generates a delivery route by repeatedly selecting the nearest unvisited destination.

- Uses Dijkstra's shortest-path distances.
- Returns to the warehouse after visiting the selected destinations.
- Produces an approximate route rather than guaranteeing the globally optimal route.

## 6. How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your system.

### Step 2: Install Matplotlib

Run:

```bash
python -m pip install matplotlib
```

### Step 3: Run the Main Application

Open the terminal in the project folder and execute:

```bash
python main.py
```

### Step 4: Run Performance Testing

```bash
python utils/performance.py
```

### Step 5: Generate Performance Charts

```bash
python utils/plot_results.py
```

## 7. Sample Results

The application performs the following operations:

1. Sorts parcels according to priority and deadline.
2. Selects parcels using the Knapsack DP algorithm.
3. Calculates a delivery route using graph algorithms.
4. Displays total parcel weight and value.
5. Reports execution time.

For the sample dataset:

- Box Capacity: 20 kg
- Selected Parcels: 4
- Total Weight: 20 kg
- Total Value: 550
- Total Delivery Route Distance: 28 km

## 8. Performance Analysis

Performance testing is conducted using parcel datasets of different sizes:

- 10 parcels
- 50 parcels
- 100 parcels
- 200 parcels

Execution times are recorded in `performance_results.csv`.

Matplotlib is used to generate three performance charts:

1. Sorting Algorithm Comparison
2. Knapsack DP Performance
3. Graph Algorithm Performance

The sorting and Knapsack tests use datasets of increasing sizes. The graph algorithms currently use a fixed road network, so their measurements compare execution time on that network rather than graph growth.

## 9. Conclusion

The Mini-Courier Planner demonstrates how different algorithmic techniques can work together to solve a practical courier planning problem.

Merge Sort handles parcel prioritization, Dynamic Programming optimizes parcel selection, Dijkstra calculates shortest paths, and the Nearest Neighbor heuristic generates a delivery route.

The project also includes performance testing and graphical analysis to evaluate the implemented algorithms.