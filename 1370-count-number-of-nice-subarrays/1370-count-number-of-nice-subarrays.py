class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Helper function to count subarrays with exactly 'k' odd numbers
        def countSubarraysWithKOdd(nums, k):
            odd_count_map = {0: 1}  # to account for subarrays starting from index 0
            odd_count = 0
            result = 0
            for num in nums:
                # Increase odd_count if the number is odd
                if num % 2 != 0:
                    odd_count += 1
                # If we have seen (odd_count - k) before, it means there are subarrays
                # that have exactly 'k' odd numbers.
                if odd_count - k in odd_count_map:
                    result += odd_count_map[odd_count - k]
                # Record the current odd_count in the map
                if odd_count in odd_count_map:
                    odd_count_map[odd_count] += 1
                else:
                    odd_count_map[odd_count] = 1
            return result
        # Return the count of subarrays with exactly 'k' odd numbers
        return countSubarraysWithKOdd(nums, k)
