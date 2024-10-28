from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        col0 = 1  # Flag for the first column
        
        # Step 1: Traverse the matrix and mark the first row and column
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # Mark the i-th row
                    matrix[i][0] = 0
                    # Mark the j-th column
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0  # Mark that the first column needs to be set to zero

        # Step 2: Use markers to set cells to zero from (1,1) to (n-1, m-1)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Set the first row to zero if needed
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Step 4: Set the first column to zero if needed
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
