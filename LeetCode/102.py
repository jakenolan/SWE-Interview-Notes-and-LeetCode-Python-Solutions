# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_helper(self, node, level):
        if node:
            # If level not in levels
            if level > len(self.levels) - 1:
                self.levels.append([])
            # Add node to its respective level
            self.levels[level].append(node.val)
            # Run recursive function for children
            self.dfs_helper(node.left, level+1)
            self.dfs_helper(node.right, level+1)

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case for empty tree
        if not root:
            return []
        
        # Edge case for just root node
        if not root.left and not root.right:
            return [[root.val]]
        
        # Create list to keep track of all levels
        self.levels = []
        
        # Start recursion with root
        self.dfs_helper(root, 0)
        
        # Return full levels list
        return self.levels