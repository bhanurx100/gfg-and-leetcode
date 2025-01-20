# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]
        def dfs(node,path):
            if not node:
                return
            path+=str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path+="->"
                dfs(node.left,path)
                dfs(node.right,path)
        dfs(root,"")
        return paths