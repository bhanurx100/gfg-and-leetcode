from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        island_id = 2  # Start from 2 to distinguish from 1
        island_sizes = {0: 0}  # Store island sizes
        
        def dfs(r, c, id):
            """ Perform DFS and mark the island with a unique id """
            stack = [(r, c)]
            grid[r][c] = id
            size = 0
            while stack:
                x, y = stack.pop()
                size += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id
                        stack.append((nx, ny))
            return size

        # Step 1: Identify all islands and mark them
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1

        # Step 2: Try converting each 0 to 1
        max_island = max(island_sizes.values())  # If no 0s, return largest existing island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    new_size = 1  # Count the flipped 0 itself
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 1:
                            seen_islands.add(grid[nx][ny])
                    for island in seen_islands:
                        new_size += island_sizes[island]
                    max_island = max(max_island, new_size)

        return max_island

