class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for sell in prices[i:]:
                profit = max(profit, sell - prices[i])
        
        return profit