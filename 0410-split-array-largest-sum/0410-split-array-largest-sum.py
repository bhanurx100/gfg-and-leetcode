from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_feasible(mid):
            # Greedy approach to check if we can split the array with the largest sum <= mid
            subarray_count = 1  # Start with one subarray
            current_sum = 0  # Sum of the current subarray

            for num in nums:
                if current_sum + num > mid:
                    # If adding the current number exceeds mid, start a new subarray
                    subarray_count += 1
                    current_sum = num
                    # If we've used more than k subarrays, return False
                    if subarray_count > k:
                        return False
                else:
                    # Otherwise, add the number to the current subarray
                    current_sum += num
            
            return True
        
        # Binary search for the minimized largest sum
        low, high = max(nums), sum(nums)
        result = high
        
        while low <= high:
            mid = (low + high) // 2  # Try the middle value
            if is_feasible(mid):
                result = mid  # If it's feasible, try for a smaller max sum
                high = mid - 1
            else:
                low = mid + 1  # If it's not feasible, increase the sum

        return result
