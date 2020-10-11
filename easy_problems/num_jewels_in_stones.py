"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


def num_jewels_in_stones(J, S):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    return sum(1 if stone in J else 0 for stone in S)


def num_jewels_in_stones_2(J, S):
    """
    More readable alternative
    """
    num = 0

    for stone in S:
        if stone in J:
            num += 1

    return num
