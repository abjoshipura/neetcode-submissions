class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
                continue

            totalProduct *= num
        
        output = []
        if zeroCount == 1:
            for num in nums:
                if num == 0:
                    output.append(totalProduct)
                else:
                    output.append(0)
                
            return output
        elif zeroCount > 1:
            return [0] * len(nums)
        else:
            for num in nums:
                output.append(totalProduct // num)
            return output