from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Step 1: If there aren't enough edges to connect all nodes, return -1
        if len(connections) < n - 1:
            return -1
        
        # Step 2: Union-Find (Disjoint Set Union - DSU)
        parent = [i for i in range(n)]  # Each node is its own parent
        rank = [1] * n  # Rank for Union by Rank

        # Find with Path Compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union by Rank
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:  # Merge if different components
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True  # Successful merge
            return False  # Already connected
        
        # Step 3: Apply Union-Find on given connections
        for u, v in connections:
            union(u, v)
        
        # Step 4: Count number of connected components
        components = len(set(find(i) for i in range(n)))

        # Step 5: Minimum operations required = (components - 1)
        return components - 1
