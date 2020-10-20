"""
Given a collection of distinct integers, return all possible permutations.
"""


def permute(nums):
    if len(nums) == 1:
        return [nums]

    result = []

    for i in range(len(nums)):
        others = nums[:i] + nums[i+1:]
        other_permutations = permute(others)

        for permutation in other_permutations:
            result.append([nums[i]] + permutation)

    return result


def permute_2(nums):
    from itertools import permutations
    return [list(p) for p in permutations(nums)]
