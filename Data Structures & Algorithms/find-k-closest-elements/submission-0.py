class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import heapq
        dist = []

        # -4, -2, -1, -2

        for num in arr:
            heapq.heappush(dist, (-abs(num-x), -num))
            if len(dist) > k:
                heapq.heappop(dist)
        
        return sorted([-n[1] for n in dist])