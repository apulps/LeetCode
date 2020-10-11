"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
"""


def shuffle_array(s, indices):
    """
    Time complexity -> O(n)
    """
    new = [""] * len(s)

    count = 0
    for index in indices:
        new[index] = s[count] 
        count += 1

    return "".join(new)
