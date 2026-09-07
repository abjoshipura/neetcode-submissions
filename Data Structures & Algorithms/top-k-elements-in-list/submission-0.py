class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        output = list()
        for i in range(k):
            max_key = max(freq, key=freq.get)
            output.append(max_key)
            del freq[max_key]
        
        return output