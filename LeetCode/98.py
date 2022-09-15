# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node, left, right):
        # If no node we can return true
        # This means we validated all the way down one way
        if not node:
            return True
        # If left value greater than or equal to node value
        if left and left.val >= node.val:
            return False
        # If right value is less than or equal to node value
        if right and right.val <= node.val:
            return False
        # Continue recursion and return bool value from both children
        # This will return false unless all return values are true
        return (self.validate(node.left, left, node) and self.validate(node.right, node, right))
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Edge case for tree with only root node
        if not root.left and not root.right:
            return True
        
        # Return outcome of recursive search
        return self.validate(root, None, None)