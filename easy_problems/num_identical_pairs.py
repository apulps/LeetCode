"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""


def num_identical_pairs(nums):
    """
    Time complexity -> O(n^2)
    Space complexity -> O(1)
    """
    number_of_goods = 0
    
    if not nums:
        return number_of_goods

    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                number_of_goods += 1

    return number_of_goods
