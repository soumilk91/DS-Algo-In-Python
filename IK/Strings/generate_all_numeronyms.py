"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Given a word, generate all possible numeronyms for it.

What is a numeronym?

A numeronym is a word where a number is used to form an abbreviation.

A numeronym for a word is another word with two or more contiguous letters replaced with their number.
Exactly one set of contiguous letters is replaced by a number. First or last letter in the initial word are
never omitted/replaced when forming a numeronym for it.

Example
{
"word": "nailed"
}
Output:

["n4d", "na3d", "n3ed", "n2led", "na2ed", "nai2d"]
"n4d" is an abbreviation of "nailed" where substring "aile" is replaced by the number of letters in it, 4.

"na3d" is an abbreviation of "nailed" where substring "ile"is replaced by number of letters in it, 3.

And so on.
"""


def generate_all_numeronyms(word):
    """
    Args:
     word(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    n = len(word)
    for i in range(2, n-1):
        for j in range(1,n-i):
            result.append(word[0]+word[1:j]+str(i)+word[i+j:-1]+word[-1])
    return result
