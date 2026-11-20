class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(k):
            ceil = lambda x, y: -(-x //y)
            hrs = 0
            for p in piles:
                hrs += ceil(p, k)
            
            return True if hrs <= h else False
        
        # binary search
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2
            if canFinish(m):
                r = m
            else:
                l = m + 1
        
        return l