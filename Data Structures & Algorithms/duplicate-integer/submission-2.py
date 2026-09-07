class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        
        freq = set()
        for num in nums:
            if num in freq:
                return True
            else:
                freq.add(num)

        return False
                