class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Init temp sum variables
        left_sum = 0
        right_sum = sum(nums)
        
        # Iterate through nums moving from left starting at 1
        # Check same number of nums on right
        for i in range(len(nums)):
            # If index 0 then no left sum
            # Avoid out of bounds
            if i != 0:
                left_sum += nums[i - 1]
            right_sum -= nums[i]
            # Check for equivalence
            if left_sum == right_sum:
                return i
            
        # If nothing returned no index exists so return -1
        return -1