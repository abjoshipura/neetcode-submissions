class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inverted_search = dict()

        for i in range(len(nums)):
            if nums[i] in inverted_search:
                return sorted([i, inverted_search[nums[i]]])
            else:
                inverted_search[target - nums[i]] = i
        