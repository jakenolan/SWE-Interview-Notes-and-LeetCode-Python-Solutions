# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case for empty linked list
        if not head:
            return head
        
        # Create previous memory variable
        previous = None
        
        # Iterate through the given linked list and reverse
        while head:
            current = head
            head = head.next
            current.next = previous
            previous = current
        
        # Return previous for final reversed head
        return previous