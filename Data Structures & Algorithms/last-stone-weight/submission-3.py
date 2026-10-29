class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]

        import heapq
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            w1 = heapq.heappop(maxHeap)
            w2 = heapq.heappop(maxHeap)

            if w1 == w2:
                continue
            else:
                heapq.heappush(maxHeap, w1-w2)
        
        if len(maxHeap) == 1: return -maxHeap[0]
        return 0