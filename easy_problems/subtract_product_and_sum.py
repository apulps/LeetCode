"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""


def subtract_product_and_sum(n):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    product = 1
    addition = 0

    while n > 0:
        element = n % 10
        n = n // 10

        product *= element
        addition += element
    
    return product - addition