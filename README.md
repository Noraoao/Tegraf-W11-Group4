# Informatics ITS Graph Theory class Group 4
|Name|NRP|
|---|---|
|Naura Rizky Ameira|5025251001|
|Farras Al-Ghifari|5025251006|
|Nisrina Zahralilla|5025251013|
|Safiya Nadira Az-zahra|5025251268|

## Week 11 Task 

## Dinic's Algorithm

- ### BRIEF ALGORITHM EXPLANATION
  **Dinic’s Algorithm** is an efficient, polynomial-time algorithm for solving the **Maximum Flow** problem in a flow network. It improves upon classic approaches like Ford-Fulkerson and Edmonds-Karp by sending flow along multiple shortest paths simultaneously in phases rather than searching for one augmenting path at a time.

  #### How It Works
  The algorithm builds a residual graph where every directed edge $u \to v$ with capacity $c$ is paired with a reverse edge $v \to u$ of capacity $0$ (allowing flow to be redirected or undone). It then repeats two main steps in phases until no path from the source $s$ to the sink $t$ remains:

  1. **Build Level Graph (BFS):** Starting from $s$, Breadth-First Search assigns a "level" (shortest edge distance from $s$) to each reachable node using only edges with remaining capacity greater than $0$. If $t$ is unreachable, the algorithm stops.
  2. **Find Blocking Flow (DFS):** Depth-First Search pushes flow from $s$ to $t$ strictly along edges that go one level deeper (`level[v] == level[u] + 1`). As flow $d$ is pushed, forward capacities decrease by $d$ and reverse capacities increase by $d$. This repeats until every valid path in the current level graph is saturated (a *blocking flow*).

- ### RUNNING THE CODE
  - Open a terminal in the folder containing `dinic.py`.
  - Run:
     ```
     python dinic.py
     ```

- ### Input Test Case & Output

  #### Input Format
  The program reads standard interactive console inputs in the following order:
  1. `n` — Total number of nodes (0-indexed: `0` to `n - 1`)
  2. `m` — Total number of directed edges
  3. `source` — ID of the source node $s$
  4. `sink` — ID of the sink node $t$
  5. `m` lines of edges — Each formatted as `from to capacity`

  #### Sample Input
  ```text
  6
  9
  0
  5
  0 1 10
  0 2 10
  1 2 2
  1 3 4
  1 4 8
  2 4 9
  3 5 10
  4 3 6
  4 5 10
  ```

  #### Expected Output

  <img width="642" height="265" alt="image" src="https://github.com/user-attachments/assets/789aae5c-1357-4974-aeab-fee13dfb1802" />

## Capacity-Scaling Algorithm

- ### BRIEF ALGORITHM EXPLANATION

  Capacity scaling is a max-flow algorithm that sets a threshold Δ to the largest power of 2 that is no bigger than the largest capacity. Then it repeatedly finds paths from the source to the sink using only edges with at least Δ capacity left (using BFS) and pushes the bottleneck amount along each path, updating the forward and reverse residual capacities. When no path exists for the current Δ, it halves Δ and repeats. The last phase with Δ = 1 is plain Ford-Fulkerson, so when it ends no augmenting path remains and the flow is maximum.
  

- ### RUNNING THE CODE

  - Open a terminal in the folder containing `capacity_scaling.py`.
  - Run:
     ```
     python capacity_scaling.py
     ```

  **Input format**
  ```
  n m
  s t
  u v c
  u v c
  ...
  ```
  - Line 1: `n m` = number of nodes and number of edges
  - Line 2: `s t` = source node and sink node
  - Next `m` lines: `u v c` = directed edge from node `u` to node `v` with capacity `c`
  - Nodes are numbered `0` to `n-1`, and capacities are non-negative integers
  - Edges are directed. For a two-way connection, add a second line `v u c`

- ### Input Test Case & Output

  Input:
  ```
  6 9
  0 5
  0 1 16
  0 2 13
  1 2 10
  2 1 4
  1 3 12
  3 2 9
  2 4 14
  4 3 7
  3 5 20
  ```

  Output:
  ```
  max flow: 19
  ```

## AI USAGE DISCLOSURE

  -
  - Capacity Scaling: https://share.gemini.google/ySJmFsii9RXM
