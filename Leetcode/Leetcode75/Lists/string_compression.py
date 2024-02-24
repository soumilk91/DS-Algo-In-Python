"""
Author: Soumil Ramesh Kulkarni
Date: 02.23.2024

Question:

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.



Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        mychar = chars[0]
        count = 0
        length = len(chars)
        chars.append(" ") # Append a space so last char group is not left out in loop
        for i in range(length+1): #+1 for extra space char we added
            char = chars.pop(0)
            if char == mychar: #if same character then just increase the count
                count += 1
            else:
                if count == 1: #if not same then append the char to chars
                    chars.append(mychar) #if count is 1 don't append count
                elif count > 1:
                    chars.append(mychar)
                    chars += (list(str(count))) #if count > 1 append count as a string
                mychar = char #update mychar as the new different char in chars
                count = 1 #reset count to 1 as we have already read the new char
        return len(chars) #since all previous are popped, only the answer remains in chars now