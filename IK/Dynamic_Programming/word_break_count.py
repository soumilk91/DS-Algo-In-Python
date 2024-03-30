"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
Given a dictionary of words and a string txt, find the number of ways the string can be broken down into the dictionary words.
Return the answer modulo 109 + 7.

Example
{
"dictionary": ["kick", "start", "kickstart", "is", "awe", "some", "awesome"],
"txt": "kickstartisawesome"
}
Output:

4
Here are all four ways to break down the string into the dictionary words:

kick start is awe some
kick start is awesome
kickstart is awe some
kickstart is awesome
4 % 1000000007 = 4 so the correct output is 4.
"""


def word_break_count(dictionary, txt):
    """
    Args:
     dictionary(list_str)
     txt(str)
    Returns:
     int32
    """
    """
    Given a dictionary of words and a string txt

    find the number of ways the string can be broken down into the dictionary words.

    2 pointer comparison to see how far we can go accurately. if we can entirely fit word

        Ah perhaps slicing is even better

        If we can fit entire word into contiguous subsequence of txt, then we take it and build on it.
        once we reach end index then we count that as one way.

    Decision tree:
                                            kickstartisawesome
                            -kick       -start      -kickstart      -is     -awe    -some   -awesome

    for word_piece in dictionary:
        if i+len(word_piece) < len(txt) and word_piece == txt[i:i+len(word_piece)+1]:

    """

    big_mod = 10 ** 9 + 7

    dictionary = set(dictionary)
    n = len(txt)
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(1, n + 1):
        for j in range(max(0, i - 100), i):
            if txt[j:i] in dictionary:
                table[i] += table[j]
        table[i] %= int(1e9 + 7)

    # Return the answer modulo 109 + 7.
    return table[n] % big_mod

