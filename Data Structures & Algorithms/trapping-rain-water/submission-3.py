class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0
        
        prefixMax = [0] * len(height)
        suffixMax = [0] * len(height)

        prefixMax[0] = height[0]
        for i in range(1, len(height)):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        suffixMax[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])
        
        total = 0
        for i in range(len(height)):
            total += min(prefixMax[i], suffixMax[i]) - height[i]
        
        return total