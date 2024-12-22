class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Edge case: check if the matrix is empty
        if not matrix or not matrix[0]:
            return False
        
        # Get dimensions
        rows, cols = len(matrix), len(matrix[0])
        
        # Start from the top-right corner
        row, col = 0, cols - 1
        
        # Traverse while within bounds
        while row < rows and col >= 0:
            current_value = matrix[row][col]
            
            # Check current value against the target
            if current_value == target:
                return True  # Found target
            elif current_value > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down
        
        # If loop exits, target is not in the matrix
        return False
