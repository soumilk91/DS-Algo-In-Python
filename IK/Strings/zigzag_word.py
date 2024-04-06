"""
Author: Soumil Ramesh Kulkarni
Date: 04.03.2024

Question:
A word can be written in a vertical zigzag fashion in a given number of lines, e.g. KICKSTART in three lines looks like this:

K     S    T
I  K  T  R
C     A
Reading this text line by line gives us KSTIKTRCA.

Given a word and a number of lines for zigzagging, return that line-by-line representation.

Example One
{
"nlines": 4,
"word": "INTERVIEW"
}
Output:

"IINVETRWE"
Because zigzagging INTERVIEW in four lines gives this:

I        I
N     V  E
T  R     W
E
Example Two
{
"nlines": 1,
"word": "KICKSTART"
}
Output:

"KICKSTART"
"""

def zigzag(nlines, word):
    """
    Args:
     nlines(int32)
     word(str)
    Returns:
     str
    """
    # Write your code here.
    if nlines == 1:
        return word
    row_arr = [""] * nlines
    row_index = 1
    going_up = True

    for ch in word:
        row_arr[row_index - 1] += ch
        if row_index == nlines:
            going_up = False
        elif row_index == 1:
            going_up = True

        if going_up:
            row_index += 1
        else:
            row_index -= 1
    return "".join(row_arr)
