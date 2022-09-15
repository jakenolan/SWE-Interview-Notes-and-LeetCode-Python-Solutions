class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # Catch if array is 4 or smaller
        # Difference will always be 0
        if len(nums) <= 4:
            return 0
        # For all other cases
        # Sort list and find optimal min
        nums.sort()
        # Check removal of 3 smallest 0 largest
        optimal_min = nums[-1] - nums[3]
        # Check remove of 2 smallest 1 largest
        optimal_min = min(nums[-2] - nums[2], optimal_min)
        # Check remove of 1 smallest 2 largest
        optimal_min = min(nums[-3] - nums[1], optimal_min)
        # Check remove of 0 smallest 3 largest
        optimal_min = min(nums[-4] - nums[0], optimal_min)
        # Return overall min
        return optimal_min