"""
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def two_sum(nums, target):
    """
    Time complexity -> O(n^2)
    Space complexity -> O(n)
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_2(nums, target):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    d = {}
    for index, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], index]
        else:
            d[n] = index
