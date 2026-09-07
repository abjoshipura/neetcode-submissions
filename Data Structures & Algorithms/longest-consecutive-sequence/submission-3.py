from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) < 1:
            return 0
            
        lcs = defaultdict(int)
        result = 0

        for num in nums:
            if not lcs[num]:
                lcs[num] = lcs[num - 1] + lcs[num + 1] + 1
                lcs[num - lcs[num - 1]] = lcs[num]
                lcs[num + lcs[num + 1]] = lcs[num]

        return sorted(list(lcs.values()))[-1]