"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Question: Given a string, Write a function to check if it has any permutation which is a palindrome.

Eg:  tactcoa
One of the permutaions of the above string is : tacotac which is a Palindrome.
Palindrome is a word that reads the same forward and backward

"""

"""
Brute Force Algorithm: 
-> Get all the permutations of the given string 
-> Check each permutation from above step to see if it is a palindrome. 

Now for this Question, we actually do not need to calculate all the permutations of the given string. We can consider the following properties
of a palindrome string. 
-> If the length of the string is odd, number of all characters except one has to be even. 
-> If the length of the string is even, number of all characters has to be even. 
Time: O(N), Space : O(N)
"""

def PalindromePermutation(input_string):
    # If Length of the given string is less than 1, return True
    if len(input_string) <= 1:
        return True

    # Create a comparison Dict, Key is the character and the value is the number of times that character appears in the string
    compare_dict = dict()
    for character in input_string:
        if character not in compare_dict:
            compare_dict[character] = 1
        else:
            compare_dict[character] += 1

    # If even characters in the given string, No characters in the given string can appear odd number of times
    # If odd characters in the given string, Only 1 character in the given string can appear odd number of times. 
    if len(input_string) % 2 == 0:
        number_of_odds = 0
        for key in compare_dict:
            # calculate if the value associated with a key is odd
            if compare_dict[key] % 2 != 0:
                number_of_odds += 1
                print("Found a character in the string which appears odd number of times ...  No Permutation of this stirng can be a palindrome... Return False")
                return False
        print("There can be some permutation of the given string which can be a palindrome. Return True ")
        return True
    else:
        number_of_odds = 0
        for key in compare_dict:
            # calculate if the value associated with a key is odd
            if compare_dict[key] % 2 != 0:
                number_of_odds += 1
                if number_of_odds > 1:
                    print("Found more than 1 character in the string which appears odd number of times.... No Permutation of this string can be a palindrome ... Return False")
                    return False
        print("There can be some permutation of the given string which can be a palindrome ... Return True")
        return True

PalindromePermutation("tacotacddce")
