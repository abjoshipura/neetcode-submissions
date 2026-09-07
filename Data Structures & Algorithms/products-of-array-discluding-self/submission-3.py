class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [1] * len(nums)
        suffixProducts = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixProducts[i] = prefixProducts[i - 1] * nums[i - 1]
        
        for i in range(-2, -1 * len(nums) - 1, -1):
            suffixProducts[i] = suffixProducts[i + 1] * nums[i + 1]
        
        return [prefixProducts[i] * suffixProducts[i] for i in range(len(nums))]