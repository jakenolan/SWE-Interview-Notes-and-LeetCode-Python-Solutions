<br />

---

## **Binary Search**

---

<br />

## Explanation

<br />

*An algorithm for finding an element in a sorted array.*

<br />

By using left, right, and midpoint indices you efficiently search through a sorted list until finding the target element. This starts with the left and right indices being the beginning and end of the array. From there calculate the midpoint's index using (1 + ((r - 1) - 1)). If the target element is less than your midpoint you know that it is on the lower half of the array and you move your right index to one less of the midpoint to cut out the greater half of the array. Vise versa, if your target element is higher than your midpoint you know that it is on the higher half of the array and you move your left index to one more than the midpoint. From there you start this cycle over again until you have cut down all possiblities except the target element.

<br />

Notes:
- The while loop uses l <= r because if one element is left then l = r and if that element is not the target element then r < 1 and either way the loop will break. This changes to l < r in certain situations (see example of LeetCode 278 below).
- The midpoint calculation is done with (1 + ((r - 1) - 1)) to avoid integer overflow (working with numbers larger than 2^31 in certain languages).
- Make sure to check if the midpoint is equal to the target.
- This algorithm has O(log n) time complexity.

<br />

---

<br />

## Code Examples

<br />

LeetCode 704 - Basic example to find given value

```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search algo initial setup
        l = 0
        r = len(nums) - 1
        while l <= r:
            # Calc current mid
            m = l + ((r - l) // 2)
            # Check if m is to the left or right of target, else it is the target
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
```

<br />

LeetCode 278 - Example to find index based on bool returns, not a given value

```
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search intial setup
        first = 1
        last = n
        # While loop to check midpoints to first bad version and adjust
        while first < last: # Just <, not <= because ???
            # Check mid version with API
            mid_version_index = first + ((last - first) // 2)
            mid_version_bad = isBadVersion(version=mid_version_index)
            # If bad then earlier version
            if mid_version_bad == True:
                last = mid_version_index # Just = mid, not mid - 1 ???
            # If good then later version
            elif mid_version_bad == False:
                first = mid_version_index + 1
        # Return first or last in case of while break (only one index available so they are the same)
        return first
```

<br />

LeetCode 35 - Find the given value and if it is not in array where to add given value
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search initial setup
        l = 0
        r = len(nums) - 1
        # Memory of index distances for insert check
        l_distance = 0
        r_distance = 0
        # While loop to check midpoint and iterate
        while l <= r:
            m = l + ((r - l) // 2)
            l_distance = abs(l - m)
            r_distance = abs(r - m)
            # If midpoint is less than target then target is on right half
            if nums[m] < target:
                l = m + 1
            # If midpoint greater than target then target is on left half
            elif nums[m] > target:
                r = m - 1
            # Else the midpoint = target
            elif nums[m] == target:
                return m
        # Catch if target element is not in array and return l as insert point (Because of the l = m + 1 when nums[m] < target and no change if nums[m] > target in while loop)
        return l
```

<br />

---