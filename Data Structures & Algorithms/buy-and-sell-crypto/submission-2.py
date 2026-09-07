class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        l, r = 0, 1
        profitMax = 0

        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                profitMax = max(profitMax, prices[r] - prices[l])
            
            r += 1
        
        return profitMax