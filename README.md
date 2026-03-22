# Data Structure and Algorithms Review
This repository serves as a data structures and algorithms reference/review in Python.


## Searching Algorithms
*Techniques to locate elements in data structures efficiently.* [See more](Searching_algs/Searching_algs.md)
|      Algorithm     | Worst Case | Best Case |                   Notes                  |
|------------------|-----------:|------------:|----------------------------------------|
| Linear Search      |       O(n) |      O(1) | Scan each element until found          |
| Binary Search      |   O(log n) |      O(1) | Array must be sorted                   |
| Jump Search        |      O(√n) |      O(1) | Jump ahead fixed steps in sorted array |
| Exponential Search |   O(log n) |      O(1) | Find range, then binary search         |


## Sorting Algorithms
*Methods to arrange elements in a specific order.*
|    Algorithm   | Worst Case |  Best Case |                   Notes                  |
|--------------|----------:|----------:|----------------------------------------|
| Bubble Sort    |      O(n²) |       O(n) |        Swap adjacent elements repeatedly |
| Selection Sort |      O(n²) |      O(n²) |             Select min element each pass |
| Insertion Sort |      O(n²) |       O(n) | Build sorted array one element at a time |
| Merge Sort     | O(n log n) | O(n log n) |              Recursively split and merge |
| Quick Sort     |      O(n²) | O(n log n) |           Pick pivot, partition, recurse |
| Heap Sort      | O(n log n) | O(n log n) |              Build max-heap, extract max |

## Data-Structure Based Algorithms
*Operations and algorithms that leverage fundamental data structures.*
| Algorithm        | Type           | Notes                         |
|------------------|----------------|-------------------------------|
| Stack Operations | LIFO           | Push, Pop, Peek               |
| Queue Operations | FIFO           | Enqueue, Dequeue, Front       |
| Priority Queue   | Heap / Sorting | Extract min/max efficiently   |
| Linked List Ops  | Pointers       | Insert/Delete in O(1) at head |

## Graph Algorithms
*Algorithms to traverse, analyze, and optimize graphs and networks.*
| Algorithm      | Type               | Complexity | Notes                              |
|----------------|--------------------|------------:|------------------------------------|
| BFS            | Graph / Traversal  | O(V+E)     | Level-order search                 |
| DFS            | Graph / Traversal  | O(V+E)     | Deep traversal / backtracking      |
| Dijkstra       | Shortest Path      | O(E log V) | Weighted graphs, no negative edges |
| Bellman-Ford   | Shortest Path      | O(VE)      | Works with negative edges          |
| Floyd-Warshall | All-Pairs Shortest | O(V³)      | Dynamic programming approach       |
| Kruskal        | MST / Greedy       | O(E log V) | Sort edges, union-find             |
| Prim           | MST / Greedy       | O(E log V) | Grow MST from single vertex        |

## Dynamic Programming
Solving complex problems by breaking them into overlapping subproblems.
| Algorithm / Problem         | Type              | Complexity  | Notes                         |
|-----------------------------|-------------------|-------------:|-------------------------------|
| Fibonacci                   | DP / Memoization  | O(n)        | Top-down or bottom-up         |
| Knapsack (0/1)              | DP / Optimization | O(nW)       | Max value for given weight    |
| Longest Common Subsequence  | DP / Sequence     | O(n*m)      | Classic string DP             |
| Matrix Chain Multiplication | DP / Optimization | O(n³)       | Order of multiplying matrices |
| Coin Change                 | DP / Counting     | O(n*amount) | Number of ways to make change |
| Kruskal                     | MST / Greedy      | O(E log V)  | Sort edges, union-find        |
| Prim                        | MST / Greedy      | O(E log V)  | Grow MST from single vertex   |