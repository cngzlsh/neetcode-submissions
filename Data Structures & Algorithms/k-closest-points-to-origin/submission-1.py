class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        maxHeap = []
        heapq.heapify(maxHeap)
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, [-dist, x, y])
            else:
                # if it's smaller than the largest element, pop the largest element
                if dist <= -maxHeap[0][0]:
                    heapq.heapreplace(maxHeap, [-dist, x, y])
                else:
                    continue
        
        return [[d[1], d[2]] for d in maxHeap]