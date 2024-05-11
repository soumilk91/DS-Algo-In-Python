"""
Author: Soumil Ramesh Kulkarni
Date: 05.11.2024

Question:
You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:

0 if it is a batch of buy orders, or
1 if it is a batch of sell orders.
Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.

There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.
Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 109 + 7.


"""

import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders):
        b, s = [], []
        heapq.heapify(b)
        heapq.heapify(s)

        for p, a, o in orders:
            if o == 0:
                heapq.heappush(b, [-p, a])

            elif o == 1:
                heapq.heappush(s, [p, a])

            # Check "good" condition
            while s and b and s[0][0] <= -b[0][0]:
                a1, a2 = b[0][1], s[0][1]

                if a1 > a2:
                    b[0][1] -= a2
                    heapq.heappop(s)
                elif a1 < a2:
                    s[0][1] -= a1
                    heapq.heappop(b)
                else:
                    heapq.heappop(b)
                    heapq.heappop(s)

        count = sum([a for p, a in b]) + sum([a for p, a in s])
        return count % (10 ** 9 + 7)