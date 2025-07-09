class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[-1][:]

        for i in range(n - 2, -1, -1):
            curr = [0] * n
            for j in range(n):
                down = prev[j]
                left = prev[j - 1] if j > 0 else float('inf')
                right = prev[j + 1] if j < n - 1 else float('inf')
                curr[j] = matrix[i][j] + min(down, left, right)
            prev = curr

        return min(prev)
