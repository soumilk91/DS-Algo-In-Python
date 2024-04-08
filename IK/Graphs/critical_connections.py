"""
Author: Soumil Ramesh Kulkarni
Date: 04.06.2024

Question:
Given a network of servers where each server is connected to every other server directly or indirectly through the
bidirectional connections in the network, find all the critical connections.

A connection in a connected network is said to be critical if removing it disconnects the network.

Example One
Example one

{
"number_of_servers": 5,
"connections": [
[0, 1],
[0, 2],
[0, 4],
[1, 2],
[1, 3]
]
}
Output:

[
[0, 4],
[1, 3]
]
Order of servers within a connection and order of connections in the output does not matter, so another one of several
other correct outputs here is

[
[3, 1]
[0, 4],
]
Example Two
Example Two

{
"number_of_servers": 4,
"connections": [
[0, 1],
[0, 2],
[0, 3]
[1, 2],
[2, 3]
]
}
Output:

[
[-1, -1]
]
Removing any one connection won't disconnect the network.
"""


def find_critical_connections(number_of_servers, connections):
    """
    Args:
     number_of_servers(int32)
     connections(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # node is index, neighbors are in the list
    graph = [[] for i in range(number_of_servers)]

    # build graph
    for n1, n2 in connections:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # min_discovery_time of nodes at respective indices from start node
    # 1. default to max which is the depth of continuous graph
    lows = [number_of_servers] * number_of_servers

    # critical edges
    critical = []

    # args: node, node discovery_time in dfs, parent of this node
    def dfs(node, discovery_time, parent):

        # if the low is not yet discovered for this node
        if lows[node] == number_of_servers:

            # 2. default it to the depth or discovery time of this node
            lows[node] = discovery_time

            # iterate over neighbors
            for neighbor in graph[node]:

                # all neighbors except parent
                if neighbor != parent:

                    expected_discovery_time_of_child = discovery_time + 1
                    actual_discovery_time_of_child = dfs(neighbor, expected_discovery_time_of_child, node)

                    # nothing wrong - parent got what was expected => no back path
                    # this step is skipped if there is a back path
                    if actual_discovery_time_of_child >= expected_discovery_time_of_child:
                        critical.append([node, neighbor])

                    # low will be equal to discovery time of this node or discovery time of child
                    # whichever one is minm
                    # if its discovery time of child - then there is a backpath
                    lows[node] = min(lows[node], actual_discovery_time_of_child)

        # return low of this node discovered previously or during this call
        return lows[node]

    dfs(number_of_servers - 1, 0, -1)

    if not critical:
        return [[-1, -1]]
    return critical
