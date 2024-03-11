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
        shortest_string = min(strs)
        longest_string = max(strs)

        start_index = 0
        while start_index < len(shortest_string):
            if shortest_string[start_index] != longest_string[start_index]:
                shortest_string = shortest_string[:start_index]
            start_index += 1
        return shortest_string

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