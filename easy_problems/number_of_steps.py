"""
Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


def number_of_steps(num):
    """
    Time complexity -> O(1)
    """
    digits = f'{num:b}'
    return digits.count('1') - 1 + len(digits)


def number_of_steps_2(num):
    steps = 0
    
    while num != 0:
        if num % 2 == 0:
            num /= 2
            steps += 1
        else:
            num -= 1
            steps +=1
        
    return steps
