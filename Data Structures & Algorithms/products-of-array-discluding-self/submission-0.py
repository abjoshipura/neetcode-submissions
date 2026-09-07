class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        containsZeros = False
        containsMultipleZeros = False

        productAll = 1
        for num in nums:
            if num == 0:
                if containsZeros:
                    containsMultipleZeros = True
                containsZeros = True
            else:
                productAll *= num

        outputs = list()
        if containsMultipleZeros:
            return [0] * len(nums)
        elif containsZeros:
            for num in nums:
                if num == 0:
                    outputs.append(productAll)
                else:
                    outputs.append(0)
        else:
            for num in nums:
                if num == 0:
                    outputs.append(productAll)
                else:
                    outputs.append(productAll // num)
            
        
        return outputs