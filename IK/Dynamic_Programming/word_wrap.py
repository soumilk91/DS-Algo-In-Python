"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:

Given a sequence of words (strings), and a limit on the number of characters that can be put in one line (line width), put line breaks in the given sequence such that the lines are printed neatly.

The word processors like MS Word do the task of placing line breaks. The idea is to have balanced lines. In other words, not have a few lines with lots of extra spaces and some lines with a small amount of extra spaces.

The extra spaces means spaces put at the end of every line.

Put line breaks such that the following total cost is minimized:

Cost of a line = (number of extra spaces in the line)3
Total Cost = sum of costs for all lines
Example One
{
"words": ["abcdefghijkl", "abcdefg", "abcdefgh", "abcdefghijklmnopqrstuv"],
"limit": 23
}
Output:

1674
The following arrangement of words in lines will have least cost:

Line1: "abcdefghijkl"
Line2: "abcdefg abcdefgh"
Line3: "abcdefghijklmnopqrstuv"
Note that we need to ignore the extra white spaces at the end of the last line. So, in the last line there will be 0 extra white spaces.

Cost for this configuration: (23 - 12)3 + (23 - (7 + 1 + 8))3 + (0)3 = 1674

Example Two
{
"words": ["omg", "very", "are", "extreme"],
"limit": 10
}
Output:

351
The following arrangement of words in lines will have least cost:

Line1: "omg "very"
Line2: "are"
Line3: "extreme"
Note that we need to ignore the extra white spaces at the end of the last line. So, in the last line there will be 0 extra white spaces.

Cost for this configuration: (10 - (3 + 1 + 4))3 + (10 - 3)3 + (0)3 = 351
"""

def solve_balanced_line_breaks(words, limit):
    cumLength = [0 for _ in range(len(words))]
    cumLength[-1] = len(words[-1])
    for i in range(len(words)-2, -1, -1):
        cumLength[i] = cumLength[i+1] + len(words[i])

    table = [0 for _ in range(len(words))]
    for i in range(len(words)-1, -1, -1):
        if limit >= cumLength[i] + (len(words) - i - 1):
            table[i] = 0
            continue

        minVal = float('inf')
        firstLineLength = 0
        firstLineWordCount = 0
        while firstLineLength + len(words[i+firstLineWordCount]) <= limit:
            firstLineLength += len(words[i+firstLineWordCount])
            firstLineWordCount += 1
            remainingSpace = limit - firstLineLength
            currLoss = remainingSpace**3 + table[i+firstLineWordCount]
            if currLoss < minVal:
                minVal = currLoss
            firstLineLength += 1

        table[i] = minVal

    return table[0]