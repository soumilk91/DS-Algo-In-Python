"""
Question:

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from typing import *
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Create the Graph. Key is going to be a pattern
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)
        # print(graph)
        # Use BFS to traverse the Graph
        visited = set()
        result = 1
        queue = deque([beginWord])
        while queue:
            for i in range(len(queue)):
                currWord = queue.popleft()
                if currWord == endWord:
                    return result
                for j in range(len(currWord)):
                    pattern = currWord[:j] + "*" + currWord[j + 1:]
                    for neighWord in graph[pattern]:
                        if neighWord not in visited:
                            visited.add(neighWord)
                            queue.append(neighWord)
            result += 1
        return 0