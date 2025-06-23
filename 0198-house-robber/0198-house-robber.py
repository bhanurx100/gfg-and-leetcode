class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Handle base cases
        if n == 0:
            return 0  # No houses to rob
        if n == 1:
            return nums[0]  # Only one house to rob

        # Step 2: Initialize dp array
        dp = [0] * n  # dp[i] = max money that can be robbed from house 0 to i
        dp[0] = nums[0]  # Rob first house
        dp[1] = max(nums[0], nums[1])  # Either rob house 0 or 1, whichever is better

        # Step 3: Fill dp[] using bottom-up approach
        for i in range(2, n):
            # Option 1: Rob current house → Add nums[i] + dp[i-2]
            # Option 2: Skip current house → dp[i-1]
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        # Step 4: Return max money that can be robbed from all houses
        return dp[n - 1]
