class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
            
        left = 0
        right = 0

        minBuy = prices[left]
        maxProfit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            
            right += 1
        
        return maxProfit