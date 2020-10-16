"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
- Initially target array is empty.
- From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
- Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.
"""


def create_target_array(nums, index):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    array = []

    for n, i in enumerate(index):
        array.insert(i, nums[n])

    return array


def create_target_array_2(nums, index):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    array = []

    for i in range(len(index)):
        array.insert(index[i], nums[i])

    return array
