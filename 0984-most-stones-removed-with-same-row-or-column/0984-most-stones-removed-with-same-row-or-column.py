from typing import List

class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        """Path compression to find the root of x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by rank to merge two sets."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def add(self, x):
        """Initialize a node if not already present."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()

        # Step 1: Add stones and union by row & column
        for x, y in stones:
            dsu.add(x)        # Row as node
            dsu.add(~y)       # Column as node (negative indexing for uniqueness)
            dsu.union(x, ~y)  # Union row with column

        # Step 2: Count unique roots (connected components)
        unique_components = len({dsu.find(x) for x, y in stones})

        # Step 3: Compute max stones that can be removed
        return len(stones) - unique_components
