"""
Given two binary trees 'original' and 'cloned' and given a reference to a node 'target' in the original tree.

The 'cloned' tree is a copy of the 'original' tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.
"""


def get_target_copy(original, cloned, target):
    result = None

    if original.val == target.val:
        return cloned

    if original.right:
        result = get_target_copy(original.right, cloned.right, target)
        if result is not None and result.val == target.val:
            return result

    if original.left:
        result = get_target_copy(original.left, cloned.left, target)
        if result is not None and result.val == target.val:
            return result
