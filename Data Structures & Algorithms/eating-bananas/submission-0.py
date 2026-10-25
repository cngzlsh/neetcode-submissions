class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ceil = lambda a, b: -(- a//b)
        # binary search for eating speed k
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            # can koko finish at rate m?
            if sum([ceil(x, m) for x in piles]) > h:
                # if takes longer than h hours, need to speed up
                l = m + 1
                
            elif sum([ceil(x, m) for x in piles]) <= h:
                # if takes shorter than h hours, we can eat slower
                # even if it matches, we can try slower
                r = m
        
        return l