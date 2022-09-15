# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min_depth_finder(self, node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1
        
        if not node.left:
            return self.min_depth_finder(node.right) + 1
        
        if not node.right:
            return self.min_depth_finder(node.left) + 1
            
        return min(self.min_depth_finder(node.left),
                   self.min_depth_finder(node.right)) + 1
    
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case for empty tree
        if not root:
            return 0
        
        # Start recursion to get overall min
        min_depth = self.min_depth_finder(root)
        
        return min_depth