"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
Given some text and a bunch of words, find where each of the words appear in the text.

Function must return a list of lists of integers. One list for each one of the words. i-th list must contain
all indices of characters in text where i-th word starts, in the ascending order. If i-th word isn’t found in
the text at all, then i-th list must be [-1].

Example
{
"text": "you are very very smart",
"words": ["you", "are", "very", "handsome"]
}
Output:

[ [0], [4], [8, 13], [-1] ]

"you" is found in the given text starting at the index 0.
"are" is found in the given text starting at the index 4.
"very" is found in the given text two times, starting at the indices 8 and 13.
"handsome" isn’t found in the given text.

"""

def find_words(text, words):
    """
    Args:
     text(str)
     words(list_str)
    Returns:
     list_list_int32
    """
    # Write your code here.
    if not text or not words:
        return []
    text_list = text.split(" ")
    compare_dict = {}
    start_index = 0
    for word in text_list:
        if word not in compare_dict:
            compare_dict[word] = [start_index]
        else:
            compare_dict[word].append(start_index)
        start_index += len(word)
        start_index += 1
    result = []
    for word in words:
        if word not in compare_dict:
            result.append([-1])
        else:
            result.append(compare_dict[word])
    return result