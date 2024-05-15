"""
Author: Soumil Ramesh Kulkarni
Date: 05.15.2024

Question:
Encode a string of English letters using Run-length Encoding (RLE). You simply need to replace all runs of
repeated characters with the count followed by the character.

Example One
{
"letters": "AAAAA"
}
Output:

"5A"
Character 'A' is repeated 5 times consecutively.

Example Two
{
"letters": "ABaaaBCC"
}
Output:

"AB3aB2C"
'a' is repeated 3 times consecutively, 'C' is repeated 2 times.


"""


def rle(letters):
    """
    Args:
     letters(str)
    Returns:
     str
    """
    # Write your code here.
    enc = ''
    curr_char = letters[0]
    curr_count = 1
    for i in range(1, len(letters)):
        if letters[i] != curr_char:
            if curr_count > 1:
                enc += str(curr_count) + curr_char
            else:
                enc += curr_char
            curr_char = letters[i]
            curr_count = 1
        else:
            curr_count += 1

    if curr_count > 1:
        enc += str(curr_count) + curr_char
    else:
        enc += curr_char

    return enc
