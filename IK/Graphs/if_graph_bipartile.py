"""
Question:

Check whether the given graph is bipartite or not?

A graph is bipartite if the nodes can be partitioned into two independent sets, A and B, such that every edge in the
graph connects a node in set A and a node in set B.

Example One
Graph

{
"n": 6,
"edges": [
[0, 1],
[1, 2],
[0, 4],
[1, 3],
[4, 3]
]
}
Output:

1
The nodes can be partitioned into two sets: {0, 3, 2, 5} and {1, 4}.

Example Two
Graph

{
"n": 3,
"edges": [
[0, 1],
[1, 2],
[2, 0]
]
}
Output:

0
"""


def is_bipartite(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Write your code here.

    # step 1: build a graph
    adjList = [[] for _ in range(n)]
    for e1, e2 in edges:
        adjList[e1].append(e2)
        adjList[e2].append(e1)

    visited = [-1] * n
    parent = [-1] * n
    distance = [-1] * n

    # step 2: BFS or DFS
    # Using BFS
    def bfs(source):
        q = []
        q.append(source)
        distance[source] = 0
        visited[source] = 1

        while q:
            node = q.pop(0)
            for neighbor in adjList[node]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = node
                    distance[neighbor] = 1 + distance[node]
                    q.append(neighbor)
                else:
                    if neighbor != parent[node]:
                        if distance[neighbor] == distance[node]:
                            return False

        return True

    # step 3: outer loop
    for v in range(n):
        if visited[v] == -1:
            if not bfs(v):
                return False

    return True
