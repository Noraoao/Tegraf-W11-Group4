# Informatics ITS Graph Theory class Group 4
|Name|NRP|
|---|---|
|Naura Rizky Ameira|5025251001|
|Farras Al-Ghifari|5025251006|
|Nisrina Zahralilla|5025251013|
|Safiya Nadira Az-zahra|5025251268|

## Week 11 Task 

## xxx Algorithm

- ### BRIEF ALGORITHM EXPLANATION
  

- ### RUNNING THE CODE
  

- ### Input Test Case & Output
    
  



## Capacity-Scaling Algorithm

- ### BRIEF ALGORITHM EXPLANATION

  Capacity scaling is a max-flow algorithm that improves on Ford-Fulkerson by pushing the big flows first. It sets a threshold Δ to the largest power of 2 that is no bigger than the largest capacity. Then it repeatedly finds paths from the source to the sink using only edges with at least Δ capacity left (using BFS) and pushes the bottleneck amount along each path, updating the forward and reverse residual capacities. When no path exists for the current Δ, it halves Δ and repeats. The last phase with Δ = 1 is plain Ford-Fulkerson, so when it ends no augmenting path remains and the flow is maximum. Because each phase needs only about 2E augmentations and there are about log U phases, the total time is O(E² · log U).
  

- ### RUNNING THE CODE

  - Make sure Python 3 is installed (no extra libraries needed).
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
