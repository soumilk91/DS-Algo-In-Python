"""
Author: Soumil Ramesh Kulkarni
Date: 03.29.2024

Question:
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
The minimum number of steps required to convert word1 to word2 with the given set of allowed operations is called edit
distance. e.g. Minimum edit distance between the words 'kitten' and 'sitting', is 3.

kitten → sitten (substitution of "s" for "k")
sitten → sittin (substitution of "i" for "e")
sittin → sitting (insertion of "g" at the end)
Read more about edit distance here.

Example One
{
"word1": "cat",
"word2": "bat"
}
Output:

1
Example Two
{
"word1": "qwe",
"word2": "q"
}
Output:

2
"""


def levenshtein_distance(word1, word2):
    """
    Args:
     word1(str)
     word2(str)
    Returns:
     int32
    """
    # Write your code here.
    len_word1 = len(word1)
    len_word2 = len(word2)

    # Initialize a cache of len + 1 and add base case to last col and last row
    cache = [[0] * (len_word2 + 1) for _ in range((len_word1 + 1))]
    for j in range((len_word2 + 1)):
        cache[len_word1][j] = len_word2 - j
    for i in range((len_word1 + 1)):
        cache[i][len_word2] = len_word1 - i

    # Compute
    for row in range(len_word1 - 1, -1, -1):
        for col in range(len_word2 - 1, -1, -1):
            if word1[row] == word2[col]:
                cache[row][col] = cache[row + 1][col + 1]
            else:
                cache[row][col] = 1 + min(cache[row + 1][col + 1],
                                          cache[row + 1][col],
                                          cache[row][col + 1])
    return cache[0][0]
