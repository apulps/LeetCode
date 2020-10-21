"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


def inorder_traversal(root):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    result = []

    if not root:
        return result

    if root.left:
        aux = inorder_traversal(root.left)
        result.extend(e for e in aux)
    
    if root.val:
        result.append(root.val)
    
    if root.right:
        aux = inorder_traversal(root.right)
        result.extend(e for e in aux)

    return result



def inorder_traversal_2(root):
    """
    Time complexity -> O(n)
    Space complexity -> O(n)
    """
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
