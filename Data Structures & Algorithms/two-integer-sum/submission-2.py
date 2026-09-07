class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return list()
        
        # Are there negative numbers? I ask, because then 0 is impossible
        # Are there duplicates?
        
        # I notice that the order matters, so I will prefer a data structure that 
        # retains that information. However, this needs me to iterate over all prefix
        # integers checking for a fit. Effectively results in a O(n^2)

        # So, I can store that index information, and instead focus on a faster lookup
        # such as a HashMap

        targetDifferentials = dict()
        for i in range(len(nums)):
            if nums[i] in targetDifferentials:
                return [targetDifferentials[nums[i]], i]
            elif nums[i] not in targetDifferentials:
                targetDifferentials[target - nums[i]] = i
        
        return list()