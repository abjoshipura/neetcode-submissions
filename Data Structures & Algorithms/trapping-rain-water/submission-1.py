class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        # From the left side ignore everything as long as it is in non-decreasing order
        # From the right side ignore everythin as long as it is in non-decreasing order

        l_ptr = 0
        r_ptr = len(height) - 1

        last_height = height[l_ptr]
        while True:
            if last_height > height[l_ptr + 1]:
                break
            else:
                last_height = height[l_ptr + 1]
            
            l_ptr += 1
        
        last_height = height[r_ptr]
        while True:
            if last_height > height[r_ptr - 1]:
                break
            else:
                last_height = height[r_ptr - 1]
            
            r_ptr -= 1

        s_ptr = l_ptr
        f_ptr = l_ptr + 1

        area = 0
        while s_ptr != r_ptr:
            temp_area = []
            while f_ptr != r_ptr and height[f_ptr] < height[s_ptr]:
                temp_area.append(height[s_ptr] - height[f_ptr])
                f_ptr += 1

            if f_ptr == r_ptr and height[f_ptr] < height[s_ptr]:
                diff = height[s_ptr] - height[f_ptr]
                for i in temp_area:
                    area += max(0, i - diff)
            else:
                area += sum(temp_area)

            s_ptr = f_ptr
            f_ptr = min(s_ptr + 1, r_ptr)

        return area
