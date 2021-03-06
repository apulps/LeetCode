"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


def reverse_integer(x):
    """
    Time complexity -> O(log n)
    Space complexity -> O(1)
    """
    s = (x > 0) - (x < 0)
    r = int(str(x*s)[::-1])
    return s*r * (r < 2**31)
