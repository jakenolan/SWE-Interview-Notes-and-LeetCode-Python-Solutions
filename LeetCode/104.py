# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_depth_finder(self, node):
        # If no node the end of this path
        if not node:
            return 0
        
        # Set local counter
        max_depth = 0
        
        # If there is a left child
        if node.left:
            max_depth = max(max_depth, self.dfs_depth_finder(node.left))
        
        # If there is a right child
        if node.right:
            max_depth = max(max_depth, self.dfs_depth_finder(node.right))
          
        # Return overall max + 1 for this node as well
        return max_depth + 1
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case if no nodes in tree
        if not root:
            return 0
        
        # Start recursion
        max_depth = self.dfs_depth_finder(root)
        
        # Return max depth after dfs recursion
        return max_depth