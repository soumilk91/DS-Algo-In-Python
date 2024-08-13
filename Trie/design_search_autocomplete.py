"""
Author: Soumil Kulkarni
Date: 08.13.2024

Question:

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Implement the AutocompleteSystem class:

AutocompleteSystem(String[] sentences, int[] times) Initializes the object with the sentences and times arrays.
List<String> input(char c) This indicates that the user typed the character c.
Returns an empty array [] if c == '#' and stores the inputted sentence in the system.
Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.


Example 1:

Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

Explanation
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
"""

from typing import *
import collections
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.three = []  # three sentences


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, sentence, time):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            for i, (t, s) in enumerate(node.three):  # update three sentences
                if s == sentence:
                    tmp = node.three[:]
                    tmp[i][0] = time
                    break
            else:
                tmp = node.three + [[time, sentence]]
            node.three = sorted(tmp, key=lambda x: (-x[0], x[1]))[:3]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.d = collections.Counter()  # keep tracking {sentence: time}
        self.trie = Trie()  # trie
        self.node = self.trie.root  # pointer to root and move along with input characters
        for sentence, time in zip(sentences, times):  # add initial info
            self.d[sentence] += time
            self.trie.add(sentence, time)
        self.cur = ''  # prefix
        self.prefix_none = False  # True if prefix cannot be found

    def input(self, c: str) -> List[str]:
        if c == '#':  # input ends
            self.node = self.trie.root  # reset self.node to root
            self.d[self.cur] += 1  # increment counter by 1
            self.trie.add(self.cur, self.d[self.cur])  # update sentence and time
            self.cur = ''  # reset prefix string
            self.prefix_none = False  # reset this flag
            return []  # return
        self.cur += c  # making prefix
        if c not in self.node.children or self.prefix_none:  # when prefix is not found the first time and time after 1st time
            self.prefix_none = True  # set flag
            return []
        self.prefix_none = False  # reset prefix_none flag
        self.node = self.node.children[c]  # move to next node
        return [word for _, word in self.node.three]  # return 3 words