# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=float('-inf')
        def max_gain(node):
            if not node:
                return 0
            lgain=max(max_gain(node.left),0)
            rgain=max(max_gain(node.right),0)
            curr_path_sum=node.val+lgain+rgain
            self.max_sum=max(self.max_sum,curr_path_sum)
            return node.val+max(lgain,rgain)
        max_gain(root)
        return self.max_sum