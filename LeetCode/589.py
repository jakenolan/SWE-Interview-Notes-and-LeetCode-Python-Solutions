"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs_helper(self, node):
        # Make sure node is not null
        if node:
            # Add node to visited first (preorder traversal)
            self.visited.append(node.val)
            # Continue recursion with all children nodes
            for child in node.children:
                self.dfs_helper(child)
        
    def preorder(self, root: 'Node') -> List[int]:
        # Edge case for empty tree
        if not root:
            return []
        
        # Edge case for single node tree
        if not root.children:
            return [root.val]
        
        # Init list to record visited order
        self.visited = []
        
        # Start recursion with root node
        self.dfs_helper(root)
        
        # Return list of visited nodes
        return self.visited