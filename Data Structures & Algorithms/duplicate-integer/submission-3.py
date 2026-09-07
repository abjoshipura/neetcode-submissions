class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 1:
            return False
        
        seenNumbers = set()
        for num in nums:
            if num in seenNumbers:
                return True
            else:
                seenNumbers.add(num)
        
        return False