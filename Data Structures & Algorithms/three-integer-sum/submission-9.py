class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # we don't care about the indices, just the values

        answers = []

        for k in range(len(nums) - 2):
            target = -1 * nums[k]
            left = k + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    answer = [nums[left], nums[right], nums[k]]
                    if answer not in answers:
                        answers.append(answer)
                    
                    left += 1
                    right -= 1
        
        return answers