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

from collections import deque
def can_be_divided(num_of_people, dislike1, dislike2):
    group = [0] * num_of_people
    adj_list = [[] for i in range(num_of_people)]

    for i in range(len(dislike1)):
        adj_list[dislike1[i]].append(dislike2[i])
        adj_list[dislike2[i]].append(dislike1[i])

    def bfs(root):
        q = deque()
        group[root] = 1
        q.append(root)

        while q:
            person = q.popleft()
            person_group = group[person]
            for disliked_person in adj_list[person]:
                if group[disliked_person] == person_group: return False
                if group[disliked_person] == 0:  # haven't visited
                    group[disliked_person] = person_group + 1
                    q.append(disliked_person)
        return True

    for i in range(num_of_people):
        if group[i] == 0:
            if not bfs(i): return False
    return True
