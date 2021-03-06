"""
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insert_into_BST(self, root, val):
        if root is None:
            return TreeNode(val)
        
        if root.val == val:
            return root
        elif root.val < val:
            root.right = self.insert_into_BST(root.right, val)
        else:
            root.left = self.insert_into_BST(root.left, val)

        return root
