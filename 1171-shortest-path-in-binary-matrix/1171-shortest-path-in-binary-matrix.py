from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Grid size

        # Edge case: If start or end is blocked, return -1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # BFS setup: queue stores (row, col, path_length)
        queue = deque([(0, 0, 1)])  # (row, col, current path length)
        directions = [  # 8 possible movements (horizontal, vertical, diagonal)
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
        ]
        
        # Mark starting cell as visited
        grid[0][0] = 1

        # BFS loop
        while queue:
            r, c, path_length = queue.popleft()

            # If we reach bottom-right corner, return shortest path length
            if r == n-1 and c == n-1:
                return path_length

            # Explore all 8 directions
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                # Check if the new position is within bounds and is a valid path
                if 0 <= new_r < n and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    queue.append((new_r, new_c, path_length + 1))  # Add to queue
                    grid[new_r][new_c] = 1  # Mark as visited

        # If no path was found
        return -1
