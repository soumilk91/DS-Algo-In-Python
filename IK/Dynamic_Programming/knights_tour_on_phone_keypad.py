"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
Given a phone keypad as shown below:

1 2 3
4 5 6
7 8 9
– 0 –

How many different phone numbers of given length can be formed starting from the given digit?
The constraint is that the movement from one digit to the next is similar to the movement of the Knight in chess.

For example, if we are at 1, then the next digit can be either 6 or 8; if we are at 6 then the next digit can be 1, 7 or 0.

Repetition of digits is allowed, e.g. 1616161616 is a valid number.
There is no need to list all possible numbers, just find how many they are.
Find a polynomial-time solution, based on Dynamic Programming.

Example One
{
"start_digit": 1,
"phone_number_length": 2
}
Output:

2
Two possible numbers of length 2: 16, 18.

Example Two
{
"start_digit": 1,
"phone_number_length": 3
}
Output:

5
The possible numbers of length 3: 160, 161, 167, 181, 183
"""

"""
Asymptotic complexity in terms of `phone_number_length`:
* Time: O(phone_number_length).
* Auxiliary space: O(phone_number_length).
* Total space: O(phone_number_length).
"""

def count_phone_numbers_of_given_length(start_digit, phone_number_length):
    list_of_neighbors = [
        # 0
        [4, 6],
        # 1
        [6, 8],
        # 2
        [7, 9],
        # 3
        [4, 8],
        # 4
        [3, 9, 0],
        # 5
        [],
        # 6
        [1, 7, 0],
        # 7
        [2, 6],
        # 8
        [1, 3],
        # 9
        [2, 4]
    ]

    numbers_till = [[0]*10 for _ in range(phone_number_length)]
    # First digit is already given. So we can only form one number of length 1.
    numbers_till[0][start_digit] = 1

    for i in range(1, phone_number_length):
        for num in range(10):
            for to in list_of_neighbors[num]:
                # We can come to num from all its neighbors.
                # So we will add all possible numbers of length (i - 1) that are neighbours of num.
                numbers_till[i][num] += numbers_till[i - 1][to]

    ans = sum(numbers_till[phone_number_length - 1])
    return ans
