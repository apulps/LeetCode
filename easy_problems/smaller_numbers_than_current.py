"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


def smaller_numbers_than_current(nums):
    """
    Time complexity -> O(n^2)
    """
    smaller = []
    
    for num in nums:
        count = 0
        for num_2 in nums:
            if num > num_2:
                count += 1
            
        smaller.append(count)

    return smaller
