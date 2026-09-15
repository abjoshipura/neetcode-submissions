class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxArea = 0
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left

            maxArea = max(h * w, maxArea)


            if heights[left] > h:
                right -= 1
            else:
                left += 1
        
        return maxArea