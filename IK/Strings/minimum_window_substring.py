"""
Author: Soumil Ramesh Kulkarni
Date: 05.16.2024

Question:
You are given alphanumeric strings s and t. Find the minimum window (substring) in s which contains all the characters of t.

Example One
{
"s": "AYZABOBECODXBANC",
"t": "ABC"
}
Output:

"BANC"
The minimum window is "BANC", which contains all letters - 'A' 'B' and 'C'. We cannot find a window of smaller length than "BANC".

Example Two
{
"s": "BACRDESDFBAER",
"t": "BAR"
}
Output:

"BACR"
Here, we can see that there are 2 smallest windows - "BACR" and "BAER". However, the output is "BACR" because it is the leftmost one.
"""


def minimum_window(s, t):
    if not s and not t and len(s) < len(t):
        return ""
    countT = {}
    window = {}
    for i in range(len(t)):
        if t[i] not in countT:
            countT[t[i]] = 1
        else:
            countT[t[i]] += 1  # create dictionary for chars in t

    need = len(countT)
    have = 0
    res = [-1, -1]
    reslen = float("infinity")
    l = 0

    for r in range(len(s)):
        if s[r] not in window:
            window[s[r]] = 1
        else:
            window[s[r]] += 1  # create dictionary for chars in s

        if s[r] in countT and countT[s[r]] == window[s[r]]:  # add to have if the chars matches chars in t
            have += 1

        while have == need:
            if r - l + 1 < reslen:
                res = [l, r]
                reslen = r - l + 1
            window[s[l]] -= 1
            if s[l] in countT and countT[s[l]] > window[s[l]]:
                have -= 1
            l += 1
    l, r = res

    if reslen != float("infinity"):
        return s[l:r + 1]
    else:
        return ""