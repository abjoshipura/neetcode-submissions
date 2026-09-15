class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = set(nums)

        max_length = 0
        for num in lcs:
            if (num - 1) in lcs:
                continue
            
            length = 1
            while (num + length) in lcs:
                length += 1

            max_length = max(length, max_length)
        
        return max_length