"""
Author: Soumil Ramesh Kulkarni
Date: 01/17/2024

Question: Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
        Return a list of all possible strings

Eg:
string: "a1b2"
output: "a1b2", "A1b2", "a1B2", "A1B2"

string: "3z4"
output: "3z4", "3Z4"

string: "12345"
output: "12345"


"""

result_list = []
def letterCasePermutation(input_string):
    #Root Case
    #_helper(input_string, 0, "")
    _helper_mutable_slate(input_string, 0, [])
    print(result_list)

def _helper_mutable_slate(input_string, start_index, slate):
    """
    IMPORTANT
    here slate is a list instead of a string which is mutable
    so we will have to pop the inserted item after every recursive call
    """

    # Base Case
    if start_index == len(input_string):
        result_list.append("".join(slate))
        return

    # Recursive Case
    if input_string[start_index].isdigit():
        slate.append(str(input_string[start_index]))
        _helper_mutable_slate(input_string, start_index+1, slate)
        slate.pop()
    else:
        #Recursive Call for Lower Case
        slate.append(input_string[start_index].lower())
        _helper_mutable_slate(input_string, start_index+1, slate)
        slate.pop()

        #Recursive Call for Upper Case
        slate.append(input_string[start_index].upper())
        _helper_mutable_slate(input_string, start_index+1, slate)
        slate.pop()

def _helper(input_string, start_index, slate):
    """
    input_string and start index : are definitions of the subproblem
    slate: Partial solution
    result_list: final list which contains all the results
    This helper function is using an immutable slate ... Which can increase the space complexity
    """

    #Lets Define the Base Case
    #If we have reached the last blank of the string, append the result becase slate is a completesolution now
    if start_index == len(input_string):
        result_list.append(slate)
        return result_list

    #Recursive Case
    if input_string[start_index].isnumeric():
        slate += input_string[start_index]
        _helper(input_string, start_index+1, slate)
    else:
        # Consider the case of Upper Character
        _helper(input_string, start_index+1, slate + input_string[start_index].upper())

        # Consider the case of Lower Character
        _helper(input_string, start_index+1, slate + input_string[start_index].lower())

letterCasePermutation("a1b2")
letterCasePermutation("abcd123546")
