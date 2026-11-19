class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search?
        l = max(weights)
        r = sum(weights)

        def canShip(m):
            d, curr_w = 1, 0
            for w in weights:
                if curr_w + w > m:
                    d += 1
                    curr_w = w
                else:
                    curr_w += w
            
            return d <= days

        while l < r:
            m = l + (r - l) // 2

            # can we ship in days DAYS with weight M?
            if canShip(m):
                r = m
            else:
                l = m + 1
            
        return l
        
        