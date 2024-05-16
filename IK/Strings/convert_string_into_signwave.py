"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:

Convert given string sinusoidally. Return the sinusoidal representation as three strings.

Example
{
"s": "InterviewKickstart"
}
Output:

[
"  t   i   i   t   ",
" n e v e K c s a t",
"I   r   w   k   r "
]
As you can see in the output, in the sinusoidal format:

you return three strings,
character #1 is printed in the first column of the third string,
character #2 is printed in the second column of the second string,
character #3 is printed in the third column of the first string,
character #4 is printed in the fourth column of the second string,
character #5 is printed in the fifth column of the third string,
character #6 is printed in the sixth column of the second string,
all other characters are spaces,
and the same pattern repeats.
Length of all three strings you return is the same.
"""


def convert_string_sinusoidally(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    n = len(s)

    row1 = [' '] * n
    row2 = [' '] * n
    row3 = [' '] * n

    for i in range(0, n, 4):
        row1[i] = s[i]

    for i in range(1, n, 2):
        row2[i] = s[i]

    for i in range(2, n, 4):
        row3[i] = s[i]
    return [''.join(row3), ''.join(row2), ''.join(row1)]