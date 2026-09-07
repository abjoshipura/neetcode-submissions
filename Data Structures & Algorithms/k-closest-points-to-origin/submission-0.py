import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        distances = defaultdict(list)
        for point in points:
            distances[distance(point)].append(point)

        dist_heap = list(distances.keys())
        heapq.heapify(dist_heap)
        
        output = list()
        while k:
            min_dist = heapq.heappop(dist_heap)
            pairs = distances[min_dist]
            
            output.extend(pairs)
            k -= len(pairs)
        
        return output