from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_numbers = n * n

        # Expected sum and square sum
        expected_sum = (total_numbers * (total_numbers + 1)) // 2
        expected_square_sum = (total_numbers * (total_numbers + 1) * (2 * total_numbers + 1)) // 6
        
        # Compute actual sum and actual square sum
        actual_sum = actual_square_sum = 0
        for row in grid:
            for num in row:
                actual_sum += num
                actual_square_sum += num * num
        
        # Equations: y - x = diff1, and y^2 - x^2 = diff2
        diff1 = actual_sum - expected_sum  # (y - x)
        diff2 = actual_square_sum - expected_square_sum  # (y^2 - x^2)

        # Solve for y (repeated) and x (missing)
        sum_xy = diff2 // diff1  # (y + x)
        repeated = (diff1 + sum_xy) // 2
        missing = sum_xy - repeated

        return [repeated, missing]
