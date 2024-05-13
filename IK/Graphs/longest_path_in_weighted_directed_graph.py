"""
Author: Soumil Ramesh Kulkarni
Date: 05.11.2024

Question:
Given a weighted directed acyclic graph (DAG), find the longest path between two nodes.

Example one

{
"dag_nodes": 4,
"dag_from": [1, 1, 1, 3],
"dag_to": [2, 3, 4, 4],
"dag_weight": [2, 2, 4, 3],
"from_node": 1,
"to_node": 4
}
Output:

[1, 3, 4]
Total there are two paths from node 1 to node 4:

1 -> 4 with length 4.
1 -> 3 -> 4 with length 2 + 3 = 5.
The latter is the longest one.

Notes
The first four arguments of the function - dag_nodes, dag_from, dag_to, dag_weight - together define the given weighted DAG: there are dag_nodes nodes and there is an edge from dag_from[i] node to dag_to[i] node with length dag_weight[i] for 0 <= i <= dag_nodes - 1.
Return an array of integers, the nodes in the longest paths from from_node to to_node (including both ends).
If from_node = to_node, return [from_node].
If there are multiple longest paths, return any one.
"""


def find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node):
    """
    Args:
     dag_nodes(int32)
     dag_from(list_int32)
     dag_to(list_int32)
     dag_weight(list_int32)
     from_node(int32)
     to_node(int32)
    Returns:
     list_int32
    """

    # Write your code here.
    def dfs(from_node, visited):

        visited[from_node] = 0  # once visited, a node is defaulted to 0

        # Base case
        if from_node == to_node:  # if current from node has reaches the destination node, set the weight of that
            visited[from_node] = (0, None)  # node to 0 and the node with the max weight (maxNode) to None
            return

        # Recursive case
        maxNode = None
        maxWeight = -1
        # Of all the edges coming out of current from_node, add the weight associated
        for toNode, nWeight in weightedEdges[
            from_node].items():  # with it, if max weight is not negative, update visited[from_node]
            # to have the maxWeight and node associated with it
            if visited[toNode] == -1:  # if node has not been visited,
                dfs(toNode, visited)  # recurse

            if visited[toNode] == 0:  # no path to to_node, do not include
                continue

            elif visited[toNode][
                0] + nWeight > maxWeight:  # if the visited node is not 0 after it's been visited, then it it would
                maxWeight = visited[toNode][
                                0] + nWeight  # have a tuple as a value, which contains maxWeight and maxNode
                maxNode = toNode

        if maxWeight > -1:
            visited[from_node] = (maxWeight, maxNode)  # update visited if maxWeight has changed

            # an array of dictionaries. Index of the array is vertex in dag_from,

    weightedEdges = []  # key is vertex in dag_to, and value is weight of that edge
    # what weightedEdges looks like, eg: [{}, {2: 2, 3: 2, 4: 4}, {}, {4: 3}, {}]
    visited = [-1] * (dag_nodes + 1)  # what visited looks like, eg: [-1, (5, 3), 0, (3, 4), (0, None)]

    for i in range(dag_nodes + 1):  # +1 because vertices are labeled from 1 to n, easier to relate indexvertex
        weightedEdges.append(dict())

    for i in range(len(dag_from)):  # How to access an element in an array of dictionaries:
        weightedEdges[dag_from[i]][dag_to[i]] = dag_weight[i]  # Eg, a = [{1: 2}, {3: 4}], so a[0][1] returns a 2

    dfs(from_node, visited)  # first DFS

    path = []  # Reconstruct path
    curr = from_node
    while visited[curr][1]:  # while there is weight, which is not None,
        path.append(curr)  # append the key of each dictionary
        curr = visited[curr][1]  # set curr to the next node in the path that has maxNode

    path.append(to_node)

    return path
