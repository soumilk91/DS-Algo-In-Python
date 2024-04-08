"""
Author: Soumil Ramesh Kulkarni
Date: 04.06.2024

Question:
Given a two-dimensional maze represented by a character grid, find the shortest path from start to goal cell.
You can move vertically or horizontally—but not diagonally—one step at a time.

There are six types of cells:

'@' for start
'+' for goal
'.' for land
'#' for water
uppercase letter for door
lowercase letter for key
There's exactly one start and one goal cell. Other cells may appear any number of times. Water can never be visited.
A door cell can only be visited after visiting a matching key, e.g. key 'a' for door 'A'. Other cells can be visited
unconditionally. It is allowed to visit a cell more than once.

Example
{
"grid": [
"...B",
".b#.",
"@#+."
]
}
Output:

[
[2, 0],
[1, 0],
[1, 1],
[0, 1],
[0, 2],
[0, 3],
[1, 3],
[2, 3],
[2, 2]
]
We start at [2, 0] where the start (@) is located, then we go up to [1, 0] where the adjacent piece of land (.) is,
and so on. We visit the following cells on the way:
@ → . → b → . → . → B → . → . → +

To get to the goal we have to walk through door 'B', and for that we have to pass by the matching key 'b' first.
We do all of that in the smallest number of steps possible.
"""

from collections import deque, defaultdict

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "abcdefghijklmnopqrstuvwxyz".upper()


def find_shortest_path(grid):
    """
    Args:
     grid(list_str)
    Returns:
     list_list_int32
    """
    # Write your code here.
    start = None
    present_keys = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in LOWERCASE:
                present_keys.add(grid[i][j])
            elif grid[i][j] == '@':
                start = (i, j)

    def neighbors(i, j, keys):
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = i + x, j + y
            if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]):
                cell = grid[new_i][new_j]
                if cell == '#' or (cell in UPPERCASE and not (keys & (1 << (ord(cell) - ord('A'))))):
                    continue
                yield new_i, new_j

    queue = deque([(start[0], start[1], [], 0)])
    visited = defaultdict(set)
    while len(queue) > 0:
        i, j, paths, keys = queue.popleft()
        paths = paths + [[i, j]]

        if grid[i][j] in present_keys:
            keys = keys | 1 << (ord(grid[i][j]) - ord('a'))

        if grid[i][j] == "+":
            return paths

        for x, y in neighbors(i, j, keys):
            if (x, y) not in visited[keys]:
                visited[keys].add((x, y))
                queue.append((x, y, paths, keys))

    return [-1]