class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            m = l + (r - l + 1) // 2      # round up, so l = m always makes progress
            if m * m <= x:
                l = m                     # m works, a larger one might too
            else:
                r = m - 1                 # m is too big
        return l