class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Edge case for s of length 1
        if len(s) == 1:
            return 1
        
        # Init a counter to find number of occurrences for each chracter
        # Init variable to counter longest palindrome
        occurrences = Counter(s)
        longest_palindrome = 0
        
        # Iterate through counter to find all duplicates for palindrome creation
        for char in occurrences:
            add = (occurrences[char] // 2) * 2
            longest_palindrome += add
            
        # If longest palindrome shorter than s then add 1
        # The 1 accounts for a single character being able to be in the middle of a palindrome
        if longest_palindrome < len(s):
            longest_palindrome += 1
        
        # Return longest_palindrome
        return longest_palindrome