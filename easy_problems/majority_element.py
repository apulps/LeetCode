"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array
"""


def majority_element(nums):
    d = {}

    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    return max(d, key=d.get)
