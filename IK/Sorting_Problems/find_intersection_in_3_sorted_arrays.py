"""
Author: Soumil Ramesh Kulkarni
Date: 02/14/2024

Question:
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.
Eg:
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output: [2, 10]

{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}
Output: [-1]

{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}
Output: [1, 2, 2]

"""


def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    # Find the shortest array from the given arrays
    return_list = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    len_arr3 = len(arr3)
    if len_arr1 == 0 or len_arr2 == 0 or len_arr3 == 0:
        return [-1]
    i = j = k = 0
    while i < len_arr1 and j < len_arr2 and k < len_arr3:
        compare_element = arr1[i]
        if arr1[i] == arr2[j] == arr3[k]:
            return_list.append(arr1[i])
        mini = min(arr1[i], arr2[j], arr3[k])

        if (mini == arr1[i]):
            i += 1
        if (mini == arr2[j]):
            j += 1
        if (mini == arr3[k]):
            k += 1
    if len(return_list) == 0:
        return_list.append(-1)
    return return_list

