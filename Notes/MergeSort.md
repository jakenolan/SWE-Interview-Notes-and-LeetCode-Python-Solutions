<br />

---

## **Merge Sort**

---

<br />

## Explanation

<br />

*This algorithm splits the input array in two halves, sorting them each individually, and then merges them.*

<br />

By using a l, m, and r variable you call merge sort for each half (l to m and m to r). This sorts each half by making sure the left pointer is less than the right. Once each half is sorted you merge the two halves together.

<br />

Notes:
- This is a memory instensive algorithm.
- This is a depth first algorithm.
- The time complexity is O(nlogn).
- The space complexity is O(n)

<br />

---

<br />

## Code Examples

<br />

LeetCode 88 - Merge sort array

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # find last index
        last = m + n - 1
        # While loop for merge
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        # Catch any values left in nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
```

<br />

LeetCode 21 - Merge two sorted lists

```
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge sort setup using dummy
        dummy = ListNode()
        tail = dummy
        # While loop for merging
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # Catch if either list is not empty yet
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # Return sorted dummy
        return dummy.next
```

<br />

---