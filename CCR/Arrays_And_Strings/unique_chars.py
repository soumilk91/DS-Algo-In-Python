"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Question: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional Data structure
"""

class UniqueChars():
    """
    Brute Force : Have nested for loops to find out if there are any duplicates. Time: O(N^2), Space: O(1)

    Question:
    1) Are the chars case sensitive? (For our implementation, Lets consider no)
    2) Are the characters Sorted? If not, Sorting them in place can be an option

    Both the brute force and sorting approches can be considered if we want to achieve this without using an additional Data Structure

    """
    def __init__(self, input_string):
        self.input_string = input_string

    def method_1(self):
        """
        -> If empty, return True
        -> Use a dict, store key as char and value as integer
        -> While traversing, for every char, try to insert into the dict, if char already present, string does not contain all unique chars
        -> Time: O(N), Space: O(N)


        :return: Bool
        """
        if not self.input_string:
            #print("Given String is Empty, Return True")
            return True
        compare_dict = dict()
        for char in self.input_string:
            if char in compare_dict:
                #print("Given String has duplicate Chars, Return False")
                return False
            else:
                compare_dict[char] = 1
        #print("Given String has all unique Chars, Return True")
        return True

def main():
    given_string = "soumil"
    temp = UniqueChars(given_string)
    if temp.method_1():
        print("Given String has all unique chars")
    else:
        print("Given String does not have all unique chars")

if __name__ == "__main__":
    main()
