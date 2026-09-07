class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[0]
        
        memo = [0] * (len(cost) + 1)

        memo[0] = 0
        memo[1] = 0

        for i in range(2, len(memo)):
            memo[i] = min(memo[i - 1] + cost[i - 1], memo[i - 2] + cost[i - 2])
        
        return memo[-1]