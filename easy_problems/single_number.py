"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""


def single_number(nums):
    """
    Time complexity -> O(n^2)
    Space complexity -> O(n)
    """
    aux = []

    for n in nums:
        if n not in aux:
            aux.append(n)
        else:
            aux.remove(n)
    
    return aux.pop()



def single_number_2(nums):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    s = list(set(nums))
    return 2 * sum(s) - sum(nums)



def single_number_3(nums):
    """
    Concept

    - If we take XOR of zero and some bit, it will return that bit
        · a ⊕ 0 = a
    - If we take XOR of two same bits, it will return 0
        · a ⊕ a = 0
    - a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = 0
    So we can XOR all bits together to find the unique number.

    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    res = 0
    for n in nums:
        res = n ^ res
    return res



def single_number_4(nums):
    values = set()

    for n in nums:
        if n in values:
            values.remove(n)
        else:
            values.add(n)

    return values.pop()
