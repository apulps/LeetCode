"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotate_right(self, head, k):
        if not head:
            return None
    
        if head.next == None:
            return head
            
        pointer = head
        length = 1
        
        while pointer.next:
            pointer = pointer.next
            length += 1
        
        rotate_times = k % length
        
        if k == 0 or rotate_times == 0:
            return head
        
        fast_pointer = head
        slow_pointer = head
        
        for _ in range(rotate_times):
            fast_pointer = fast_pointer.next
        
        
        while fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        
        temp = slow_pointer.next
        
        slow_pointer.next = None
        fast_pointer.next = head
        head = temp
        
        return head
