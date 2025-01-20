# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}  # To store parent references
        def build_parent(node, parent=None):
            if node:
                parent_map[node] = parent
                build_parent(node.left, node)
                build_parent(node.right, node)
        
        build_parent(root)  # Build the parent map
        
        # Step 2: BFS to find all nodes at distance K
        queue = deque([(target, 0)])  # Start from the target node with distance 0
        visited = set()  # To avoid cycles
        visited.add(target)
        
        result = []
        
        while queue:
            if queue[0][1] == k:
                result = [node.val for node, _ in queue]
                break
            
            for _ in range(len(queue)):
                node, distance = queue.popleft()
                
                # Explore neighbors (left, right, and parent)
                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return result