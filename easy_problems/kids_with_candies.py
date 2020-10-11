"""
Given the array candies and the integer extra_candies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extra_candies among the kids such that he or she can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.
"""


def kids_with_candies(candies, extra_candies):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    top = max(candies)
    return [(candies_kid + extra_candies) >= top for candies_kid in candies]


def kids_with_candies_2(candies, extra_candies):
    """
    More readable alternative
    """
    top = max(candies)
    result = []
    for candies_kid in candies:
        if (candies_kid + extra_candies) >= top:
            result.append(True)
        else:
            result.append(False)
    
    return result
