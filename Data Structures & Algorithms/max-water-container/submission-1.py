class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        mx_area = 0
        while left < right:
            h = min(heights[left], heights[right])
            w = right - left

            mx_area = max(mx_area, h * w)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return mx_area