class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        output = []
        for i in range(len(nums) - 2):
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    result = [nums[i], nums[left], nums[right]]
                    if result not in output:
                        output.append(result)

                    left += 1
                    right -= 1

        return output