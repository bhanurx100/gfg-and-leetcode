# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def buildBST(preorder,lower,upper):
            if not preorder or preorder[0]<lower or preorder[0]>upper:
                return None
            val=preorder.pop(0)
            root=TreeNode(val)
            root.left=buildBST(preorder,lower,val)
            root.right=buildBST(preorder,val,upper)
            return root
        return buildBST(preorder,float('-inf'),float('inf'))