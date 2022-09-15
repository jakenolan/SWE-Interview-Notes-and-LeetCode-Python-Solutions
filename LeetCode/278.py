# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Edge case for only one version
        if n == 1 and isBadVersion(1):
            return 1
        
        # Create bounding variables for binary search
        left = 1
        right = n
        
        # Loop through versions applying binary search
        while left <= right:
            # Calculate moving midpoint
            mid = (right + left) // 2
            # If midpoint is a bad version then first bad version is the midpoint or before
            if isBadVersion(mid):
                # Check if previous version is bad
                # This confirms immediately if midpoint is first bad version
                if not isBadVersion(mid - 1):
                    return mid
                # If midpoint not first bad version adjust right boundary and continue
                right = mid - 1
            # Else version is good so first bad version after midpoint
            # Adjust left boundary and continue
            else:
                left = mid + 1
                
        # If loop finishes without returning then no bad versions
        # Because of constraints, this line does not need to be here (just added to cover all bases)
        return 'No bad version!'