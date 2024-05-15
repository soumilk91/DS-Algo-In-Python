"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Given n buildings on a two-dimensional plane, find the skyline of these buildings.

Each building on the two-dimensional plane has a start and end x-coordinates, and a y-coordinate height.
Skyline is defined as a unique representation of rectangular strips of different heights which are created
after the overlap of multiple buildings on a two-dimensional plane.

The following picture demonstrates some buildings on the left side and their skyline on the right.

Buildings Buildings

Example
{
"buildings": [
[2, 9, 10],
[3, 7, 15],
[5, 12, 12],
[15, 20, 10],
[19, 24, 8]
]
}
Output:

[
[2, 10],
[3, 15],
[7, 12],
[12, 0],
[15, 10],
[20, 8],
[24, 0]
]
From the image referenced above, we see the blue building at the start and the corresponding red dot in the
right image at (2, 10). The next change in skyline occurs at an x coordinate of 3 with the red building coming up
at the height of 15, so in the output, the next line is printed as (3, 15). Similarly, all the buildings are traversed
to find the output as given in the sample output section.
"""

import heapq
import math

def find_skyline(buildings):
    buildings_min = []

    for start, end, height in buildings:
        buildings_min.append((start, -height, end))
        buildings_min.append((end, 0, 0))
    buildings_min.sort()

    processing_heap = [(0, math.inf)]
    res = [[0, 0]]

    for start, height, end in buildings_min:

        while start >= processing_heap[0][1]:
            heapq.heappop(processing_heap)

        if height:
            heapq.heappush(processing_heap, (height, end))

        if res[-1][1] != -1 * processing_heap[0][0]:
            res.append([start, -processing_heap[0][0]])

    return res[1:]
