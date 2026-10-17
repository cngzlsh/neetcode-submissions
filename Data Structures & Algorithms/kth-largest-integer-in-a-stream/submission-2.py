import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k 
        for n in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, n)
            else:
                if n > self.h[0]:
                    heapq.heapreplace(self.h, n)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
            return self.h[0]

        if val <= self.h[0]:
            return self.h[0]
        else:
            heapq.heapreplace(self.h, val)
            return self.h[0]
        
