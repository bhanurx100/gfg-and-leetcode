class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to check if Koko can finish all bananas at speed `k` within `h` hours
        def canFinish(k):
            total_hours = 0  # Track the total hours needed
            for pile in piles:
                # Calculate hours required for this pile with speed `k`
                # Equivalent to math.ceil(pile / k)
                total_hours += (pile + k - 1) // k
            # If total hours is within the given limit `h`, return True
            return total_hours <= h

        # Initialize binary search range
        left, right = 1, max(piles)  # Minimum speed is 1, maximum speed is eating the largest  pile in one hour

        # Perform binary search to find the minimum speed
        while left < right:
            mid = (left + right) // 2  # Midpoint speed
            if canFinish(mid):
                # If Koko can finish at this speed, try to find a slower feasible speed
                right = mid
            else:
                # If not, increase the speed to finish faster
                left = mid + 1

        # When the loop ends, `left` will hold the minimum feasible speed
        return left
