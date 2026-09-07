class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {element: index for index, element in enumerate(nums)}
        results = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                add_inverse = -1 * s
                if add_inverse in nums_dict and nums_dict[add_inverse] != i and nums_dict[add_inverse] != j:
                    results.add(tuple(sorted([nums[i], nums[j], add_inverse])))
        
        return [list(t) for t in results]