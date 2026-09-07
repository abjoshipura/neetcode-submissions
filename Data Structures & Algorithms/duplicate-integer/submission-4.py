class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        
        seenNumbers = set()
        for num in nums:
            if num in seenNumbers:
                return True
            seenNumbers.add(num)
        
        return False