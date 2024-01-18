"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given 'n' pairs for paranthesis, Write a function to generate all Well formed parenthesis
This is a Backtracking Example
Eg: n = 3
output: ['((()))', '(()())', '(())()', '()(())', '()()()']
"""

result = []
def _helper(leftnumber, rightnumber, slate):
    # Backtracking Case
    if rightnumber < leftnumber or rightnumber < 0 or leftnumber < 0:
        return

    # Base Case
    if leftnumber == rightnumber == 0:
        result.append("".join(slate))
        return

    # Recursive Case
    #Left Paranthesis
    slate.append("(")
    _helper(leftnumber-1, rightnumber, slate)
    slate.pop()

    # Right Parenthesis
    slate.append(")")
    _helper(leftnumber, rightnumber-1, slate)
    slate.pop()

def generate_valid_parenthesis(n):
    _helper(n,n, [])

generate_valid_parenthesis(3)
print(result)
