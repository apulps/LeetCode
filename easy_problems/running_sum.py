"""
Given an array nums. We define a running sum of an array as running_sum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


def running_sum(nums):
    """
    Time complexity -> O(n^2)
    Space complexity -> O(n)
    """
    return [sum(num for num in nums[index::-1]) for index in range(0, len(nums))]
        

def running_sum_2(nums):
    """
    More readable alternative
    """
    result = []
    aux = 0

    for index in range(0, len(nums)):
        for num in nums[index::-1]:
            aux += num
        
        result.append(aux)
        aux = 0

    return result


def running_sum_3(nums):
    """
    Itertools alternative
    """
    from itertools import accumulate
    return [num for num in accumulate(nums)]
