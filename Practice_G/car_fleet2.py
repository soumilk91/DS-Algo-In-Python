"""
Question:

There are n cars traveling at different speeds in the same direction along a one-lane road.
You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy
the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the
formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1
if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.



Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s.
After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
"""

from typing import *
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        # Stack: go from back and use stack to get ans
        # Time: O(n)
        # Space: O(n)

        stack = []  # index
        ans = [-1] * len(cars)
        for i in range(len(cars) - 1, -1, -1):
            # remove cars that are faster than current car since it will never collide
            while stack and cars[i][1] <= cars[stack[-1]][1]:
                stack.pop()

            while stack:  # if car left, we can compute collide time with current car.
                collision_t = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
                # if current car's collide time is greater than previous car's collide time
                # (previous collided before current), then we have to find previous car's previous car
                # to compute collide time with that car, so we pop from stack and re-process
                # Otherwise, we add that collide time to answer and break
                if ans[stack[-1]] == -1 or collision_t <= ans[stack[-1]]:
                    ans[i] = collision_t
                    break
                stack.pop()
            stack.append(i)
        return ans