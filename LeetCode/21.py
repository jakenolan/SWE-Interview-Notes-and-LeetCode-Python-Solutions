# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Set combined list
        combined_list = head = ListNode()
        
        # Compare through both lists to merge
        while list1 and list2:
            # If list1 node is smaller add first
            if list1.val < list2.val:
                combined_list.next = list1
                list1 = list1.next
            # Else list2 node is smalle
            else:
                combined_list.next = list2
                list2 = list2.next
            # Move to next combined node for next compare
            combined_list = combined_list.next
        
        # Catch remaining values in list1
        if list1:
            combined_list.next = list1
        # Or catch remaining values in list2
        elif list2:
            combined_list.next = list2
        
        # Return complete combined list
        return head.next