"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


def remove_duplicates(nums):
    """
    Without using sets
    
    Time complexity -> O(n^2)
    Space complexity -> O(1)
    """
    accumulate = 0

    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    for index in range(len(nums)):
        if nums[index - accumulate] == nums[index - 1 - accumulate] and len(nums) != 1:
            nums.pop(index - accumulate)
            accumulate += 1

    return len(nums)


def remove_duplicates_2(nums):
    """
    Faster alternative

    Time complexity -> O(n log n)
    Space complexity -> O(1)
    """
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)
