class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Create running sum python list
        # Init with first index of nums to catch below edge case
        runningSum = [nums[0]]
        
        # Iterate through nums from 1
        for i in range(1, len(nums)):
            runningSum.append(runningSum[i-1] + nums[i])
            
        # Return all sums
        return runningSum