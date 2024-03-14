"""
Author: Soumil Ramesh Kulkarni
Date: 03.03.2024

Question:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution_Better:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs)
        longest = max(strs)
        result = []
        start = 0

        while start < len(shortest):
            if shortest[start] == longest[start]:
                result.append(shortest[start])
                start += 1
            else:
                break
        if not result:
            return ""
        else:
            return "".join(result)

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest_string_in_list = min(strs, key=len)
        #print(shortest)
        for i, char in enumerate(shortest_string_in_list):
            for other in strs:
                if other[i] != char:
                    return shortest_string_in_list[:i]
        return shortest_string_in_list

temp = Solution()
print(temp.longestCommonPrefix(["flower","flow","flight"]))