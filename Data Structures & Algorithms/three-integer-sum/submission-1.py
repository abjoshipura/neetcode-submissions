class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        for i in range(len(nums) - 2):
            target = nums[i] * -1
            remaining_nums = nums[i + 1:] if i + 1 < len(nums) else []

            left = 0
            right = len(remaining_nums) - 1
            while left < right:
                s = remaining_nums[left] + remaining_nums[right]
                if s < target:
                    left = left + 1
                elif s > target:
                    right = right - 1
                else:
                    result = [nums[i], remaining_nums[left], remaining_nums[right]]
                    if result not in output:
                        output.append(result)
                    
                    left = left + 1
                    right = right - 1

        return output
