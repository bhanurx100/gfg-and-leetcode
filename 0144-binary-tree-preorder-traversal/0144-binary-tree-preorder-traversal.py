# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]      # Initialize stack with root
        result = []         # List to store preorder traversal

        while stack:
            node = stack.pop()       # Pop the top node
            result.append(node.val)  # Visit the node (Root)

            # Push right first so that left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
