class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(heights) - 1

        max_area = 0
        while l_ptr != r_ptr:
            area = (r_ptr - l_ptr) * min(heights[l_ptr], heights[r_ptr])
            max_area = max(max_area, area)

            if heights[l_ptr] <= heights[r_ptr]:
                l_ptr += 1
            else:
                r_ptr -= 1
        
        return max_area