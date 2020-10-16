"""
Given an integer 'n' and an integer 'start'.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""


def xor_operation(n, start):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    result = 0

    for i in range(n):
        result = result ^ (start + 2*i)

    return result
