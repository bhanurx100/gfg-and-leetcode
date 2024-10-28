class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        col0 = False  # Track if the first column should be zeroed
        
        # Step 1: Use the first row and column as markers
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 2: Set elements to zero based on markers, skipping the first row and column initially
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 3: Update the first row if needed
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        # Step 4: Update the first column if needed
        if col0:
            for i in range(n):
                matrix[i][0] = 0
