# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        queue=[root]
        res=[]
        while queue:
            node=queue.pop(0)
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="null":
            return None
        nodes=data.split(",")
        root=TreeNode(int(nodes[0]))
        queue=[root]
        i=1
        while queue and i<len(nodes):
            curr=queue.pop(0)
            if nodes[i]!="null":
                curr.left=TreeNode(int(nodes[i]))
                queue.append(curr.left)
            i+=1
            if i<len(nodes) and nodes[i]!="null":
                curr.right=TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))