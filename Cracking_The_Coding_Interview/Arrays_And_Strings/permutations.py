"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Question: Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
-> A permutation is basically rearrangement of letters. 
EG: input: ABC
Permutations: ABC, ACB, BAC, BCA, CAB, CBA

-> So the length of the given 2 strings should be exactly the same
-> Question to be asked, is if the chars are supposed to case sensitive 
-> One method that comes to mind is to use 2 dicts and compare. Time: O(N), Space: O(N)


Returning a bool of weather 2 strings are permutations of each other is trivial, 
the better question is to find out all the permutations of a given string.  

"""

class Permutation_methods():
    def __init__(self):
        pass

    def find_if_permute(self, string1, string2):
        """
        : if lenght of the 2 strings is not same, return False
        : Use 2 dicts to compare

        :return:  Bool
        """
        if len(string1) != len(string2):
            print("Length of the two given strings is not the same, Return False")
            return  False

        string1_dict = dict()
        string2_dict = dict()

        for i in range(len(string1)):
            # Create a dict for the First String
            if string1[i] not in string1_dict:
                string1_dict[string1[i]] = 1
            else:
                string1_dict[string1[i]] += 1

            # Create a dict for the Second String
            if string2[i] not in string2_dict:
                string2_dict[string2[i]] = 1
            else:
                string2_dict[string2[i]] += 1

        # Compare the 2 Dicts created above
        if string1_dict == string2_dict:
            return True
        else:
            return False


def main():
    temp = Permutation_methods()
    print(temp.find_if_permute("ABC", "ACB"))

if __name__ == "__main__":
    main()