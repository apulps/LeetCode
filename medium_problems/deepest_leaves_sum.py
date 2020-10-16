"""
Given a binary tree, return the sum of values of its deepest leaves.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def deepest_leaves_sum(root):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    if not root:
        return 0

    tree = [root]

    while True:
        aux = [leaf.left for leaf in tree if leaf.left]
        aux += [leaf.right for leaf in tree if leaf.right]

        if not aux:
            break

        tree = aux

    return sum([node.val for node in tree])
