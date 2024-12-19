import math
from typing import List

class Solution:
    def sumByD(self, nums: List[int], divisor: int) -> int:
        """
        Calculates the sum of the numbers in `nums` divided by `divisor`,
        with each division result rounded up to the nearest integer.
        
        Args:
        nums (List[int]): The list of numbers to be divided.
        divisor (int): The divisor for division.
        
        Returns:
        int: The total sum of the rounded-up divisions.
        """
        total_sum = 0
        for num in nums:
            # Use math.ceil to round up the division result.
            total_sum += math.ceil(num / divisor)
        return total_sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        Finds the smallest divisor such that the sum of the divisions
        is less than or equal to the given threshold using binary search.
        
        Args:
        nums (List[int]): The list of numbers to be divided.
        threshold (int): The maximum allowable sum of divisions.
        
        Returns:
        int: The smallest divisor that satisfies the condition, or -1 if not possible.
        """
        n = len(nums)
        # If the number of elements is greater than the threshold, it's impossible.
        if n > threshold:
            return -1

        # Initialize binary search boundaries.
        low, high = 1, max(nums)

        # Perform binary search to find the smallest divisor.
        while low <= high:
            mid = (low + high) // 2  # Calculate the middle divisor.
            
            # Check if the current divisor meets the threshold.
            if self.sumByD(nums, mid) <= threshold:
                # If it meets the threshold, try smaller divisors.
                high = mid - 1
            else:
                # Otherwise, try larger divisors.
                low = mid + 1

        # The smallest divisor that works will be stored in `low`.
        return low
