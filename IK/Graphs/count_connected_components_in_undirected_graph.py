"""
Author: Soumil Ramesh Kulkarni
Date: 03.04.2024

Question:
Given an undirected graph, find its total number of connected components.

Example One
Graph

{
"n": 5,
"edges": [[0 ,1], [1, 2], [0, 2], [3, 4]]
}
Output:

2
Example Two
Graph

{
"n": 4,
"edges": [[0 , 1], [0 , 3], [0 , 2], [2 , 1], [2 , 3]]
}
Output:

1
"""


def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    if n < 1:
        return 0
    if n < 2:
        return 1

    # Build the Graph
    # Build n vertices first
    graph = {}
    for i in range(n):
        graph[i] = []

    # Build adj lists using each edge
    for edge in edges:
        graph[edge[0]].append(edge[1])
        # Since undirected (basically bidirectional)
        graph[edge[1]].append(edge[0])

    # print the Graph
    # print(graph)

    # Now Traverse through the graph and find out if all vertices can be reached from a given point
    visited = [None] * n
    component_list = [0] * n
    component = 0
    for i in range(n):
        if visited[i] == None:
            component += 1
            bfs(i, graph, visited, component, component_list)
    # print(component_list)
    return component


def bfs(node, graph, visited, component, component_list):
    queue = [node]
    while queue:
        temp = queue.pop(0)
        visited[temp] = True
        component_list[temp] = component
        for neighbor in graph[temp]:
            if visited[neighbor] == None:
                queue.append(neighbor)