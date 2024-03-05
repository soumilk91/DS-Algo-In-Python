"""
Author: Soumil Ramesh Kulkarni
Date: 03.04.2024

Question:
Given an undirected graph, find out whether it is a tree.

The undirected edges are given by two arrays edge_start and edge_end of equal size. Edges of the given graph connect nodes edge_start[i] and edge_end[i] for all valid i.

Example One
Graph 1

{
"node_count": 4,
"edge_start": [0, 0, 0],
"edge_end": [1, 2, 3]
}
Output:

1
This graph is a tree because all the nodes are connected, and it does not have cycles.

Example Two
Graph 2

{
"node_count": 4,
"edge_start": [0, 0],
"edge_end": [1, 2]
}
Output:

0
This graph is not a tree because node 3 is not connected to the other nodes.

Example Three
Graph 3

{
"node_count": 4,
"edge_start": [0, 0, 1, 2],
"edge_end": [3, 1, 2, 0]
}
Output:

0
This graph is not a tree: nodes 0, 1 and 2 form a cycle.

Example Four
Graph 4

{
"node_count": 4,
"edge_start": [0, 0, 0, 1],
"edge_end": [1, 2, 3, 0]
}
Output:

0
This graph is not a tree because the two edges that connect nodes 0 and 1 form a cycle.
"""

"""
Asymptotic complexity in terms of number of nodes `n` and number of edges `m`:
* Time: O(n + m).
* Auxiliary space: O(n + m).
* Total space: O(n + m).
"""
from collections import deque

# Function to check if the graph is a tree
def is_it_a_tree(node_count, edge_start, edge_end):
    visited = [False] * node_count
    parent = [-1] * node_count
    edge = [[] for _ in range(node_count)]
    set_of_edges = set()

    # Constructing the graph
    for i in range(len(edge_start)):
        if edge_start[i] == edge_end[i]:
            return False  # Self-loop detected

        edge[edge_start[i]].append(edge_end[i])
        edge[edge_end[i]].append(edge_start[i])

        u, v = edge_start[i], edge_end[i]
        if (min(u, v), max(u, v)) in set_of_edges:
            return False  # Graph has multi-edges
        set_of_edges.add((min(u, v), max(u, v)))

    source = 0
    q = deque([source])
    visited[source] = True

    while q:
        u = q.popleft()
        for v in edge[u]:
            if not visited[v]:
                parent[v] = u
                visited[v] = True
                q.append(v)
            else:  # Found a neighbor that has already been discovered
                if v != parent[u]:
                    return False  # Found a cycle

    # Check if the graph is connected
    for i in range(node_count):
        if not visited[i]:
            return False  # The graph is not connected

    return True  # The graph is connected and does not have any cycle, hence it is a tre