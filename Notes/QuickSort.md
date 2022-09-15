<br />

---

## **Quick Sort Algorithm**

---

<br />

## Explanation

<br />

*Bidirectionally sort through data. Moving elements to the right or left of pivot point and repeating until sorted.*

<br />

Starting by choosing a pivot point, you start at each end of the data moving towards the pivot point. Once the pointer at each end finds an element that should be on the other side, they are swapped. This continues until the pointers are next to each other. At that point the data is split and quicksort is applied to both sides. This continues until everything is in the right order.

<br />

Notes:
- Average time complexity is O(nlogn) but the worst case is O(n^2)
- Pivot point can be chosen randomly but by making a more educated choice you can keep time down.

<br />

---

<br />

## Code Examples

<br />

LeetCode 75 - Sort Colors

```
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Quick sort algo setup
        l = 0
        i = 0
        r = len(nums) - 1
        # Swap helper function where j is pointer
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        # While loop to handle sorting
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
```

<br />

LeetCode 238 - Move Zeros

```
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Quick sort algo setup
        i = 0
        j = 0
        # While loop to handle sorting
        while i < len(nums):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
            i += 1
```

<br />

---