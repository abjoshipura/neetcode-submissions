from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
        
        return [k for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:k]]