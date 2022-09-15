class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case for list of length 1
        if len(prices) == 1:
            return 0
        
        # Init variables for max_profit and min_price
        max_profit = 0
        min_price = prices[0]
        
        # Iterate through prices to maximize profit
        for i in range(len(prices)):
            # If min_price still min then compare profits
            if min_price < prices[i]:
                max_profit = max(max_profit, prices[i] - min_price)
            # Else min_price is not min anymore so update min_price
            else:
                min_price = prices[i]
        
        # Return max_profit
        return max_profit