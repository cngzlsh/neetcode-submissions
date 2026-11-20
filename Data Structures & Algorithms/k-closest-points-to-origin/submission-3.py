class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        h = []

        for x, y in points:
            heapq.heappush(h, [-(x ** 2 + y ** 2), x, y])
        
            if len(h) > k:
                heapq.heappop(h)
        
        return [[x[1], x[2]] for x in h]

