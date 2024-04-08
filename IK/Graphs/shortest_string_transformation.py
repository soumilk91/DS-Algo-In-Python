"""
Author: Soumil Ramesh Kulkarni
Date: 04.06.2024

Question:
You are given a dictionary called words and two string arguments called start and stop. All given strings have equal length.

Transform string start to string stop one character per step using words from the dictionary. For example, "abc" → "abd" is
a valid transformation step because only one character is changed ("c" → "d"), but "abc" → "axy" is not a valid one because
two characters are changed ("b" → "x" and "c" → "y").

You need to find the shortest possible sequence of strings (two or more) such that:

First string is start.
Last string is stop.
Every string (except the first one) differs from the previous one by exactly one character.
Every string (except, possibly, first and last ones) are in the dictionary of words.
Example One
{
"words": ["cat", "hat", "bad", "had"],
"start": "bat",
"stop": "had"
}
Output:

["bat", "bad", "had"]
OR

["bat", "hat", "had"]
In "bat", change "t" → "d" to get "bad".
In "bad", change "b" → "h"to get "had".

OR

In "bat", change "b" → "h" to get "hat".
In "hat", change "t" → "d" to get "had".

Example Two
{
"words": [],
"start": bbb,
"stop": bbc
}
Output:

["bbb", "bbc"]
In "bbb", the last character to "b" and get "bbc".

Example Three
{
"words": [],
"start": "zzzzzz",
"stop": "zzzzzz"
}
Output:

["-1"]
No sequence of strings exists that would satisfy all requirements. For example, ["zzzzzz", "zzzzzz"]
does not satisfy requirement #3. In such situations, ["-1"] is the correct answer.
"""

from collections import deque


def string_transformation(words, start, stop):
    """
    Args:
     words(list_str)
     start(str)
     stop(str)
    Returns:
     list_str
    """
    # Write your code here.
    words_set = set(words)
    visited = {}

    def getNeighbors(target, words_set):
        neighbor = []
        if len(words_set) > 26:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(target)):
                    word = target[:i] + c + target[i + 1:]
                    if word in words_set:
                        neighbor.append(word)
        else:
            for word in words_set:
                count = 0
                for i in range(len(target)):
                    if target[i] != word[i]:
                        count += 1
                    if count > 1:
                        break
                if count == 1:
                    neighbor.append(word)

        return neighbor

    def getDistance(word, stop):
        count = 0
        for i in range(len(word)):
            if word[i] != stop[i]:
                count += 1
            if count > 1:
                return count
        return count

    if getDistance(start, stop) == 1:
        return [start, stop]

    def bfs(start):
        q = deque([(start, [start])])
        visited[start] = True
        while q:
            node, trans = q.popleft()
            for neighbor in getNeighbors(node, words_set):
                if getDistance(neighbor, stop) == 1:
                    return trans + [neighbor, stop]
                if neighbor not in visited:
                    visited[neighbor] = True
                    q.append((neighbor, trans + [neighbor]))
        return ["-1"]

    return bfs(start)