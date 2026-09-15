class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) < 1:
            return 0
        
        lcs = set(nums)

        max_length = 1
        for num in lcs:
            length = 1
            
            if (num - 1) in lcs:
                continue
            
            while (num + 1) in lcs:
                length += 1
                num += 1

            max_length = max(length, max_length)
        
        return max_length