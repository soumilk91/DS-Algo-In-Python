"""
Author: Soumil Ramesh Kulkarni
Date: 04.06.2024

Question:
There are zombies in Seattle. Some of them know each other directly. Others might know each other transitively,
through others. For example, if zombies A<->B and B<->C know each other directly, then A and C know each other
indirectly and all three belong to one cluster.

Knowing which zombies know each other directly, find the number of the zombie clusters.

Input is a square matrix where each cell, zombies[A][B], indicates whether zombie A knows zombie B directly.


{
"zombies": [
"1100",
"1110",
"0110",
"0001"
]
}
Output:

2Example Two
Example one

{
"zombies": [
"10000",
"01000",
"00100",
"00010",
"00001"
]
}
Output:

5
Each zombie forms their own cluster: {z0}, {z1}, {z2}, {z3}, and {z4}. The total number of clusters is 5.
"""

from collections import deque
def zombie_cluster(zombies):
    """
    Args:
     zombies(list_str)
    Returns:
     int32
    """
    # Write your code here.
    visited = [-1] * len(zombies)
    count = 0
    q = deque()
    for v in range(len(zombies)):
        if visited[v] == -1:
            visited[v] = 1
            count += 1
            q.append(v)

        while q:
            node = q.popleft()
            for neighbor in range(len(zombies)):
                if visited[neighbor] == -1 and zombies[node][neighbor] == '1':
                    visited[neighbor] = 1
                    q.append(neighbor)

    return count