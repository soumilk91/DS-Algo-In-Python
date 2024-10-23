"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped
within days days.



Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into
parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
Example 2:

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

from typing import *
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if a given capacity can ship all packages within the required days
        def canShipWithCapacity(capacity):
            total_weight = 0
            day_count = 1
            for weight in weights:
                if total_weight + weight > capacity:
                    day_count += 1
                    total_weight = weight  # Start a new day with the current package
                    if day_count > days:
                        return False
                else:
                    total_weight += weight
            return True

        # Binary search between the max weight (smallest capacity) and the total weight (largest capacity)
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShipWithCapacity(mid):
                right = mid  # Try for a smaller capacity
            else:
                left = mid + 1  # Increase the capacity

        return left  # The minimum capacity to ship within 'days' days
