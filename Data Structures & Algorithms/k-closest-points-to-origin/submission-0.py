import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for (x,y) in points:
            dist = x ** 2 + y ** 2
            if len(h) < k:
                heapq.heappush(h, (-dist, x, y))
            else:
                if dist < -h[0][0]:
                    heapq.heapreplace(h, (-dist, x, y))
    
        return [pt[1:] for pt in h]

        