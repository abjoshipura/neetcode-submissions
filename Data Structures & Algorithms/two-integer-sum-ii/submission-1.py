class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force

        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]

        # two pointer solution

        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]