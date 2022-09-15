<br />

---

## **Depth First Search**

---

<br />

## Explanation

<br />

*Used to traverse a graph or tree. In a tree it visits the children of each node level by level before moving left to right. Vertical search first and then horizontal and repeat.*

<br />

Starting from the root node of a tree, mark as visited and push to stack. From there, while the stack is not empty, remove the node from the stack and add to the DFS traversal order. Then add the children of the current node to the stack. Repeat this process by removing the node at the top of the stack, adding it to DFS traversal order, and adding its children to the stack. Because stacks are LIFO the traversal will continue vertically until it can't anymore before traversing horizontally.

<br />

Notes:
- Remember you are using a stack here (unlike a queue in BFS).
- Always add a edge case catch for a possibly empty tree before your recursion.
- For trees, time/space complexity is O(n).

<br />

---

<br />

## Code Examples

<br />

LeetCode 104 - Maximum depth of binary tree

```
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# Recursive DFS Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

<br />

LeetCode 113 - Path sum II

```
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Check if tree is empty
        if not root:
            return []
        
        # Setup output list
        self.output = []
        
        # Helper function
        def dfs(node, path, sum):
            sum += node.val
            temp = path + [node.val]
            if node.left:
                dfs(node.left, temp, sum)
            if node.right:
                dfs(node.right, temp, sum)
            if not node.left and not node.right and sum == targetSum:
                self.output.append(temp)
                
        # Recursion start
        dfs(root, [], 0)
        
        # Return output list
        return self.output
```

<br />

---