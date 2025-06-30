class Solution:
    def findLHS(self, nums):
        # Step 1: Sort the array
        nums.sort()

        left = 0
        max_len = 0

        # Step 3: Loop with right pointer
        for right in range(len(nums)):

            # Step 4: Shrink window if needed
            while nums[right] - nums[left] > 1:
                left += 1

            # Step 5: If difference is 1, update max_len
            if nums[right] - nums[left] == 1:
                max_len = max(max_len, right - left + 1)

        # Step 6: Return result
        return max_len