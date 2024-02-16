"""
Author: Soumil Ramesh Kulkarni
Date: 02.14.2024

Question:
"""

#Optimal Solution using 2 pointers
# Time : O(n)
# Space: O(1)

def segregate_evens_and_odds_optimal(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) -  1
    while i < j:
        if numbers[j] %2 == 0:
            numbers[j], numbers[i] = numbers[i], numbers[j]
            i += 1
        else:
            j -= 1
    return numbers

# Time: O(n)
# Space: O(n) for the stacks Created
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    even_stack = []
    odd_stack = []
    for i in numbers:
        if i % 2 == 0:
            even_stack.append(i)
        else:
            odd_stack.append(i)
    i = 0
    while even_stack:
        numbers[i] = even_stack.pop()
        i += 1
    while odd_stack:
        numbers[i] = odd_stack.pop()
        i += 1
    return numbers