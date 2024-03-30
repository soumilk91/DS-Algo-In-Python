"""
Author: Soumil Ramesh Kulkarni
Date : 03.03.2024

Question:
Some Basic Fundamental Functions on Graph Theory
"""

import os

class GraphTheory:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, bidirectional=False):
        # Add 2 nodes to the graph if not present
        # Both start and end are two separate nodes in the graph
        # Create adj list to represent the connection between them
        if source not in self.graph:
            self.graph[source] = [destination]
        else:
            self.graph[source].append(destination)


        # Now if Bidirectional is True Create the same thing for the other item
        if destination not in self.graph:
            self.graph[destination] = []
        if bidirectional:
            self.graph[destination].append(source)


    def has_eulerian_cycle(self):
        # A given Graph has a Euerian cycle only if all the vertices in the graph
        # have even degree
        # Degree of a vertex is the number of neighbors it has
        for vertex in self.graph:
            if len(self.graph[vertex]) % 2 != 0:
                return False
        return True

    def has_eulerian_path(self):
        # A given Graph has a Eulerian Path only if the number of vertices that have odd degree are exactly 0 or 2
        odd = 0
        for vertex in self.graph:
            if len(self.graph[vertex]) % 2 != 0:
                odd += 1
        if odd == 0 or odd == 2:
            return True
        return False

    def bfs_traversal(self, vertex):
        """
        Breadth First Search
        -> Choose the fringe edge that was seen first
        -> Use Queues for this
        -> When you reach any node,
            -> first capture all the nieghbors put them in a queue
            -> Treverse until queue is empty
            -> Maintain a dict to know if a node has been visted before
        """

        captured = {}
        parent = {}
        visited = {}

        visited[vertex] = True
        captured[vertex] = True

        queue = [vertex]

        while queue:
            temp = queue.pop(0)
            captured[temp] = 1
            for w in self.graph[temp]:
                if w not in visited:
                    visited[w] = True
                    parent[w] = temp
                    queue.append(w)

    def dfs_traversal(self, vertex):
        """
        Deapth First Search
        -> Choose the fringe edge that was seen last
        -> Use Stacks for this
        -> Instead of going broad, go as deep as possible
        """

        captured = {}
        parent = {}
        visited = {}

        visited[vertex] = True
        captured[vertex] = True

        stack = [vertex]

        while stack:
            temp = stack.pop()
            captured[temp] = 1
            for w in self.graph[temp]:
                if w not in visited:
                    visited[w] = True
                    parent[w] = temp
                    stack.append(w)

    def dfs_recursive(self, vertex):
        visited[vertex] = True
        for w in self.graph[vertex]:
            if w not in visited:
                parent[vertex] = vertex
                self.dfs_recursive(w)


    def is_graph_connected(self):
        # A graph is connected if all the vertices in the graph can reach each other
        # In other words from any given vertex, if all other vertics in the graph have a path (are reachable), then the
        # graph is connected
        pass
