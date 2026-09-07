import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if stones else 0
        
        heap = [-1 * stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -1 * abs(x - y))
        
        if len(heap):
            return -1 * heapq.heappop(heap)
        else:
            return 0

