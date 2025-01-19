# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes by (column, row)
        node_map = defaultdict(list)

        # Queue for BFS traversal with (node, column, row)
        queue = deque([(root, 0, 0)])  # (node, column, row)

        while queue:
            node, col, row = queue.popleft()

            # Add node value to the map for its column and row
            node_map[col].append((row, node.val))

            # Add left and right children with updated column and row
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        # Prepare the output by sorting
        result = []
        for col in sorted(node_map.keys()):  # Sort by column
            # Sort by row first, then by value
            column_nodes = sorted(node_map[col], key=lambda x: (x[0], x[1]))
            result.append([val for _, val in column_nodes])

        return result
