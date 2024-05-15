"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
ower of Hanoi is a mathematical puzzle where we have three pegs and n disks. The objective of the
puzzle is to move the entire stack to another peg, obeying the following simple rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e.
a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
Given n denoting the number of disks in the first peg, return all the steps required to move all disks from the
first peg to the third peg in minimal number of steps.

Example
{
"n": 4
}
Output:

[
[1, 2],
[1, 3],
[2, 3],
[1, 2],
[3, 1],
[3, 2],
[1, 2],
[1, 3],
[2, 3],
[2, 1],
[3, 1],
[2, 3],
[1, 2],
[1, 3],
[2, 3]
]
Following steps:

[1, 2] = Shift top disk of the first peg to top of the second peg.
Picture after this step will be:
First peg: 2 3 4
Second peg: 1
Third peg: Empty

[1, 3] = Shift top disk of the first peg to top of the third peg.
Picture after this step will be:
First peg: 3 4
Second peg: 1
Third peg: 2

Similarly after following remaining steps, the final configuration will be:
First peg: Empty
Second peg: Empty
Third peg: 1 2 3 4

Hence, our objective is achieved.


"""


def tower_of_hanoi(n):

    move_map = {}

    def move(n, from_tower, to_tower):
        if n == 1:
            move_map[(n, from_tower, to_tower)] = [[from_tower,to_tower]]
        else:
            if from_tower == 1:
                if to_tower == 3:
                    if (n - 1, 1, 2) not in move_map:
                        move(n-1, 1, 2)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 1, 2)][:]
                    move_map[(n, from_tower, to_tower)].append([1, 3])
                    if (n - 1, 2, 3) not in move_map:
                        move(n - 1, 2, 3)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 2, 3)]
                elif to_tower == 2:
                    if (n - 1, 1, 3) not in move_map:
                        move(n-1, 1, 3)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 1, 3)][:]
                    move_map[(n, from_tower, to_tower)].append([1, 2])
                    if (n - 1, 3, 2) not in move_map:
                        move(n - 1, 3, 2)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 3, 2)]
            elif from_tower == 2:
                if to_tower == 1:
                    if (n - 1, 2, 3) not in move_map:
                        move(n-1, 2, 3)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 2, 3)][:]
                    move_map[(n, from_tower, to_tower)].append([2, 1])
                    if (n - 1, 3, 1) not in move_map:
                        move(n - 1, 3, 1)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 3, 1)]
                elif to_tower == 3:
                    if (n - 1, 2, 1) not in move_map:
                        move(n-1, 2, 1)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 2, 1)][:]
                    move_map[(n, from_tower, to_tower)].append([2, 3])
                    if (n - 1, 1, 3) not in move_map:
                        move(n - 1, 1, 3)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 1, 3)]
            elif from_tower == 3:
                if to_tower == 1:
                    if (n - 1, 3, 2) not in move_map:
                        move(n-1, 3, 2)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 3, 2)][:]
                    move_map[(n, from_tower, to_tower)].append([3, 1])
                    if (n - 1, 2, 1) not in move_map:
                        move(n - 1, 2, 1)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 2, 1)]
                elif to_tower == 2:
                    if (n - 1, 3, 1) not in move_map:
                        move(n-1, 3, 1)
                    move_map[(n, from_tower, to_tower)] = move_map[(n - 1, 3, 1)][:]
                    move_map[(n, from_tower, to_tower)].append([3, 2])
                    if (n - 1, 1, 2) not in move_map:
                        move(n - 1, 1, 2)
                    move_map[(n, from_tower, to_tower)] += move_map[(n - 1, 1, 2)]

    move(n, 1, 3)

    return move_map[(n, 1, 3)]
