class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Edge case if strings are not the same length
        # Edge case if number of unique characters are not the same
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        
        # Init dict to track replacement characters
        rep_chars = {}
        
        # Iterate through s and check against replacement dict
        for i in range(len(s)):
            # If char is not in dict yet then add in
            # Key is char and value is replacement from other string
            if s[i] not in rep_chars:
                rep_chars[s[i]] = t[i]
            # Catch case for non isommorphic strings
            # If char is in dict and value doesnt match other replacement
            if rep_chars[s[i]] != t[i]:
                return False
            
        # If iteration finishes then s and t are isomorphic
        return True