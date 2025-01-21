# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepthLeft(node):
            depth=0
            while node:
                depth+=1
                node=node.left
            return depth
        def getDepthRight(node):
            depth=0
            while node:
                depth+=1
                node=node.right
            return depth
        if not root:
            return 0
        left_depth=getDepthLeft(root)
        right_depth=getDepthRight(root)
        if (left_depth==right_depth):
            return (1<<left_depth)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)