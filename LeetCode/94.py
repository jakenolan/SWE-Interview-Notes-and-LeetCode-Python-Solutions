# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_helper(self, node):
        if node:
            self.dfs_helper(node.left)
            self.inorder_nodes.append(node.val)
            self.dfs_helper(node.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_nodes = []
        self.dfs_helper(root)
        return self.inorder_nodes