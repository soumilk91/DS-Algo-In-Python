"""
Author: Soumil Ramesh Kulkarni
Date: 01/28/2023

Question:
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
 return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 Eg:

 Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                count += 1
                flowerbed[i] = 1
            if count == n: return True
        return False

