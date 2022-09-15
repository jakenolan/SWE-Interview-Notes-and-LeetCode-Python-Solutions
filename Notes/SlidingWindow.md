<br />

---

## **Sliding Window Algorithm**

---

<br />

## Explanation

<br />

*Making use of a subarray to slide along the input array working with only one subsection of input array at a time and adjusting.*

<br />

Start with creating two index integers to represent the two sides of the window. You will also need a set to keep track of the characters you need to remember in your subarray. Depending on the problem you may need to track other things (e.g. max number of unique characters below). Using a for/while loop, go through the input array moving your right window side forward. Inside of that for/while loop you adjust the left window side according to what you are looking for (e.g. finding a repeat character below).

<br />

Notes:
- Time complexity is usually O(n) and most characters are handled twice.
- Remember to track specifics according to the application.
- What needs to be tracked also updates the conditionals inside the parent for/while loop.

<br />

---

<br />

## Code Examples

<br />

LeetCode 3 - Longest Substring Without Repeating Characters

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If s has no characters then return 0
        if len(s) == 0:
            return 0
        # Sliding window algo setup
        i = 0
        j = 0
        m = 0
        charSet = set()
        # For loop for sliding window
        for i in range(len(s)):
            # While character is in charSet already
            while s[i] in charSet:
                charSet.remove(s[j])
                j += 1
            # When only unique characters
            charSet.add(s[i])
            m = max(m, ((i - j) + 1))
        # Return max
        return m
```

<br />

---