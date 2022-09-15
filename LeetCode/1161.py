# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Edge case check
        if not root.left and not root.right:
            return 1
        # Init dict for level sums
        self.levels_dict = defaultdict(int)
        # Recursive BFS
        self.bfs_helper(root, level=1)
        # Return level of max sum from dict
        return max(self.levels_dict, key=self.levels_dict.get)
    
    # BFS helper function
    def bfs_helper(self, node, level):
        if node:
            self.levels_dict[level] += node.val
            self.bfs_helper(node.left, level + 1)
            self.bfs_helper(node.right, level + 1)