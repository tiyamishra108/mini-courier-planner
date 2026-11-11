# MINI-COURIER PLANNER
## Design and Analysis of Algorithms (ETCCDA302)

**University:** KR Mangalam University  
**Project Title:** Mini-Courier Planner  
**Programming Language:** Python  
**Project Type:** Algorithm-Based Application

---

# 1. Abstract

The Mini-Courier Planner is a Python-based application designed to improve courier delivery planning through the application of different algorithmic techniques.

The system prioritizes parcels according to their delivery priority and deadlines, selects valuable parcels within a limited box capacity, calculates shortest paths between delivery locations, and generates an approximate delivery route.

The project integrates Merge Sort, Dynamic Programming, Dijkstra's Shortest Path Algorithm, and the Nearest Neighbor Approximation Algorithm. It also includes performance testing to study the execution time of the implemented algorithms.

# 2. Problem Statement

Courier delivery services need to manage multiple parcels with different weights, values, priorities, deadlines, and destinations.

Planning deliveries manually can result in inefficient parcel selection and unnecessary travel distances.

The objective of this project is to develop a system that:

- Prioritizes parcels based on urgency.
- Selects parcels within a fixed carrying capacity.
- Calculates shortest paths between locations.
- Generates an efficient delivery route.
- Evaluates algorithm performance using different input sizes.

# 3. Project Objectives

1. Implement sorting techniques for parcel prioritization.
2. Apply Dynamic Programming to optimize parcel selection.
3. Implement graph-based shortest-path calculations.
4. Apply an approximation algorithm for route planning.
5. Measure and compare execution times.
6. Generate graphical representations of algorithm performance.

# 4. System Design

The application consists of four major algorithmic components.

### 4.1 Parcel Prioritization

Parcels are sorted according to:

- Delivery priority.
- Delivery deadline.

A lower priority number represents a more urgent parcel. When priorities are equal, the earlier deadline is considered first.

### 4.2 Optimal Parcel Selection

The 0/1 Knapsack algorithm selects a combination of parcels that maximizes total parcel value without exceeding the available box capacity.

Each parcel is either selected completely or excluded.

### 4.3 Shortest Path Calculation

Dijkstra's algorithm calculates the shortest distance from the warehouse to other delivery locations using the road network.

Each road has a distance represented as a positive edge weight.

### 4.4 Delivery Route Generation

The Nearest Neighbor approximation algorithm selects the nearest unvisited destination at each step.

The route begins at the warehouse, visits the selected destinations, and returns to the warehouse.

# 5. Algorithms and Complexity Analysis

| Algorithm | Purpose | Time Complexity | Space Complexity |
|---|---|---|---|
| Merge Sort | Parcel prioritization | O(n log n) | O(n) |
| 0/1 Knapsack DP | Parcel selection | O(nW) | O(nW) |
| Dijkstra | Shortest paths | O((V+E) log V) | O(V+E) |
| Nearest Neighbor | Route approximation | Depends on graph and destinations | Depends on graph and route |

Where:

- n = Number of parcels.
- W = Box capacity.
- V = Number of vertices.
- E = Number of edges.

# 6. Implementation Details

The project is implemented in Python and divided into separate modules.

| File | Responsibility |
|---|---|
| main.py | Integrates all algorithms |
| sorting.py | Implements Merge Sort |
| knapsack.py | Implements 0/1 Knapsack DP |
| dijkstra.py | Implements shortest-path calculation |
| nearest_neighbor.py | Generates delivery routes |
| performance.py | Measures algorithm execution time |
| plot_results.py | Generates performance charts |
| parcels.json | Stores parcel information |
| locations.json | Stores locations and road distances |

The main application reads input data from JSON files and combines the outputs of the individual algorithms into a courier planning report.

# 7. Sample Execution Results

The application was tested using the sample parcel and location datasets.

### Parcel Selection

- Box Capacity: 20 kg
- Selected Parcels: 4
- Total Weight: 20 kg
- Total Value: 550
- Remaining Capacity: 0 kg

### Selected Parcels

| Parcel ID | Destination | Weight | Value |
|---|---|---:|---:|
| P103 | C | 4 kg | 120 |
| P106 | A | 3 kg | 90 |
| P105 | E | 6 kg | 180 |
| P107 | C | 7 kg | 160 |

### Delivery Route

Warehouse: W

Generated Route:

W → A → B → C → E → D → B → W

Total Distance: 28 km

# 8. Performance Testing

Performance testing was conducted using datasets containing 10, 50, 100, and 200 parcels.

The execution time of each algorithm was measured in milliseconds.

The results were stored in a CSV file and visualized using Matplotlib.

Three performance charts were generated:

1. Sorting Algorithm Comparison.
2. Knapsack DP Performance.
3. Graph Algorithm Performance.

### Performance Observations

- Merge Sort execution time increased as the number of parcels increased.
- Built-in Python sorting was faster than the implemented Merge Sort for the tested dataset sizes.
- Knapsack DP execution time increased with the number of parcels.
- Dijkstra and Nearest Neighbor were tested using a fixed road network. Their results therefore represent performance on that particular graph, not performance across increasing graph sizes.

# 9. Testing and Validation

The following tests were performed:

1. Parcel sorting was checked against priority and deadline.
2. Knapsack selection was checked against the box capacity.
3. Shortest-path distances were checked using the sample road network.
4. The delivery route was checked for destination coverage and return to the warehouse.
5. Performance testing was conducted on multiple parcel dataset sizes.
6. Generated CSV results and performance charts were verified.

# 10. Limitations

- The current application uses predefined sample datasets.
- The Nearest Neighbor algorithm provides an approximate route and does not guarantee the globally shortest route.
- The graph performance tests currently use a fixed road network.
- Real-time traffic and changing road conditions are not considered.
- The current model does not account for multiple delivery vehicles.

# 11. Future Scope

The project can be improved by adding:

- Real-time traffic information.
- Multiple courier vehicles.
- A graphical user interface.
- Database integration.
- Dynamic parcel and location management.
- More advanced route optimization algorithms.
- Performance testing on larger and dynamically generated road networks.

# 12. Conclusion

The Mini-Courier Planner successfully demonstrates the practical application of Design and Analysis of Algorithms in a courier delivery planning problem.

The integration of Merge Sort, Dynamic Programming, Dijkstra's algorithm, and Nearest Neighbor approximation provides a structured approach to parcel prioritization, packing optimization, and delivery route generation.

Performance testing and graphical analysis further help evaluate the implemented algorithms.

The project demonstrates how theoretical algorithmic concepts can be applied to solve practical computational problems.