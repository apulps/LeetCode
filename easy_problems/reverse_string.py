"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


def reverse_string(s):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    s.reverse()



def reverse_string_2(s):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    s[:] = s[::-1]
