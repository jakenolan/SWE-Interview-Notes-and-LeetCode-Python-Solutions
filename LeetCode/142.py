# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case for empty list or list of length 1
        if not head or not head.next:
            return None
        
        # Init list for constant look up to compare check values
        seen_list = []
        
        # Loop through linked list
        # Track value positions and check agaainst seen list
        while head:
            if head.next in seen_list:
                return head.next
            seen_list.append(head)
            head = head.next
        
        # If loop does not catch cycle then there is no cycle
        return None