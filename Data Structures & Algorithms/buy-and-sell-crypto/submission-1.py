class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = [0] * len(prices)
        min_buy[0] = prices[0]

        for i in range(1, len(min_buy)):
            max_profit = max(max_profit, prices[i] - min_buy[i - 1])
            min_buy[i] = min(min_buy[i - 1], prices[i])
        
        return max_profit