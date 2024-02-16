"""
Author: Soumil Ramesh Kulkarni
Date: 02.15.2024

Question:
First array has n positive numbers, and they are sorted in the non-descending order.

Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.

Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.

Eg:
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
[1, 2, 3, 4, 5, 6]

"""
"""
Asymptotic complexity in terms of size of `first` `n`:
* Time: O(n).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def merge_one_into_another(first, second):
    n = len(first)
    last1 = n - 1
    last2 = n - 1
    last = n + n - 1

    while last >= 0: # While at least one element remains to be processed.
        if last1 < 0:
            # No elements remain in the first array.
            # Think about the case when first = [4, 5, 6] & second = [1, 2, 3, 0, 0, 0].
            # Once last1 = -1, second will be [1, 2, 3, 4, 5, 6]. So, we can stop here.
            break
        elif last2 < 0:
            # All `n` non-zero elements present in second array (initially) are used.
            second[last] = first[last1]
            last -= 1
            last1 -= 1
        elif first[last1] <= second[last2]:
            # The next number in the second array is greater,
            # so it goes to the next position.
            second[last] = second[last2]
            last -= 1
            last2 -= 1
        else:
            second[last] = first[last1]
            last -= 1
            last1 -= 1

    return second