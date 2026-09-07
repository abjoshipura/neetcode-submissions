class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        suffixProduct = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1]
        
        return [prefixProduct[i] * suffixProduct[i] for i in range(len(nums))]