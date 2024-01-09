"""
Author: Soumil Ramesh Kulkarni
Date: 01/03/2024

Question: Write a method to replace all spaces in a string with "%20"
"""

def URLify(input_string):
    input_string_split = input_string.split(" ")
    outstring_list = []
    for i in input_string_split:
        if i != "":
            outstring_list.append(i)
    return "%20".join(outstring_list)


print(URLify("Mr John  Smith  "))
