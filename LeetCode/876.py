# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Put linked list into a Python list for indexing
        # This will help us find the middle
        indexed_list = []
        while head:
            indexed_list.append(head)
            head = head.next
        
        # Return middle index
        return indexed_list[len(indexed_list) // 2]