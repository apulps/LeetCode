"""
Reverse a singly linked list.
"""


def reverse_linkedlist(head):
    """
    Time complexity -> O(n)
    Space complexity -> O(1)
    """
    current = head
    previous = None

    while current:
        aux = current.next
        current.next = previous
        previous = current
        current = aux

    return previous
