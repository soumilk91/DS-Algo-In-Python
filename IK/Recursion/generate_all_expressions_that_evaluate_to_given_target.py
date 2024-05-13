"""
Author: Soumil Ramesh Kulkarni
Date: 05.12.2024

Question:
Given a string s that consists of digits ("0".."9") and target, a non-negative integer,
find all expressions that can be built from string s that evaluate to the target.

When building expressions, you have to insert one of the following operators between each pair of
consecutive characters in s: join or * or +. For example, by inserting different operators between the two characters of string "12" we can get either 12 (1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").

Other operators such as - or ÷ are NOT supported.

Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.

Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the
lowest precedence. For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.

You have to return ALL expressions that can be built from string s and evaluate to the target.

Example
{
"s": "202",
"target": 4
}
Output:

["2+0+2", "2+02", "2*02"]
Same three strings in any other order are also a correct output.

"""


def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.

    if not s:
        return []

    output = []

    def helper(so_far, evaluation, idx, prev):
        if idx == len(s):
            if evaluation == target:
                output.append(so_far)
            return

        for i in range(idx, len(s)):
            curr = s[idx: i + 1]
            curr_int = int(curr)

            if idx == 0:
                helper(curr, curr_int, i + 1, curr_int)
            else:
                helper(so_far + '+' + curr, evaluation + curr_int, i + 1, curr_int)
                helper(so_far + '*' + curr, (evaluation - prev) + (prev * curr_int), i + 1, prev * curr_int)
        return

    helper('', 0, 0, 0)
    return output
