# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue=deque([(root.left,root.right)])
        while queue:
            t1,t2=queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val!=t2.val:
                return False
            queue.append((t1.left,t2.right))
            queue.append((t1.right,t2.left))
        return True
