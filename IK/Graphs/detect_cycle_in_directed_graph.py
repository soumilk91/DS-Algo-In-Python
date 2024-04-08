"""
Author: Soumil Ramesh Kulkarni
Date: 04.06.2024

Question:
Given a directed graph, find out whether it has a cycle.

Example
Graph

{
"number_of_vertices": 5,
"number_of_edges": 7,
"edges": [
[0, 1],
[0, 3],
[1, 3],
[1, 2],
[2, 3],
[4, 0],
[2, 4]
]
}
Output:

1
Given graph has one cycle: 0→1→2→4→0.


"""

"""
* Asymptotic complexity in terms of the number of nodes `n` and the number of edges `m`:
* Time: O(n + m).
* Auxiliary space: O(n + m).
* Total space: O(n + m).
"""

def dfs(current_vertex, adjacency_list, visited, is_in_stack):
    if is_in_stack[current_vertex]:
        # We came to a vertex which we started from or passed by in current
        # DFS traversal. In other words, we found a back edge, and a cycle.
        return True

    if visited[current_vertex]:
        # We had already visited current_vertex once. If a cycle including
        # current_vertex existed, we would have found it then.
        return False

    # Mark current_vertex visited and a part of the recursion stack.
    visited[current_vertex] = True
    is_in_stack[current_vertex] = True

    # Recur for all vertices adjacent to current_vertex.
    for v in adjacency_list[current_vertex]:
        if dfs(v, adjacency_list, visited, is_in_stack):
            return True

    is_in_stack[current_vertex] = False
    return False

def has_cycle(number_of_vertices, number_of_edges, edges):
    """
    Args:
     number_of_vertices(int32)
     number_of_edges(int32)
     edges(list_list_int32)
    Returns:
     bool
    """
    # Create an adjacency list
    adjacency_list = [[] for _ in range(number_of_vertices)]

    for edge in edges:
        adjacency_list[edge[0]].append(edge[1])

    visited = [False] * number_of_vertices
    is_in_stack = [False] * number_of_vertices

    for i in range(number_of_vertices):
        if dfs(i, adjacency_list, visited, is_in_stack):
            return True
    return False
