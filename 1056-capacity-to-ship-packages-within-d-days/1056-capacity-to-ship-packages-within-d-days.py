from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Helper function to check if we can ship with a given capacity
        def canShipWithCapacity(cap: int) -> bool:
            load = 0  # Current load on the ship
            required_days = 1  # Start with 1 day
            for weight in weights:
                if load + weight > cap:  # If adding this weight exceeds capacity
                    required_days += 1  # Increment the day count
                    load = weight  # Start a new day with the current weight
                else:
                    load += weight  # Add weight to the current day
            return required_days <= days  # Return True if we can ship within `days`

        # Binary search for the minimum capacity
        low = max(weights)  # Minimum capacity needed is at least the heaviest weight
        high = sum(weights)  # Maximum capacity is the sum of all weights

        while low <= high:
            mid = (low + high) // 2  # Middle point of current search range
            if canShipWithCapacity(mid):  # Check if `mid` capacity works
                high = mid - 1  # Try to find a smaller capacity
            else:
                low = mid + 1  # Increase capacity if it doesn't work

        return low  # Return the minimum capacity that works

