class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Finds the largest rectangle containing only 1's in a binary matrix.
        
        :param matrix: List[List[str]] - binary matrix with '0's and '1's
        :return: int - area of the largest rectangle
        """
        # Edge case: if the matrix is empty or has no columns
        if not matrix or not matrix[0]:
            return 0
        
        # Number of rows and columns in the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Array to keep track of histogram heights for each column
        heights = [0] * cols
        max_area = 0  # Variable to store the maximum rectangle area found so far
        
        # Helper function to calculate the largest rectangle area in a histogram
        def largestRectangleArea(heights):
            """
            Computes the largest rectangle area in a histogram using a monotonic stack.
            
            :param heights: List[int] - histogram heights
            :return: int - largest rectangle area
            """
            stack = []  # Stack to store indices of histogram bars
            max_area = 0  # Variable to store the maximum area
            
            # Traverse all heights, including a dummy height at the end
            for i in range(len(heights) + 1):
                # Use a dummy 0 height at the end to process remaining bars in the stack
                current_height = heights[i] if i < len(heights) else 0
                
                # Pop from the stack while the current height is less than the height at stack top
                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]  # Height of the popped bar
                    w = i if not stack else i - stack[-1] - 1  # Width of the rectangle
                    max_area = max(max_area, h * w)  # Update the maximum area
                    
                # Push the current index to the stack
                stack.append(i)
            
            return max_area
        
        # Process each row in the matrix to build and update histogram heights
        for row in matrix:
            for col in range(cols):
                # Update the height: increment for '1', reset to 0 for '0'
                heights[col] = heights[col] + 1 if row[col] == '1' else 0
            
            # Calculate the maximum rectangle area for the current histogram
            max_area = max(max_area, largestRectangleArea(heights))
        
        # Return the maximum rectangle area found
        return max_area
