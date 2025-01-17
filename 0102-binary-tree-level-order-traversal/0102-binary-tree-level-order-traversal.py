# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []  # To store the result of level order traversal
        queue = deque([root])  # Initialize the queue with the root node
        while queue:
            level = []  # To store the nodes at the current level
            level_size = len(queue)  # Number of nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()  # Pop the leftmost node from the queue
                level.append(node.val)  # Add the node's value to the current level list
                # If the node has a left child, add it to the queue
                if node.left:
                    queue.append(node.left)                
                # If the node has a right child, add it to the queue
                if node.right:
                    queue.append(node.right)
            result.append(level)  # Add the current level list to the result
        return result