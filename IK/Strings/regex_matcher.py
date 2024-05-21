"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:

Given a text string containing characters only from lowercase alphabetic characters and a pattern string
containing characters only from lowercase alphabetic characters and two other special characters '.' and '*'.

Your task is to implement a pattern matching algorithm that returns true if pattern is matched with text otherwise returns false.
The matching must be exact, not partial.

Explanation of the special characters:

'.' - Matches a single character from lowercase alphabetic characters.
'*' - Matches zero or more preceding character. It is guaranteed that '*' will have one preceding character which can
be any lowercase alphabetic character or special character '.'. But '*' will never be the preceding character of '*'.
(That means "**" will never occur in the pattern string.)
'.' = "a", "b", "c", ... , "z"
a* = "a", "aa", "aaa", "aaaa",... or empty string("")
ab* = "a", "ab", "abb", "abbb", "abbbb", ...
Example One
{
"text": "abbbc",
"pattern": "ab*c"
}
Output:

1
Given pattern string can match: "ac", "abc", "abbc", "abbbc", "abbbbc", ...

Example Two
{
"text": "abcdefg",
"pattern": "a.c.*.*gg*"
}
Output:

1
".*" in pattern can match "", ".", "..", "...", "....", ... . "g*" in pattern can match "", "g", "gg", "ggg", "gggg", ... .
Now, consider:
'.' at position 2 as 'b',
'.*' at position {4, 5} as "...",
'.*' at position {6,7} as "" and
[g*] at position {8,9} as "".
So, "a.c.*gg*" = "abc...g" where we can write "..." as "def". Hence, both matches.

Example Three
{
"text": "abc",
"pattern": ".ab*.."
}
Output:

0
If we take 'b*' as "" then also, length of the pattern will be 4 (".a.."). But, given text's length is only 3. Hence, they can not match.
"""

def pattern_matcher(text, pattern):
    T = len(text)
    P = len(pattern)

    def helper(t, p, wild_used=False):
        while t < T and p < P:
            match = pattern[p]
            if (p + 1) < P and pattern[p + 1] == '*':
                p += 2
                if p == P:
                    return True

                while t < T:
                    res = helper(t, p, wild_used)
                    if res != None:
                        return res
                    if match != '.' and match != text[t]:
                        return None
                    wild_used = True
                    t += 1
            else:
                if match != '.' and match != text[t]:
                    return None
                t += 1
                p += 1
        while (p + 1) < P and pattern[p + 1] == '*':
            p += 2
        if t == T and p == P:
            return True
        if not wild_used:
            return False
        return None

    return helper(0, 0) or False