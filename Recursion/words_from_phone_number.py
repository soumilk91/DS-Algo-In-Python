"""
Author: Soumil Ramesh Kulkarni
Date: 01/19/2024

Question: Given a seven-digit phone number, return all the character combinations that can be generated according to the following mapping:

character mapping to number on the keypad on any phone
mapping_dict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']
    }

Eg: {
"phone_number": "1234567"
}

Output:
[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
"""


def _helper(phone_number, phone_number_index, mapping_dict, slate, results):
    # Base Case
    if phone_number_index == len(phone_number):
        results.append("".join(slate))
        return

    # Recursive Case

    # If number not in mapping_dict do noting
    if phone_number[phone_number_index] not in mapping_dict:
        _helper(phone_number, phone_number_index + 1, mapping_dict, slate, results)
    else:
        # Create a list of all possible characters for a specific number and loop over them to include the one at a time
        temp_list = mapping_dict[phone_number[phone_number_index]]
        for runner in temp_list:
            slate.append(runner)
            _helper(phone_number, phone_number_index + 1, mapping_dict, slate, results)
            slate.pop()


def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.
    mapping_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
                    }
    results = []
    _helper(phone_number, 0, mapping_dict, [], results)
    return results


print(get_words_from_phone_number("1234567"))