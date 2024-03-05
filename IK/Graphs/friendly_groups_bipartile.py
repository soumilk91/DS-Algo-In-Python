"""
Author: Soumil Ramesh Kulkarni
Date: 03.04.2024

Question:
There are n people living in a town. Some of them dislike each other. Given the value of n and two equal length integer arrays called dislike1 and dislike2. For each i in [0, dislike1_size - 1], the person dislike1[i] dislikes the person dislike2[i]. Check if we can divide the people of the town into two sets such that each person belongs to exactly one set and no two persons disliking each other belong to the same set.

Example One
{
"num_of_people": 5,
"dislike1": [0, 1, 1, 2, 3],
"dislike2": [2, 2, 4, 3, 4]
}
Output:

1
The people can be partitioned into two sets [0, 1, 3] and [2, 4].

Example Two
{
"num_of_people": 4,
"dislike1": [0, 0, 0, 1, 2],
"dislike2": [1, 2, 3, 2, 3]
}
Output:

0
"""


def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # Write your code here.

    if num_of_people <= 1:
        return True

        # Create a graph

    # This is going to be a directed graph
    graph = {}
    for i in range(num_of_people):
        graph[i] = []

    for i in range(len(dislike1)):
        graph[dislike1[i]].append(dislike2[i])

    color = [-1] * num_of_people

    for i in range(num_of_people):
        if color[i] == -1:
            if not bfs(i, graph, color):
                return False
    return True


def bfs(node, graph, color):
    queue = [node]
    color[node] = 0

    while queue:
        temp_node = queue.pop(0)
        for i in graph[temp_node]:
            if color[temp_node] == color[i]:
                return False

            if color[i] == -1:
                color[i] = 1 - color[temp_node]
                queue.append(i)
    return True