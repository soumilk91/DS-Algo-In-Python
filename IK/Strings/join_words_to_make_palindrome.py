"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Given a list of strings words, of size n, check if there is any pair of words that can be joined (in any order) to
form a palindrome then return the pair of words forming palindrome.

Example One
{
"words": ["bat", "tab", "zebra"]
}
Output:

["bat", "tab"]
As "bat" + "tab" = "battab", which is a palindrome.

Example Two
{
"words": ["ant", "dog", "monkey"]
}
Output:

["NOTFOUND", "DNUOFTON"]
As for each 6 combinations of string of words, there is no single generated word which is a palindrome hence result
list will be ["NOTFOUND", "DNUOFTON"].
"""


def is_palindrome(string):
    st, end = 0, len(string) - 1
    while st < end:
        if string[st] != string[end]:
            return False
        st += 1
        end -= 1
    return True


def join_words_to_make_a_palindrome(words):
    """
    Args:
     words(list_str)
    Returns:
     list_str
    """
    words2 = [(word[::-1], pos) for pos, word in enumerate(words)]
    words2.sort()

    words = [(word, pos) for pos, word in enumerate(words)]
    words.sort()

    i, j = 0, 0
    while i < len(words) and j < len(words2):
        word1, pos1 = words[i]
        word2, pos2 = words2[j]

        if pos1 != pos2:
            if word1 == word2:
                return [word1, word2[::-1]]

            if len(word1) > len(word2) and word1[:len(word2)] == word2 and is_palindrome(word1[len(word2):]):
                return [word1, word2[::-1]]

            if len(word2) > len(word1) and word2[:len(word1)] == word1 and is_palindrome(word2[len(word1):]):
                return [word1, word2[::-1]]

        if word1 < word2:
            i += 1
        else:
            j += 1

    return ["NOTFOUND", "DNUOFTON"]