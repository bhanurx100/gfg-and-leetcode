class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize minimum price and maximum profit
        mini = prices[0]
        profit = 0
        
        # Loop through the prices starting from the second element
        for i in range(1, len(prices)):
            # Calculate the profit if selling today and update maximum profit so far
            profit = max(profit, prices[i] - mini)
            
            # Update mini if the current price is lower than the recorded minimum
            mini = min(mini, prices[i])
        
        return profit
