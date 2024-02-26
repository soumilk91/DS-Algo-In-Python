"""
Author: Soumil Ramesh Kulkarni
Date: 02.24.2024

Question:
You have to check whether a given string is a valid mathematical expression or not.
A string is considered valid if it contains matching opening and closing parenthesis as well as valid mathematical operations.
The string contains the following set of parentheses ‘(‘, ’)’, ’[’, ’]’, ’{’, ’}’,
numbers from 0 to 9 and following operators ‘+’, ’-’ and ‘*’.

Example One
{
"expression": "{(1+2)*3}+4"
}
Output:

1
The mathematical expression as well as the parentheses are valid.

Example Two
{
"expression": "((1+2)*3*)"
}
Output:

0
Here the parentheses are valid but the mathematical expression is not.
There is an operator ‘*’ without any operand after it.
"""

"""
Asymptotic complexity in terms of length of `expression` `n`:
* Time: O(n).
* Auxiliary space: O(n).
* Total space: O(n).
"""

def is_valid(expression):
    st1 = []  # stores digits
    st2 = []  # stores operators and parantheses
    isTrue = True
    for char in expression:
        if char.isdigit():  # if the character is a digit, we push it to st1
            st1.append(int(char))
            if isTrue:
                isTrue = False
            else:
                return False
        elif is_operator(char):  # if the character is an operator, we push it to st2
            st2.append(char)
            isTrue = True
        else:
            if is_bracket_open(char):  # if the character is an opening parantheses we push it to st2
                st2.append(char)
            else:  # If it is a closing bracket
                flag = True
                while st2:  # we keep on removing characters until we find the corresponding open bracket or the stack becomes empty
                    c = st2.pop()
                    if c == get_corresponding_char(char):
                        flag = False
                        break
                    else:
                        if len(st1) < 2:
                            return False
                        else:
                            st1.pop()
                if flag:
                    return False

    while st2:
        c = st2.pop()
        if not is_operator(c):
            return False
        if len(st1) < 2:
            return False
        else:
            st1.pop()

    return len(st1) <= 1 and not st2


def get_corresponding_char(c):
    if c == ')':
        return '('
    elif c == ']':
        return '['
    else:
        return '{'


def is_bracket_open(c):
    return c in ['(', '[', '{']


def is_operator(c):
    return c in ['+', '-', '*']
