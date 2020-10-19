"""
Data structures needed for medium problems.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Definition for singly-linked list.
class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None
