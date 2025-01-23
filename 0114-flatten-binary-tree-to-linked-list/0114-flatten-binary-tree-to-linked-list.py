# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        
        while current:
            if current.left:
                predecessor = current.left
                # Find the rightmost node in the left subtree
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Connect right subtree to predecessor's right
                predecessor.right = current.right
                current.right = current.left
                current.left = None
            
            current = current.right  # Move to the next right node
  