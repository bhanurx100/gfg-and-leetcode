class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: build heights
        heights = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    heights[r][c] = (heights[r-1][c] + 1) if r > 0 else 1
        
        ans = 0
        # Step 2: for each row, count submatrices
        for r in range(m):
            for c in range(n):
                if heights[r][c] > 0:
                    min_h = heights[r][c]
                    for k in range(c, -1, -1):
                        if heights[r][k] == 0:
                            break
                        min_h = min(min_h, heights[r][k])
                        ans += min_h
        return ans
