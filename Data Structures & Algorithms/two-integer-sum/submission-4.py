class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return [-1, -1]

        # Using HashMaps

        targetComplement = dict()
        
        for i in range(len(nums)):
            if nums[i] in targetComplement:
                return [targetComplement[nums[i]], i]
            targetComplement[target - nums[i]] = i
        
        return [-1, -1]