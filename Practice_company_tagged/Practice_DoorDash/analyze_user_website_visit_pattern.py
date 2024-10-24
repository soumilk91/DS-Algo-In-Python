"""
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

Note that the websites in a pattern do not need to be visited contiguously, they only need to be visited in the order they appeared in the pattern.



Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
Example 2:

Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]

"""
from itertools import combinations
from typing import *
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Combine and sort the input data by timestamp
        data = sorted(zip(username, timestamp, website), key=lambda x: x[1])

        # Step 2: Group websites visited by each user
        user_visits = defaultdict(list)
        for user, _, site in data:
            user_visits[user].append(site)

        # Step 3: Count the occurrence of each 3-sequence pattern for each user
        pattern_count = defaultdict(set)  # pattern -> set of users

        for user, sites in user_visits.items():
            # Find all unique 3-sequences of websites for this user
            if len(sites) >= 3:
                patterns = set(combinations(sites, 3))  # All combinations of length 3
                for pattern in patterns:
                    pattern_count[pattern].add(user)

        # Step 4: Find the pattern with the largest score (most users visited it)
        max_pattern = None
        max_count = 0

        for pattern, users in pattern_count.items():
            count = len(users)
            if count > max_count or (count == max_count and pattern < max_pattern):
                max_count = count
                max_pattern = pattern

        # Return the lexicographically smallest pattern with the largest count
        return list(max_pattern)