class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = set(nums)

        seeds = list()
        for num in nums:
            if num - 1 not in lcs:
                seeds.append(num)

        max_length = 0
        for seed in seeds:
            length = 1
            temp = seed
            while temp + 1 in lcs:
                length += 1
                temp += 1

            max_length = max(length, max_length)
        
        return max_length
