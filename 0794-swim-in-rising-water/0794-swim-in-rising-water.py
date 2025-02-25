from heapq import heappush, heappop
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Grid size
        directions = [(0,1), (0,-1), (1,0), (-1,0)]  # Right, Left, Down, Up
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, x, y)
        visited = set()  # Track visited cells
        max_elevation = 0  # Track highest elevation encountered
        
        while min_heap:
            elevation, x, y = heappop(min_heap)  # Get lowest elevation cell
            max_elevation = max(max_elevation, elevation)  # Update max elevation
            
            # If we reach the bottom-right corner, return the max elevation seen
            if x == n - 1 and y == n - 1:
                return max_elevation
            
            # Explore all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    heappush(min_heap, (grid[nx][ny], nx, ny))  # Push next cell
            
        return -1  # This should never be reached
