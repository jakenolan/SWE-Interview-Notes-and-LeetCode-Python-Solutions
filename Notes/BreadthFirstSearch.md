<br />

---

## **Breadth First Search**

---

<br />

## Explanation

<br />

*Searching a tree level by level, left to right. Once traversing all nodes on a level then you search the next one down and repeat.*

<br />

Starting at the root node, you add the children nodes to your queue. After traversing the root node (top level) you move down to the next level. Traversing the children nodes that were added to the queue left to right, adding their own children to the queue as you traverse them. Once all the nodes are traversed on that level you move to the next, repeating the process until all nodes are traversed.

<br />

Notes:
- Level-order tree traversal has O(n) time complexity.
- When a node is missing children the null value is skipped over and not added to queue.

<br />

---

<br />

## Code Examples

<br />

LeetCode 102 - Binary tree level order traversal

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Breadth first search algo setup
        result = []
        q = collections.deque()
        q.append(root)
        # While loop for traversing tree
        while q:
            qLen = len(q)
            level = []
            # Loop through all nodes on a level
            for i in range(qLen):
                # Pop left node in queue
                node = q.popleft()
                if node:
                    # Add node to level list
                    level.append(node.val)
                    # Add children of node to queue
                    q.append(node.left)
                    q.append(node.right)
            # Add completed level to result
            if level:
                result.append(level)
        # Return final result
        return result
```

<br />

LeetCode 98 - Validate binary search tree

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate subtree
        def validate(node, leftBoundary, rightBoundary):
            # If there is no node
            if not node:
                return True
            # If binary search tree conditions not met
            if not (node.val > leftBoundary and node.val < rightBoundary):
                return False
            # Recursion
            return (validate(node.left, leftBoundary, node.val) and                                                             (validate(node.right, node.val, rightBoundary)))
        # Return answer
        return validate(root, float("-inf"), float("inf"))
```

<br />

LeetCode 200 - Number of islands

```
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for empty grid
        if not grid:
            return 0
        
        # Init setup for necessary variables
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0
        
        # BFS helper function
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r, c))
            # Continue while loop while queue not empty
            while queue:
                # Take positions from queue and find neighbors
                row, col = queue.popleft() # Change to queue.pop() to make this iterative DFS not BFS
                neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # Go through neighbors and check if they are new found land
                for nr, nc in neighbors:
                    # Use positions and neighbor changes to remember neighbor positions
                    nrow, ncol = row + nr, col + nc
                    # If neighbor is new found land
                    if (nrow in range(rows) and ncol in range(cols) and grid[nrow][ncol] == "1" and (nrow,                         ncol) not in visited):
                            queue.append((nrow, ncol))
                            visited.add((nrow, ncol))
        
        # Nested for loop for bfs search through graph
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        # Return final total
        return islands
```

<br />

---