"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
from assets.problems_data_structures import TreeNode 


def sorted_array_to_BTS(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    tree = TreeNode(nums[mid])
    tree.left = sorted_array_to_BTS(nums[:mid])
    tree.right = sorted_array_to_BTS(nums[mid + 1:])

    return tree
