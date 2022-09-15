class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Edge case if s is empty
        if not s:
            return True
        
        # Edge case if t is empty
        if not t:
            return False
        
        # Edge case if the strings are the same
        if s == t:
            return True
        
        # Index to track s letter for checking
        s_index = 0
        
        # Iterate through t
        for i in range(len(t)):
            # If current s letter check passes
            if s[s_index] == t[i] and s_index < len(s):
                s_index += 1
            # If s completed in order check fully
            # Has to come after current letter check
            # Saves us from always having to complete the iteration
            if s_index >= len(s):
                return True
            
        # If nothing returned then s is not a subsequence of t
        return False