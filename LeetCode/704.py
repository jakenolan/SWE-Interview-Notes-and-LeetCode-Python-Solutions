class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Edge case list of length 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # Init boundary variable for binary search
        left = 0
        right = len(nums) - 1
        
        # Apply binary search on nums
        while left <= right:
            # Calcular moving midpoint
            mid = (right + left) // 2
            # If target is to the left of midpoint
            if target < nums[mid]:
                right = mid - 1
            # If target is to the right of midpoint
            elif target > nums[mid]:
                left = mid + 1
            # Else the target is the midpoint value
            else:
                return mid
        
        # If loop completes with no return then target not in nums
        return -1