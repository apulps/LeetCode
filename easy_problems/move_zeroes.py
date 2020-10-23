"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""


def move_zeroes(nums):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    count = 0

    for n in nums:
        if n == 0:
            count += 1
            
    for _ in range(count):
        nums.remove(0)
        nums.append(0)


def move_zeroes_2(nums):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    length = len(nums)
    count = 0

    for i in range(length):
        if nums[i] != 0:
            nums[count], nums[i] = nums[i], nums[count]
            count += 1
    