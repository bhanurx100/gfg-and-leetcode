class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Total flowers needed to make m bouquets with k flowers each
        total_flowers_needed = m * k
        
        # If the garden doesn't have enough flowers, it's impossible to make bouquets
        if len(bloomDay) < total_flowers_needed:
            return -1  # Return -1 as making m bouquets is not possible
        
        # Helper function to check if it's possible to make m bouquets in "days"
        def canMakeBouquets(days):
            bouquets = 0  # Count of bouquets formed
            flowers = 0   # Count of adjacent flowers for the current bouquet
            
            for bloom in bloomDay:
                if bloom <= days:  # Flower blooms within "days"
                    flowers += 1
                    if flowers == k:  # Form a bouquet
                        bouquets += 1
                        flowers = 0  # Reset flower count for the next bouquet
                else:
                    flowers = 0  # Reset adjacent flower count if bloom > days
                
                if bouquets >= m:  # Early exit if we already have enough bouquets
                    return True
            
            return bouquets >= m  # Return whether we formed at least m bouquets
        
        # Binary search over the range of days
        left, right = min(bloomDay), max(bloomDay)
        result = -1  # Store the minimum days required
        
        while left <= right:
            mid = (left + right) // 2  # Calculate the mid-point of days
            if canMakeBouquets(mid):  # Check if it's feasible to make m bouquets in "mid" days
                result = mid          # Update result with the feasible day
                right = mid - 1       # Try to find a smaller feasible day
            else:
                left = mid + 1        # Increase the days as "mid" was not enough
        
        return result
