class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """
        This function finds a peak element in a 2D grid using binary search.
        """
        # Dimensions of the matrix
        m = len(mat)  # number of rows
        n = len(mat[0])  # number of columns

        # Perform binary search on columns
        low, high = 0, n - 1  # Search space for column index
        while low <= high:
            mid_col = (low + high) // 2  # Middle column
            
            # Find the row with the maximum element in the current column
            max_row = 0
            for i in range(1, m):
                if mat[i][mid_col] > mat[max_row][mid_col]:
                    max_row = i
            
            # Get neighbors safely
            left_val = mat[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
            right_val = mat[max_row][mid_col + 1] if mid_col < n - 1 else float('-inf')

            # Check if the maximum element is a peak
            if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
                return [max_row, mid_col]
            elif mat[max_row][mid_col] < right_val:
                # Move to the right half
                low = mid_col + 1
            else:
                # Move to the left half
                high = mid_col - 1
        
        # Return -1, -1 if no peak is found (theoretically unreachable)
        return [-1, -1]
